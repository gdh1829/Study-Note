Java IO, NIO, AIO(NIO2)
---

## 함수 호출 모델
Blocking 동기 Java IO / 비동기 X
Non-Blocking 동기 Java NIO(File IO는 non-blocking 불가), 비동기 Java AIO

## I/O 모델
Blocking 동기 Java IO / 비동기 X
Non-blocking 동기 Java NIO, Java AIO / 비동기 x

### Java IO
- Java 1.0부터 도입
- 파일과 네트워크에 데이터를 read/write API 제공
- byte 단위로 read/write 할 수 있는 Input/OutputStream
  - FileIn/OutputStream, Buffered, ByteArray, Socket, etc의 In/OuputStream 구현체가 있음
- blocking 동작

#### SocketInputStream
server Socket accept
    - 소켓을 열고 특정 주소:포트와 바인드 후 리슨 상태에서 수신 대기 중
server socker read
    - 클라이언트의 커넥션 리퀘스트를 수용 하면, 클라이언트의 데이터 read하기 위한 소켓을 클라이언트에게 반환.
    - client socket의 getInputStream으로 socket의 inputStream에 접근
SocketInputStream
- socketInputStream은 퍼블릭이 아니기 때문에 socket.getInputStream 함수를 통해 접근 가능
- blocking 발생

```java
ServerSocket serverSocket = new ServerSocket(8080);

// blocking
Socket clientSocket = serverSocket.accept();

var inputStream = clientSocket.getInputStream();

try (BufferedInputStream bis = new BufferedInputStream(inputStream)) {
    byte[] buffer = new Byte[1024];
    int bytesRead = bis.read(buffer);
    String inputLine = new String(buffer, 0, bytesRead);
    log.info("bytes: {}", inputLine);
}

clientSocket.close();
serverSocket.close();
```

#### OutputStream implements Closable, Flushable
- write시 바로 전송하지 않고 버퍼에 저장한 다음 일정량의 데이터가 모이면 한번에 전달.
- write: stream으로 데이터를 쓴다.
- flush: 버퍼의 모든 데이터를 출력하고 비운다.
- close: stream을 닫고 더 이상 쓰지 않는다.

```java
ServerSocket serverSocket = new ServerSocket(8080);

Socket clientSocket = serverSocket.accpet();

byte[] buffer = new byte[1024];
clientSocket.getInputStream().read(buffer);

var outputStream = clientSocket.getOutputStream();
var bos = new BufferedOutputStream(outputStream);
var bytes = "Hellow".getBytes();
bos.write(bytes);
bos.flush();

clientSocket.close();
serverSocket.close();
```

#### Java IO Reader/Writer
- since java 1.1
- 기존 stream은 byte 단위로만 읽고 쓰기가 가능했음. 그러나 실사용에서는 문자 단위가 필요하여 탄생.
- character 단위로 read/write 가능한 stream
- 문자 인코딩 지원
- blocking 동작

#### Java IO의 한계
- 커널 버퍼에 직접 접근 불가. 따라서 메모리 copy가 발생.
  - 이 말의 의미는?
  - 하드웨어에서 값을 읽어오면, disk controller가 DMA(Direct Memory Access)를 통해서 커널 버퍼에 값을 복사한다.
  - 그러나 자바에서 위의 커널 버퍼로 직접 접근이 불가하기 때문에 커널 버퍼에서 jvm 버퍼로 한 번 더 복사(User Buffer Copy) 과정이 필요하게 된다.
  - DMA 카피의 상황에서는 cpu 리소스가 불필요하지만, 커널 버퍼의 데이터를 JVM으로 읽어오는 User Buffer copy이 과정에서는 cpu 자원이 소모한다.
  - jvm 버퍼는 즉 jvm 메모리에 있기 때문에 gc 대상이 되고 이 또한 cpu 자원 소모
- 동기 blocking으로 동작.
  - application이 read를 호출하면, 커널이 응답을 돌려줄때까지 아무것도 할 수 없는 상태가 된다.
  - I/O 요청이 발생할 때마다 쓰레드를 새로 할당하면, 쓰레드를 생성 및 관리하는 비용과 컨텍스트 스위칭으로 인한 cpu 자원 소모가 발생한다.
  
### Java NIO
위의 문제점들을 해결하기 위해 Java NIO가 탄생
- Java New Input/Ouput
  - NIO의 N은 Non-blocking의 의미가 아니라 New ㅋㅋ 
- since java 1.4
- 파일과 네트워크에 데이터를 read/write APIs 제공
- buffer 객체 기반 (Java IO는 byte 객체 기반)
- non-blocking 지원
  - blocking도 지원하고, 일부 non-blocking이 불가능한 API도 잔여함.
- selector, channel 도입으로 높은 성능 보장.
  
#### Java NIO vs IO
데이터 흐름: 양방향 vs 단방향 => 의미? 기존 IO에서는 Input/Output 스트림으로 인풋/아웃풋 경로가 따로 존재하였으나 NIO는 Channel 하나를 통하여 in/out 모두 가능하다는 의미
종류: Channel vs In/OutputStream
데이터 단위: buffer vs byte or char
블락킹 여부: 논블락킹 지원 vs 블락킹만 지원
특이사항: Selector 지원 vs x

##### Channel과 Buffer (ex. File <-> Channel <-> Buffer)
- 데이터 read: 적절한 크기의 Buffer를 생성하고 Channel의 read() 메서드를 사용하여 데이터를 Buffer에 저장.
- 데이터 write: 데이터를 Buffer에 저장하고 Channel의 write() 메서드를 사용하여 목적지로 전달
- 초기화: clear() 메서드로 초기화하여 다시 사용 가능.
- Buffer의 종류
  - ByteBuffer, Char, Short, Int, Long, Float, Double 등 다양하게 있음.
- Buffer의 위치 속성
  - capacity: 버퍼가 저장할 수 있는 데이터의 최대 크기. 버퍼 생성시 결정되며 변경 불가
  - position: 버퍼에서의 현재 위치를 가리킴. 버퍼에서 데이터를 read/write시, 해당 위치부터 시작. Buffer에 1Byte가 추가될때마다 1증가.
  - limit: 버퍼에서 데이터를 read/write 할 수 있는 마지막 위치. limit 이후로 데이터를 read/write 불가. 최초 생성시 capacity와 동일
  - mark: 현재 position을 mark()로 지정할 수 있고 reset() 호출시 position을 mark로 이동
  - 0 <= mark <= position <= limit <= capacity
- Buffer 위치 메서드
  - flip
    - 버퍼의 limit 위치를 현재 position 위치로 이동시키고, position을 0으로 리셋. 이는 버퍼를 쓰기 모드 -> 읽기 모드로 전환하는 경우 사용한다.
    - 총 capa 1024 버퍼에 100 포지션까지 데이터를 쓰기 후 -> 읽기를 위하여 flip을 실행하면 -> limit은 100 포지션에 위치하고 포지션은 0으로 리셋된다 -> 그러면 메모리에 적재하기 위해 읽기 작업시 현재 포지션 0부터 리밋 100까지(딱 데이터가 있는 만큼만)만 읽기 작업이 가능해지는 것.
  - rewind
    - 버퍼의 포지션 위치를 0으로 리셋. limit은 유지.
    - 데이터를 처음부터 다시 읽는 경우 사용.
  - clear
    - 버퍼의 limit 위치를 capacity 위치로 이동시키고, 포지션을 0으로 리셋.
    - 즉, 버퍼를 초기화할때 사용.
```java
try (var fileChannel = FileChannel.open(file.toPath())) {
    var byteBuffer = ByteBuffer.allocateDirect(1024);
    logPosition("allocate", byteBuffer); // allocate) position:0, limit:1024, capacity:1024

    // 파일로부터 값을 읽어서 byteBuffer에 write
    fileChannel.read(byteBuffer);
    logPosition("write", byteBuffer); // write) position:12, limit:1024, capacity:1024

    // flip()을 호출하여 읽기모드 전환
    byteBuffer.flip();
    logPosition("flip1", byteBuffer); // flip1) position:0, limit:12, capacity:1024

    // 읽기모드로 전환하여 처음부터 limit(마지막 write한 위치까지)까지 읽음
    var result = StandardCharacters.UTF_8.decode(byteBuffer); 
    log.info("result: {}", result); // result: Hellow world
    logPosition("read1", byteBuffer); // read1) position:12, limit:12, capacity:1024

    // 다시 읽기를 위한 포지션 위치 초기화
    byteBuffer.rewind();
    logPosition("rewind", byteBuffer); // rewind) position:0, limit:12, capacity:1024

    // 한번더 읽기
    var result2 = StandardCharacters.UTF_8.decode(byteBuffer); 
    log.info("result2: {}", result2); // result2: Hellow world
    logPosition("read2", byteBuffer); // read2) position:12, limit:12, capacity:1024

    // rewind 없이 또 한 번 읽어보기
    // 포지션:12 리밋:12인 상태이므로 더 읽어들일 위치가 아니므로 출력되는 결과물이 없음.
    var result3 = StandardCharacters.UTF_8.decode(byteBuffer); 
    log.info("result3: {}", result3); // result2: 
    logPosition("read3", byteBuffer); // read3) position:12, limit:12, capacity:1024

    // 초기화
    byteBuffer.clear();
    logPosition("clear", byteBuffer); // clear) position:0, limit:1024, capacity:1024
}
```

##### Java NIO는 어떻게 커널 버퍼에 직접 접근할까?
###### Buffer의 종류
- DirectByteBuffer
  - native 메모리(off-heap)에 저장
  - 커널 메모리에서 복사를 하지 않으므로 데이터를 읽고 쓰는 속도가 빠름
  - 비용이 많이 드는 system call을 직접 사용하므로 allocate,deallocate이 느림
- HeapByteBuffer
  - JVM heap 메모리에 저장. byte array 랩핑.
  - 커널 메모리에서 복사가 일어나므로 데이터를 읽고 쓰는 속도가 느림
  - 이 과정에서 내부적으로 임시로 Direct Buffer를 만들기 떄문에 성능 저하
  - gc에서 관리가 되므로 allocate,deallocate가 빠름
- 구분
```java
// DirectByteBuffer
var directByteBuffer = ByteBuffer.allocateDirect(1024);
assert directByteBuffer.isDirect();

// HeapByteBuffer
var heapByteBuffer = ByteBuffer.allocate(1024);
assert !heapByteBuffer.isDirect();

// HeapByteBuffer
var byteBufferByWrap = ByteBuffer.wrap("hello".getBytes());
assert !byteBufferByWrap.isDirect();
```

###### FileChannel - read
```java
var file = new File(FileChannelReadExample.class
    .getClassLoader()
    .getResource("hello.txt")
    .getFile());

try (var fileChannel = FileChannel.open(file.toPath())) {
    var byteBuffer = ByteBuffer.allocateDirect(1024);
    fileChannel.read(byteBuffer);
    byteBuffer.flip();

    var result = StandardCharsets.UTF_8.decode(byteBuffer);
    log.info("result: {]", result); // Hello world
}
```

###### FileChannel - write
```java
var file = new File(FileChannelReadExample.class
    .getClassLoader()
    .getResource("hello.txt")
    .getFile());

// write는 별도로 모드 인자를 제공해야함.
var mode = StandardOpenOption.WRITE;
try (var fileChannel = FileChannel.open(file.toPath(), mode)) {
    var byteBuffer = ByteBuffer.wrap("hellow world2".getBytes());
    var result = fileChannel.write(byteBuffer);
    log.info("result: {]", result); // hello world2
}
```

###### Client SocketChannel - read,write
```java
try (var socketChannel = SocketChannel.open()) {
    var addr = new InetSocketAddress("localhost", 8080);
    // 서버의 localhost:8080 소켓 연결
    var connected = socketChannel.connect(addr);
    log.info("connected: {}", connected); // connected: true

    String request = "This is client.";
    // 힙 바이트 버퍼
    ByteBuffer requestBuffer = ByteBuffer.wrap(request.getBytes());
    // 소켓 전송
    socketChannel.write(requestBuffer);
    // 전송한 버퍼 클리어
    requestBuffer.clear();

    // 서버 응답 읽기용 다이렉트 바이트 버퍼
    ByteBuffer res = ByteBuffer.allocateDirect(1024);
    // 응답 읽기 준비
    while (socketChannel.read(res) > 0) {
        // 읽기용 (버퍼 포지션과 리밋 조정)
        res.flip();
        // 서버 응답 메시지 출력
        log.info("res: {}", StandardCharsets.UTF_8.decode(res)); // res: This is server.
        res.clear();
    }
}
```

###### ServerSocketChannel - read,write
```java
try (var serverChannel = ServerSocketChannel.open()) {
    var addr = new InetSocketAddress("localhost", 8080);
    serverChannel.bind(addr);

    // 클라이언트와 연결될때까지 블록킹
    try (var clientSocker = serverChannel.accept()) {
        ByteBuffer buffer = ByteBuffer.allocateDirect(1024);
        clientSocket.read(buffer);
        buffer.flip();

        var request = new String(buffer.array().trim());
        log.info("request: {}", request); // request: This is client.

        var response = "This is server.";
        var responseBuffer = ByteBuffer.wrap(response.getBytes());
        clientSocket.write(responseBuffer);
        responseBuffer.flip();
    }
}
```

##### Java NIO를 논블록킹하게 쓰러면?
- SelectableChannel 인터페이스를 먼저 알아야함.
- 상속관계: SocketChannel, ServerSocketChannel -> AbstractSelectableChannel -> SelectableChannel
- SelectableChannel
```java
public abstract class SelectableChannel 
    extends AbstractInterruptibleChannel 
    implements Channel 
{

    // serverSocketChannel.accept, socketChannel.connect 등이 논블록킹으로 동작.
    public abstract SelectableChannel configureBlocking(boolean block) throws IOException;

    public final SelectionKey register(Selector sel, int ops) throws ClosedChannelException { ... }
}
```
###### 위의 configureBlocking의 적용예시

###### ServerSocketChannel - 논블록킹 accept
```java
try (var serverChannel = ServerSocketChannel.open()) {
    var addr = new InetSocketAddress("localhost", 8080);
    serverChannel.bind(addr);
    // 논블록킹으로 설정(디폴트 true. 블록킹 way)
    serverChannel.configureBlocking(false);

    // 논블록킹으로 동작. 바로 다음 라인으로 넘어간다.
    var clientSocket = serverChannel.accept();
    // 논블록킹으로 동작하였으므로 아직 클라이언트와 연결되지 않아 바로 null이 내려옴
    assert clientSocket == null;
}
```

###### ServerSocketChannel - 논블록킹 accept
```java
try (var socketChannel = SocketChannel.open()) {
    var addr = new InetSocketAddress("localhost", 8080);
    // 논블록킹 설정
    socketChannel.configureBlocking(false);

    // 논블록킹 동작. 바로 다음 라인으로 넘어간다.
    var connected = socketChannel.connect(addr);
    assert !connected; // 논블록킹 동작하였으므로 즉시 false;
}
```

###### FileChannel
```java
public abstract class FileChannel 
    extends AbstractInterruptibleChannel 
    implements SeekableByteChannel, GatheringByteChannel, ScatteringByteChannel
{ ... }
```
- SelectableChannel을 구현하고 있지 않아 모든 FILE I/O는 블록킹 동작.
- 때문에 FileChannel.open(...) 후 fileChannel.configureBlocking(false);라는 함수는 존재하지 않음.
- 즉 자바 NIO에서 모든 I/O는 논블록킹으로 동작할수는 없음.

### Java AIO(NIO2)

- since Java 1.7
- AsynchronousChannel 지원
  - AsynchronousSocketChannel -> AsynchronousByteChannel -> AsynchronousChannel
  - AsynchronousServerSocketChannel -> AsynchronousChannel
  - AsynchronousFileChannel -> AsynchronousChannel
- callback과 future 지원.
  
![screenshot](./Images/java_aio.png) 
- Thread pool과 epoll, kqueue 등의 이벤트 알림 system call을 이용
- I/O가 준비되었을때, Future 또는 callback으로 비동기적인 로직 처리.

#### AsynchronousFileChannel - callback 방식
```java
var file = new File(
    AsyncFileChannelReadCallbackExample.class
        .getClassLoader()
        .getResource("hello.txt")
        .getFile()
);

var channel = AsynchronousFileChannel.open(file.toPath());
ByteBuffer buffer = ByteBuffer.allocateDirect(1024);

/**
 * 첫번째 인자: ByteBuffer
 * 두번째: 버퍼의 읽기 시작 포지션
 * 세번째: Object attachment 전달 인자
 * 네번째: 콜백 함수
 */ 
channel.read(buffer, 0, null, new CompletionHandler<>() {
    @SneakyThrows
    @Override
    public void completed(Integer result, Object attachment) {
        buffer.flip();
        var resultString = StandardCharsets.UTF_8.decode(buffer);
        log.info("result: {}", resultString);
        channel.close();
    }

    @Override
    public void failed(Throwable ex, Object attachment) { ... }
});

// 채널 대기동안 로그 출력.
while (channel.isOpen()) {
    log.info("Reading...");
}
```

#### AsynchronousFileChannel - future 방식
```java
var file = new File(
    AsyncFileChannelReadCallbackExample.class
        .getClassLoader()
        .getResource("hello.txt")
        .getFile()
);

try(var channel = AsynchronousFileChannel.open(file.toPath())) {
    var buffer = ByteBuffer.allocateDirect(1024);
    // Future 방식으로 별도 콜백 함수를 인자 전달 X
    Future<Integer> channelRead = channel.read(buffer, 0);

    // 읽기 대기.
    // 콜백방식보다는 간결하지만 while문을 통한 지속적 체크를 통한 리소스 낭비가 있음.
    while (!channelRead.isDone()) {
        log.info("Reading...");
    }

    buffer.flip();
    var result = StandardCharsets.UTF_8.decode(buffer);
    log.ingo("result: {}", result);
}
```

#### AsynchronousServerSocketChannel - callback 방식
```java
/**
 * 첫번째 인자: Object attachement
 * 두번째: 컴플리션 핸들러 콜백
 */ 
// 기존 Java I/O의 serverSocketChannel이 바로 ClientChannel을 반환하던 것과 달리 콜백 completed 함수에서 clientChannel 사용.
serverSocketChannel.accept(null, new CompletionHandler<>() {
    @Override
    public void completed(AsynchronousSocketChannel clientChannel, Object attachment) {
        var requestBuffer = ByteBuffer.allocateDirect(1024);

        clientSocket.read(requestBuffer, null, new CompletionHandler<>() {
            @SneakyThrows
            @Override
            public void completed(Integer a, Object attachment) {
                requestBuffer.flip();
                var request = StandardCharsets.UTF_8.decode(requestBuffer);
                log.info("request: {}", request);

                var response = "This is server.";
                var responseBuffer = ByteBuffer.wrap(response.getBytes());
                clientSocket.write(responseBuffer);
                clientSocket.close();
                log.info("end client");
            }

            @Override
            public void failed(Throwable ex, Object attachment) { ... }
        });

        @Override
            public void failed(Throwable ex, Object attachment) { ... }
    }
});
```

#### AsynchronousServerSocketChannel - future 방식
```java
var serverSocketChannel = AsynchronousServerSocketChannel.open();
var addr = new InetSocketAddress("localhost", 8080);
serverSocketChannel.bind(addr);

// 콜백방식과 달리 Future를 바로 반환.
Future<AsynchronousSocketChannel> clientSocketFuture = serverSocketChannel.accpet();
// Future 완료까지 대기.
while (!clientSocketFuture.isDone()) {
    Thread.sleep(100);
    log.info("Waiting...");
}

// Future가 준비되어 읽기 시작
var clientSocket = clientSocketFuture.get();

var requestBuffer = ByteBuffer.allocateDirect(1024);
Future<Integer> channelRead = clientSocket.read(requestBuffer);
while (!channelRead.isDone()) {
    log.info("Reading...");
}

requestBufer.flip();
var request = StandardCharsets.UTF_8.decode(requestBuffer);
log.info("request: {}", request);

var response = "This is server.";
var responseBuffer = ByteBuffer.wrap(response.getBytes());
clientSocket.write(responseBuffer);
clientSocket.close();
```

## JAVA AIO의 다음.
Java NIO를 사용하며 논블록킹이 되었지만 여전히 찝찝한 것들이 남아있었다.
응답 대기를 위한 while문을 사용을 좀 더 최적하기 위해서는?
=> reactor pattern
