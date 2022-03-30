document.addEventListener("DOMContentLoaded", function() { 
    const changeLang = document.querySelector('.lang');

    let current_text = document.getElementById('text-block').textContent.trim();
    let current_text_arr = current_text.split("");
    let words_num = current_text.split(" ").length;
    let new_text = '';
    let type_counter = 0;
    let miss_counter = 0;
    let is_time_started_flag = false;
    let langg = new FormData(document.querySelector('form'));
    changeLang.addEventListener('change', async (event) => {
        langg = new FormData(document.querySelector('form'));
        console.log(langg.get("lang"))
        let response = await fetch('/select_language', {
            method: 'POST',
            body: langg
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
        is_time_started_flag = false;
    
          
    });

    let excludes = ['Shift', 'Alt', '\`', 'Control', 'CapsLock', 'NumLock', 'Escape', 'Tab', 'GroupNext', 'Backspace',
                    'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12']
    let start_time = new Date().getTime();
    document.addEventListener('keydown', (keyEvent) => {
        if (type_counter != current_text.length) {

        if (is_time_started_flag == false) {
            start_time = new Date().getTime();
            is_time_started_flag = true;
        }
        let key = keyEvent.key;
            if (key != current_text_arr[0] && excludes.includes(key) == false && type_counter != current_text.length) {
                console.log(key)
                miss_counter++;
            }
            if (key == current_text_arr[0]) {
                type_counter++;
                indx = current_text.length - current_text_arr.length;
                new_text += current_text.charAt(indx).fontcolor("#FFFFFF");
                
                document.getElementById('text-block').innerHTML = new_text + current_text.slice(indx+1);
                current_text_arr.shift();
            }
        
        if (type_counter == current_text.length) {
            let end_time = new Date().getTime() - start_time
            end_time = new Date(end_time);
            let time_spend = end_time.getMinutes() * 60 + end_time.getSeconds();

            document.getElementById("container-right").innerHTML = 
            `Accuracy: ${Math.round((((type_counter - miss_counter) / type_counter) * 100), -2)}%<br>
             SPM: ${Math.round(type_counter/time_spend*60)}<br>
             WPM: ${Math.round(words_num/time_spend*60)}
            `;
        }
           
    }
        
    })

});