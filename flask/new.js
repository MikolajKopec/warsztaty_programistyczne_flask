
window.addEventListener('DOMContentLoaded', (event) => {
 function check(){
     x = document.querySelectorAll('.img-note')
     z = document.querySelector('.note')
     
     if (x[0].parentElement.classList.contains('slider-slide-active')){
     z.textContent=x[0].textContent;
     }
     else if (x[1].parentElement.classList.contains('slider-slide-active')){
     z.textContent=x[1].textContent;
     }
     if (x[2].parentElement.classList.contains('slider-slide-active')){
     z.textContent=x[2].textContent;
     }
     }
 var timer = setInterval(check, 100);
 q=document.querySelectorAll('.slider-button')
 n=document.querySelector('.next');
 p=document.querySelector('.prev');
 p.addEventListener('click',function(){
 q[0].click();
 })
 n.addEventListener('click',function(){
 q[1].click();
 })
 q[0].click();
 });
 