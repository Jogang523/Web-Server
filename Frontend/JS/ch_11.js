// scope
// 전역변수 : 프로그램 전체에서 사용 가능한 변수
// 지역변수 : 특정 함수, 영역 내에서만 사용하는 변수
// 전역변수 저장공간, 지역변수 저장공간이별도로 존재
// 지역변수 저장공간은 블록별로 여러개가 존재
// 특정 블록 내에서는 그 블록에 할당된 지역변수 저장공간에 저장된 값만 사용이 가능
// 특정 블록 내에서 변수를 찾았는데 없으면, 전역변수 저장공간에 가서 값을 찾아서 출력

let a = 1; // 전역변수

function funcA(){
    let b = 2; // 지역변수
    console.log(a);
    console.log(b);
}

funcA();

if (true){
    let c =1;
    console.log(c);
}

//console.log(c); // 에러 발생

for (let i=0; i < 10; i++){
    let d = 1;
    console.log(d);
}

function funcB(){
    let b=2;
    console.log(b);

    function funcC(){
        console.log(c);
        console.log(a);
    }
    funcC();
}
funcB();