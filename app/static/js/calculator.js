let currentInput = '0';
let history = [];

function updateDisplay() {
    document.getElementById('input').textContent = currentInput;
}

function insert(value) {
    if (currentInput === '0' && !isNaN(value)) {
        currentInput = value;
    } else {
        currentInput += value;
    }
    updateDisplay();
}

function clearAll() {
    currentInput = '0';
    document.getElementById('result').textContent = '';
    updateDisplay();
}

function backspace() {
    if (currentInput.length > 1) {
        currentInput = currentInput.slice(0, -1);
    } else {
        currentInput = '0';
    }
    updateDisplay();
}

async function calculate() {
    try {
        const response = await fetch('/api/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ expression: currentInput })
        });
        
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('result').textContent = '= ' + data.result;
            addToHistory(currentInput, data.result);
        } else {
            document.getElementById('result').textContent = 'Error: ' + data.error;
        }
    } catch (error) {
        document.getElementById('result').textContent = 'Error: ' + error.message;
    }
}

function addToHistory(expr, result) {
    history.unshift({ expr, result });
    if (history.length > 10) history.pop();
    updateHistoryDisplay();
}

function updateHistoryDisplay() {
    const historyList = document.getElementById('historyList');
    historyList.innerHTML = history.map(item => `
        <div class="history-item">
            <div class="expr">${item.expr}</div>
            <div class="res">= ${item.result}</div>
        </div>
    `).join('');
}

// Keyboard support
document.addEventListener('keydown', (e) => {
    if (e.key >= '0' && e.key <= '9') insert(e.key);
    else if (e.key === '.') insert('.');
    else if (e.key === '+') insert('+');
    else if (e.key === '-') insert('-');
    else if (e.key === '*') insert('*');
    else if (e.key === '/') insert('/');
    else if (e.key === '(') insert('(');
    else if (e.key === ')') insert(')');
    else if (e.key === 'Enter') calculate();
    else if (e.key === 'Escape') clearAll();
    else if (e.key === 'Backspace') backspace();
});
