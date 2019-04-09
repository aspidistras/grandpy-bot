function ajax(url, callback) {
    var request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (request.readyState == 4 && request.status == 200) {
            response = request.responseText;
            callback(response);
            }
    };
    request.open("GET", url,  true);
    request.send(null);
};

