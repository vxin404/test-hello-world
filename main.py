from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import math
import json

app = FastAPI(title="Advanced Calculator Service")

class CalcRequest(BaseModel):
    expression: str

class CalcResponse(BaseModel):
    result: str
    success: bool
    error: str = None

@app.get("/", response_class=HTMLResponse)
async def root():
    return CALCULATOR_HTML

@app.post("/api/calculate", response_model=CalcResponse)
async def calculate(request: CalcRequest):
    try:
        result = evaluate_expression(request.expression)
        return CalcResponse(result=str(result), success=True)
    except Exception as e:
        return CalcResponse(result="", success=False, error=str(e))

@app.get("/api/hello")
async def api_hello():
    return {"message": "Hello World", "service": "OpenClaw FastAPI Calculator"}

def evaluate_expression(expr: str):
    """Safely evaluate mathematical expression."""
    # Clean the expression
    expr = expr.strip()
    
    # Replace common symbols
    expr = expr.replace('×', '*').replace('÷', '/').replace('^', '**')
    
    # Define safe functions and constants
    safe_dict = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'asin': math.asin,
        'acos': math.acos,
        'atan': math.atan,
        'sinh': math.sinh,
        'cosh': math.cosh,
        'tanh': math.tanh,
        'sqrt': math.sqrt,
        'log': math.log,
        'log10': math.log10,
        'log2': math.log2,
        'ln': math.log,
        'exp': math.exp,
        'abs': abs,
        'round': round,
        'floor': math.floor,
        'ceil': math.ceil,
        'factorial': math.factorial,
        'pow': pow,
        'pi': math.pi,
        'e': math.e,
        'tau': math.tau,
        'deg': math.degrees,
        'rad': math.radians,
    }
    
    # Add math module functions
    safe_dict['math'] = math
    
    try:
        result = eval(expr, {"__builtins__": {}}, safe_dict)
        return result
    except Exception as e:
        raise ValueError(f"计算错误: {str(e)}")

CALCULATOR_HTML = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>高级计算器 | Advanced Calculator</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            display: flex;
            gap: 20px;
            max-width: 1200px;
            width: 100%;
            flex-wrap: wrap;
            justify-content: center;
        }
        
        .calculator {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            width: 400px;
        }
        
        .display {
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            text-align: right;
        }
        
        .display .history {
            color: rgba(255, 255, 255, 0.5);
            font-size: 14px;
            min-height: 20px;
            margin-bottom: 5px;
            word-break: break-all;
        }
        
        .display .input {
            color: white;
            font-size: 32px;
            font-weight: 300;
            word-break: break-all;
            min-height: 40px;
        }
        
        .display .result {
            color: #00d4ff;
            font-size: 24px;
            margin-top: 10px;
            min-height: 30px;
        }
        
        .buttons {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 10px;
        }
        
        button {
            padding: 18px 10px;
            font-size: 16px;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.2s;
            font-weight: 500;
        }
        
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }
        
        button:active {
            transform: translateY(0);
        }
        
        .btn-number {
            background: rgba(255, 255, 255, 0.15);
            color: white;
        }
        
        .btn-number:hover {
            background: rgba(255, 255, 255, 0.25);
        }
        
        .btn-operator {
            background: rgba(255, 149, 0, 0.8);
            color: white;
        }
        
        .btn-operator:hover {
            background: rgba(255, 149, 0, 1);
        }
        
        .btn-function {
            background: rgba(0, 212, 255, 0.8);
            color: white;
            font-size: 13px;
        }
        
        .btn-function:hover {
            background: rgba(0, 212, 255, 1);
        }
        
        .btn-clear {
            background: rgba(255, 59, 48, 0.8);
            color: white;
        }
        
        .btn-clear:hover {
            background: rgba(255, 59, 48, 1);
        }
        
        .btn-equals {
            background: rgba(52, 199, 89, 0.8);
            color: white;
            grid-column: span 2;
        }
        
        .btn-equals:hover {
            background: rgba(52, 199, 89, 1);
        }
        
        .btn-zero {
            grid-column: span 2;
        }
        
        .info-panel {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            width: 350px;
            color: white;
        }
        
        .info-panel h2 {
            color: #00d4ff;
            margin-bottom: 15px;
            font-size: 20px;
        }
        
        .info-panel h3 {
            color: rgba(255, 255, 255, 0.8);
            margin: 15px 0 10px 0;
            font-size: 14px;
        }
        
        .info-panel code {
            background: rgba(0, 0, 0, 0.3);
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
        
        .info-panel ul {
            list-style: none;
            font-size: 13px;
            line-height: 1.8;
        }
        
        .info-panel li:before {
            content: "• ";
            color: #00d4ff;
        }
        
        .history-panel {
            margin-top: 20px;
            max-height: 200px;
            overflow-y: auto;
        }
        
        .history-item {
            background: rgba(0, 0, 0, 0.2);
            padding: 10px;
            margin-bottom: 8px;
            border-radius: 8px;
            font-size: 13px;
        }
        
        .history-item .expr {
            color: rgba(255, 255, 255, 0.6);
        }
        
        .history-item .res {
            color: #00d4ff;
            font-weight: bold;
        }
        
        @media (max-width: 800px) {
            .container {
                flex-direction: column;
                align-items: center;
            }
            
            .calculator, .info-panel {
                width: 100%;
                max-width: 400px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="calculator">
            <div class="display">
                <div class="history" id="history"></div>
                <div class="input" id="input">0</div>
                <div class="result" id="result"></div>
            </div>
            <div class="buttons">
                <!-- Row 1: Functions -->
                <button class="btn-function" onclick="insert('sin(')">sin</button>
                <button class="btn-function" onclick="insert('cos(')">cos</button>
                <button class="btn-function" onclick="insert('tan(')">tan</button>
                <button class="btn-function" onclick="insert('log(')">log</button>
                <button class="btn-function" onclick="insert('ln(')">ln</button>
                
                <!-- Row 2: More Functions -->
                <button class="btn-function" onclick="insert('sqrt(')">√</button>
                <button class="btn-function" onclick="insert('pow(')">x^y</button>
                <button class="btn-function" onclick="insert('factorial(')">n!</button>
                <button class="btn-function" onclick="insert('pi')">π</button>
                <button class="btn-function" onclick="insert('e')">e</button>
                
                <!-- Row 3: Clear and Operators -->
                <button class="btn-clear" onclick="clearAll()">AC</button>
                <button class="btn-clear" onclick="backspace()">⌫</button>
                <button class="btn-operator" onclick="insert('(')">(</button>
                <button class="btn-operator" onclick="insert(')')">)</button>
                <button class="btn-operator" onclick="insert('/')">÷</button>
                
                <!-- Row 4: Numbers and Operators -->
                <button class="btn-number" onclick="insert('7')">7</button>
                <button class="btn-number" onclick="insert('8')">8</button>
                <button class="btn-number" onclick="insert('9')">9</button>
                <button class="btn-operator" onclick="insert('*')">×</button>
                <button class="btn-function" onclick="insert('abs(')">|x|</button>
                
                <!-- Row 5 -->
                <button class="btn-number" onclick="insert('4')">4</button>
                <button class="btn-number" onclick="insert('5')">5</button>
                <button class="btn-number" onclick="insert('6')">6</button>
                <button class="btn-operator" onclick="insert('-')">−</button>
                <button class="btn-function" onclick="insert('deg(')">deg</button>
                
                <!-- Row 6 -->
                <button class="btn-number" onclick="insert('1')">1</button>
                <button class="btn-number" onclick="insert('2')">2</button>
                <button class="btn-number" onclick="insert('3')">3</button>
                <button class="btn-operator" onclick="insert('+')">+</button>
                <button class="btn-function" onclick="insert('rad(')">rad</button>
                
                <!-- Row 7 -->
                <button class="btn-number btn-zero" onclick="insert('0')">0</button>
                <button class="btn-number" onclick="insert('.')">.</button>
                <button class="btn-equals" onclick="calculate()">=</button>
            </div>
        </div>
        
        <div class="info-panel">
            <h2>🧮 高级计算器</h2>
            <p>支持科学计算、三角函数、对数运算等高级功能。</p>
            
            <h3>可用函数</h3>
            <ul>
                <li><code>sin(x)</code> - 正弦</li>
                <li><code>cos(x)</code> - 余弦</li>
                <li><code>tan(x)</code> - 正切</li>
                <li><code>sqrt(x)</code> - 平方根</li>
                <li><code>log(x)</code> - 对数</li>
                <li><code>ln(x)</code> - 自然对数</li>
                <li><code>pow(x,y)</code> - 幂运算</li>
                <li><code>factorial(n)</code> - 阶乘</li>
                <li><code>abs(x)</code> - 绝对值</li>
                <li><code>deg(x)</code> - 弧度转角度</li>
                <li><code>rad(x)</code> - 角度转弧度</li>
            </ul>
            
            <h3>常数</h3>
            <ul>
                <li><code>pi</code> - π (3.14159...)</li>
                <li><code>e</code> - 自然常数 (2.71828...)</li>
            </ul>
            
            <div class="history-panel" id="historyPanel">
                <h3>计算历史</h3>
                <div id="historyList"></div>
            </div>
        </div>
    </div>
    
    <script>
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
    </script>
</body>
</html>
"""
