const hamburger = document.getElementById('bars');
const navUL = document.getElementById('nav');

hamburger.addEventListener('click',() =>{
    navUL.classList.toggle('show');
    navUL.classList.toggle('change-bg');
    
})