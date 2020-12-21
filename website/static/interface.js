// FormElement class.
class FormElement{
    constructor(){
        this.askButton = document.getElementById("ask_button");
        this.inputQuestion = document.getElementById("question");
        this.chat = document.querySelector("#chat");
        this.grandpyMap = document.getElementById("grandpy_map");
    }
};


// UserHtmlElement class. Class used for creating DOM objects for user
// questions.
class UserHtmlElement{
    constructor(){
        this.divUser = document.createElement("div");
        this.divUserCol = document.createElement("div");
        this.divUserColRow1 = document.createElement("div");
        this.divUserColRow2 = document.createElement("div");
        this.spanUserPrefix = document.createElement("span");
        this.spanTime = document.createElement("span");
        this.spanQuestion = document.createElement("span");
    };

    // Method that set attribute and attribute values.
    defineAttribute() {
        this.divUser.setAttribute("class", "row mt-4 mb-4");
        this.divUserCol.setAttribute("class", "col border border-dark rounded ml-3 mr-5");
        this.divUserColRow1.setAttribute("class", "row pl-1 text-white text-align-justify bg-dark talk");
        this.divUserColRow2.setAttribute("class", "row pl-1 text-light text-align-justify bg-success");
        this.spanUserPrefix.textContent = "# Utilisateur ";
        this.spanUserPrefix.setAttribute("class", "font-weight-bold");
        this.time = new Date();
        this.spanTime.textContent = "[" + this.time.getHours() + ":" + this.time.getMinutes() + ":" + this.time.getSeconds() + "]";
        this.spanQuestion.textContent = formElement.inputQuestion.value;
        this.spanQuestion.setAttribute("class", "text-align-justify font-weight-bold");
    }

    // Method that set build the DOM.
    buildHtml(){
        this.divUser.append(this.divUserCol);
        this.divUserCol.append(this.divUserColRow1);
        this.divUserCol.append(this.divUserColRow2);
        this.divUserColRow1.append(this.spanUserPrefix);
        this.divUserColRow1.append(this.spanTime);
        this.divUserColRow2.append(this.spanQuestion);
    }

};


// GrandpyHtmlElement class. Class used for creating DOM objects for grandpy
// answers.
class GrandPyHtmlElement{
    constructor(){
        this.divGrandPy = document.createElement("div");
        this.divGrandPyCol = document.createElement("div");
        this.divGrandPyColRow1 = document.createElement("div");
        this.divGrandPyColRow2 = document.createElement("div");
        this.divGrandPyColRow3 = document.createElement("div");
        this.spanGrandpyPrefix = document.createElement("span");
        this.spanTime = document.createElement("span");
        this.spanGrandpyPrefixAddress = document.createElement("span");
        this.spanGrandpyAddress = document.createElement("span");
        this.spanGrandpyPrefixWiki = document.createElement("span");
        this.spanGrandpyWiki = document.createElement("span");
        this.spanGrandpyWikiLink = document.createElement("a");
    };

    // Method that set attribute and attribute values.
    defineAttribute(addressPrefix, addressData, wikiPrefix, wikiData, wikiLink) {
        this.divGrandPy.setAttribute("class", "row");
        this.divGrandPyCol.setAttribute("class", "col border border-dark rounded ml-5 mr-3");
        this.divGrandPyColRow1.setAttribute("class", "row pl-1 text-white text-align-justify bg-dark");
        this.divGrandPyColRow2.setAttribute("class", "row pl-1 text-light text-align-justify bg-info");
        this.divGrandPyColRow3.setAttribute("class", "row pl-1 text-light text-align-justify bg-info");
        this.spanGrandpyPrefix.textContent = "# Grandpy";
        this.spanGrandpyPrefix.setAttribute("class", "font-weight-bold");
        this.time = new Date();
        this.spanTime.textContent = "[" + this.time.getHours() + ":" + this.time.getMinutes() + ":" + this.time.getSeconds() + "]";
        this.spanGrandpyPrefixAddress.textContent = addressPrefix;
        this.spanGrandpyAddress.textContent = addressData;
        this.spanGrandpyAddress.setAttribute("class", "font-weight-bold");
        this.spanGrandpyPrefixWiki.textContent = wikiPrefix;
        this.spanGrandpyWiki.textContent = wikiData;
        this.spanGrandpyWiki.setAttribute("class", "font-weight-bold");
        this.spanGrandpyWikiLink.textContent = "[En savoir plus sur WikiPedia]";
        this.spanGrandpyWikiLink.setAttribute("href", wikiLink);
        this.spanGrandpyWikiLink.setAttribute("class", "font-weight-normal text-light");
    }

    // Method that set build the DOM.
    buildHtml(){
        this.divGrandPy.append(this.divGrandPyCol);
        this.divGrandPyCol.append(this.divGrandPyColRow1);
        this.divGrandPyCol.append(this.divGrandPyColRow2);
        this.divGrandPyCol.append(this.divGrandPyColRow3);
        this.divGrandPyColRow1.append(this.spanGrandpyPrefix);
        this.divGrandPyColRow1.append(this.spanTime);
        this.divGrandPyColRow2.append(this.spanGrandpyPrefixAddress);
        this.divGrandPyColRow2.append(this.spanGrandpyAddress);
        this.divGrandPyColRow3.append(this.spanGrandpyPrefixWiki);
        this.divGrandPyColRow3.append(this.spanGrandpyWiki);
        this.spanGrandpyWiki.append(this.spanGrandpyWikiLink);
    }
};


let formElement = new FormElement();


// Function sending a request to application for getting map default url
// on page load.
fetch(`${window.origin}/index/get-url`, {
    method: "GET"
})
.then(function(response) {
    if (response.status !== 200) {
        console.log(`Looks like there was a problem. Status code: ${response.status}`);
        return;
    }
    response.json().then(function(data) {
        formElement.grandpyMap.setAttribute("src", data.gmap_url);
    });
})
.catch(function(error) {
    console.log("Fetch error: " + error);
});


// Function that set form input text box value to null when user click on it.
formElement.inputQuestion.addEventListener("click", function(event) {
    event.preventDefault();
    formElement.inputQuestion.value = null;
});


// Function that set that when user type the "Enter" key, the form button will
// behave as user click on it.
formElement.inputQuestion.addEventListener("keydown", function(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
        formElement.askButton.click();
    }
});    


// Function sending a request to application for posting user input question
// to the app and getting the app response
formElement.askButton.addEventListener('click', function(event) { 
    event.preventDefault();
    let entry = { 
        question: formElement.inputQuestion.value
    };

    fetch(`${window.origin}/index/create-entry`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })

    .then(function(response) {
        if (response.status !== 200) {
            console.log(`Looks like there was a problem. Status code: ${response.status}`);
            return;
        }
        response.json().then(function(data) {

            let userHtml = new UserHtmlElement();
            let grandPyHtml = new GrandPyHtmlElement();
            userHtml.defineAttribute();
            userHtml.buildHtml();

            if (!data.parser_status) {
                let addressPrefix = "Désolé, je n'ai pas compris la question"
                let addressData = null
                let wikiPrefix = null
                let wikiData = null
                let wikiLink = null
                grandPyHtml.defineAttribute(addressPrefix, addressData, wikiPrefix, wikiData, wikiLink);
            } else if (data.parser_status && !data.address_status) {
                let addressPrefix = "Désolé, je ne connais pas cet endroit"
                let addressData = null
                let wikiPrefix = null
                let wikiData = null
                let wikiLink = null
                grandPyHtml.defineAttribute(addressPrefix, addressData, wikiPrefix, wikiData, wikiLink);
            } else if (data.parser_status && data.address_status && !data.information_status) {
                let addressPrefix = "L'adresse de l'endroit recherché est ..."
                let addressData = data.address;
                let wikiPrefix = "... Par contre, je ne sais rien de cet endroit ..."
                let wikiData = null
                let wikiLink = null
                grandPyHtml.defineAttribute(addressPrefix, addressData, wikiPrefix, wikiData, wikiLink);
            } else {
                let addressPrefix = "L'adresse de l'endroit recherché est ..."
                let addressData = data.address;
                let wikiPrefix = "... Et savais tu que... "
                let wikiData = data.information;
                let wikiLink = data.wikipedia_url;
                grandPyHtml.defineAttribute(addressPrefix, addressData, wikiPrefix, wikiData, wikiLink);
            };
            grandPyHtml.buildHtml();
            formElement.chat.prepend(grandPyHtml.divGrandPy);
            formElement.chat.prepend(userHtml.divUser);
            formElement.grandpyMap.setAttribute("src", data.gmap_url);
        });
    })

    .catch(function(error) {
        console.log("Fetch error: " + error);
    });

});
