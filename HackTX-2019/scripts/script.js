function getInput() {
    var fullname = document.getElementById("fullname").value;
    var dob = document.getElementById("DOB").value;
    var email = document.getElementById("email").value;
    var drop = document.getElementById("drop").value;

    if(fullname == "" || dob == "" || email=="" || drop == "Choose One") {
        window.alert("ERROR: No valid input!");
    } else {
        console.log(fullname);
        console.log(dob);
        console.log(email);
        console.log(drop);
        
      var myData = new Array(fullname, dob, email, drop);

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
      window.open("question.html")

    }   
}