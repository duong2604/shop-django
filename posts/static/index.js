const root = document.documentElement
const darkBtn = document.getElementById('dark')
const lightBtn = document.getElementById('light')
console.log(root.getAttribute('data-bs-theme'))

function setDarkTheme(){
    root.setAttribute("data-bs-them", 'dark')
}

function setLightTheme(){
    console.log('light')
    root.setAttribute("data-bs-them", 'light')
}


darkBtn.onclick = ()=>{
    root.getAttribute('data-bs-theme')
}

lightBtn.onclick = ()=>{
    setLightTheme()
    root.getAttribute('data-bs-theme')
    }


