let englishToFrench = () => {
    let textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                document.getElementById("translated_text").innerHTML = xhttp.responseText;
            } else {
                console.error('Translation request failed with status:', this.status);
            }
        }
    };
    xhttp.open("GET", "/englishToFrench?textToTranslate=" + textToTranslate, true);
    xhttp.send();
}

let frenchToEnglish = () => {
    let textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                document.getElementById("translated_text").innerHTML = xhttp.responseText;
            } else {
                console.error('Translation request failed with status:', this.status);
            }
        }
    };
    xhttp.open("GET", "/frenchToEnglish?textToTranslate=" + textToTranslate, true);
    xhttp.send();
}