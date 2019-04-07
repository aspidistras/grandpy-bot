function ajax(url, callback) {
    var request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (request.readyState == 4 && request.status == 200) {
            response = request.responseText;
            alert(response);
            return response;
            }
    };
    request.open("GET", "page.html",  true);
    request.send(null);
};
