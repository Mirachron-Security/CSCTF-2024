#include <stdio.h>

int main() {
    int input;

    printf("Enter a hexadecimal number: ");
    if (scanf("%x", &input) == 1) {
        int new = input ^ 10101010; 
        if (new == 0x499602D2) {
            printf("Good job! Go get your flag!\n");
        } else {
            printf("Try again.\n");
        }
    } else {
        printf("Invalid input.\n");
    }

    return 0;
}