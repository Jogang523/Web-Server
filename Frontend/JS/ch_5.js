// 1. null 병합 연산자

let var1;
let var2 = 10;
let var3 = 20;

let var4 = var1 ?? var2; //var1이 null이나 undefined이면 var2를 출력, 아니면 var1을 출력
let var5 = var1 ?? var3;
let var6 = var2 ?? var3;



let userName;
let userNickName = '조갱';

let displayName = userName ?? userNickName;

console.log('null 병합 연산자 결과 :' ,var4, var5, var6 , displayName);

// 2. typeof 연산자 - 값의 타입을 리턴

let var7 = 10;
var7 = 'hello';
var7 = true;

let t1 = typeof var7;

console.log('typeof 연산자 결과 :' ,t1);

// 3. 삼황 연산자
// -> 항을 3개 사용하는 연산자
// 조건식을 따라서, 참, 거짓에 따라서 다른 값을 반환
// 조건 ? v1 : b2 => 조건이 참이면 v1, 거짓이면 v2

let var8 = 10;

let res = var8 % 2 === 0 ? '짝수' : '홀수';
console.log('삼황 연산자 결과 : ',res);
