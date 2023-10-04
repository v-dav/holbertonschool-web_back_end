# ES6 Data Manipulation

![Ubuntu Version](https://img.shields.io/badge/Ubuntu-18.04%20LTS-green.svg)
![Node Version](https://img.shields.io/badge/NodeJS-12.11.x-blue.svg)
![Jest Testing](https://img.shields.io/badge/Jest-Testing_Framework-blue.svg)
![Babel](https://img.shields.io/badge/Babel-ES6_Transpiler-orange.svg)
![ESLint Linter](https://img.shields.io/badge/ESLint-Linter-red.svg)

## Project Overview

Welcome to the Array, Typed Array, Set, Map, WeakMap Learning project! This project is part of your journey to master JavaScript and its core data structures. In this project, you will delve into the world of arrays, typed arrays, and various data structures provided by JavaScript, including Sets, Maps, and WeakMaps.

The goal of this project is to help you gain a deep understanding of these essential JavaScript concepts. You will learn how to use array methods like `map`, `filter`, and `reduce` to manipulate arrays effectively. Additionally, you will explore typed arrays, which allow you to work with binary data efficiently.

The project will also introduce you to data structures like Sets, Maps, and WeakMaps. You will understand how to use them to store and manipulate data, making your JavaScript code more powerful and flexible.

By the end of this project, you will be well-versed in handling arrays, typed arrays, and JavaScript's various data structures, making you a more proficient JavaScript developer.

## Learning Objectives

By the end of this project, you will be able to explain the following concepts without the need for external references:

- How to use map, filter and reduce on arrays
- Typed arrays
- The Set, Map, and Weak link data structures

## Ressources

**Read or watch**:

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Typed Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays)
- [Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

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
