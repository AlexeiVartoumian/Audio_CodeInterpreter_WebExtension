
chrome.runtime.onMessage.addListener(function(request,sender,sendResponse){

    if(request.data){
        const url = 'http://127.0.0.1:5000/receive-data';

        fetch(url, {
            method: 'POST',
            headers:{
                'Content-Type':'application/json',
            },
            body:JSON.stringify(request.data),
        })
        .then(response => response.text())
        .then(responseText => {
            sendResponse({message:responseText})
        })
        .catch(error => {
            sendResponse({message: "error sending data"})
        })
        return true;
    }
})

function printhtml(){
    const item = window.document.getElementsByClassName("ace_layer ace_text-layer")
    console.log(item[0])
    //const data = Array.from(item);
    //console.log(data)
    data= []
    for(let i = 0; i< item.length;i++){
        const items = item[i];
        const itemData= {
            textContent: items.textContent,
            className:items.className
        }
        data.push(itemData)
    }
    const jsonData = JSON.stringify(data);
    console.log(jsonData)
    fetch('http://127.0.0.1:5000/receive-data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: jsonData
    })
    .then(response => {
        if (response.ok) {
            console.log('Data sent successfully');
            return fetch('http://127.0.0.1:5000/send-mp3',{
                method:'GET',
            })
        } else {
            console.error('Failed to send data');
        }
    })
    .then(response =>{
        if(response.ok){
            return response.blob()
        }else{
            console.log("failed to recieve data")
        }
    } )
    .then(mp3Blob =>{
        //console.log('received data:',data)
        const audio = new Audio(URL.createObjectURL(mp3Blob))
        audio.play()
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
chrome.action.onClicked.addListener((tab) => {

    if(!tab.url.includes('chrome://')){
        chrome.scripting.executeScript({
            target:{ tabId: tab.id},
            function: printhtml
        })
    }
})