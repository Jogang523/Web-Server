// 함수의 정의

// 1. 함수 표현식
function funcA(){
    console.log('funcA');
}

let varA = funcA

varA();

// 2. 람다식 (익명함수)

let varB = function(){
    console.log('funcB');
}
varB();

// 3. 화살표 함수

let varC = (value) => {
    console.log(value);
    return value + 1;
}

console.log(varC(10));

let varD = () => 1;

console.log(varD());

