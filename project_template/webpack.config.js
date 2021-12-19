const path = require("path");
// Считываем переменные окружения из файла `npm install dotenv`
const envy = require("dotenv").config({ path: "./__env.env" });
//Получаем имя проекта из переменных окружения
const ProjName = envy.parsed.NAME_PROJ;
console.log(ProjName);

// https://webpack.js.org/guides/typescript/
module.exports = {
  // Режим работы
  mode: "development",
  // Включить карты кода для отладки вывода webpack
  devtool: "inline-source-map",

  entry: [path.resolve(__dirname, `${ProjName}/frontend_react/src/index.tsx`)],
  output: {
    // куда помещаются скомпилированные файлы
    path: path.resolve(
      __dirname,
      `${ProjName}/frontend_react/static/frontend_react/public/`
    ),

    // 127.0.0.1/static/frontend_react/public/ откуда подаются файлы
    publicPath: "/static/frontend_react/public/",
    filename: "main.js", // имя для импорта в `index.html`
  },

  resolve: {
    // Добавить разрешения '.ts' и '.tsx' к обрабатываемым
    extensions: [".ts", ".tsx", ".js"],
  },

  module: {
    // конфигурация относительно модулей
    rules: [
      {
        // проверка `regex` для `js` и `jsx` файлов
        test: /\.tsx?$/,
        // Игнорирует папки [node_modules/, bower_components/]
        exclude: /(node_modules|bower_components)/,
        // для поиска подходящих файлов используйте  `babel-loader`
        use: 'ts-loader',
      },
    ],
  },
  // externals: {
  //   react: "React",
  //   "react-dom": "ReactDOM",
  // },
  devServer: {
    devMiddleware: {
      // Записывать изменения в файл, а не в ОЗУ
      writeToDisk: true,
    },
  },
};
