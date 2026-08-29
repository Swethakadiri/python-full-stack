let a ={
    title:"pfsd",
    description:"full stack",
    trainer:"swetha"
}

console.log(a['title']);


//reference
let k={name:"naresh"};
let y=k;
k="swetha";
console.log(k);
console.log(y);

///Arrays
let course=['pfsd','jfsd','mern'];
console.log(course);
console.log(course[0]);
console.log(course[1]);
console.log(course[2]);
console.log(course[3]);
console.log(course[4]);
console.log(course[5]);

//execution content
//1.memory phase-variable environment
//2.code phase-thread of  environment
createCourse('jfsd');
console.log(m)
function createCourse(coursename){
    console.log('creating' + coursename);
}
createCourse('pfsd');
createCourse('jfsd');


//let & var ,const
{
let z = 10;
var o = 20;
const v = 30;
}
console.log(z);
console.log(o);
console.log(v);

//
function hello(){
    var x = 10;
    console.log(x);

}
hello();

//add
let m = function add(a,b){
    return a+b
}
console.log(a);
console.log(a(1,2));

//
let add=(a,b) => a+b;
let diff = (a,b) => a-b;
console.log(add(2,3));
console.log(diff(2,3));

//
let n = 10;
function outer(){
    n = 100;
    function inner(){
        console.log(n);
    }
    return inner;
}
let returnFunc = outer();
console.log(returnFunc);
returnFunc();













