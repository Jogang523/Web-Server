// 원시타입 - number, string, boolean, null, undefined
// 변수에 저장할 경우, 값 자체로 저장되고 복사된다 - 깊은 복사

// 객체타입 - object, array, function
// 변수에 저장할 경우, 값이 복사되는 것이 아니라, 값이 저장되어 있는 주소값(참조값)이 복사된다 - 앝은 복사 - 주소값을 공유

let p1 = 1;
let p2 = p1;  // 깊은 복사

p2 = 10;

console.log(p1, p2);


let o1 = {name : '김민호'};
let o2 = o1;   // 앝은 복사 - 주소값을 공유

o2.name = '박철순';

console.log(o1, o2);

 o2 = {...o1}; // Spread연산자 이용 : 새로운 객체를 생성하고 새로운 주소값을 갖는다 -  깊은 복사

 o2.name = '이정훈';

 console.log(o1, o2);



 // 얕은 비교, 깊은 비교

 let o3 = {name:'박기훈', age:27};
 let o4 = o3;   // 얕은 복사
 let o5 = {...o3};  // 깊은 복사

 // 얕은 비교
 console.log(o3 === o4);  // 동일한 객체를 참조
 console.log(o3 === o5);  // 다른 객체를 참조
 console.log(o4 === o5);  // 다른 객체를 참조

// 깊은 비교
console.log(JSON.stringify(o3) === JSON.stringify(o5));  // 객체를 문자열로 변환해서 비교..

