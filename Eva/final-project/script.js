function getApartments() {
    var beds = document.getElementById("beds").value;
    var baths = document.getElementById("baths").value;
    var price = document.getElementById("price-select").value;
    var major = document.getElementById("major").value;

    const url = "https://hqoz62l7j7.execute-api.us-east-1.amazonaws.com/dev/notes";
    const data = {
        'title' : major,
        'description' : price
    };
    const other_params = {
        headers : { "content-type" : "application/json; charset=UTF-8" },
        body : data,
        method : "POST",
        mode : "cors"
    };

    fetch(url, other_params)
        .then(function(response) {
            if (response.ok) {
                alert(response.json());
            } else {
                throw new Error("Could not reach the API: " + response.statusText);
            }
        }).then(function(data) {
            document.getElementById("message").innerHTML = data.encoded;
        }).catch(function(error) {
            document.getElementById("message").innerHTML = error.message;
        });
    
    return false;
}