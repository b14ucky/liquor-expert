const prompt = document.getElementById('prompt')
const generateButton = document.getElementById('generate')
const output = document.getElementById('output')

const url = "http://localhost/api/generate"

generateButton.addEventListener('click', e => {
    output.innerHTML = "Myślę..."
    fetch(url, {
        method: "POST",
        body: JSON.stringify({
            question: prompt.value
        }),
        headers: {
            "Content-Type": "application/json"
        }
    })
        .then(response => response.json())
        .then(json => {
            output.innerHTML = marked.parse(json.response)
        })
})