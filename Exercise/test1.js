document.addEventListener('DOMContentLoaded', () => {
let x = document.querySelector("#first");
x.addEventListener("mouseover", () =>{
    x.innerHTML = "<p id =p1>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illum, commodi odio! Nam, doloremque porro quos tenetur excepturi, vel corrupti provident, quibusdam nemo explicabo totam laborum? Consequuntur nesciunt expedita quo nulla fugiat, excepturi deleniti! Sit quia, quae porro odit aliquid assumenda at nostrum voluptates possimus delectus sint nam vel eum nulla dolores, numquam tempora, doloremque suscipit? Consequuntur voluptates reiciendis dignissimos culpa facere odio eligendi quis, asperiores quos non impedit sequi placeat numquam fugiat provident, quas doloremque quod magni pariatur! Quaerat, dolore deleniti quas molestias ratione illo qui, nihil, reprehenderit repudiandae quidem repellendus quod excepturi delectus iure doloribus? Voluptas voluptate quasi mollitia!</p>";

    });
x.addEventListener("mouseout", () => {
    x.innerHTML= "<h1 id ='first'> The first is back </h1>"
    });

});

var count = 0;
function counter() {
    count ++;
};

document.addEventListener('DOMContentLoaded', () => {
    let y = document.querySelector("#second");
    y.addEventListener("mouseover", () => {
    counter();    
    y.innerHTML = `<h1>${count}</h1>`;
    });
});

var count2 = 0

document.addEventListener('DOMContentLoaded', () => {
    let z = document.querySelector("#counting");

    document.querySelector("#buttonOne").onclick = () => {
        count2 += 10;
        if (count2 % 5 === 0) {
            z.innerHTML = `<h1>${count2}</h1> <br> <p>Divisible by 5!</p>`
        }else{
            z.innerHTML = `<h1>${count2}</h1> <br> <p>Not Divisible by 5!</p>`

        }
    };

    document.querySelector("#buttontwo").onclick = () => {
        count2 += 22;
        if (count2 % 5 === 0) {
            z.innerHTML = `<h1>${count2}</h1> <br> <p>Divisible by 5!</p>`
        }else{
            z.innerHTML = `<h1>${count2}</h1> <br> <p>NOT Divisible by 5!</p>`

        }
    };

});