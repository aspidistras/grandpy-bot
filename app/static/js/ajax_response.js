function ajax(url, callback) {
    var request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (request.readyState == 4 && request.status == 200) {
            response = request.response;
            callback(response);
            }
    };

    if (withCredentials in request) {
        request.open("GET", url,  true);
    }

    else {
        request = null;
        return request;
    }

    request.send(null);
};
