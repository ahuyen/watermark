let user = "{{ user }}"
async function instascan_ready() {
    console.log("Instascan ready!")        
    document.querySelector("#scan-button").disabled = false
    launch_instascan()
}

async function launch_instascan() {
    let camera = (await Instascan.Camera.getCameras())[0]
    let options = { 
        video: document.getElementById('scan-view'), 
        backgroundScan: false,
        mirror: false
    }
    let scanner = new Instascan.Scanner(options);
    scanner.addListener('scan', function (content) {
        window.location.href = "card/" + content
    });

    let button = document.querySelector("#scan-button")
    let stop = document.querySelector("#stop-button")
    button.onclick = async function() {
        await scanner.start(camera)
        button.style.display = "none"
        stop.style.display = "block"
    }

    stop.onclick = async function() {
        await scanner.stop()
        button.style.display = "block"
        stop.style.display = "none"
    }


    /*Instascan.Camera.getCameras().then(function (cameras) {
        if (cameras.length > 0) {
            scanner.start(cameras[0]);
        } else {
            console.error('No cameras found.');
        }
    }).catch(function (e) {
        console.error(e);
    });*/
}

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
