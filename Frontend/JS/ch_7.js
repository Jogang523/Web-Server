// 반복문

for(let idx=1; idx<=10; idx++){
    console.log(idx);

    if(idx%2 === 0){
        continue; // 아래를 실행하지 않고 반복문 처음으로 회귀
    }

    if(idx >= 5){
        break; // 반복문을 빠져나온다
    }
}
