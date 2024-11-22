function showPage(view) {
    event.preventDefault();
    let xhr = new XMLHttpRequest();
    xhr.open("GET", `/api/views${view}/`, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if (xhr.status == 200) {
                document.getElementById('content').innerHTML = JSON.parse(xhr.responseText).html;
                loadScripts();
            }
            else
                document.getElementById('content').innerHTML = `<h1>Error ${xhr.status}</h1>`;
        }
    };
    history.pushState({ path: view }, '', view);
    xhr.send();
}

window.onpopstate = function (event) {
    if (event.state) {
        let path = event.state.path;
        let xhr = new XMLHttpRequest();
        xhr.open("GET", `/api/views${path}/`, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    document.getElementById('content').innerHTML = JSON.parse(xhr.responseText).html;
                    loadScripts();
                }
                else
                    document.getElementById('content').innerHTML = `<h1>Error ${xhr.status}</h1>`;
            }
        };
        xhr.send();
    }
    else
        document.getElementById('content').innerHTML = '<h1>Error</h1><p>State not found</p>';
};

function loadScripts() {
    let scripts = document.getElementById('content').getElementsByTagName('script');
    
    for (let i = 0; i < scripts.length; i++) {
        let script = document.createElement('script');
        script.type = scripts[i].type || 'text/javascript';
        if (scripts[i].src)
            script.src = scripts[i].src;
        else
            script.innerHTML = scripts[i].innerHTML;
        document.body.appendChild(script);
    }
}

window.onload = function() {
    let path = window.location.pathname;
    if (path === '/')
        showPage("/home");
    else
        showPage(path);
};