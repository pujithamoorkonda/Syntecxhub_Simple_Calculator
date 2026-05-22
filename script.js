function addValue(value) {
    document.getElementById("display").value += value;
}

function clearDisplay() {
    document.getElementById("display").value = "";
    document.getElementById("result").value = "";
}

function backspace() {
    let current = document.getElementById("display").value;
    document.getElementById("display").value = current.slice(0, -1);
}

function calculate() {

    let expression = document.getElementById("display").value;

    try {

        expression = expression.replace('%', '%');

        let result = eval(expression);

        document.getElementById("result").value = result;

    } catch {

        document.getElementById("result").value = "Error";

    }
}