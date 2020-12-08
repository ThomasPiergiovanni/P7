class FormElement{
    constructor(){
        this.askButton = document.getElementById("ask_button");
        this.inputQuestion = document.getElementById("question");
        this.chat = document.querySelector("#chat");
        this.grandpyMap = document.getElementById("grandpy_map");
    }
};

class UserHtmlElement{
    constructor(){
        this.divUser = document.createElement("div");
        this.divUserRow = document.createElement("div");
        this.divUserCol = document.createElement("div");
        this.divUserColRow1 = document.createElement("div");
        this.divUserColRow2 = document.createElement("div");
        this.spanUserPrefix = document.createElement("span");
        this.spanTime = document.createElement("span");
        this.spanQuestion = document.createElement("span");
    };

    defineAttribute(number) {
        this.divUser.setAttribute("class", "mb-2");
        this.divUserRow.setAttribute("class", "row");
        this.divUserCol.setAttribute("class", "col-10");
        this.divUserColRow1.setAttribute("class", "row");
        this.divUserColRow2.setAttribute("class", "row");
        this.spanUserPrefix.textContent = "# Utilisateur ";
        this.spanUserPrefix.setAttribute("class", "font-weight-bold");
        this.time = new Date();
        this.spanTime.textContent = "[" + this.time.getHours() + ":" + this.time.getMinutes() + ":" + this.time.getSeconds() + "]";
        this.spanQuestion.textContent = formElement.inputQuestion.value
        this.spanQuestion.setAttribute("class", "text-align-justify")
    }

    buildHtml(){
        this.divUser.append(this.divUserRow);
        this.divUserRow.append(this.divUserCol);
        this.divUserCol.append(this.divUserColRow1);
        this.divUserCol.append(this.divUserColRow2);
        this.divUserColRow1.append(this.spanUserPrefix);
        this.divUserColRow1.append(this.spanTime);
        this.divUserColRow2.append(this.spanQuestion);
    }

};

class GrandPyHtmlElement{
    constructor(){
        this.divGrandPy = document.createElement("div");
        this.divGrandPyRow = document.createElement("div");
        this.divGrandPyCol1= document.createElement("div");
        this.divGrandPyCol2= document.createElement("div");
        this.divGrandPyCol2Row1= document.createElement("div");
        this.divGrandPyCol2Row2= document.createElement("div");
        this.divGrandPyCol2Row3= document.createElement("div");
        this.spanGrandpyPrefix = document.createElement("span");
        this.spanTime = document.createElement("span");
        this.spanGrandpyPrefixAddress = document.createElement("span");
        this.spanGrandpyAddress = document.createElement("span");
        this.spanGrandpyPrefixWiki = document.createElement("span");
        this.spanGrandpyWiki = document.createElement("span");
    };

    defineAttribute(data) {
        this.divGrandPy.setAttribute("class", "mb-4");
        this.divGrandPyRow.setAttribute("class", "row");
        this.divGrandPyCol1.setAttribute("class", "col-2");
        this.divGrandPyCol2.setAttribute("class", "col-10");
        this.divGrandPyCol2Row1.setAttribute("class", "row");
        this.divGrandPyCol2Row2.setAttribute("class", "row");
        this.divGrandPyCol2Row3.setAttribute("class", "row");
        this.spanGrandpyPrefix.textContent = "# Grandpy"
        this.spanGrandpyPrefix.setAttribute("class", "font-weight-bold");
        this.time = new Date();
        this.spanTime.textContent = "[" + this.time.getHours() + ":" + this.time.getMinutes() + ":" + this.time.getSeconds() + "]";
        this.spanGrandpyPrefixAddress.textContent = "L'adresse de l'endroit recherché est ..."
        this.spanGrandpyAddress.textContent = data.address
        this.spanGrandpyAddress.setAttribute("class", "font-italic text-align-justify");
        this.spanGrandpyPrefixWiki.textContent = "... Et savais tu que... "
        this.spanGrandpyWiki.textContent = data.information;
        this.spanGrandpyWiki.setAttribute("class", "font-italic text-align-justify");
    }

    buildHtml(){
        this.divGrandPy.append(this.divGrandPyRow);
        this.divGrandPyRow.append(this.divGrandPyCol1);
        this.divGrandPyRow.append(this.divGrandPyCol2);
        this.divGrandPyCol2.append(this.divGrandPyCol2Row1);
        this.divGrandPyCol2.append(this.divGrandPyCol2Row2);
        this.divGrandPyCol2.append(this.divGrandPyCol2Row3);
        this.divGrandPyCol2Row1.append(this.spanGrandpyPrefix);
        this.divGrandPyCol2Row1.append(this.spanTime);
        this.divGrandPyCol2Row2.append(this.spanGrandpyPrefixAddress);
        this.divGrandPyCol2Row2.append(this.spanGrandpyAddress);
        this.divGrandPyCol2Row3.append(this.spanGrandpyPrefixWiki);
        this.divGrandPyCol2Row3.append(this.spanGrandpyWiki);
    }
};

let formElement = new FormElement();

formElement.inputQuestion.addEventListener("click", function(event) {
    event.preventDefault();
    formElement.inputQuestion.value = null;
});

formElement.inputQuestion.addEventListener("keydown", function(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
        formElement.askButton.click();
    }
});    

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
        grandPyHtml.defineAttribute(data);
        grandPyHtml.buildHtml();
        formElement.chat.prepend(grandPyHtml.divGrandPy);
        formElement.chat.prepend(userHtml.divUser);
        formElement.grandpyMap.src = data.map;

        });
    })
    .catch(function(error) {
        console.log("Fetch error: " + error);
    });

});