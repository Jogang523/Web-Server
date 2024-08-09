let varA = false;
let varB = true;

console.log(varA && varB);
console.log(varA || varB);

function returnFalse(){
    console.log('returnFalse');
    return false;
}

function returnTrue(){
    console.log('returnTrue');
    return true;
}

console.log(returnFalse() && returnTrue());
console.log(returnFalse() || returnTrue());

function printName(person){
    const name = person && person.name;
    console.log(name||'이름이 없습니다');
}

printName({name : '박민호'});