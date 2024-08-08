// 1. number type

let num1 = 27;
let num2 = 1.5;
let num3 = -20;

let inf = Infinity;
let mInf = -Infinity;

let nan = NaN;

console.log(2*'hello')
console.log(num1)
console.log(num2)
console.log(num3)


//2. string type

let myName='조갱';
let myLocation='서울';
let introduce = myName+' '+myLocation;

console.log(introduce)

// "`" backtick ES6부터 최근에 추가된 템플릿 리터럴이라는 문법입니다.
// "`" backtick은 문자열로 취급하지만 ${} 안에는 변수나 식을 넣을 수 있다..

let introduceText= `${myName}은 ${myLocation}에 살고 있습니다.`;
console.log(introduceText)

//3. boolean type

let isTrue = true;
let isFalse = false;

console.log(isTrue)
console.log(isFalse)

//4. Null type - 값이 존재 하지 않음

let empty = null;

console.log(empty)

//5. Undefined type - 값이 할당되지 않음

let none;
console.log(none)