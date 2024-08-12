// 5가지 변형 메서드

// 1. filter
// 기존 배열에서 조건을 만족하는 요소들만 필터링 하여 새로운 배열로 변환..
let arr1 = [
    {name:'박철순', hobby:'테니스'},
    {name:'강호동', hobby:'테니스'},
    {name:'유재석', hobby:'독서'}
];

const tennisArr = arr1.filter(
    (item) => {
        if (item.hobby==='테니스') return true;
    }
);

console.log('filter 결과 : ',tennisArr);
console.log('-------------------');

// 2. map
// 배열의 모든 요소를 순회하면서, 각각의 요소에 특정 동작을 수행시키는 메서드

let arr2 = [1,2,3,4,5];

const mapResult = arr2.map( 
    (item, idx, arr) => {
        return item*2;
    }
);

console.log('map 결과 : ',mapResult);
console.log('-------------------');

// 3. sort 
// 배열을 정렬하는 메서드
let arr3 = ['a','c','b'];
arr3.sort();
console.log('sort 결과 : ',arr3);
console.log('-------------------');

// 4. toSorted
let arr4 = ['a','c','b'];
const sortResult = arr4.toSorted()
console.log('toSorted 결과 : ',sortResult);
console.log('-------------------');

// 5. join
// 배열의 모든 요소를 문자열로 변환하는 메서드
let arr5 = ['hi','im','winterlood'];
const joinResult = arr5.join(' ');
console.log('join 결과 : ',joinResult);
console.log('-------------------');