// 1. 배열 순회

let arr = [1,2,3,4,5];

// 1-1 배열 인덱스를 순회
for (let i = 0; i < arr.length; i++){
    console.log('for문 결과 : ',arr[i]);
}

// 1-2 for ~ of 문을 사용한 배열 순회
for (let value of arr){
    console.log('for ~ of 결과 : ',value);
}
//for ~ of 문은 배열에서만 사용 가능하다.

// 객체 순회
let person = {
    name : '홍길동',
    age : 27,
    hobby : '테니스'
}
// 2-1 객체의 key를 순회
let keys = Object.keys(person);

for (let key of keys){ 
    const value = person[key];
    console.log('key : ',key, 'value : ',value);
}

// 2-2 객체의 value를 순회
let values = Object.values(person);

for (let value of values){
    console.log('value : ',value);
} 

// 2-3 객체의 for ~ in 반복문을 사용 - 객체에서만 사용 가능

for (let key in person){
    const value = person[key];
    console.log('key : ',key, 'value : ',value);
}