setTimeout(fade_out, 2000);

function fade_out() {
  $("#mydiv").fadeTo("fast",0).remove();
}
setTimeout(fade_in,3000);
function fade_in(){
  $("#q1").fadeTo("normal",0.9)
};
function no_question(n){
  for ( var i = 1; i < n; i++ ) (function(i){ 

        $("#submit"+i.toString()).on('click',function(){
          $("#q"+(i+1).toString()).fadeTo("normal",0.9)
    }); 

 
  })(i);
}
no_question(11);

