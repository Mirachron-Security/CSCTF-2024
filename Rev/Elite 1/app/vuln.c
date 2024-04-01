#include <stdio.h>

int main() {
    int input;

    printf("Enter a number: ");
    if (scanf("%d", &input) == 1) {
        if (input == 0x539) { 
            printf("Good job! You got the flag!\n");
        } else {
            printf("Try again.\n");
        }
    } else {
        printf("Invalid input.\n");
    }

    return 0;
}
