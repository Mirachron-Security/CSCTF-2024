#include <stdio.h>
#include <string.h>

int main() {
    char answer[100];
    const char correctAnswer[] = "2023";
    const char *flag1 = "CSCTF{couldn't_";
    const char *flag2 = "think_of";
    const char *flag3 = "_a_";
    const char *flag4 = "cool_flag_";
    const char *flag5 = "so_there_you_go}";

    printf("When was the first edition of CSCTF?\n");
    printf("Your answer: ");

    scanf("%99s", answer);

    if (strcmp(answer, correctAnswer) == 0) {
        printf("Congratulations! You got it right.\n");
    } else {
        printf("Sorry, that's not correct. Try again.\n");
    }

    return 0;
}
