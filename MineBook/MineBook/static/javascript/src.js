const searchInput = document.getElementById("src")
const spinner = document.getElementById("spinner")
const t = document.getElementById("table")


searchInput.addEventListener("input",e =>{
    const value = e.target.value
    let row = [...t.rows]
    console.log(value)
    i=-1
    for (let r of row.slice(1, row.length)){
        let isNotIncluded = false
        i+=1
        for (let c of r.cells) {
            if (c.innerHTML.includes(value)){
                isNotIncluded = true
            }
        }
        if (!isNotIncluded) {
            document.getElementById(`a${i}`).style.display = "none";
        }
        else {
            document.getElementById(`a${i}`).style.display = "";

        }
    } 
})


