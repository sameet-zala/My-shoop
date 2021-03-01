// const hamburger = document.getElementById('bars');
// const navUL = document.getElementById('nav');

// hamburger.addEventListener('click',() =>{
//     navUL.classList.toggle('show');
//     navUL.classList.toggle('change-bg');
    
// })

function onClickMenu(){
    document.getElementById('nav').classList.toggle('show');
    // document.getElementById('nav').classList.toggle('change-bg');
    document.getElementById('bars').classList.toggle('change-bg');
}