// 1. 상수 객체

const animal = {
    type : '고양이',
    name : '나비',
    color : '검정색'
};

animal.age = 2; // 프로퍼티 추가
animal.name = '야옹이'; // 프로퍼티 수정
delete animal.color; // 프로퍼티 삭제

console.log(animal);

// 2. 매서드
// -> 값이 함수인 프로퍼티...

const person = {
    name : '박민호',
    sayHi(){
        console.log('안녕하세요');
    },
    sayHi1 : function(){
        console.log('안녕하세요');
    },
    sayHi2 : () => {
        console.log('안녕하세요');
    }   
};

person.sayHi();
person['sayHi']();