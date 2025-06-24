console.log("Hello1");
console.log("hello2");

setTimeout(() => {
  console.log("Hello from timeout");
}, 4000);

console.log("Hello3");

function sayhello() {
  return "Hello from the sayHello function!";
}
console.log(sayhello());
