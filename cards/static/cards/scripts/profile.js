let token = Cookies.get('csrftoken')

function post(url, data, callback) {
    let xhr = new XMLHttpRequest()
    xhr.open("POST", url)
    xhr.setRequestHeader("X-CSRFToken", token)
    xhr.setRequestHeader("Content-type", "application/json")

    xhr.send(JSON.stringify(data))

    xhr.addEventListener('load', callback)
}

function createCard() {
    post("create_card", {name: "whatever"}, function() {console.log(this.response.text)})
}

function getCards() {

}

function deleteCard(id) {
    post("delete_card", {"id": id}, function() {console.log("Delete done.")})
}

document.querySelectorAll("[id^=card-]").forEach(el => {
    new QRCode(el, {
        text: el.children[0].textContent,
        width: 100,
        height: 100
    })
})
