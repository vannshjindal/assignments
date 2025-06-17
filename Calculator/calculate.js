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

document.addEventListener("keydown", function (event) {
  const key = event.key;

  if (!isNaN(key)) {
    appendValue(key);
  }
 
  if (['+', '-', '*', '/', '%', '.'].includes(key)) {
    appendValue(key);
  }

  if (key === 'Enter') {
    event.preventDefault(); 
    calculate();
  }
 
  if (key === 'Backspace') {
    display.value = display.value.slice(0, -1);
  }

  if (key === 'Escape') {
    clearDisplay();
  }
});
