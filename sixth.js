const person = {
    name: "Vansh Jindal",
    age : 22,
    address: {
        city : "Jaipur",
        state : "Rajasthan"
    },
    greet : function greet(){
      return "heyyyyy!";
    }}

console.log(person.greet());
console.log(person.name);

let personstring = JSON.stringify(person);
localStorage.setItem("person", personstring);
let res = JSON.parse(personstring);

console.log(localStorage.getItem("person"));
console.log(res.name)