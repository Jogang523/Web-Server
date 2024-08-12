// 1. 배열의 구조 분해 할당
let arr = [1,2,3];

let one = arr[0];
let two = arr[1];
let three = arr[2];

console.log(one, two, three);

let [one1, two1, three1] = arr;  
console.log(one1, two1, three1);

let [one2, two2, three2, four=4] = arr;
console.log(one2, two2, three2, four);

// 2. 객체의 구조 분해 할당
let person = {
    name: '박민호', 
    age : 27,
    hobby: '테니스',
};

let {
    age: myAge,
    hobby, 
    name, 
    extra='hello',
} = person;

console.log(myAge, hobby, name, extra);

// 3. 객체 구조 분해 할당을 이용해서 함수 매개변수 전달
const func = ({name, age, hobby, extra=4}) => {
    console.log(name, age, hobby, extra);
};

func(person);