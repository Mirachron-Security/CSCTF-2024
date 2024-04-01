#include <stdio.h>

void hacked()
{
    printf("You need NATO secret clearance! Get out of here immediately! Also, we have flags.\n");
}

void accept_name()
{
    char buffer[16];

    printf("Who are you?\n");
    scanf("%s", buffer);
    printf("This way, %s\n", buffer);    
}

int main()
{
    accept_name();

    return 0;
}
