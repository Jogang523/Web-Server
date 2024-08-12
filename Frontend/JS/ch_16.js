let varA = false;
let varB = true;

// && : 왼쪽이 falsy하면 그 값을 반환, 그렇지 않으면 오른쪽 값을 반환
// || : 왼쪽이 truthy하면 그 값을 반환, 그렇지 않으면 오른쪽 값을 반환

console.log(varA && varB);
console.log(varA || varB);

function returnFalse() {
    console.log('returnFalse함수...');
    return false;
}

function returnTrue() {
    console.log('returnTrue함수...');
    return true;
}

console.log(returnFalse() && returnTrue());  // returnFalse()까지만 실행
console.log(returnFalse() || returnTrue());  // returnFalse(), returnTrue() 모두 실행 후 출력함..

function printName(person) {
    const name = person && person.name;
    console.log(name || "person의 값이 없음");
}

printName({name: '박민호'})