console.log("HELLO");

var token=2222

var login = function(e){
    console.log(e);
    var n = document.getElementById('name').value;
    var p = document.getElementById('password').value;
    payload = {'name':n,'password':p};
    console.log("PAYLOAD");
    console.log(JSON.stringify(payload));

    fetch('http://127.0.0.1:5000/login', {
	method: 'POST', // or 'PUT'
	headers: {
	    'Content-Type': 'application/json',
	},
	body: JSON.stringify(payload),
    })
	.then(response => response.json())
	.then(data => {
	    console.log('Success:', data);
	    window.token=data.token
	    if (data.token==1){
		make_data_page()
	    }
	    console.log(window.token);
	})
	.catch((error) => {
	    console.error('Error:', error);
	});

}

var get_movies = function(e){
    console.log("GETTING MOVIES")
    console.log(e);
    var n = document.getElementById('query').value;
    console.log(window.token);
    payload = {'token':window.token,'q':n};
    fetch('http://127.0.0.1:5000/get_movies', {
	method: 'POST', // or 'PUT'
	headers: {
	    'Content-Type': 'application/json',
	},
	body: JSON.stringify(payload),
    })
	.then(response => response.json())
	.then(data => {
	    console.log('Success:', data);
	    var c = document.getElementById('page')
	    var l = document.createElement('ul');
	    for (i in data.data){
		var item = document.createElement('li')
		item.innerText = data.data[i][0]
		l.appendChild(item);
	    }
	    c.appendChild(l)
	    
	    
	})
	.catch((error) => {
	    console.error('Error:', error);
	});

    
}



var make_login_page = function(){
    var p = document.createElement("div");
    p.setAttribute("id","page");
    var e = document.createElement("p")
    e.innerText="Name:"
    p.appendChild(e);
    e = document.createElement("input")
    e.setAttribute("id","name")
    p.appendChild(e);
    var e = document.createElement("p")
    e.innerText="Password:"
    p.appendChild(e);
    e = document.createElement("input")
    e.setAttribute("id","password")
    p.appendChild(e);
    e = document.createElement("button")
    e.innerText="submit"
    e.addEventListener('click',login);
    p.appendChild(e);
    var div = document.getElementById('app');
    div.firstChild.remove()
    div.appendChild(p)
}


var make_data_page = function(){
    var p = document.createElement("div");
    p.setAttribute("id","page");
    var e = document.createElement("h1")
    e.innerText="Get Movies:"
    p.appendChild(e);
    e = document.createElement("p")
    e.innerText="Query:"
    p.appendChild(e);
    e = document.createElement("input")
    e.setAttribute("id","query");
    p.appendChild(e);
    e = document.createElement("button")
    e.innerText="submit"
    e.addEventListener('click',get_movies);
    p.appendChild(e);

    var div = document.getElementById('app');
    div.firstChild.remove()
    div.appendChild(p)

}

var make_route_page = function(){
    var p = document.createElement("div");
    var b = document.createElement("button");
    b.innerText="Login Page";
    b.setAttribute('id','lbutton');
    b.addEventListener('click',make_login_page)
    p.appendChild(b);
    b = document.createElement("button");
    b.innerText="Movies Page";
    b.setAttribute('id','mbutton');
    b.addEventListener('click',make_data_page)
    p.appendChild(b);
    
    var div = document.getElementById('routes');
    div.appendChild(p)

}



make_login_page()
make_route_page()
