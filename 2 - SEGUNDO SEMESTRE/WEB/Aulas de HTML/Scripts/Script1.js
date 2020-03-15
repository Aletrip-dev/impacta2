var nome = "Alexandro Barros de Carvalho";
var idade = 38;
var cursos = ["ADM","DB","PYTHON"];
//vetor ref. a cursos
var notas = [
    [7,4,2],
    [4,8,8],
    [9,9,10]
];
console.log("Olá "+nome)
console.log("idade: "+idade+" anos")

//laço para imprimir cada elemento do vetor em uma linha
for(var i = 0; i <  cursos.length; i++){
    console.log("Cursos: "+cursos[i]);
    var media =0;
    for (var j = 0;j < notas[i].length; j++){
        media = media + notas[i][j];
    }
    media = media /3;
    if (media >= 6){
        console.log("Aprovado!");
    }else{
        console.log("Reprovado!")
    }
}

console.log(3+"4")
