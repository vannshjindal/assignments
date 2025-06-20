//  IFFE concept where we use var and still the output comes out to be reference error
//  in this we create tow moon brackets ()() and in first bracket we create a function and then
//  we write the code in that function using var which then gives the reference error

function call() {
  (function () {
    var a = 9;
    var b = 10;
  })();
  console.log(a, b);
}

call();
 