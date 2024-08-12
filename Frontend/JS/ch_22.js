// 배열에서 6가지 요소 조작 메서드
// 1. push
// 배열에 맨 뒤에 새로운 요소를 추가하는 메서드

let arr = [1,2,3];
arr.push(10);
console.log('push 결과 : ',arr);

// 2. pop
// 맨 마지막 요소를 제거 하면서, 제거된 요소를 리턴...
let arr2 = [1,2,3];
const result = arr2.pop();
console.log('pop 결과 : ',result);

// 3. shift
// 배열의 맨 앞 요소를 제거하고, 제거된 요소를 반환
let arr3 = [1,2,3];
const result2 = arr3.shift();
console.log('shift 결과 : ',result2);

// 4. unshift
// 배열의 맨 앞에 요소를 추가
let arr4 = [1,2,3];
const result3 = arr4.unshift(0);
console.log('unshift 결과 : ',result3);

//  5. slice
// 배열의 일부분을 추출하여 새로운 배열로 반환
let arr5 = [1,2,3,4,5];
const result4 = arr5.slice(1,3);
console.log('slice 결과 : ',result4);

// 6. concat
// 배열을 합쳐서 새로운 배열을 반환
let arr6 = [1,2,3];
let arr7 = [4,5,6];
const result5 = arr6.concat(arr7);
console.log('concat 결과 : ',result5);