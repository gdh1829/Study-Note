Javascript's Array
======================

1. Array
Generally, Array is a collection set that stores elements in regular sequence so as to access to each element by using integer index(offest).
일반적 프로그래밍 언어에서 배열은 정수 index(offset)를 이용해 각 요소에 접근할 수 있게 순차적으로 요소를 저장한 집합체이다.

However, JS offers different types of Array defined above unlike general programming languages.
JS에서는 위와 같은 일반적 프로그래밍 언어와는 다른 종류의 Array를 제공한다. JS의 Array는 특화된 JS 객체이며 integer index(객체의 property's name)로 객체 내 데이터 offset을 포현한다. 정수를 index로 사용하면 JS 객체 요구사항에 맞게 내부적으로 정수를 String으로 변환한다. JS에서 공식적으로 제공하는 객체이므로 미리 정의된 property와 function을 이용할 수 있다.

JS는 한 배열이 다양한 타입의 elements를 포함할 수 있다. JS는 Function도 Argument로서 사용 가능.
    <pre>
        <code>
            var mixedTypeArray = [1, "Joe", true, null, undefined, function abc() { return "function is in Array" }];
            console.log(mixedTypeArray); // [ 1, 'Joe', true, null, undefined, [Function: abc] ]
            console.log(mixedTypeArray[mixedTypeArray.length-1]()); // function is in array
        </code>
    <pre>
Shallow copy와 Deep copy
shallow copy란 call by reference. 즉, Array를 다른 Array로 할당할 때 실제로는 할당된 Array의 Reference를 할당하는 것. 즉, Original Array가 바뀌면 할당된 Array도 데이터가 바뀐다.
Deep copy란 shallow copy의 반대 개념이다. 객체로서 전체를 할당하지 말고, 객체 내부의 데이터를 하나하나 옮기면 된다.
<pre>
    <code>
        function copy(arr1, arr2) {
            for(var i=0; i < arr1.length; i++) {
                arr2[i] = arr1[i];
            }
        }
        var nums = [1,2,3];
        var copyedNums = [];
        copy(nums, copyedNums);
        console.log(copyedNums); //[1,2,3]
    </code>
        !!이상한 점 하나 발견..! call by reference인데, 왜 resultArray1의 출력값이 []가 아닌거지??? 후에 다시 확인!!!
    <code>
        var nameArray = ["Jack", "is", "Miller"];
        var resultArray1 = nameArray;
        nameArray = [];
        console.log(nameArray); // []
        console.log(resultArray1); // ["Jack", "is", "Miller"]

        var nameArray2 = ["I", "am", "Adam"];
        var resultArray2 = nameArray2.concat();
        nameArray2 = [];
        console.log(nameArray2); // []
        console.log(resultArray2);  // ["Jack", "is", "Miller"]
    </code>

<pre>

2. How to make Array 
    <pre>
        <code>
            //대괄호
            var array = [];
            //대괄호를 이용한 Array 생성과 함께 내부 elemets 함께 구성
            var array = [1,2,3,4,5];
            // Array() 생성자
            var array = new Array();
            // Array() 생성자와 함께 내부 elements 구성
            var array = new Array(1,2,3,4,5);
            // length가 5인 Array 생성
            var array = new Array(5);
        </code>
        .length property를 통해 제대로 생성되었는지 확인 가능.
    <pre>
    > 더글라스 크락포드의 JS 핵심 가이드에서는 Array 생성자 호출 방식보다는 []를 사용한 방법이 더 효율적이라고 한다.
3. JS Array의 기본 내장 Methods 또는 관련 Methods
    
    * Array.isArray(var variable) return boolean
        args가 Array인지 아닌지 알려준다.
    * String.split(var delimeter) return Array
        argument로 주어진 delimeter를 기준으로 String을 Array로 만듭니다.
    <pre>
        <code>
            var sentence = "Jack is in the house";
            var array = sentence.split(" ");
            console.log(array); // ["Jack", "is", "in", "the", "house"]
        </code>
    <pre>
    * Accessor Function of Array
        Array.indexOf(var target) return integer
            찾고 싶은 var target이 array에 있는지 알려준다. 있다 => index number / 없다 => -1
            만약 복수의 같은 values가 있다면 가장 첫번째로 발견한 element의 index를 반환한다.
        Array.lastIndexOf(var target) return integer
            indexOf()와 같은 역할이지만 가장 마지막 element의 index를 반환한다. 
    * Array를 String으로 표현
        Array.join() return String
            해당 Array를 String으로 표현해준다. Array의 각 values는 쉼표(,)로 연결된다.
    <pre>
        <code>
            var nameArray = ["Jack", "is", "Miller"];
            console.log(nameArray.join()); //Jack,is,Miller
        </code>
    <pre>
        Array.toString() return String
            join과 같은 역할이다. 역시 쉼표(,)로 연결된다.
            단, toString은 모든 객체의 부모인 Object의 Method로서 출력시 명시적으로 입력하지 않아도 그 자손 객체들의 출력이라면 자동 적용된다.
    * 기존 Array를 이용하여 New Array 만들기
        Array.concat(value1[, value2[, ...[, valueN]]]) return New Array
            두 개 이상의 배열을 합쳐 새 배열을 만든다.
            without Argus
                기존 Array가 새로운 Array로 deep copy되어 반환된다.
            with Argus
                기준 Array 뒤로 Argus Array가 뒤로 Append되어 새로운 Array가 탄생한다.
            <pre><code>
                var nameArray = ["Jack", "is", "Miller"];
                var nameArray2 = ["But", "Miller", "is", "not", "Jack"];
                var newArray = nameArray.concat(nameArray2);
                console.log(newArray); // [ 'Jack', 'is', 'Miller', 'But', 'Miller', 'is', 'not', 'Jack' ]
            </code><pre>
        Array.splice(start, deleteCount[, item1[, item2[, ...]]]])
            기존 배열의 서브셋으로 새 배열을 만든다.
            start(Integer) : 사용할 첫 element의 index
            deleteCount(Integer) : [optional] elements를 삭제할 경우, 몇개의 elements를 삭제할 것인지. 
            itemN(Element) : [optional] elements를 새롭게 추가하는 경우, 넣고 싶은 elements.
    * Mutator Function of Array
