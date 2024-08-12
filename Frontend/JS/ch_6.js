// 1. 조건문 => if / switch ~ case

// 1-1. if문

let num = 4;

if(num >= 10){
    console.log('num은 10보다 이상입니다.')
}
else if(num >= 5){
    console.log('num은 5보다 이상입니다.')
}
else if(num >= 3){
    console.log('if문 결과 : ','num은 3보다 이상입니다.')
}
else{
    console.log('num은 3보다 작습니다.')
}

//1-2. switch

let animal = 'owl';

switch(animal){
    case 'dog':
        console.log('강아지');
        break;
    case 'cat':
        console.log('고양이');
        break;
    case 'owl':
        console.log('switch문 결과 : ','올빼미');
        break;
    default:
        console.log('동물이 아닙니다.')
}

// 반복문

for(let idx=1; idx<=10; idx++){
    console.log('반복문 결과 : ',idx);

    if(idx%2 === 0){
        continue; // 아래를 실행하지 않고 반복문 처음으로 회귀
    }

    if(idx >= 5){
        break; // 반복문을 빠져나온다
    }
}
