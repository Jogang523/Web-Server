let area1 = getArea(10, 20);
console.log(area1);

let area2 = getArea(30, 20);
console.log(area2);

getArea(120, 200);

function getArea(width, height){
    function anther(){
        console.log(anther);
    }

    anther();
    let area = width * height;

    return area;

}