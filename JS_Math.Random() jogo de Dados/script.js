
const button = document.querySelector('#button')
const declaration = document.querySelector('.winner')
const dados_Computador = document.querySelector('.dadosComputador')
const dados_Jogador = document.querySelector('.dadosJogador')


// Criar pontos
// function teste(){
//     const teste = document.querySelector('#dados3set1')
//     teste.innerText = 'oi'
// }


// function dice_Face(){

//     let valor = []

//     for ( let i = 1; i <= 6; i++){
//         valor[i] = document.querySelector(`#dados${i}`)
//         const dot = document.createElement('div')
//         dot.className = 'dot'
        
//         if (valor[i] === 1){
//             setor.id.appendChild(dot)  
//         } else if (valor[i] === 2){
//             setor.id.appendChild(dot)
//         }
//     }
// }


function mostrar_Dados(){
    function criar_Pontos(dot){
        const pontos = document.createElement('div')
        pontos.className = 'dot'
        dot.appendChild(pontos)
        
    }
    //dado1
    if( valor1 === 1){
        let dot1 = document.querySelector('#dados1set5')
        criar_Pontos(dot1)
    } else if ( valor1 === 2){
        let dot1 = document.querySelector('#dados1set1')
        let dot2 = document.querySelector('#dados1set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2)
    } else if ( valor1 === 3){
        let dot1 = document.querySelector('#dados1set1')
        let dot2 = document.querySelector('#dados1set5')
        let dot3 = document.querySelector('#dados1set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2) 
        criar_Pontos(dot3)
    } else if (valor1 === 4){
        let dot1 = document.querySelector('#dados1set1')
        let dot2 = document.querySelector('#dados1set3')
        let dot3 = document.querySelector('#dados1set7')
        let dot4 = document.querySelector('#dados1set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4)
    } else if ( valor1 === 5){
        let dot1 = document.querySelector('#dados1set1')
        let dot2 = document.querySelector('#dados1set3')
        let dot3 = document.querySelector('#dados1set5')
        let dot4 = document.querySelector('#dados1set7')
        let dot5 = document.querySelector('#dados1set9')
        criar_Pontos(dot1) 
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4) 
        criar_Pontos(dot5)
    } else if (valor1 === 6){
        let dot1 = document.querySelector('#dados1set1')
        let dot2 = document.querySelector('#dados1set3')
        let dot3 = document.querySelector('#dados1set4')
        let dot4 = document.querySelector('#dados1set6')
        let dot5 = document.querySelector('#dados1set7')
        let dot6 = document.querySelector('#dados1set9')
        criar_Pontos(dot1) 
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4) 
        criar_Pontos(dot5) 
        criar_Pontos(dot6)
    }

    //dado2
    if( valor2 === 1){
        let dot1 = document.querySelector('#dados2set5')
        criar_Pontos(dot1)
    } else if ( valor2 === 2){
        let dot1 = document.querySelector('#dados2set1')
        let dot2 = document.querySelector('#dados2set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2)
    } else if ( valor2 === 3){
        let dot1 = document.querySelector('#dados2set1')
        let dot2 = document.querySelector('#dados2set5')
        let dot3 = document.querySelector('#dados2set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2) 
        criar_Pontos(dot3)
    } else if ( valor2 === 4){
        let dot1 = document.querySelector('#dados2set1')
        let dot2 = document.querySelector('#dados2set3')
        let dot3 = document.querySelector('#dados2set7')
        let dot4 = document.querySelector('#dados2set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4)
    } else if ( valor2 === 5){
        let dot1 = document.querySelector('#dados2set1')
        let dot2 = document.querySelector('#dados2set3')
        let dot3 = document.querySelector('#dados2set5')
        let dot4 = document.querySelector('#dados2set7')
        let dot5 = document.querySelector('#dados2set9')
        criar_Pontos(dot1) 
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4) 
        criar_Pontos(dot5)
    } else if ( valor2 === 6){
        let dot1 = document.querySelector('#dados2set1')
        let dot2 = document.querySelector('#dados2set3')
        let dot3 = document.querySelector('#dados2set4')
        let dot4 = document.querySelector('#dados2set6')
        let dot5 = document.querySelector('#dados2set7')
        let dot6 = document.querySelector('#dados2set9')
        criar_Pontos(dot1) 
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4) 
        criar_Pontos(dot5) 
        criar_Pontos(dot6)
    }

    //dado3
    if( valor3 === 1){
        let dot1 = document.querySelector('#dados3set5')
        criar_Pontos(dot1)
    } else if ( valor3 === 2){
        let dot1 = document.querySelector('#dados3set1')
        let dot2 = document.querySelector('#dados3set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2)
    } else if ( valor3 === 3){
        let dot1 = document.querySelector('#dados3set1')
        let dot2 = document.querySelector('#dados3set5')
        let dot3 = document.querySelector('#dados3set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2) 
        criar_Pontos(dot3)
    } else if ( valor3 === 4){
        let dot1 = document.querySelector('#dados3set1')
        let dot2 = document.querySelector('#dados3set3')
        let dot3 = document.querySelector('#dados3set7')
        let dot4 = document.querySelector('#dados3set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4)
    } else if ( valor3 === 5){
        let dot1 = document.querySelector('#dados3set1')
        let dot2 = document.querySelector('#dados3set3')
        let dot3 = document.querySelector('#dados3set5')
        let dot4 = document.querySelector('#dados3set7')
        let dot5 = document.querySelector('#dados3set9')
        criar_Pontos(dot1) 
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4) 
        criar_Pontos(dot5)
    } else if ( valor3 === 6){
        let dot1 = document.querySelector('#dados3set1')
        let dot2 = document.querySelector('#dados3set3')
        let dot3 = document.querySelector('#dados3set4')
        let dot4 = document.querySelector('#dados3set6')
        let dot5 = document.querySelector('#dados3set7')
        let dot6 = document.querySelector('#dados3set9')
        criar_Pontos(dot1) 
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4) 
        criar_Pontos(dot5) 
        criar_Pontos(dot6)
    }

    //dado4
    if( valor4 === 1){
        let dot1 = document.querySelector('#dados4set5')
        criar_Pontos(dot1)
    } else if ( valor4 === 2){
        let dot1 = document.querySelector('#dados4set1')
        let dot2 = document.querySelector('#dados4set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2)
    } else if ( valor4 === 3){
        let dot1 = document.querySelector('#dados4set1')
        let dot2 = document.querySelector('#dados4set5')
        let dot3 = document.querySelector('#dados4set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2) 
        criar_Pontos(dot3)
    } else if ( valor4 === 4){
        let dot1 = document.querySelector('#dados4set1')
        let dot2 = document.querySelector('#dados4set3')
        let dot3 = document.querySelector('#dados4set7')
        let dot4 = document.querySelector('#dados4set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4)
    } else if ( valor4 === 5){
        let dot1 = document.querySelector('#dados4set1')
        let dot2 = document.querySelector('#dados4set3')
        let dot3 = document.querySelector('#dados4set5')
        let dot4 = document.querySelector('#dados4set7')
        let dot5 = document.querySelector('#dados4set9')
        criar_Pontos(dot1) 
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4) 
        criar_Pontos(dot5)
    } else if ( valor4 === 6){
        let dot1 = document.querySelector('#dados4set1')
        let dot2 = document.querySelector('#dados4set3')
        let dot3 = document.querySelector('#dados4set4')
        let dot4 = document.querySelector('#dados4set6')
        let dot5 = document.querySelector('#dados4set7')
        let dot6 = document.querySelector('#dados4set9')
        criar_Pontos(dot1) 
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4) 
        criar_Pontos(dot5) 
        criar_Pontos(dot6)
    }

    //dado5
    if( valor5 === 1){
        let dot1 = document.querySelector('#dados5set5')
        criar_Pontos(dot1)
    } else if ( valor5 === 2){
        let dot1 = document.querySelector('#dados5set1')
        let dot2 = document.querySelector('#dados5set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2)
    } else if ( valor5 === 3){
        let dot1 = document.querySelector('#dados5set1')
        let dot2 = document.querySelector('#dados5set5')
        let dot3 = document.querySelector('#dados5set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2) 
        criar_Pontos(dot3)
    } else if ( valor5 === 4){
        let dot1 = document.querySelector('#dados5set1')
        let dot2 = document.querySelector('#dados5set3')
        let dot3 = document.querySelector('#dados5set7')
        let dot4 = document.querySelector('#dados5set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4)
    } else if ( valor5 === 5){
        let dot1 = document.querySelector('#dados5set1')
        let dot2 = document.querySelector('#dados5set3')
        let dot3 = document.querySelector('#dados5set5')
        let dot4 = document.querySelector('#dados5set7')
        let dot5 = document.querySelector('#dados5set9')
        criar_Pontos(dot1) 
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4) 
        criar_Pontos(dot5)
    } else if ( valor5 === 6){
        let dot1 = document.querySelector('#dados5set1')
        let dot2 = document.querySelector('#dados5set3')
        let dot3 = document.querySelector('#dados5set4')
        let dot4 = document.querySelector('#dados5set6')
        let dot5 = document.querySelector('#dados5set7')
        let dot6 = document.querySelector('#dados5set9')
        criar_Pontos(dot1) 
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4) 
        criar_Pontos(dot5) 
        criar_Pontos(dot6)
    }

    //dado6
    if( valor6 === 1){
        let dot1 = document.querySelector('#dados6set5')
        criar_Pontos(dot1)
    } else if ( valor6 === 2){
        let dot1 = document.querySelector('#dados6set1')
        let dot2 = document.querySelector('#dados6set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2)
    } else if ( valor6 === 3){
        let dot1 = document.querySelector('#dados6set1')
        let dot2 = document.querySelector('#dados6set5')
        let dot3 = document.querySelector('#dados6set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2) 
        criar_Pontos(dot3)
    } else if ( valor6 === 4){
        let dot1 = document.querySelector('#dados6set1')
        let dot2 = document.querySelector('#dados6set3')
        let dot3 = document.querySelector('#dados6set7')
        let dot4 = document.querySelector('#dados6set9')
        criar_Pontos(dot1)
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4)
    } else if ( valor6 === 5){
        let dot1 = document.querySelector('#dados6set1')
        let dot2 = document.querySelector('#dados6set3')
        let dot3 = document.querySelector('#dados6set5')
        let dot4 = document.querySelector('#dados6set7')
        let dot5 = document.querySelector('#dados6set9')
        criar_Pontos(dot1) 
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4) 
        criar_Pontos(dot5)
    } else if ( valor6 === 6){
        let dot1 = document.querySelector('#dados6set1')
        let dot2 = document.querySelector('#dados6set3')
        let dot3 = document.querySelector('#dados6set4')
        let dot4 = document.querySelector('#dados6set6')
        let dot5 = document.querySelector('#dados6set7')
        let dot6 = document.querySelector('#dados6set9')
        criar_Pontos(dot1) 
        criar_Pontos(dot2) 
        criar_Pontos(dot3) 
        criar_Pontos(dot4) 
        criar_Pontos(dot5) 
        criar_Pontos(dot6)
    }


}
    
// }

// criar Dados
function create_Dice(){
    for(let i=1; i<=3; i++){
        const dados = document.createElement('div');
        dados.className = 'dados';
        dados.id = 'dados' + i;
        document.querySelector('.dadosComputador').appendChild(dados)
    }
    for(let i=4; i<=6; i++){
        const dados = document.createElement('div');
        dados.className = 'dados';
        dados.id = 'dados' + i;
        document.querySelector('.dadosJogador').appendChild(dados)
    }
       
    //Criar setores para colocar os pontos
    function setor_Dice(){
        const dadosComputador = document.querySelectorAll('.dadosComputador .dados')
        const dadosJogador = document.querySelectorAll('.dadosJogador .dados')

        for( const dados of dadosComputador){
            for (let i = 1; i <= 9; i++){
            const setor = document.createElement('div');
            setor.className = 'setor'
            setor.id = dados.id + 'set' + i
            dados.appendChild(setor)
        } 
        }

        for( const dados of dadosJogador){
            for (let i = 1; i <= 9; i++){
            const setor = document.createElement('div');
            setor.className = 'setor'
            setor.id = dados.id + 'set' + i
            dados.appendChild(setor)
        } 
        }
        

        

    } 
    setor_Dice()   
   
}

function clean_Dice(){
    const setorComputador = document.querySelector('.dadosComputador')
    const setorJogador = document.querySelector('.dadosJogador')

    setorComputador.innerHTML = '';
    setorJogador.innerHTML = '';
    create_Dice();
}
    

function dice_Throw(){
    valor1 = Math.floor(Math.random()*6) + 1
    valor2 = Math.floor(Math.random()*6) + 1
    valor3 = Math.floor(Math.random()*6) + 1
    valor4 = Math.floor(Math.random()*6) + 1
    valor5 = Math.floor(Math.random()*6) + 1
    valor6 = Math.floor(Math.random()*6) + 1

    soma1 = valor1 + valor2 + valor3
    soma2 = valor4 + valor5 + valor6

    console.log(`O computador tem esses numeros ${valor1},
    ${valor2} e ${valor3}. A soma dele dá ${soma1}.` )

    console.log(`O jogador tem esses numeros ${valor4},
    ${valor5} e ${valor6}. A soma dele dá ${soma2}.`)

    if (soma1 > soma2){
        console.log('O computador ganhou!')
        declaration.innerText = `O computador venceu do jogador: (${soma1} e ${soma2}).`
    }else if (soma2 > soma1){
        console.log('O jogador ganhou!');
        declaration.innerText = `O jogador venceu do computador: (${soma2} e ${soma1}).`
    }else{
        console.log("Empate!")
        declaration.innerText = `O jogador e o computador empataram: (${soma1} e ${soma2}).`
    } 
    
    mostrar_Dados()
}


button.addEventListener('click', ()=>{
    console.clear()
    clean_Dice();
    dice_Throw();
    // teste()
    // console.log(list_setorId);

})


