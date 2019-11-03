function getInput() {
    var city = document.getElementById("city").value;
    var money = document.getElementById("money").value;
    var sex = document.getElementById("sex").value;


    if(city == "" || money=="Choose One" || sex == "Choose One") {
        window.alert("ERROR: No valid input!");
    } else {
        console.log(city);
        console.log(money);
        console.log(sex);
        var myData = new Array(city, money, sex);

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
    }   
}