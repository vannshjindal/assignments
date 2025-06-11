// call, apply, bind

function printName() {
  console.log(this.name);
}

const exampleFun = printName.bind({ name: "John" });

exampleFun(); // Output: John