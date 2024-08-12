    // 1. 콜백 함수

    function main(value){ // 함수를 매개변수로 받음
        value()
    }

    function sub(){
        console.log('CallBack 함수 결과1 : ','sub 함수 실행');
    }

    main(sub);

    main(
        function () { // 익명함수를 매개변수로 받음
        console.log('CallBack 함수 결과2 : ','sub 함수 실행2');
    });

    main(
        () => {
            console.log('CallBack 함수 결과3 : ','sub 함수 실행3');
        }
    )

    // 2. 콜백함수의 활용

    function repeat(count, callback){
        for(let idx=1; idx <= count; idx++){
            callback(idx);
        }
    }

    repeat(5,
        function(idx){
            console.log(idx + '번째 실행');
        }
    )