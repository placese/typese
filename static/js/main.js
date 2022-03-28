document.addEventListener("DOMContentLoaded", function() { 
    const changeLang = document.querySelector('.lang');

    let current_text = document.getElementById('text-block').textContent.trim();
    let current_text_arr = current_text.split("");
    let new_text = '';
    let type_counter = 0;
    let miss_counter = 0;
    changeLang.addEventListener('change', async (event) => {

        let response = await fetch('/select_language', {
            method: 'POST',
            body: new FormData(document.querySelector('form'))
        })
        let response_text = await response.text();
        let parser = new DOMParser();
        let doc = parser.parseFromString(response_text, 'text/html');
        document.getElementById("text-block").innerHTML = doc.getElementById('text-block').textContent;
        current_text = document.getElementById('text-block').textContent.trim();
        current_text_arr = current_text.split("");
        new_text = '';
        type_counter = 0;
        miss_counter = 0;
    });

    
    
    let excludes = ['Shift', 'Alt', '\`', 'Control', 'CapsLock', 'NumLock', 'Escape', 'Tab', 'GroupNext']
    document.addEventListener('keydown', (keyEvent) => {
        let key = keyEvent.key;
            if (key != current_text_arr[0] && excludes.includes(key) == false && type_counter != current_text.length) {
                console.log(key)
                miss_counter++;
            }
            if (key == current_text_arr[0]) {
                type_counter++;
                indx = current_text.length - current_text_arr.length;
                new_text += current_text.charAt(indx).fontcolor("#FFFFFF") ;
                
                document.getElementById('text-block').innerHTML = new_text + current_text.slice(indx+1);
                current_text_arr.shift();
            }
        
        if (type_counter == current_text.length) {
            document.getElementById("container-right").innerHTML = `Accuracy: ${Math.round((((type_counter - miss_counter) / type_counter) * 100), -2)}%`;
        }
           
        
    })

});