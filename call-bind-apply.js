const person1 = {
    Fname: "Vansh",
    Lname:"Jindal",
    Fullname : function (hometown,country){
        return this.Fname + " " + this.Lname + " " + hometown + " " + country;
    }
}

const person2 = {
    Fname: "abc",
    Lname: "def"
}

console.log(person1.Fullname.call(person2,"Jaipur","India")); //call
console.log(person1.Fullname.apply(person2,["Jaipur","India"])); //apply

let result = person1.Fullname.bind(person2,"Jaipur","India"); //bind
console.log(result());


