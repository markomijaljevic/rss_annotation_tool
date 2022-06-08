
function setAndSendRequest(url, body, method="POST"){

    var xhr = new XMLHttpRequest();

    xhr.open(method, url, true);
    xhr.setRequestHeader('X-CSRFToken', document.getElementsByName('csrfmiddlewaretoken')[0].value);
    xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8");
    xhr.setRequestHeader("Accept", "application/json");


    if (method == "POST")
        xhr.send(JSON.stringify({"body":body}));
    else
        xhr.send();

    window.location.reload();
}


function showCommentBox(commentBoxId){
    const box = document.getElementById(commentBoxId);
    box.style.display = "block";
}

function closeCommentBox(commentBoxId){
    const box = document.getElementById(commentBoxId);
    box.style.display = "none";
}

function addComment(commentBoxId){
    const box = document.getElementById(commentBoxId);
    const comment = box.getElementsByTagName("textarea")[0].value;
    const url = "feeds/article/" + commentBoxId

    setAndSendRequest(url, comment)
    closeCommentBox(commentBoxId);
}