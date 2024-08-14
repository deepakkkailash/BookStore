
console.log('hello')
const toggledisps = (div1,div2) =>{
       div1.classList.add('opacity-0')
       div1.classList.remove('opacity-100')
       div1.classList.add('z-0')
       div2.classList.remove('opacity-0')
       div2.classList.add('opacity-100')
       div2.classList.remove('z-0')
       div2.classList.add('z-50')

}

document.getElementById('showhome').addEventListener('click',()=>{

    toggledisps(document.getElementById('welcomediv'),document.getElementById('homediv'));

});

document.getElementById('loginbut').addEventListener('click',()=>{
    toggledisps(document.getElementById('homediv'),document.getElementById('loginform'))
})

document.getElementById('tosignup').addEventListener('click',(event)=>{
    event.preventDefault()
    toggledisps(document.getElementById('loginform'),document.getElementById('signupform'))
})

document.getElementById('backtologin').addEventListener('click',(event)=>{
event.preventDefault()
    toggledisps(document.getElementById('signupform'),document.getElementById('loginform'))
})

