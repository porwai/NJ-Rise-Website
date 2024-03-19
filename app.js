// Imports
const express = require('express')
const app = express()
const port = 5000

// Static Files
app.use(express.static('public'))
app.use('*/css',express.static('public/css'));
app.use('*/js',express.static('public/js'));
app.use('*/assets',express.static('public/assets'));

// Set Views
app.set('views', './views')
app.set('view engine', 'ejs')

app.get('/', (req, res) => {
    res.render('pages/login', { title: 'Login'})
})

app.get('/index', (req, res) => {
    res.render('pages/index', { title: 'Pantry Dashboard'})
})

app.get('/reports', (req, res) => {
    res.render('pages/reports', { title: 'Reports'})
})

app.get('/staff', (req, res) => {
    res.render('pages/staff', { title: 'Manage Staff'})
})

app.get('/profile', (req, res) => {
    res.render('pages/profile', { title: 'Profile'})
})

// Listen on Port 5000
app.listen(port, () => console.info(`App listening on port ${port}`))