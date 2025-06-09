// const a= "volvo" + 20 +20;
// console.log(a);



// const b = 20 + 20 + "bmw";
// console.log(b);



// function tocelcius(f){
//     return (5/9) * (f-32);
// }
// let value = tocelcius(99);
// console.log(value + " Celsius");


// console.log("Hey 1");
// setTimeout(function(){
//     console.log("Hey 2");
// },4000)




// function abcd(){
//     fetch("https://jsonplaceholder.typicode.com/users")
//     .then(function(raw){
//         return raw.json();
//     })
//     .then(function(data){
//         console.log(data);
//     })

// }
// abcd();


async function abcd(){
    let raw = await fetch("https://jsonplaceholder.typicode.com/users"); 
    let data = await raw.json();
    console.log(data);
}

abcd();