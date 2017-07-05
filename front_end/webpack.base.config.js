const path = require('path');
const webpack = require('webpack');


module.exports = {
    entry: './src/app.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'app.bundle.js'
    },
    module: {
        rules: [
            {
                test: /\.js$/, exclude: /node_modules/, use: "babel-loader"
            }
        ]
    }
    // devServer: {
    //     contentBase: path.join(__dirname, 'dist'),
    //     port: 9000,
    //     stats: 'errors-only',
    //     open: true
    // }
};