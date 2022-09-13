'use strict';

let user_answer = prompt('What\'s the official name of Javascript?', '').toLowerCase();


if (user_answer == 'idk'){
    while (user_answer == 'idk'){
        alert('Atleast guess')
        user_answer = prompt('What\'s the official name of Javascript?', '').toLowerCase();
    }
    check_answer(user_answer)
}
else{
    check_answer(user_answer)
}

function check_answer(answer){
    if (answer == 'ecmascript'){
        alert('RIGHT');
    }
    else{
        alert('WOW, you don\'t know the official name!');
    }
}

let default_name = 'Anonymous';
let given_name = prompt('What is your name?', '')

given_name = given_name ?? default_name //if empty will make the alert return empty
alert(`${given_name} has signed in.`)
given_name = given_name || default_name //if empty will return anonymous
alert(`${given_name} has signed in.`)

//?? will work with null and undefined values but || works with any empty value alongside null and undefined

//example change

