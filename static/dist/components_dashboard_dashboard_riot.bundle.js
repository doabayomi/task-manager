"use strict";
/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(self["webpackChunk"] = self["webpackChunk"] || []).push([["components_dashboard_dashboard_riot"],{

/***/ "./components/common/sidebar.riot":
/*!****************************************!*\
  !*** ./components/common/sidebar.riot ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ({\n  css: `sidebar nav,[is=\"sidebar\"] nav{ background-color: #f9df56; width: 80px; height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; }sidebar li,[is=\"sidebar\"] li{ list-style: none; margin: 15px 0; cursor: pointer; }sidebar li.active,[is=\"sidebar\"] li.active{ background-color: #000; color: #fff; border-radius: 8px; padding: 10px; }`,\n\n  exports: {\n    /*props: {\n      items: [\n        { icon: \"🏠\", active: true },\n        { icon: \"🔗\", active: false },\n        { icon: \"⚙️\", active: false },\n      ],\n    },*/\n    mounted() {\n      console.log('Sidebar mounted with items:', this.items);\n    },\n\n    select(item) {\n      this.update({\n        items: this.items.map((i) => ({ ...i, active: i === item })),\n      });\n    }\n  },\n\n  template: (\n    template,\n    expressionTypes,\n    bindingTypes,\n    getComponent\n  ) => template(\n    '<div><ul><li class=\"nav-item\"><span>🏠</span></li><li class=\"nav-item\"><span>🔗</span></li><li class=\"nav-item\"><span>⚙️</span></li></ul></div>',\n    []\n  ),\n\n  name: 'sidebar'\n});\n\n//# sourceURL=webpack:///./components/common/sidebar.riot?");

/***/ }),

/***/ "./components/common/task-card.riot":
/*!******************************************!*\
  !*** ./components/common/task-card.riot ***!
  \******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ({\n  css: `task-card .card,[is=\"task-card\"] .card{ border-radius: 10px; padding: 20px; margin: 10px; position: relative; }task-card .priority,[is=\"task-card\"] .priority{ font-size: 12px; margin-top: 10px; }task-card .priority.high,[is=\"task-card\"] .priority.high{ color: red; }task-card .priority.medium,[is=\"task-card\"] .priority.medium{ color: orange; }task-card .priority.low,[is=\"task-card\"] .priority.low{ color: green; }task-card .action,[is=\"task-card\"] .action{ position: absolute; top: 10px; right: 10px; }`,\n\n  exports: {\n    props: {\n      time: \"5:21 PM\",\n      date: \"12/24/14\",\n      title: \"Task Title\",\n      description: \"Task description...\",\n      priority: \"High\", // High, Medium, Low\n      bgColor: \"#f28b82\",\n    },\n\n    actionClick() {\n      console.log(\"Action clicked for:\", this.title);\n    }\n  },\n\n  template: (\n    template,\n    expressionTypes,\n    bindingTypes,\n    getComponent\n  ) => template(\n    '<div expr7=\"expr7\" class=\"card\"><p expr8=\"expr8\" class=\"time\"> </p><h3 expr9=\"expr9\"> </h3><p expr10=\"expr10\" class=\"description\"> </p><p expr11=\"expr11\"> </p><button class=\"action\" onclick=\"actionClick()\">↗</button></div>',\n    [\n      {\n        redundantAttribute: 'expr7',\n        selector: '[expr7]',\n\n        expressions: [\n          {\n            type: expressionTypes.ATTRIBUTE,\n            isBoolean: false,\n            name: 'style',\n\n            evaluate: _scope => [\n              'background-color: ',\n              _scope.bgColor,\n              ';'\n            ].join(\n              ''\n            )\n          }\n        ]\n      },\n      {\n        redundantAttribute: 'expr8',\n        selector: '[expr8]',\n\n        expressions: [\n          {\n            type: expressionTypes.TEXT,\n            childNodeIndex: 0,\n\n            evaluate: _scope => [\n              _scope.time,\n              ' | ',\n              _scope.date\n            ].join(\n              ''\n            )\n          }\n        ]\n      },\n      {\n        redundantAttribute: 'expr9',\n        selector: '[expr9]',\n\n        expressions: [\n          {\n            type: expressionTypes.TEXT,\n            childNodeIndex: 0,\n            evaluate: _scope => _scope.title\n          }\n        ]\n      },\n      {\n        redundantAttribute: 'expr10',\n        selector: '[expr10]',\n\n        expressions: [\n          {\n            type: expressionTypes.TEXT,\n            childNodeIndex: 0,\n            evaluate: _scope => _scope.description\n          }\n        ]\n      },\n      {\n        redundantAttribute: 'expr11',\n        selector: '[expr11]',\n\n        expressions: [\n          {\n            type: expressionTypes.TEXT,\n            childNodeIndex: 0,\n            evaluate: _scope => _scope.priority\n          },\n          {\n            type: expressionTypes.ATTRIBUTE,\n            isBoolean: false,\n            name: 'class',\n\n            evaluate: _scope => [\n              'priority ',\n              _scope.priority.toLowerCase()\n            ].join(\n              ''\n            )\n          }\n        ]\n      }\n    ]\n  ),\n\n  name: 'task-card'\n});\n\n//# sourceURL=webpack:///./components/common/task-card.riot?");

/***/ }),

/***/ "./components/dashboard/add-task-button.riot":
/*!***************************************************!*\
  !*** ./components/dashboard/add-task-button.riot ***!
  \***************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ({\n  css: `add-task-button .add-task,[is=\"add-task-button\"] .add-task{ border: 2px dashed #5c5cff; padding: 20px; text-align: center; }add-task-button button,[is=\"add-task-button\"] button{ background-color: #5c5cff; color: white; font-size: 20px; border: none; border-radius: 50%; width: 50px; height: 50px; }`,\n\n  exports: {\n    addTask() {\n      console.log(\"Add Task clicked\");\n    }\n  },\n\n  template: (\n    template,\n    expressionTypes,\n    bindingTypes,\n    getComponent\n  ) => template(\n    '<div class=\"add-task\"><button onclick>+</button><p>Add new task</p></div>',\n    []\n  ),\n\n  name: 'add-task-button'\n});\n\n//# sourceURL=webpack:///./components/dashboard/add-task-button.riot?");

/***/ }),

/***/ "./components/dashboard/calendar.riot":
/*!********************************************!*\
  !*** ./components/dashboard/calendar.riot ***!
  \********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ({\n  css: `calendar .calendar,[is=\"calendar\"] .calendar{ border: 2px dashed #ddd; padding: 20px; text-align: center; height: 300px; }`,\n\n  exports: {\n    props: {\n      month: \"May\",\n      year: 2023,\n    }\n  },\n\n  template: (\n    template,\n    expressionTypes,\n    bindingTypes,\n    getComponent\n  ) => template(\n    '<div class=\"calendar\"><h2 expr6=\"expr6\"> </h2><p>Calendar view here</p></div>',\n    [\n      {\n        redundantAttribute: 'expr6',\n        selector: '[expr6]',\n\n        expressions: [\n          {\n            type: expressionTypes.TEXT,\n            childNodeIndex: 0,\n\n            evaluate: _scope => [\n              _scope.month,\n              ', ',\n              _scope.year\n            ].join(\n              ''\n            )\n          }\n        ]\n      }\n    ]\n  ),\n\n  name: 'calendar'\n});\n\n//# sourceURL=webpack:///./components/dashboard/calendar.riot?");

/***/ }),

/***/ "./components/dashboard/dashboard.riot":
/*!*********************************************!*\
  !*** ./components/dashboard/dashboard.riot ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var _components_common_sidebar_riot__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @components/common/sidebar.riot */ \"./components/common/sidebar.riot\");\n/* harmony import */ var _components_common_task_card_riot__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @components/common/task-card.riot */ \"./components/common/task-card.riot\");\n/* harmony import */ var _components_dashboard_calendar_riot__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @components/dashboard/calendar.riot */ \"./components/dashboard/calendar.riot\");\n/* harmony import */ var _components_dashboard_add_task_button_riot__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @components/dashboard/add-task-button.riot */ \"./components/dashboard/add-task-button.riot\");\n\n\n\n\n\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ({\n  css: `dashboard .dashboard,[is=\"dashboard\"] .dashboard{ display: flex; height: 100vh; padding: 5px; }dashboard .main,[is=\"dashboard\"] .main{ flex: 1; padding: 20px; }dashboard .task-list,[is=\"dashboard\"] .task-list{ display: flex; flex-wrap: wrap; }`,\n\n  exports: {\n    components: {\n      Sidebar: _components_common_sidebar_riot__WEBPACK_IMPORTED_MODULE_0__[\"default\"],\n      TaskCard: _components_common_task_card_riot__WEBPACK_IMPORTED_MODULE_1__[\"default\"],\n      Calendar: _components_dashboard_calendar_riot__WEBPACK_IMPORTED_MODULE_2__[\"default\"],\n      AddTaskButton: _components_dashboard_add_task_button_riot__WEBPACK_IMPORTED_MODULE_3__[\"default\"],\n    },\n\n    props: {\n      tasks: [\n        { title: \"Design System\", priority: \"High\", description: \"...\", bgColor: \"#f28b82\" },\n        { title: \"Code Documentation\", priority: \"Medium\", description: \"...\", bgColor: \"#fbc15e\" },\n      ],\n    }\n  },\n\n  template: (\n    template,\n    expressionTypes,\n    bindingTypes,\n    getComponent\n  ) => template(\n    '<div class=\"dashboard\"><sidebar expr23=\"expr23\"></sidebar><div class=\"main\"><h1>Pending Tasks (5)</h1><div class=\"task-list\"></div></div></div>',\n    [\n      {\n        type: bindingTypes.TAG,\n        getComponent: getComponent,\n        evaluate: _scope => 'sidebar',\n        slots: [],\n        attributes: [],\n        redundantAttribute: 'expr23',\n        selector: '[expr23]'\n      }\n    ]\n  ),\n\n  name: 'dashboard'\n});\n\n//# sourceURL=webpack:///./components/dashboard/dashboard.riot?");

/***/ })

}]);