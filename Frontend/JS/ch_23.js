// 5가지 요소 순회 및 탐색 메서드

// 1. forEach
//  모든 요소를 순회 하면서, 각각의 요소에 특정 동작을 수행시키는 메서드
let arr = [1,2,3,4,5];

arr.forEach(function(item, idx, arr){
    console.log('forEach 결과1 : ',idx, item*2); // idx는 인덱스, item은 요소, arr은 배열
}
);
console.log('-------------------');

let doubleArr = [];
arr.forEach(function(item){
    doubleArr.push(item*2);
});
console.log('forEach 결과2 : ',doubleArr);
console.log('-------------------');
// 2. includes
// 배열에 특정 요소가 포함되어 있는지 확인하는 메서드
let arr2 = [1,2,3,4,5];
let isInclude = arr2.includes(10);
console.log('includes 결과 : ',isInclude);
console.log('-------------------');

// 3. indexOf
// 배열에 특정 요소가 몇 번째 인덱스에 위치하는지 확인하는 메서드
let arr3 = [1,2,3,4,5];
let idx0 = arr3.indexOf(3);
let idx1 = arr3.indexOf(10);//-1
console.log('indexOf 결과 : ',idx0, idx1);
console.log('-------------------');

// 4. findIndex
// 배열에서 특정 조건을 만족하는 요소의 인덱스를 반환하는 메서드
let arr4 = [1,2,3,4,5];
const findIndex = arr4.findIndex(
    (item) =>{
        if (item === 2){
            return true;
        }
    }
);
console.log('findIndex 결과 : ',findIndex);
console.log('-------------------');

// 5. find - python의 filter와 비슷한 역할
// 모든 요소를 순회 하면서 콜백 함수를 만족하는 요소를 반환
let arr5 = [
    {name:'박철순'},
    {name:'홍길동'},
];

const finded = arr5.find(
    (item) => item.name === '홍길동');
console.log('find 결과 : ',finded);
