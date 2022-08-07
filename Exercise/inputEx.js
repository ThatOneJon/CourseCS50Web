
document.addEventListener('DOMContentLoaded', () => {

document.querySelector("form").onsubmit = () => {
    let inp  = document.querySelector("#text").value;
    let el = document.createElement('li');
    el.innerHTML = inp;

    document.querySelector("#list").append(el);
    
    document.querySelector("#text").value=" ";
    return false;

    }; 
});


document.addEventListener('DOMContentLoaded', () => {
    document.querySelector("#GO").onclick = () => {
    fetch("https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0")
    .then((response) => response.json())
    .then(data => {
        console.log(data.dataseries[0])
        for(let i = 0; i < data.dataseries.length; i++){
            console.log(data.dataseries.i["cloudcover"]);
        }
        })
    }
});
