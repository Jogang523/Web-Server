function fetchData(callback){
    setTimeout(() => {
        const data = {user: 'jinsu', age: 27};
        callback(data);
    }, 2000);
}

fetchData(
    (result) => {
        console.log('Data received : ', result);
    }
);

console.log('Requesting data...');