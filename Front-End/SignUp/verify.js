function validate(){
var rname= ^[a-zA-Z\s]+$;
    if(signup.name.value == ""){
        alert("Please Enter Your Name");
        return false;}
    if(!rname.test(signup.name.value)){
        alert("Enter name in proper format");
        return false;
        
    
}