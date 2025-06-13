function outer() {
  let name = "Vansh";
  function inner() {
    console.log(name);
  }
  return inner;
}
const greet = outer();
greet(); 


function counter() {    
  let count = 0;
  return function () {
    count++;
    console.log(count);
  };
}
const increment = counter();
increment();
increment();
increment(); 

function createCounter() {
  let count = 0;
  return function () {
    return ++count;
  };
}
const counter1 = createCounter();
const counter2 = createCounter();
console.log(counter1()); 
console.log(counter2()); 
console.log(counter1()); 



// //DOUBTS-------------------------------
for (var i = 0; i <= 3; i++) {
  setTimeout(function () {
    console.log(i);
  }, 1000);
}
//--------------------------------------
for (let i = 0; i <= 3; i++) {
  setTimeout(function () {
    console.log(i);
  }, 5000);
 }
// //--------------------------------------


function makecounter(){
    let count = 1;

     function incre(){
        console.log(count++);
     }
     return incre;
}

let increcount= makecounter();
increcount();


const myName = document.getElementById("my-name");
const btn = document.getElementById("my-btn");


function makeTextsizer(size){
    function changeSize(){
        myName.style.fontSize = `${size}px`;
    }
    return changeSize;
}
const size10 = makeTextsizer(10);
const size20 = makeTextsizer(20);
const size30 = makeTextsizer(30);
const size70 = makeTextsizer(70);
const size100 = makeTextsizer(100);   
btn.addEventListener("click",size100);



