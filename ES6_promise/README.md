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
