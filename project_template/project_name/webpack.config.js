// Для относительных путей
const path = require('path');
// https://github.com/jantimon/html-webpack-plugin#options
const HTMLWebpackPlugin = require('html-webpack-plugin');
// https://github.com/johnagan/clean-webpack-plugin
const {CleanWebpackPlugin} = require('clean-webpack-plugin');
// https://www.npmjs.com/package/copy-webpack-plugin
const CopyWebpackPlugin = require('copy-webpack-plugin');
// https://webpack.js.org/plugins/mini-css-extract-plugin/
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
// https://www.npmjs.com/package/optimize-css-assets-webpack-plugin
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');
// https://webpack.js.org/plugins/terser-webpack-plugin/
const TerserPlugin = require('terser-webpack-plugin');
// https://www.npmjs.com/package/webpack-bundle-analyzer
const {BundleAnalyzerPlugin} = require('webpack-bundle-analyzer');

// Считываем переменные окружения из файла `npm install dotenv`
const envy = require('dotenv').config({path: './__env.env'});
//Получаем имя проекта из переменных окружения
const ProjName = envy.parsed.NAME_PROJ;
console.log('ProjName:\t', ProjName);
// Получить режим разработки (bool)
const isDev = envy.parsed.DEBUG === 'true';
console.log('isDev:\t\t', isDev);
const strDev = isDev ? 'development' : 'production';
console.log('DEBUG:\t\t', strDev);

// Функция для настроек оптимизации (сжатия) файлов
const optimization = () => {
    // Оптимизировать импорты сторонних библиотек
    const conf = {
        splitChunks: {
            chunks: 'all',
        },
    };
    // Если не режим разработки то сжимаем `JS` и `CSS`
    if (!isDev) {
        conf.minimize = true;
        conf.minimizer = [new OptimizeCssAssetsPlugin(), new TerserPlugin()];
    }
    return conf;
};

// Нужно ли создавать хешь в имени файлов. Не нужно в режиме разработки
const filename = (ext) =>
    isDev ? `[name].bundle.${ext}` : `[name].[contenthash].${ext}`;

// Функция для подключения плагинов
const plugins = () => {
    plug = [
        // Плагин для автоматического подключения актуальной
        // версии `TS` когда в `index.html`
        new HTMLWebpackPlugin({
            // Какой `HTML` шаблон взять за основу
            template: path.resolve(
                __dirname,
                `frontend_react/src/index.template.html`,
            ), // Куда поместить итоговый `HTMl` файл
            filename: path.resolve(
                __dirname,
                `frontend_react/templates/frontend_react/index.html`,
            ), // Оптемезировать сборки `HTMl` если не режим разработки
            minify: {
                // Варианты: https://github.com/terser/html-minifier-terser#options-quick-reference
                collapseWhitespace: !isDev,
                keepClosingSlash: !isDev,
                removeComments: !isDev,
                removeRedundantAttributes: !isDev,
                removeScriptTypeAttributes: !isDev,
                removeStyleLinkTypeAttributes: !isDev,
                useShortDoctype: !isDev,
            },
        }),
        // Удалять старые версии скриптов из `output`
        new CleanWebpackPlugin(),
        // Создать общий `.css` файл со стилями
        new MiniCssExtractPlugin({
            filename: filename('css'),
        }),
        // // Копировать файлы или папки при сборки проекта
        // new CopyWebpackPlugin([
        //         // Копирование
        //         {
        //             // Откуда копировать
        //             from: path.resolve(__dirname,``),
        //             // Куда копировать
        //             to: path.resolve(__dirname,``)
        //         },
        //     ]
        // )
    ];
    if (!isDev) {
        plug.push(new BundleAnalyzerPlugin());
    }

    return plug;
};

// https://webpack.js.org/guides/typescript/
module.exports = {
    // Режим работы [production(сжатие кода)/development]
    mode: strDev,

    // Вариант сборки https://webpack.js.org/configuration/devtool/
    devtool: isDev ? 'source-map' : false,

    // Выходные файл приложения
    entry: {
        // Его мы подключаем в `index.html`
        main: path.resolve(
            __dirname,
            `frontend_react/src/index.tsx`,
        ),
        // Путь к другому файлу для компиляции
        // other: path.resolve(__dirname, `src/other.tsx`)
    },

    // Выходные файлы компиляции
    output: {
        // Имя выходного файла.
        // `name` возьмётся из ключа `entry`.
        // `contenthash` будет создавать хеш файла для индивидуальности
        filename: filename('js'),
        // Путь куда помещаются скомпилированные файлы
        path: path.resolve(__dirname, `frontend_react/static/frontend_react/public/`), // 127.0.0.1/static/frontend_react/public/ откуда подаются файлы
        // Путь который будет в html ссылке
        publicPath: `/static/frontend_react/public/`,
    },

    // Оптимизировать импорты сторонних библиотек
    optimization: optimization(),

    // Файлы с каким расширением мы подключаем без указания расширения
    resolve: {
        extensions: ['.ts', '.tsx', '.js'],
    },

    // Список используемых плагинов
    plugins: plugins(),

    // Настройки для различных форматов файлов (предпроцессоры)
    module: {
        // конфигурация относительно модулей
        rules: [
            // TS
            {
                // свойство определяет, какой файл или файлы следует преобразовать.
                test: /\.tsx|ts?$/,
                // Игнорирует папки [node_modules/, bower_components/]
                exclude: /(node_modules|bower_components)/,
                // какой загрузчик следует использовать для преобразования.
                use: 'ts-loader',
            },
            // CSS
            {
                test: /\.css$/,
                // `css-loader` - поваляет импортировать `.css` в `js`
                // `style-loader` - подключает  `.css` в `HTML` (Удален)
                // `MiniCssExtractPlugin` -  создавать отдельный `.css` файл
                use: [
                    // Настройки для `MiniCssExtractPlugin`
                    {
                        loader: MiniCssExtractPlugin.loader,
                        options: {},
                    },
                    'css-loader',
                ],
            },
            // SASS-SCSS
            {
                test: /\.s[ac]ss$/,
                // `css-loader` - поваляет импортировать `.css` в `js`
                // `style-loader` - подключает  `.css` в `HTML` (Удален)
                // `MiniCssExtractPlugin` -  создавать отдельный `.css` файл
                use: [
                    // Настройки для `MiniCssExtractPlugin`
                    {
                        loader: MiniCssExtractPlugin.loader,
                        options: {},
                    },
                    'css-loader',
                    'sass-loader',
                ],
            },
            // File
            {
                test: /\.(png|jpg|svg|gif|web)$/,
                use: ['file-loader'],
            },
            // Fonts
            {
                test: /\.(ttf|woff|woff2|eot)$/,
                use: ['file-loader'],
            },
        ],
    },

    // Для кеширования
    // externals: {
    //     "react": "React",
    //     "react-dom": "ReactDOM"
    // },

    // Настройка `webpack-dev-server`
    devServer: {
        // Порт на котором будет запущен Лайф сервер
        port: 8011,
        devMiddleware: {
            // Записывать изменения в файл, а не в ОЗУ
            writeToDisk: true,
        },
        // Разрешить все домены
        allowedHosts: 'all',
        // Атоперезагрузка если режим разработки
        hot: isDev,
    },
};
