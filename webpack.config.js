module.exports = {
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: { loader: `awesome-typescript-loader`}
            },
            {
                enforece: `pre`,
                test: /\.js$/,
                loader: `source-map-loader`
            }
        ]
    }
}