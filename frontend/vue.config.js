module.exports = {
  "devServer": {
    "disableHostCheck": true,
    "proxy": {
      '/api': {
        "target": 'http://localhost:8080',
        "pathRewrite": { '^/api': '' },
        "changeOrigin": true,
        "secure": false
      }
    }
  },
  "transpileDependencies": [
    "vuetify"
  ]
}
