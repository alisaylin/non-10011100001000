function getInput() {
    var city1 = document.getElementById("city1").value;
    var city2 = document.getElementById("city2").value;
    var city3 = document.getElementById("city3").value;
    var money = document.getElementById("money").value;
    var sex = document.getElementById("sex").value;


    if(city1 == "" || city2 == "" || city3 == "" || money=="Choose One" || sex == "Choose One") {
        window.alert("ERROR: No valid input!");
    } else {
        var myData = new Array(city1, city2, city3, money, sex);

        $.ajax
        ({
            type: "POST",
            dataType : 'json',
            async: false,
            url: 'http://localhost:8000/save_json.php',
            data: { data: JSON.stringify(myData) },
            success: function () {alert("Thanks!"); },
            failure: function() {alert("Error!");}
        });
        window.close();
    }   
}