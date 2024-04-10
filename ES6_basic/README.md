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

## Loops
We can loop over an array, a string.
```jsx
while (i < 5) {
	myarray.push(i);
	i++;
}

for (var i = 0; i < 5; i++) {
	ourArray.push(i);
}

for (var i = 0; i < 5; **i+=2)** { //can also be decremented
	ourArray.push(i);
}

//iteration over element

const cars = ["BMW", "Volvo", "Mini"];

let text = "";
for (let x of cars) {
  text += x + "<br>";
}

// do ...while loop: always run at least one time before the coditions checks

do {
	myarray.push(i);
	i++;
} while (i < 5)
```

## Objects
```jsx
//JS object Notaton = JSON. Properties ans values

var ourDog = {
	"name": "Camper",
	"legs": 4,
	"tails": 1,
	"friends": ["everything"]
}
```

Accessing properties of an object with dot notation.

```jsx
ourDog.name = "Happy Camper"
ourDog.legs
```

Accessing properties of an object with a bracket notation. REQUIERED if the propertie has a space in its name. Ex: “the drink”. It’s like a dictionary with key value storage.

```jsx
ourDog["the drink"]
```

Add new property to an object using one of the above notations

```jsx
myDog["bark"] = "woof" //added
```

Delete the property

```jsx
delete ourDog.bark
```

Method to check if an object has a property:

```jsx
myDog.hasOwnProperty(the_property) --> returns true or false
```

## Nested functions & Closures
<aside>
💡 A closure is a function having access to the parent scope, even after the parent function has closed.

</aside>

In JavaScript, a closure is a function that has access to variables from its outer (enclosing) scope, even after that scope has finished executing. Closures allow functions to "remember" the environment in which they were created, capturing and retaining the values of variables in that environment.

Here's a simple example:

```jsx
function outerFunction(x) {
  // innerFunction is a closure, as it has access to the 'x' parameter of outerFunction
  function innerFunction(y) {
    return x + y;
  }

  return innerFunction;
}

// createClosure is now a reference to innerFunction, capturing the environment of outerFunction
const createClosure = outerFunction(10);

// Use the closure with different arguments
console.log(createClosure(5)); // Output: 15
console.log(createClosure(20)); // Output: 30

```

In this example, `innerFunction` is a closure because it has access to the `x` parameter of `outerFunction`, even after `outerFunction` has completed its execution. When we call `outerFunction(10)`, it returns a reference to `innerFunction` as `createClosure`, and we can later invoke `createClosure` with different arguments.

Closures are powerful in JavaScript and are often used to create private variables, implement data encapsulation, and create functions with dynamic behavior.

In JavaScript, closures can be used to create private variables by encapsulating them within a function scope. Here's an example of a function that uses closure to create a counter with a private variable:

```jsx
function createCounter() {
  // Private variable encapsulated within the closure
  let count = 0;

  // The returned object contains methods that can access and modify the private variable
  return {
    increment: function() {
      count++;
      console.log('Counter incremented:', count);
    },
    decrement: function() {
      count--;
      console.log('Counter decremented:', count);
    },
    getCount: function() {
      console.log('Current count:', count);
      return count;
    }
  };
}

// Create an instance of the counter
const myCounter = createCounter();

// Use the methods to interact with the private variable
myCounter.increment(); // Output: Counter incremented: 1
myCounter.increment(); // Output: Counter incremented: 2
myCounter.decrement(); // Output: Counter decremented: 1
myCounter.getCount();   // Output: Current count: 1

```

In this example, `createCounter` is a function that returns an object with methods (`increment`, `decrement`, and `getCount`). These methods are closures because they have access to the `count` variable even after `createCounter` has finished executing. The `count` variable is private to the returned object, and it cannot be directly accessed or modified from outside the object. This pattern allows you to create instances of a counter with its own private state.

[Variable scope, closure](https://javascript.info/closure#nested-functions)

[JavaScript Function Closures](https://www.w3schools.com/js/js_function_closures.asp)

A function is called “nested” when it is created inside another function.

It is easily possible to do this with JavaScript.

We can use it to organize our code, like this:

```jsx
function sayHiBye(firstName, lastName) {// helper nested function to use below
	function getFullName() {return firstName + " " + lastName;}
	alert( "Hello, " + getFullName() );
	alert( "Bye, " + getFullName() );}
```

Here the *nested* function `getFullName()` is made for convenience. It can access the outer variables and so can return the full name. Nested functions are quite common in JavaScript.

What’s much more interesting, a nested function can be returned: either as a property of a new object or as a result by itself. It can then be used somewhere else. No matter where, it still has access to the same outer variables.

Below, `makeCounter` creates the “counter” function that returns the next number on each invocation:

`function makeCounter() {let count = 0;return function() {return count++;};}let counter = makeCounter();alert( counter() ); // 0alert( counter() ); // 1alert( counter() ); // 2`

Despite being simple, slightly modified variants of that code have practical uses, for instance, as a [random number generator](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) to generate random values for automated tests.

How does this work? If we create multiple counters, will they be independent? What’s going on with the variables here?

## More On Closures

[Javascript Closure tutorial ( Closures Explained )](https://www.youtube.com/watch?v=71AtaJpJHw0)

Are functions that can access variables outside their own curly braces. Closures are nothing but FUNCTIONS WITH PRESERVED DATA

```jsx
function createClassRoom(numbersOfStudents) {
	function studentSeat(seat) {
		return function () { return seat };
	}

	let students = [];
	let i = 0;

	while (i < numbersOfStudents) {
		i++;
		students.push(studentSeat(i));
	}

	return students;
}

const classRoom = createClassRoom(10);
```

```jsx
function changeMode(size, weight, transform, background, color) {
	return function () {
		document.body.style.fontSize = size;
		document.body.style.fontWeight = weight;
		document.body.style.textTransform = transform;
		document.body.style.backgroundColor = background;
		document.body.style.color = color;
	}
}

function main() {
	const spooky = changeMode(9, 'bold', 'uppercase', 'pink', 'green');
	const darkMode = changeMode(12, 'bold', 'capitalize', 'black', 'white');
	const screamMode = changeMode(12, 'normal', 'lowercase', 'white', 'black');

	const paragraph = document.createElement('p');
	paragraph.innerText = "Welcome Holberton!";
	document.body.appendChild(paragraph);

	const spookyButton = document.createElement("button");
	spookyButton.innerText = "Spooky";
	document.body.appendChild(spookyButton);
	spookyButton.addEventListener("click", spooky);

	const darkButton = document.createElement("button");
	darkButton.innerText = "Dark Mode";
	document.body.appendChild(darkButton);
	darkButton.addEventListener("click", darkMode);

	const screamButton = document.createElement("button");
	screamButton.innerText = "Scream Mode";
	document.body.appendChild(screamButton);
	screamButton.addEventListener("click", screamMode);
}

main();
```

Dans cet exemple, **`changeScoreBy`** est une fonction interne qui est une closure car elle a accès aux variables locales (**`privateScore`** et **`name`**) de la fonction externe. Les méthodes telles que **`setName`**, **`rewardStudent`**, etc., sont des fonctions qui sont renvoyées par la fonction externe, et elles ont toujours accès aux variables locales grâce à la closure.

Cela permet de créer des membres "privés" qui ne sont pas directement accessibles en dehors de l'objet renvoyé. Notez que cette approche utilise une fonction de constructeur plutôt qu'une classe pour illustrer le concept de closure, mais vous pouvez appliquer des idées similaires dans le contexte des classes avec des membres privés utilisant les membres privés des classes (disponibles à partir de ES2022).

```jsx
function StudentHogwarts() {
	let privateScore = 0;
	let name = null;

	function changeScoreBy(points) {
			privateScore += points;
	}

	return {
			setName: function(newName) {
					name = newName;
			},
			rewardStudent: function() {
					changeScoreBy(1);
			},
			penalizeStudent: function() {
					changeScoreBy(-1);
			},
			getScore: function() {
					return `${name}: ${privateScore}`;
			}
	};
}

//harry
const harry = StudentHogwarts();
harry.setName("Harry");
for (let i = 0; i < 4; i++) {
	harry.rewardStudent();
}
console.log(harry.getScore());

//draco
const draco = StudentHogwarts();
draco.setName("Draco");
draco.rewardStudent();
for (let i = 3; i > 0; i--) {
	draco.penalizeStudent();
}
console.log(draco.getScore());
```

Dans le code que vous avez fourni, l'utilisation de closures avec la fonction `changeMode` présente plusieurs avantages :

1. **Encapsulation des Paramètres :** Les closures permettent d'encapsuler les paramètres spécifiques de chaque mode (spooky, darkMode, screamMode) de manière propre et organisée. Chaque fonction retournée par `changeMode` contient ses propres paramètres, ce qui évite d'avoir à passer les mêmes paramètres à chaque appel.
2. **Réutilisabilité :** La fonction `changeMode` est générique et peut être réutilisée pour créer d'autres fonctions de changement de mode avec des paramètres différents. Cela facilite l'ajout de nouveaux modes ou la modification des paramètres existants sans avoir à modifier directement le code des boutons.
3. **Facilité d'Ajout d'Événements :** En utilisant des closures, vous pouvez attacher chaque fonction de changement de mode directement à un bouton en utilisant un événement. Cela simplifie le code de gestion des événements et le rend plus lisible.
4. **Maintien de l'État :** Les closures maintiennent la référence aux variables de la portée externe (ici, les paramètres de `changeMode`). Cela signifie que chaque fonction créée a accès aux paramètres spécifiques qui lui ont été fournis lors de sa création, même si ces paramètres ne sont plus dans la portée globale après l'exécution de `changeMode`.

En résumé, l'utilisation de closures dans ce contexte rend le code plus modulaire, réutilisable et facilite la gestion des événements en associant chaque fonction de changement de mode à un bouton spécifique. Cela contribue à un code plus lisible, organisé et évolutif.

## This -call() - apply() - bind()
[call, apply and bind method in JavaScript](https://www.youtube.com/watch?v=75W8UPQ5l7k)
[JavaScript this Keyword](https://www.youtube.com/watch?v=gvicrj31JOM)

This  = the object that is executing the current function. Whoever calling the function = whoever on the left side of the function invocation. Few cases:

- If the function is a method of an obkect → this references the object itself
- If the function is a regular function —> this references the global object which is
    - Window object in browsers
    - Global otherwise

[What is THIS keyword in JavaScript? - Tutorial for beginners](https://www.youtube.com/watch?v=fVXp7ZWjlO4&list=PL1PqvM2UQiMoGNTaxFMSK2cih633lpFKP&index=6)

With call method we can borrow a method from another object to use it with another object, and if we have a regular function that uses this keyword, we can using call method pass the object on wich we want to apply the function to.

The difference between call and apply method is that in apply method we pass the arguments other than an object as an array list.

The bind method create a function that can be invoked later.

## Ternary Operators
Basic syntax: condition ? statement-if-true:statement if false
```jsx
return a === b ? true : false
return num > 0 ? "positiv" : num < 0 ? "négative" : "zero"
```

## Export/Import

Pour rendre les fonctions JavaScript exportables afin qu'elles puissent être utilisées dans d'autres fichiers, vous devez utiliser le système d'exportation d'ES6 (ECMAScript 2015) qui est pris en charge par la plupart des environnements JavaScript modernes, notamment les navigateurs et Node.js. Voici comment vous pouvez exporter des fonctions :

**Méthode 1 : Exporter une fonction par défaut**

```jsx
// MaFonction.js
function maFonction() {
  // Code de la fonction
}

export default maFonction;

```

Dans un autre fichier, vous pouvez importer cette fonction de la manière suivante :

```jsx
import maFonction from './MaFonction';

// Utilisez maFonction ici

```

**Méthode 2 : Exporter plusieurs fonctions individuelles**

```jsx
// Fonctions.js
export function fonction1() {
  // Code de la fonction 1
}

export function fonction2() {
  // Code de la fonction 2
}

```

Dans un autre fichier, vous pouvez importer ces fonctions individuellement :

```jsx
import { fonction1, fonction2 } from './Fonctions';

// Utilisez fonction1 et fonction2 ici

```

**Méthode 3 : Exporter des fonctions à partir d'un objet**

```jsx
// Fonctions.js
function fonction1() {
  // Code de la fonction 1
}

function fonction2() {
  // Code de la fonction 2
}

export { fonction1, fonction2 };

```

Dans un autre fichier, vous pouvez importer ces fonctions en les destructurant depuis l'objet :

```jsx
import { fonction1, fonction2 } from './Fonctions';

// Utilisez fonction1 et fonction2 ici

```

Les exemples ci-dessus sont destinés à être utilisés dans un environnement compatible avec ES6, comme Node.js avec le support ES6 activé ou les navigateurs modernes. Si vous travaillez dans un environnement plus ancien qui ne prend pas en charge les modules ES6, vous devrez utiliser une méthode de transpilation (comme Babel) pour convertir votre code en une version compatible avec ES5, puis utilisez une syntaxe de module différente, telle que CommonJS, pour les modules Node.js.

```jsx
export //a function

//in another file
import { the finction name } from "file.name"

//import everything
import * as capitalizedStrings from "filename" //the capitalizedStrings is an object here
```

## Maps

[JavaScript Maps](https://www.w3schools.com/js/js_object_maps.asp)

[Map - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)

#### Differences between JavaScript Objects and Maps:

| Object | Map |
| --- | --- |
| Not directly iterable | Directly iterable |
| Do not have a size property | Have a size property |
| Keys must be Strings (or Symbols) | Keys can be any datatype |
| Keys are not well ordered | Keys are ordered by insertion |
| Have default keys | Do not have default keys |

## WeakMap

[WeakMap et WeakSet](https://fr.javascript.info/weakmap-weakset)

## Sets

- Collection of unique values
- Can hold any data type

[JavaScript Sets](https://www.w3schools.com/js/js_object_sets.asp)

## Profile Lookup

```jsx
function profileLookup(list, name, property) {
	for (var i = 0; i < list.length; i++) {
		if (list[i][firstName] === name) {
			return list[i][property] || "No such property";
		}
	}
	return "No such contact"
}
```

## Anonymous functions and arrow functions

- No “function” keyword
- If only one parameter: remove parentheses around the parameter. But ESlint doesnt allow to do that
- If function returns some value: remove curly braces and return keyword

Problèms:

- Applicable to anonimous functions, no named functions. So we cannot have named arrowed functions, arrow functions are always anonimous functions
- Arrow functions don’t automatically binding with `this`
- It is not applicable to constructor functions

When not to use arrow functions:

- Object methods
- Prototypes
- Constructors
- Event handlers

Binding off anonimous functions with `this`

```jsx
var magic = function() {
	return new Date();
);

//an anonymous function can be converted into a arrow function

var magic = () **=>** {
	return new Date();
};

//but it can be even shorter
var magic = () => new Date(); 
```

Don’t need **function** keyword or **return** keyword or **curly braces.**
You can only omit the `return` keyword and the curly brackets if the function is a single statement. Because of this, it might be a good habit to always keep them:

```jsx
const x = (x, y) => x * y;
```

Syntax:

```jsx
() => expression

param => expression

(param) => expression

(param1, paramN) => expression

() => {
  statements
}

param => {
  statements
}

(param1, paramN) => {
  statements
}
```

## Default parameters

```jsx
function test(arg1, arg2 = 1) {} 
```

## Rest operator …

Allows to create a function that takes a variable number of arguments. 

```jsx
function sum(...args) {
let sum = 0;
  for (let arg of args) sum += arg;
  return sum;
}

let x = sum(4, 9, 16, 25, 29, 100, 66, 77);
```

## Spread operator (…)

It expands an iterable (like an array) into more elements

```jsx
const q1 = ["Jan", "Feb", "Mar"];
const q2 = ["Apr", "May", "Jun"];
const q3 = ["Jul", "Aug", "Sep"];
const q4 = ["Oct", "Nov", "May"];

const year = [...q1, ...q2, ...q3, ...q4]
```

## Destructuring assignement

```jsx
var voxel = {x: 3,2, y: 5, z: 6,54}

const {x : a, y : b, z : c} = voxel: //so a = 3,2, y = 5, z = 6,54
```

## Template litérals = Template strings = Strings templating

Le "string templating", également connu sous le nom de "template literals" ou "template strings", est une fonctionnalité de nombreux langages de programmation, y compris JavaScript, qui permet d'incorporer des expressions ou des variables dans des chaînes de caractères de manière plus lisible et plus expressive. Cette fonctionnalité permet de créer des chaînes de caractères complexes en intercalant des variables ou des expressions directement à l'intérieur de la chaîne, en utilisant des marqueurs spéciaux.

En JavaScript, les template literals sont délimitées par des backticks ( ``) au lieu des guillemets simples ou doubles traditionnels. Par exemple :

```jsx
const prenom = 'John';
const nom = 'Doe';

// Utilisation de template literals pour créer une chaîne de caractères
const message = `Bonjour, je m'appelle ${prenom} ${nom}.`;
console.log(message); // Affiche : "Bonjour, je m'appelle John Doe."

```

Dans cet exemple, le `${}` est utilisé pour insérer les variables `prenom` et `nom` directement dans la chaîne de caractères, ce qui rend le code plus lisible et plus propre.

Les avantages du string templating sont les suivants :

1. **Lisibilité améliorée :** Les templates literals rendent le code plus lisible en permettant l'insertion directe de variables et d'expressions dans la chaîne, ce qui évite d'utiliser des opérations de concaténation fastidieuses.
2. **Interpolation de variables :** Il est facile d'incorporer des variables et des expressions dans le texte, ce qui rend la création de chaînes dynamiques plus naturelle.
3. **Support des sauts de ligne :** Les template literals prennent en charge les sauts de ligne, ce qui les rend idéaux pour la création de chaînes de caractères multilignes.
4. **Expression de fonctions :** En plus des variables, vous pouvez également incorporer des appels de fonctions et des expressions JavaScript complexes à l'intérieur des templates literals.

En résumé, le string templating (template literals) est une fonctionnalité JavaScript qui permet de créer des chaînes de caractères dynamiques de manière plus élégante et lisible en incorporant des variables et des expressions directement dans le texte, ce qui améliore la maintenance du code et sa clarté.

## Class and constructor

Classes are templates for JavaScript Objects. A class is not an object, it’s a template.

Use `class` to create a class and always add a method named `constructor`

```jsx
function makeClass() {
	class Vegetable {
		constructor(name) {
			this.name = name;
		}
	)
	return Vegetable;
)
const Vegetable = makeClass();
const carrot = new Vegetable("carrot");
console.log(carrot.name)
```

## Getter and setter

When variables are private, and one never interact directly with the attributes

```jsx
class Book {
	constructor(author) {
		this._author = author;
	}

	//getter
	get writer(){
		return this._author;
	}
	
	//setter
	set writer(updatedAuthor) {
		this._author = updatedAuthor;
	}
}
```
