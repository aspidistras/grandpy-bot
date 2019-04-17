function ajax(url, callback) { // ajax call
    var request = new XMLHttpRequest(); // create request object
    request.onreadystatechange = function() {
        if (request.readyState == 4 && request.status == 200) { // if the request succeeded
            response = request.response; // get request response
            callback(response); // calling callback function to handle data
            }
    };

    request.withCredentials = true; // to allow CORS
    request.open("GET", url,  true);

    request.send(null);
};

