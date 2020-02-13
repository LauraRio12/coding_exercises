function greet(gender){
 if (gender== "male"){
    return "Hello Sir! Welcome back!";
 }else if(gender== "female"){
     return "Hello Madam!Welcome back!";
 } else{
     return "Hello!Welcome back!";
 }
}
console.log (greet("male"));
console.log (greet("female"));
console.log (greet ("notSpecified"));