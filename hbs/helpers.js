var hbs = require('hbs');

hbs.registerHelper('getAnio', () => {
    return new Date().getFullYear();
})
hbs.registerHelper('getNombre', () => {
    return 'matías';
})

hbs.registerHelper('capitalizar', (texto) => {
    let palabras = texto.split(' ');
    palabras.forEach((palabra, idx) => {
        palabras[idx] = palabra.charAt(0).toUpperCase() + palabra.slice(1).toLowerCase()
    })
    return palabras.join(' ')
});