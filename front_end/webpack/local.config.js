const path = require('path');
const webpack = require('webpack');

const merge = require('webpack-merge');
const BundleTracker = require('webpack-bundle-tracker');

const config = require('./base.config');
const constants = require('../constants');

const ip = 'localhost';


module.exports = merge(config, {
    devtool: '#eval-source-map',
    output: {
        publicPath: 'http://' + ip + ':9000' + '/static/js/'
    },
    module: {
        rules: [
            { test: /\.jsx?$/, exclude: /node_modules/, use: ['babel-loader'] },
        ]
    },
    plugins: [
        new BundleTracker({path: constants.staticFilesJsDir, filename: 'webpack-stats.json'}),
        new webpack.HotModuleReplacementPlugin(),
    ],
    devServer: {
        contentBase: constants.staticFilesJsDir,
        port: 9000,
        stats: 'errors-only'
    },
});
