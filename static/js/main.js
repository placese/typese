document.addEventListener("DOMContentLoaded", function() { 
    const changeLang = document.querySelector('.lang');

    changeLang.addEventListener('change', async (event) => {

        let response = await fetch('/select_language', {
            method: 'POST',
            body: new FormData(document.querySelector('form'))
        })
        let response_text = await response.text();
        let parser = new DOMParser();
        let doc = parser.parseFromString(response_text, 'text/html');
        document.getElementById("text-block").innerHTML = doc.getElementById('text-block').textContent

    });

    current_text = document.getElementById('text-block').textContent.trim()
    current_text_arr = current_text.split("")
    new_text = ''

    document.addEventListener('keydown', (keyEvent) => {
        let key = keyEvent.key;
        for (var i = 0; i < current_text_arr.length; i++) {
            if (key == current_text_arr[0]) {
                indx = current_text.length - current_text_arr.length
                console.log(new_text);
                new_text += current_text.charAt(indx).fontcolor("#FFFFFF") ;
                
                document.getElementById('text-block').innerHTML = new_text + current_text.slice(indx+1);
                current_text_arr.shift();
                console.log(document.getElementById('text-block'))
            }
        }
    })

});