// 1. Spread 연산자
// -> 뿌리다, 펼치다
// 객체나 배열에 저장된 여러 개의 값들을 펼쳐주는 역할...

let arr1 = [1,2,3];

let arr2 = [4, ...arr1, 5, 6]

console.log(arr2);

let obj1 = {
    a:1,
    b:2,
};

let obj2 = {
    ...obj1,
    c:3,
    d:4,
};

console.log(obj2);


function funcA(p1, p2, p3) {
    console.log(p1, p2, p3);
}

funcA(...arr1);

// Reset 매개변수 
// -> Reset는 나머지, 나머지 매개변수, reset 매개변수는 마지막에 위치해야 한다..
// 가변매개변수와 유사 => *var

function funcB(one, two, ...ds) {
    console.log(ds);
}

funcB(...arr1);