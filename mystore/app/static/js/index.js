
  $('#slider1,#slider2,#slider3,.owl-carousel').owlCarousel({
    // loop:true,
    margin:20,
    nav:true,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
            nav:true,
            autoplay:true
        },
        600:{
            items:3,
            nav:false,
            autoplay:true

        },
        1000:{
            items:4,
            nav:false,
            // loop:true,
            autoplay:true,
        }
    }
})


$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var elm=this.parentNode.children[1]
 
    $.ajax({
        type:"GET",
        url:"/plus",
        data:{
            product_id:id
        },
        success:function(data){
            // console.log(data)
            elm.innerText=data.quantity
            document.getElementById('amount').innerHTML=data.amount+".00"
            document.getElementById('totalamount').innerHTML=data.totalamount+".00"
        }
    })
})


$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var elm=this.parentNode.children[1]
    $.ajax({
        type:"GET",
        url:"/minus",
        data:{
            product_id:id
        },
        success:function(data){
            // console.log(data)
            elm.innerText=data.quantity
            document.getElementById('amount').innerHTML=data.amount+".00"
            document.getElementById('totalamount').innerHTML=data.totalamount+".00"
        }
    })
})


$('.remove').click(function(){
    var id=$(this).attr("pid").toString();
    var elm=this
    $.ajax({
        type:"GET",
        url:"/remove",
        data:{
            product_id:id
        },
        success:function(data){
            elm.parentNode.parentNode.parentNode.parentNode.remove()
            document.getElementById('amount').innerHTML=data.amount+".00"
            document.getElementById('totalamount').innerHTML=data.totalamount+".00"
        }
    })
})


let burger=document.querySelector(".burger")
let closee =document.querySelector(".close")
burger.onclick=function(){
   var myclass=document.querySelector(".nav_div")
   myclass.classList.add("display")

}
closee.onclick=function(){
   var myclass=document.querySelector(".nav_div")
   myclass.classList.remove("display")

}

// slider

let temp= 0;


function control(x){
    temp+=x
    show(temp)
}

function show(num){
   let slider=document.getElementsByClassName("slider")
     
    if(num == slider.length){
        temp=0
        num=0
    }
    if(num < 0){
        temp=slider.length-1;
        num=slider.length-1;
    }

   for(let y of slider){
    y.style.display='none';
   }  

   slider[num].style.display='block';
   
}
show(temp)





// form show

let pop=document.querySelector(".window");
let=time=setTimeout(fun,3000);
function fun(){ 
    
    pop.style.opacity="1"
    pop.style.visibility="visible"
    pop.style.height="100vh"
    
}

let close1=()=>{
    pop.style.display="none"
    console.log(pop)
}


// form validation

function fun(){
    let user=String(document.querySelector("#username").value);
    let bg=document.querySelector(".form_box")
    let box=document.querySelector(".form_box .box")
    let max_char=document.getElementById("max_char");
    if (user.length >= 5){
        bg.style.boxShadow="2px 5px 10px 1px rgba(19, 247, 68, 0.945)"
        max_char.style.opacity="0"
        box.classList.add("active")
        console.log(box)
   }else{
        max_char.style.opacity="0.6"
        
        bg.style.boxShadow=""
        box.classList.remove("active")

   }
}


