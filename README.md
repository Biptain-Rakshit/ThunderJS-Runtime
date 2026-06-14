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
