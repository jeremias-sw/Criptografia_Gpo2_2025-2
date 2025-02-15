#include <stdio.h>
#include <stdlib.h>
#include <string.h>



//funciones
void cifrado();
void descifrado();

int main() {
	//declarar variables



	int opcion;
	printf("Cifrado Cesar \n");

	while (opcion != 3) {
		printf("\nQu� desea hacer?\n");
		printf("1.) Cifrar\n");
		printf("2.) Descifrar\n");
		printf("3.) Salir\n");
		printf("Seleccione una opci�n: \n");
		scanf("%d", &opcion);
		system("cls");

		//menu para elegir la funci�n
		switch (opcion) {
		case 1:
			//funcion de cifrado
			cifrado();
			break;
		case 2:
			descifrado();
			break;
		case 3:
			return 3;
		default:
			return 0;
		}
	}
}
// ------------------------------------------
// funci�n de cifrado
void cifrado() {
	int llave;
	char mensaje[100], letra, cipher[100];
	// recepci�n de mensaje y llave
	printf("\nIngrese el mensaje en min�sculas que desea cifrar: ");
	scanf("%s", &mensaje);
	printf("\nIngrese la llave (valor num�rico entero): ");
	scanf("%d", &llave);
	// proceso de cifrado
	int i;
	for (int i = 0; i < strlen(mensaje); i++) {
		letra = mensaje[i];
		letra = (letra - 'a' + llave + 26) % 26 + 'a';
		cipher[i] = letra;
	}
	printf("\n Mensaje cifrado: %s \n", &cipher);


}

// -----------------------------------------
// funcion de descifrado
void descifrado() {
    int llave;
	char mensaje[100], letra, cipher[100];
	// recepci�n de mensaje y llave
	printf("\nIngrese el mensaje en min�sculas que desea descifrar: ");
	scanf("%s", &mensaje);
	printf("\nIngrese la llave (valor num�rico entero): ");
	scanf("%d", &llave);
	// proceso de cifrado
	int i;
	for (int i = 0; i < strlen(mensaje); i++) {
		letra = mensaje[i];
		letra = (letra - 'a' - llave + 26) % 26 + 'a';
		cipher[i] = letra;
	}
	printf("\n Mensaje original: %s \n", &cipher);

}
