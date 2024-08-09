// 1. javascript에서 false로 간주되는 것

let f1 = undefined;
let f2 = null;
let f3 = 0;
let f4 = -0;
let f5 = NaN;
let f6 = '';

if (!f1){
    console.log('f1은 false');
}

// 2. javascript에서 true로 간주되는 것

let t1 = 'hello';
let t2 = 10;
let t3 = []; //빈 배열
let t4 = {}; //빈 객체
let t5 = function(){};

if (t1){
    console.log('t1은 true');
}

// 3. 활용 예시

function printName(person){
    if (!person){
        console.log('person이 없습니다');
        return;
    }
    console.log(person.name);
}

let person = "";
printName(person);