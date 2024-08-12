// 1. Date 객체를 생성하는 방법
let date1 = new Date();
let date2 = new Date(1997, 1, 7, 23, 59, 59);
console.log(date1,date2);
console.log('-------------------');

// 2. 타임 스탬프
// 특정시간이 " 1970.01.01 00시 00분 00초 "로부터 얼마나 경과했는지를 나타내는 숫자

let ts1 = date1.getTime();
console.log(ts1);

let date3 = new Date(ts1);
console.log(date3);
console.log(date3.toLocaleDateString());
console.log('-------------------');

// 3. 시간 요소들을 추출하는 방법
let year = date3.getFullYear();
let month = date3.getMonth() + 1;
let day = date3.getDate();

let hour = date3.getHours();
let minute = date3.getMinutes();
let second = date3.getSeconds();

console.log(year, month, day, hour, minute, second);
console.log('-------------------');

// 4. 시간 수정하기
date3.setFullYear(2021);
date3.setMonth(2);
date3.setDate(30);
date3.setHours(23);
date3.setMinutes(50);
date3.setSeconds(43);

console.log(date3);
console.log('-------------------');

// 5. 시간을 여러 포맷으로 출력...
console.log(date3.toDateString());
console.log(date3.toTimeString());
console.log(date3.toLocaleString());
console.log('-------------------');
