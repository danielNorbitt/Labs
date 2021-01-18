#include <stdio.h>
#include <stdlib.h>


int corretor(char** dic, char* palavra)

int main(){
    
    int n,q;

    char* palavraBuscada;

    scanf("%d %d",&n,&q);

    char** dic = (char**) malloc(n*sizeof(char*)*26); 
    
    for (int i = 0; i < n; i++){
        char *palavra = (char *)malloc(sizeof(char) * 26);
        scanf("%s ", palavra);
        dic[i] = palavra;
    }
    
    for (int i = 0; i < q; i++)
        scanf("%s ",palavraBuscada);
    

    return 0;
}
