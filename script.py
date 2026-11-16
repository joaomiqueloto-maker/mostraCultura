#include <stdio.h>

struct Aluno{
    char nome[50];
    int idade;
    float notas[3];
};

void imprimirAluno(struct Aluno aluno) {
    printf("Nome: %s\n", aluno.nome);
    printf("Idade: %s\n", aluno.idade);
    printf("Notas: %.2f, %.2f, %.2f\n", aluno.notas[0], aluno.notas[1], aluno.notas[2]);
}

int main() {
    struct Aluno aluno1 = {"João", 20, {8.5, 7.0, 90}};
    imprimirAluno(aluno1);
    return 0;
}
