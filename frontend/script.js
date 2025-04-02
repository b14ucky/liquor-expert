const prompt = document.getElementById('prompt')
const generateButton = document.getElementById('generate')
const output = document.getElementById('output')

const url = "http://fastapi:8000/generate"

generateButton.addEventListener('click', e => {
    fetch(url, {
        method: "POST",
        body: JSON.stringify({
            prompt: prompt.value
        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(response => response.json())
        .then(json => {
            output.innerHTML = marked.parse(json.response)
        })
})
