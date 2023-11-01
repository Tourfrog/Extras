
const texto = document.querySelector('#texto');
const palavra = document.querySelector('#palavra');
const botao = document.querySelector('#botao');
let lista_Palavra_Geral = [];
let lista_Letra_Geral = [];

const card = document.querySelector('.card')
const letra_Proibida = document.querySelector('.letraProibida');
const digitada = document.querySelector('.digitada');

// Criar os player, e fazer com que os player não saiba 
// as palavras e letras proibidas dos outros
// função automatica de declaração de quantidade de player,

//testando o prompt e captura de valor 
// var player1 = prompt('Qual é o seu nome?')
// console.log(`Olá ${player1}`)

let numberPlayer = prompt('Digite a quantidade de jogadores:');



let players = [];

for ( let i = 0; i < numberPlayer; i++){
    let playerName = prompt(`Jogador nº${i + 1}. Qual é o seu nome?`);
    let player = {
        id: i + 1,
        name: playerName,
        list_first_letter: [],
        list_first_word: []
    }
    players.push(player)
};
console.log(players);

if (players.length === 0){
        alert('Coloque a quantidade de pessoas que vão jogar.')
        window.location.reload()
}

function showName(){
    
    let currentPlayer = players[0];
    texto.innerText = `${currentPlayer.name}. Digite aqui uma palavra: `; 

}
showName();


// Tentando colocar as proprias palavras e letras usadas e agora proibidas
// do proprio jogador. Os outros jogadores não pode ver as palavras e letras dos outros.
// function show_Tabboo_Words(player){

//     let currentPlayer = players[player];

//     if (currentPlayer.list_first_letter.length === 0 &&
//          currentPlayer.list_first_word.length === 0){
//         digitada.innerText = '';
//         letra_Proibida.innerText = '';
//     } else{
//         digitada.innerText = currentPlayer.list_first_word.join(', ');
//         letra_Proibida.innerText = currentPlayer.list_first_letter.join(', ') 
//     }       
// }
// show_Tabboo_Words();


function mostrar_Letras_Usadas(){
    digitada.innerText = players[0].list_first_word
    letra_Proibida.innerText = players[0].list_first_letter 
}


function pegarPalavra(){
    
    // // colocar a palavra no array lista_Palavra
    // lista_Palavra.push(palavra.value)
    // // colocar a primeira letra no array lista_Letra
    // lista_Letra.push(palavra.value.charAt(0))
    // // Verificar se está funcionando a função do click, charAt e push
    // console.log(palavra.value , lista_Palavra , lista_Letra)

    // agora criar uma condição que proibi a utilização 
    // de palavras que comece com as letras no array lista_Letra 

    const primeiraLetra = palavra.value.charAt(0).toLowerCase();

    if (lista_Letra_Geral.includes(primeiraLetra) ){
        alert("Perdeu. Essa letra já foi usada antes!")
        // alert(`Perdeu ${currentPlayer.name}! Essa letra já foi usada antes!`)

        //embaixo, tem uma função de atualizar a pag. depois de apertar o botão
        window.location.reload()

    } else{

        // colocar a palavra no array lista_Palavra
        lista_Palavra_Geral.push(palavra.value)
        //colocando a palavra que o player escreveu na propria lista
        players[0].list_first_word.push(palavra.value)
            
        // colocar a primeira letra no array lista_Letra
        lista_Letra_Geral.push(primeiraLetra)
        //colocando a primeira letra no proprio array 
        players[0].list_first_letter.push(primeiraLetra)

        //Colocando as Listas no HTML

        // digitada.innerText = players[0].list_first_word
        // letra_Proibida.innerText = players[0].list_first_letter        

        // Verificar se está funcionando a função do click, charAt e push
        console.log(players)
        console.log(`Esta é da lista geral,
        palavras usadas : ${lista_Palavra_Geral},
        letras poribidas: ${lista_Letra_Geral}.`);
        // letra_Proibida.innerText = lista_LetraProibida_player;
        // digitada.innerText = lista_PalavraProibida_player;
        palavra.value = ''
        
        
        players.push(players.shift())
        
        
    }
};



botao.addEventListener('click', (e)=>{
    e.preventDefault();
    pegarPalavra();
    showName();
    mostrar_Letras_Usadas();
    palavra.value = ''
})



//Dar a tecla 'Enter' a função de pegarPalavra() e evita a atualização da pagina
palavra.addEventListener('keydown', function(e){
    if (e.key === 'Enter'){
        e.preventDefault();
        pegarPalavra();
        showName();
        mostrar_Letras_Usadas();
        palavra.value = ''
    }
});

// setTimeout((
//     alert(`Já passou de 15 segundos, ${players[0].name}. Você perdeu!`)
// ), 20000)

//Nova função, atrelar a pegarPalavra(), 
// um efeito css de transição animação,
// um 'rolamento' da pagina do player 1 e
// do player 2 ...7yuuuuull