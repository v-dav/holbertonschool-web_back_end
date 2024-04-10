# ECMAScript 6 (ES6) Concepts

![NodeJS Version](https://img.shields.io/badge/NodeJS-12.11.x-green.svg)
![Jest Testing](https://img.shields.io/badge/Jest-Testing_Framework-blue.svg)
![Babel](https://img.shields.io/badge/Babel-ES6_Transpiler-orange.svg)
![ESLint Linter](https://img.shields.io/badge/ESLint-Linter-red.svg)

![image](https://github.com/v-dav/holbertonschool-web_back_end/assets/115344057/60400fe8-3c72-4b44-ab6b-523ec1127012)


## Project Overview

Welcome to the ECMAScript 6 (ES6) Concepts project! In this project, you will dive into the world of ES6, also known as ECMAScript 2015, and explore its new features and concepts. ES6 introduced significant changes and improvements to JavaScript, and this project will help you understand them. You will learn about block-scoped variables, arrow functions, default parameters, rest and spread function parameters, string templating, object creation, iterators, and for-of loops.

## Learning Objectives

By the end of this project, you will be able to explain the following concepts without the need for external references:

- What ES6 is
- New features introduced in ES6
- The difference between a constant and a variable
- Block-scoped variables
- Arrow functions and function parameters defaulting to them
- Rest and spread function parameters
- String templating in ES6
- Object creation and their properties in ES6
- Iterators and for-of loops

## Resources

**Read or watch**:

- [ECMAScript 6 - ECMAScript 2015](https://www.w3schools.com/js/js_es6.asp)
- [Statements and declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
- [Rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
- [Javascript ES6 — Iterables and Iterators](https://towardsdatascience.com/javascript-es6-iterables-and-iterators-de18b54f4d4)

## Author

- [Vladimir Davidov](https://github.com/v-dav) - Holberton School

---

# Personal Notes
![image](https://github.com/v-dav/holbertonschool-web_back_end/assets/115344057/30ac9b79-bfa8-4718-9498-04e8a17bf9ca)

## Introduction

JavaScript is often referred to as a "single-threaded, non-blocking, asynchronous, concurrent language" due to its execution model and characteristics:

1. **Single-Threaded:**
    - JavaScript operates in a single-threaded environment, meaning it has only one call stack and one memory heap.
    - Execution of JavaScript code occurs in a single sequence, one operation at a time.
2. **Non-Blocking:**
    - JavaScript is non-blocking, primarily in the context of I/O operations like fetching data, making network requests, or reading files.
    - When a non-blocking operation is encountered (e.g., fetching data from a server), JavaScript doesn't wait for the operation to complete. Instead, it continues executing other tasks.
3. **Asynchronous:**
    - Asynchronous programming is a key feature of JavaScript. It allows certain operations to be deferred, and the program can continue to execute other tasks while waiting for the completion of asynchronous operations.
    - Callbacks, Promises, and the `async/await` syntax are mechanisms for handling asynchronous behavior.
4. **Concurrent:**
    - Although JavaScript is single-threaded, it can still exhibit concurrent behavior through mechanisms like Web Workers.
    - Web Workers enable the execution of JavaScript code in the background, in parallel with the main thread. This allows for concurrent processing, especially in web applications dealing with heavy computations.
    

In summary, JavaScript's single-threaded nature means that it executes one operation at a time, but it leverages non-blocking and asynchronous patterns to handle I/O operations without waiting, resulting in efficient and responsive applications. The term "concurrent" is also applied in the context of Web Workers, allowing for parallel execution in certain scenarios.

Javascript has an event loop, a call stack and callback queue.

## Data Types
- Undefined
- Null
- bool
- string
- Symbol = a unique "hidden" identifier that no other code can accidentally access.
- Number
- Object

```jsx
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue"
};

let id = Symbol('id');
person[id] = 140353;
// Now person[id] = 140353
// but person.id is still undefined

Symbols are always unique.

If you create two symbols with the same description they will have different values:

Symbol("id") == Symbol("id"); // false
```

## Variable types and scope
Les principales différences entre `let`, `var` et `const` en JavaScript sont les suivantes :

1. **Scope (portée) :**
    - `var` a une portée de fonction (fonction-scope). Cela signifie que la variable déclarée avec `var` est accessible partout dans la fonction où elle est déclarée, même en dehors des blocs.
    - `let` et `const` ont une portée de bloc (block-scope). Cela signifie que la variable déclarée avec `let` ou `const` est limitée à la portée du bloc (par exemple, une boucle `for`, une condition `if`, etc.) où elle est déclarée. Introduites depuis ECMA6. By using **let** and **const**, you can write more predictable, readable, and maintainable code while avoiding common pitfalls associated with **var**. If a variable is declared inside a code block `{...}`, it’s only visible inside that block.
    
    ```jsx
    // show message
    let message = "Hello";
    alert(message);
    
    // show another message
    let message = "Goodbye"; // Error: variable already declared
    alert(message);
    ```
    
2. **Hoisting (élevation) :**
    - Les déclarations `var` sont "élevées" (hoisted) en haut de la fonction ou du bloc où elles sont déclarées. Cela signifie que vous pouvez accéder à une variable `var` avant sa déclaration, mais elle sera initialisée à `undefined`.
    - Les déclarations `let` et `const` sont également élevées, mais elles ne sont pas initialisées avant leur déclaration, ce qui évite les comportements imprévisibles.
3. **Réassignation (modification) :**
    - Les variables déclarées avec `var` et `let` peuvent être réassignées, c'est-à-dire que leur valeur peut être changée après leur déclaration.
    - Les variables déclarées avec `const` ne peuvent pas être réassignées après leur initialisation. Cependant, cela ne signifie pas que les objets qu'elles référencent sont immuables ; seulement que la liaison de la variable à l'objet est constante.
4. **Temporal Dead Zone (TDZ) :**
    - Les variables déclarées avec `let` et `const` sont soumises à la Temporal Dead Zone (zone morte temporelle), ce qui signifie que vous ne pouvez pas les utiliser avant leur déclaration dans le code.

**Pourquoi il n'est plus recommandé d'utiliser `var` depuis ES6 (ECMAScript 2015) :**

- `var` a des comportements imprévisibles en raison de la portée de fonction et de l'élevation, ce qui peut conduire à des bugs difficiles à déboguer.
- `let` et `const` introduisent une portée de bloc plus prévisible, évitant ainsi de nombreux problèmes associés à `var`.
- `const` en particulier encourage la programmation immuable en empêchant la réaffectation des variables après leur initialisation, ce qui peut améliorer la stabilité et la lisibilité du code.
- L'utilisation de `let` et `const` permet de mieux contrôler la portée des variables et d'éviter des erreurs courantes, ce qui en fait un choix plus sûr et recommandé depuis ES6.

<aside>
  
💡 Variables created **without** a declaration keyword (`var`, `let`, or `const`) are always global, even if they are created inside a function.

</aside>

## Conditions
```jsx
function fonctionQuelconque() {
	if (isItTrue) {
		return "Yes"
	}
	return "Non"
```

## Syntax
- camelCase: ex: studlyCapVar (the first letter is lowercase)
- myVar++
- myVar += 12
- Escaping quote characters: with \ or with using single quotes ‘’
- Backticks``can escape both single and double quotes
- Concatenate strings with + operator
- Strings are immutable
- function functionName() {}
- array = []
- Functions doesn’t need to have return statements, so return value is **undefined**
- A function can return **undefined**
- Spread operator arr2 = […arr1]
- Backticks allow to write multiline strings and allow to put variables directly inside the string with ${hkjhk}

## Some Common Methods
- firstName**.length**; // Finds the length of a string
- firstName[0] //refers to the first letter of the string
- **typeof** variable —> checks the type of the variable
- Math.random() —> return a random decimal number
- Math.floor() —> return a whole number
- parseInt(str) —> converts a string to an integer. Have an option to precise the base ex: parseInt(str, 2)
- object.freeze(): prevent the object properties to be mutated
- arr1.concat(arr2): concatenates 2  arrays

**String methods:**

- String.includes()
- String.startsWith()
- String.endsWith()

**Array metthods:**

- array**.push**() // appends an element to the end of an array
- array**.pop()** //removes and returns the last element from the array
- array.**shift()** //removes and returns the first element from the array
- array**.unshift()** //adds a new element to the beginning
- array.from() // returns an array object from any object with a length property or any iterable object

```jsx
Array.from("ABCDEFG")   // Returns [A,B,C,D,E,F,G]
```

- array keys() //returns an array iterator with the keys of an array

```jsx
const fruits = ["Banana", "Orange", "Apple", "Mango"];
const keys = fruits.keys();

let text = "";
for (let x of keys) {
  text += x + "<br>";
}
```

## Logical Operators
- && (AND)
- || (OR)

## Flow Operators
```jsx
if (val > 5) {
	result = "Bigger than 5"
	} else {
		result = "5 or smaller"
	}

if (val > 5) {
	result = "Bigger than 5"
	} else if {
		result = "5 or smaller"
	} else {
		result = "machin"
	}

//order matters
```

## Comparison Operators
- val == 12 //equality operator. Compare les valeurs sans tenir compte de leur type
- 3 === 3 // strict equality operator. Compare à la fois la valeur ET le type
- but 3 === ‘3’ /is false with strict equality operator bu would be true with 3 ==’3’ because will be converted in an integer
- The opposite ≠ and ≠=

```jsx
const a = 5;
const b = "5";

console.log(a == b);   // true (conversion automatique, les valeurs sont égales)
console.log(a === b);  // false (les types sont différents)

const x = null;
const y = undefined;

console.log(x == y);   // true (conversion automatique, les valeurs sont équivalentes)
console.log(x === y);  // false (les types sont différents)
```
