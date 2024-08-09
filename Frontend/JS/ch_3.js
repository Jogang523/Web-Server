// 형변환

// 1. 묵시적 형변환(타입 캐스팅) - 자바스크립트 엔진이 자동으로 형변환

let num = 10;
let str = '20';

const result = num + str; // 숫자가 문자열로 변환

// 2. 명시적 형 변환(타입 캐스팅) - 개발자가 직접 형변환

let str1 = '10';
let strTOnum = Number(str1); // 문자열을 숫자로 변환

let str2 = '10개';
let strTOnum2 = parseInt(str2); // 문자열에서 숫자만 추출


let num1 = 20;
let numTostr = String(num1); // 숫자를 문자열로 변환

console.log(numTostr+'입니다.')