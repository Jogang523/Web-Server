// 1. 객체 생성

let obj1 = new Object(); // 객체 생성자를 사용하여 객체 생성
let obj2 = {}; // 갹채 리터럴을 사용하여 객체 생성 - 대부분 이 방법을 사용

// 2. 객체 리터럴

let person={
    name: '박민수',
    age:27,
    hobby:'테니스',
    job:'Developer',
    extra: {},
    10:20,
    'like cat': true // 키가 문자열로 되어있으면 ''로 감싸줘야함
} ;

// 3. 객체 프로퍼티를 다루는 방법

let name = person.name; //정표기법
let age = person['age']; //대괄호 표기법

let age2 = person['age2']; // 없는 프로퍼티에 접근하면 undefined 출력

let property = 'hobby'; 
let hobby = person[property]; // 변수를 사용해서 프로퍼티에 접근할 때는 대괄호 표기법만 사용 가능

// 4. 새로운 프로퍼티를 추가하는 방법

person.job = 'Designer'; // 존재하는 프로퍼티에 접근하면 값이 변경됨
person['fav food'] = '라면'; // 없는 프로퍼티에 접근하면 새로운 프로퍼티가 추가됨

console.log(person);

// 5. 프로퍼티 수정

person.age = 30; // 존재하는 프로퍼티에 접근하면 값이 변경됨

// 6. 프로퍼티 삭제

delete person.age; // 프로퍼티 삭제
delete person['fav food']; // 프로퍼티 삭제

console.log(person);

// 7. 프로퍼티가 존재하는지 확인

let result = 'name' in person; 
console.log(result);