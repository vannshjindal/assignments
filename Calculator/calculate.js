let display = document.getElementById("display");

function appendValue(value) {
  display.value += value;
}

function clearDisplay() {
  display.value = "";
}

function calculate() {
  let expression = display.value;

  if (expression.includes("/0")) {
    alert("Cannot divide by zero!");
    return;
  }
  let result = eval(expression);
  display.value = result;
}
