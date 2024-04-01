#include <stdio.h>

void hacked()
{
    printf("You hacked this level! CSCTF{w0W_y6u_r3al1y_g0T_1T_anD_th3_f1@g_!S_y0urs} \n");
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
