# ThunderJS Runtime

A lightweight JavaScript runtime built in Python using QuickJS bindings.

## Overview

ThunderJS Runtime accepts JavaScript code as input, executes it, and prints the output to standard output.

The project was developed for Thunder Hackathon 2.0 – Build Your Own JavaScript.

## Features

* Execute JavaScript code from `.js` files
* Execute JavaScript code from command-line arguments
* Execute JavaScript code through standard input (stdin)
* Support for:

  * Variables (`let`, `const`)
  * Arrays and Objects
  * Functions and Arrow Functions
  * Loops (`for`, `while`)
  * Conditionals (`if`, `else`)
  * Array methods (`map`, `filter`, etc.)
  * Spread operator (`...`)
  * Math object operations
  * Callback functions

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run a JavaScript file:

```bash
python main.py tests/test1.js
```

Run JavaScript directly:

```bash
python main.py "console.log('Hello World')"
```

Run through stdin:

Windows PowerShell:

```powershell
Get-Content tests\test1.js | python main.py
```

## Version

```bash
python main.py --version
```

## Example

Input:

```js
let num = 7;

if (num % 2 === 0) {
    console.log(num + " is Even");
} else {
    console.log(num + " is Odd");
}
```

Output:

```text
7 is Odd
```

## Tech Stack

* Python
* QuickJS


## Project Structure

```text
ThunderJS-Runtime/
│
├── main.py
├── requirements.txt
├── README.md
│
├── tests/
│   ├── test1.js
│   ├── test2.js
│   ├── test3.js
│   ├── test4.js
│   └── test5.js
│
└── additional_tests/
    ├── map_test.js
    ├── filter_test.js
    ├── object_test.js
    ├── spread_test.js
    ├── callback_test.js
    └── math_test.js
```

## Supported JavaScript Features

The runtime supports:

* Variable declarations (`let`, `const`)
* Numbers, strings, booleans, arrays, and objects
* Arithmetic and comparison operators
* Conditional statements (`if`, `else`)
* Loops (`for`, `while`)
* Functions and arrow functions
* Callback functions
* Array methods (`map`, `filter`, `reduce`, etc.)
* Spread operator (`...`)
* Math object operations
* Console output via `console.log()`

## Additional Testing

In addition to the official hackathon test cases, the runtime was verified using:

* Array `map()`
* Array `filter()`
* Objects
* Spread operator
* Callback functions
* Math object methods

## Running the Official Test Cases

```bash
python main.py tests/test1.js
python main.py tests/test2.js
python main.py tests/test3.js
python main.py tests/test4.js
python main.py tests/test5.js
```


