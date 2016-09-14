/*
    From "CSP Is Dead, Long Live CSP! On the Insecurity of Whitelists and the
    Future of Content Security Policy", Listing 7.
*/
var array = document.getElementById('cmd').value.split(',');
window[array[0]].apply(this, array.slice(1));
