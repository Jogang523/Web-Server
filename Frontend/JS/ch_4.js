// 1. 대입 연산자 : 오른쪽의 값을 왼쪽에 변수에 할당
let var1 = 1;

// 2. 산술 연산자
let num1 = 3 + 2;
let num2 = 3 - 2;
let num3 = 3 * 2;
let num4 = 3 / 2;
let num5 = 3 % 2;

let num6 = (1+2) * 10;

// 3. 복합 대입 연산자
let num7  = 10;
num7 += 20; // 30
num7 -= 20; // 10
num7 *= 20; // 200

// 4. 증감 연산자
let num8 = 10;
console.log(num8++); // 10
console.log(++num8); // 12

// 5. 논리 연산자

let or = true || false; // true
let and = true && false; // false
let not = !true; // false

// 6. 비교 연산자
let com1 = 1 == '1'; // true
let com2 = 1 != '1'; // false

let com3 = 1 === '1'; // false
let com4 = 1 !== '1'; // true

console.log(com1, com2, com3, com4)

let com5 = 2 > 1;
let com6 = 2 < 1;

let com7 = 2 >= 1;
let com8 = 2 <= 1;

console.log(com5, com6, com7, com8)