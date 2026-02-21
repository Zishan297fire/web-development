function validate(e){
    e.preventDefault();

    const email=document.getElementById("email").value
   const pass=document.getElementById("password").value
    const age=document.getElementById("age").value
     const msgBox=document.getElementById("message").value
     let message=""
     if (email ===""){
        message="please enter the email"
     }
     else if(pass ===""){
        message="please enter a password"
     }
       else if(age ===""){
        message="please enter a age"
       }
       else{
        message="login success full"
       }
       msgBox.innerhtml=message
    }
       document.getElementById("loginForm").onsubmit = validate;

// Real-time validation (like the screenshots)

document.getElementById("email").oninput = () => validate({ preventDefault: () => {} });

document.getElementById("password").oninput = () => validate({ preventDefault: () => {} });

document.getElementById("age").oninput = () => validate({ preventDefault: () => {} });




