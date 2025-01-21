const crypto = require('crypto');
const fs = require('fs');

function hashAndTruncate(str, n) {
    const hash = crypto.createHash('sha256').update(str).digest('hex');
    const truncatedHash = parseInt(hash.substr(0, Math.ceil(n/ 4)), 16).toString(2).padStart(n, '0').slice(0, n);
    return truncatedHash;
}


// Fonction pour comparer les hachages
function sameHash(message, data, numBits) {
    let count = 0;

    for (let word of data) {
        count++;
        if (hashAndTruncate(word, numBits) === hashAndTruncate(message, numBits)) {
            console.log(`The message ${message} is the same as ${word} in ${count} steps`);
            count = 0;
        }   
    }
}

function randomHashCollision(data, numBits) {
    let count = 0;

    for (let i = 0; i < data.length; i++) {
        let randomIndex1 = Math.floor(Math.random() * data.length);
        let randomIndex2 = Math.floor(Math.random() * data.length);

        while (randomIndex1 === randomIndex2) {
            randomIndex2 = Math.floor(Math.random() * data.length);
        }

        let word1 = data[randomIndex1];
        let word2 = data[randomIndex2];
        
        count++;

        if (hashAndTruncate(word1, numBits) === hashAndTruncate(word2, numBits)) {
            console.log(`The message ${word1} is the same as ${word2} in ${count} steps`);
            count = 0;
        }   
    }
}

// Lire le fichier .txt et utiliser son contenu
fs.readFile('data.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }
    const words = data.split(/\r?\n/); // Diviser le contenu du fichier en lignes
    //sameHash('hello', words, 12); 
    randomHashCollision(words, 16);
});