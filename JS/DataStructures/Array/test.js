var nameArray = ["Jack", "is", "Miller"];
var resultArray1 = nameArray;
nameArray = [];
console.log(nameArray);
console.log(resultArray1);

var nameArray2 = ["I", "am", "Adam"];
var resultArray2 = nameArray2.concat();
nameArray2 = [];
console.log(nameArray2);
console.log(resultArray2);

var nameArray = ["Jack", "is", "Miller"];
                var nameArray2 = ["But", "Miller", "is", "not", "Jack"];
                var newArray = nameArray.concat(nameArray2);
                console.log(newArray); // 