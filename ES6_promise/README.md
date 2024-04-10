# ES6 Promises

![Ubuntu Version](https://img.shields.io/badge/Ubuntu-18.04%20LTS-green.svg)
![Node Version](https://img.shields.io/badge/NodeJS-12.11.x-blue.svg)
![Jest Testing](https://img.shields.io/badge/Jest-Testing_Framework-blue.svg)
![Babel](https://img.shields.io/badge/Babel-ES6_Transpiler-orange.svg)
![ESLint Linter](https://img.shields.io/badge/ESLint-Linter-red.svg)

![image](https://github.com/v-dav/holbertonschool-web_back_end/assets/115344057/840a2994-7791-4a49-91c9-01eb24615e5f)


## Project Overview

Welcome to the ES6 Promises project! In this project, you will dive into the world of ES6 Promises, a powerful feature in modern JavaScript for handling asynchronous operations. You will learn the ins and outs of Promises, including how, why, and when to use them. Additionally, you will explore the use of `then`, `resolve`, `catch`, and other methods of the Promise object, as well as the `await` operator and async functions. By the end of this project, you will have a solid understanding of Promises and be equipped to work with asynchronous code like a pro.

## Learning Objectives

By the end of this project, you will be able to explain the following concepts without the need for external references:

- Promises (how, why, and what)
- How to use the `then`, `resolve`, `catch` methods
- How to use every method of the Promise object
- Throw / Try
- The `await` operator
- How to use an async function

## Ressources

**Read or watch**:

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript Promise: An introduction](https://web.dev/promises/)
- [Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
- [Async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [Throw/Try](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)

## Setup

### Install NodeJS 12.11.x
(in your home directory):
```
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y

$ nodejs -v
v12.11.1

$ npm -v
6.11.3
```


### Install Jest, Babel, and ESLint
in your project directory:

- Install Jest using: npm install --save-dev jest
- Install Babel using: npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli
- Install ESLint using: npm install --save-dev eslint

### Files

- `package.json`
```{
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "dev": "npx babel-node",
    "test": "jest",
    "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
  },
  "devDependencies": {
    "@babel/core": "^7.6.0",
    "@babel/node": "^7.8.0",
    "@babel/preset-env": "^7.6.0",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "jest": "^24.9.0"
  }
}
```
- `babel.config.js`
```
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
  ],
};
```
- `utils.js` (Use when you get to tasks requiring uploadPhoto and createUser.)
```
export function uploadPhoto() {
  return Promise.resolve({
    status: 200,
    body: 'photo-profile-1',
  });
}


export function createUser() {
  return Promise.resolve({
    firstName: 'Guillaume',
    lastName: 'Salva',
  });
}
```
- `.eslintrc.js`
```
module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
  },
  overrides:[
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    }
  ]
};
```

Don’t forget to run `$ npm install` when you have the `package.json`.

## Response Data Format

`uploadPhoto` returns a response with the format
```
{
  status: 200,
  body: 'photo-profile-1',
}
```

`createUser` returns a response with the format

```
{
  firstName: 'Guillaume',
  lastName: 'Salva',
}
```
---

# Personal Notes
![image](https://github.com/v-dav/holbertonschool-web_back_end/assets/115344057/12c6e020-9667-4468-8714-c8d14fa934f9)

## Fetch API

```jsx
fetch("url")
	.then(response => {
		return response.json();
	})
	.then(data => {
		console.log(data);
	})
	.catch(error => {
		console.error("Il y a une erreur,", error);
	});
```

## XMLHttpRequest

[Урок 14. JavaScript. Запросы на сервер. Fetch, XMLHttpRequest (XHR), Ajax](https://www.youtube.com/watch?v=eKCD9djJQKc)

XMLHttpRequest **(XHR)** est une technologie JavaScript permettant de faire des requêtes vers des serveurs web et d'obtenir des données **sans avoir à recharger complètement la page web**. C'est une méthode plus ancienne pour effectuer des requêtes HTTP asynchrones, mais elle est toujours largement utilisée. Je vais expliquer son fonctionnement avec des exemples simples.

**Exemple de demande GET avec XMLHttpRequest :**

Supposons que tu veuilles récupérer des informations sur un chat mignon depuis un serveur. Voici comment tu pourrais le faire avec XMLHttpRequest :

```jsx
// Crée un nouvel objet XMLHttpRequest
var xhr = new XMLHttpRequest();

// Configure la demande GET avec l'URL du serveur
xhr.open('GET', '<https://api.example.com/chat-mignon>', true);

// Gère la réponse lorsque la demande est terminée
xhr.onload = function() {
  if (xhr.status === 200) {
    // La demande a réussi (code 200)
    var responseData = JSON.parse(xhr.responseText);
    console.log(responseData);
  } else {
    // La demande a échoué avec un autre code de statut
    console.error('La demande a échoué avec le code de statut : ' + xhr.status);
  }
};

// Gère les erreurs de réseau
xhr.onerror = function() {
  console.error('Une erreur de réseau s\\'est produite');
};

// Envoie la demande
xhr.send();

```

- `new XMLHttpRequest()`: Crée un nouvel objet XMLHttpRequest.
- `xhr.open('GET', '<https://api.example.com/chat-mignon>', true)`: Configure la demande en spécifiant la méthode HTTP (GET dans cet exemple), l'URL du serveur et si la demande doit être asynchrone (true).
- `xhr.onload`: Cette fonction est appelée lorsque la demande est terminée avec succès. On vérifie si le code de statut HTTP est 200 (OK), puis on traite la réponse.
- `xhr.onerror`: Cette fonction est appelée en cas d'erreur de réseau.
- `xhr.send()`: Envoie la demande au serveur.

**Exemple de demande POST avec XMLHttpRequest :**

Si tu veux envoyer des données au serveur, tu peux utiliser une demande POST :

```jsx
var xhr = new XMLHttpRequest();
var dataToSend = { nom: 'Chaton', age: 2 };

xhr.open('POST', '<https://api.example.com/ajouter-chat>', true);
xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');

xhr.onload = function() {
  if (xhr.status === 200) {
    console.log('Le chat a été ajouté avec succès !');
  } else {
    console.error('La demande a échoué avec le code de statut : ' + xhr.status);
  }
};

xhr.onerror = function() {
  console.error('Une erreur de réseau s\\'est produite');
};

xhr.send(JSON.stringify(dataToSend));

```

- Ici, nous utilisons `xhr.open('POST', ...)` pour spécifier une méthode POST.
- `xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8')` définit l'en-tête de la demande pour indiquer que nous envoyons des données JSON.
- `xhr.send(JSON.stringify(dataToSend))` envoie les données au serveur après les avoir converties en format JSON avec `JSON.stringify`.

C'est ainsi que fonctionne XMLHttpRequest pour effectuer des requêtes HTTP asynchrones en JavaScript. Cependant, note que l'utilisation de la Fetch API est désormais recommandée, car elle offre une syntaxe plus moderne et conviviale pour gérer les requêtes réseau en JavaScript.

# Fetch API vs XHR

La Fetch API et XMLHttpRequest (XHR) sont toutes deux des méthodes permettant d'effectuer des requêtes réseau en JavaScript pour récupérer ou envoyer des données depuis ou vers des serveurs web. Cependant, il existe plusieurs différences importantes entre ces deux approches :

1. **Syntaxe :**
    - **Fetch API :** La Fetch API utilise une syntaxe plus moderne basée sur les Promises. Elle offre une approche plus claire et plus propre pour effectuer des requêtes et gérer les réponses.
    - **XMLHttpRequest (XHR) :** XMLHttpRequest utilise une syntaxe plus ancienne, basée sur des événements et des fonctions de rappel. Elle est souvent considérée comme moins intuitive et plus verbeuse.
2. **Asynchronicité :**
    - **Fetch API :** La Fetch API est toujours asynchrone. Les requêtes Fetch sont promises-based, ce qui signifie que tu peux utiliser les Promises ou `async/await` pour gérer la réponse de manière plus propre.
    - **XMLHttpRequest (XHR) :** XMLHttpRequest peut être utilisé de manière asynchrone ou synchronisée. Cependant, il est fortement recommandé d'utiliser XMLHttpRequest de manière asynchrone pour éviter de bloquer l'interface utilisateur.
3. **Gestion des en-têtes (headers) :**
    - **Fetch API :** La Fetch API offre une gestion plus flexible des en-têtes HTTP à travers l'objet `Headers`, ce qui facilite l'ajout, la modification ou la suppression d'en-têtes.
    - **XMLHttpRequest (XHR) :** La gestion des en-têtes avec XMLHttpRequest est un peu moins intuitive et se fait à travers des méthodes spécifiques comme `setRequestHeader`.
4. **Support CORS (Cross-Origin Resource Sharing) :**
    - **Fetch API :** La Fetch API gère nativement les requêtes CORS, ce qui simplifie les requêtes vers des domaines différents de celui de la page web.
    - **XMLHttpRequest (XHR) :** Les requêtes XHR nécessitent généralement plus de configuration pour gérer les requêtes CORS, bien que cela soit possible.
5. **Traitement des réponses :**
    - **Fetch API :** Les réponses Fetch sont souvent plus faciles à manipuler car elles sont traitées à travers des méthodes promises telles que `.json()`, `.text()`, etc.
    - **XMLHttpRequest (XHR) :** La gestion des réponses avec XHR peut être un peu plus complexe, car il faut souvent vérifier l'état de la requête et les gestionnaires d'événements pour obtenir la réponse.

En résumé, bien que les deux méthodes permettent d'effectuer des requêtes réseau en JavaScript, la Fetch API est généralement préférée pour sa syntaxe plus moderne, son utilisation des Promises, et sa gestion plus propre des réponses et des en-têtes. Cependant, XMLHttpRequest est encore largement utilisé, en particulier dans des projets plus anciens, et il peut être utile de connaître les deux approches en fonction des besoins du projet.

# Asynchrony

[Урок 4. JavaScript. Асинхронность.Что такое Event Loop. JS SetTimeout 0](https://www.youtube.com/watch?v=vIZs5tH-HGQ&list=PLqKQF2ojwm3l4oPjsB9chrJmlhZ-zOzWT&index=4)

```jsx
console.log("Start");
console.log("Start 2");

window.setTimeout(function () {
	console.log("Inside timout)
}, 2000); //la fonction anonyme sera executée après un délai de 2000 ms
```

# Promise

It’s a JavaScript Object that links “Producing Code” and “Consuming Code”.

"Producing Code" can take some time and "Consuming Code" must wait for the result.

```jsx
const myPromise = new Promise(function(myResolve, myReject) {
// "Producing Code" (May take some time)

  myResolve(); // when successful
  myReject();  // when error
});

// "Consuming Code" (Must wait for a fulfilled Promise).
myPromise.then(
  function(value) { /* code if successful */ },
  function(error) { /* code if some error */ }
);
```

Les Promises en JavaScript sont un concept qui facilite la gestion des opérations asynchrones de manière plus propre et plus structurée. Imaginons-les comme une manière élégante de gérer des tâches qui peuvent prendre du temps à s'exécuter, comme les requêtes réseau, les opérations de fichiers, ou les calculs intensifs.

**Promesse comme une boîte magique :**

Pense aux Promises comme à une boîte magique. Tu lui donnes une tâche à accomplir, puis elle te promet de te donner le résultat une fois que la tâche est terminée, que cela réussisse ou échoue.

**Les trois états d'une Promise :**

1. **Pendante (pending) :** Au début, une Promise est dans un état "pendant", ce qui signifie qu'elle est en train de travailler sur la tâche que tu lui as donnée.
2. **Résolue (fulfilled) :** Si la tâche réussit, la Promise passe à l'état "résolue". Elle te donne le résultat que tu attendais.
3. **Rejetée (rejected) :** Si la tâche échoue, la Promise passe à l'état "rejetée". Elle te donne une raison pour laquelle la tâche n'a pas pu être accomplie.

**Exemple concret :**

Imaginons que tu veuilles charger une image depuis Internet :

```jsx
javascriptCopy code
const maPromise = new Promise((resolve, reject) => {
  const image = new Image();
  image.src = 'https://example.com/mon_image.jpg';

  image.onload = () => {
    resolve(image); // Tâche réussie, nous renvoyons l'image.
  };

  image.onerror = () => {
    reject('Impossible de charger l\'image.'); // Tâche échouée, nous renvoyons une raison.
  };
});

```

- Dans cet exemple, nous créons une Promise qui charge une image depuis Internet. Si le chargement réussit, nous appelons **`resolve`** avec l'image. Si cela échoue, nous appelons **`reject`** avec un message d'erreur.

**Utilisation de la Promise :**

Une fois que tu as une Promise, tu peux utiliser **`.then()`** pour réagir lorsque la tâche est réussie et **`.catch()`** pour réagir en cas d'échec. Par exemple :

```jsx
javascriptCopy code
maPromise
  .then(image => {
    // Tâche réussie, utilisons l'image.
    document.body.appendChild(image);
  })
  .catch(erreur => {
    // Tâche échouée, affichons l'erreur.
    console.error(erreur);
  });

```

- Avec **`.then()`**, tu peux spécifier ce qu'il faut faire lorsque la tâche réussit.
- Avec **`.catch()`**, tu peux spécifier ce qu'il faut faire lorsque la tâche échoue.

Cela rend la gestion des opérations asynchrones beaucoup plus lisible et plus facile à comprendre.

En résumé, les Promises en JavaScript te permettent de gérer de manière propre et structurée les opérations asynchrones en utilisant un modèle basé sur les états. Elles sont largement utilisées pour effectuer des requêtes réseau, des opérations de fichiers, des animations, etc. Elles simplifient la gestion des erreurs et améliorent la lisibilité du code.

A promise is a promise, it can be fulfilled or rejected.

A new Promise takes one parameter which is a function that gets passed 2 parameters: resolve and reject. And we need t create a definition of the function inside.

```jsx
p = new Promise((resolve, reject) => {
	let a = 1 + 1;
	if (a === 2) {
		resolve("Success")
	} else {
		reject("Failed")
		}
});

//How we interact with promises. Method then. Anything inside then will be run for resolve.
p.then((message) => {
	console.log(message);
}
.catch((message) => {
	console.log(message)
}
```

Promises are good when you need to do a long task in a background such downloading an image.

[JavaScript Promises In 10 Minutes](https://www.youtube.com/watch?v=DHvZLI7Db8E)
