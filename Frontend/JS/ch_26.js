// setTimeout(함수, 시간) : 시간이 지난 후 함수를 실행
// 비동기 처리 함수
console.log(1);

setTimeout(
    ()=>{
        console.log(2);
    }, 3000
);

console.log(3);