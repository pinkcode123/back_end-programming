document.getElementById('login').addEventListener ("submit", function(event) {
    const name = "EnGentech";
    const passcode = "Admin1234"; 
    
    const inputname = document.getElementById("name").value;
    const inputpasscode =  document.getElementById("passcode").value;
  if( inputname == name && inputpasscode == passcode) {
    alert("success");
  } else {
    alert("fail");
  }
   });