// 1. 배열 - 순차적으로 값을 담는 것

let arrA = new Array(); // 배열 생성자를 이용한 배열 생성
let arrB = []; // 배열 리터럴을 이용한 배열 생성 - 대부분 사용

let arrC =[
    1,
    2,
    3,
    true,
    'string',
    null,
    undefined,
    () => {console.log('hello')}, // 화살표 함수
    {},// 빈 객체
    [] // 빈 배열
];

// 2. 배열 요소 접근

let itme1 = arrC[0];
let itme2 = arrC[1];

console.log(itme1, itme2);
console.log(arrC);

