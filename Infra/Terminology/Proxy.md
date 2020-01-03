# Proxy

## What is Proxy

```plantuml

skinparam rectangle {
    BackgroundColor DarkSeaGreen
    FontStyle Bold
    FontColor DarkGreen
}
(internetA) as a
rectangle proxy as p
(internetB) as b

a -> p
p -> b
b -> p
p -> a
```

- 프록시 서버는 클라이언트가 자신을 통해서 다른 네트워크 서비스에 간접적으로 접속할 수 있게 해 주는 컴퓨터 시스템이나 응용 프로그램을 가리킴
- 서버와 클라이언트 사이에 중계기로서 대리로 통신을 수행하는 것을 가리켜 `Proxy`
- 그 중계 기능을 하는 것을 `Proxy Server`

## Advantage with Proxy

- 프록시 서버에 요청된 내용들을 캐시를 이용하여 저장해 두고, 요청 정보가 이미 캐시 안에 존재하고 있다면, 원격 서버에 접속할 필요가 없어지므로 전송 시간을 절약할 수 있게 됨과 동시에 불필요한 외부와의 연결을 줄일 수 있다.
- 이로써 외부와의 트래픽을 줄이게 됨으로써 네트워크 병목 현상을 방지하는 효과도 얻는다.
- 익명으로 서버를 유지 가능

## Kinds

### Forward Proxy

```plantuml
left to right direction

rectangle clients {
    actor client as a
    actor client as b
    actor client as c
    actor client as d
}

rectangle proxy {
    rectangle ForwardProxy as fp
    (firewall) as fw
    fp -> fw
}

(internet)
(server)

a --> fp
b --> fp
c --> fp
d --> fp: Large number of clients \nwith long-term keepalive conntections
fw --> internet: Reduces connections \nto the minimum number \nnecessary
internet --> server

```

- 클라이언트의 웹 서버 요청이 Proxy 서버에게 전달되고, Proxy 서버는 그 요청을 웹 서버에게 전달하여 받아와 클라이언트에게 돌려준다.
- Usage
  - Content Filter
  - Email Security
  - NAT
  - Compliance Repot

### Reverse Proxy

```plantuml
left to right direction
actor client
(internet)
rectangle proxy {
    rectangle ReverseProxy as rp
    (firewall) as fw
    fw -> rp
}
rectangle servers {
  (server1) as s1
  (server2) as s2
  (server3) as s3
}

client --> internet
internet --> fw
rp --> s1
rp --> s2
rp --> s3: load balancing

```

- 클라이언트는 웹 서버의 주소가 아닌 Reverse Proxy로 설정된 주소로 요청을 하게 되고, Proxy 서버가 받아 그 뒷단에 숨어 있는 웹 서버에게 다시 요청을 전달하는 방식
- 클라이언트에게 웹 서버의 정보를 숨길 수 있다.
- Usage
  - Load Balancing
  - SSL Offload/Acceration
  - Caching
  - Compression
  - Content Switching/Redirection
  - Application Firewall
  - Server Obfuscation
  - Authentication
  - Single Sign On
