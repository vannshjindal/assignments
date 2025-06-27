let person = {
  name: "John Doe",
  details: {
    age: 25,
    hobbies: [
      { name: "cricket", level: "advanced" },
      { name: "reading", level: "intermediate" },
      { name: "gaming", level: "beginner" },
    ],
    showHobbies: function () {
      this.hobbies.forEach((hobby) => {
        console.log(hobby.name);
      });
    },
  },
  languages: ["English", "Hindi"],
};

person.details.hobbies.forEach(x=>{
    console.log(x.name)
})

person.details.hobbies.forEach(x=>{
    console.log(x.level)
})

let count = 0;
person.details.hobbies.forEach(x=>{
    if(x.level==="beginner"){
        count ++;
    }
})

console.log(count)

person.details.hobbies.push({name: "chess", level: "pro"})
console.log(person.details.hobbies)

let filteredHobbies = [];
person.details.hobbies.forEach(x=>{
    if(x.level == "intermediate" || x.level=="advanced"){
        filteredHobbies.push(x)
    }

})
console.log(filteredHobbies)

console.log(person.details.hobbies.name.length);

