#include <stdio.h>

int main()
{
    int enough = 0;
    char rule[50];

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    puts("Do you know the military regulation? Give me a good rule:");
    gets(rule);

    if (enough != 0)
    {
        puts("I didn't know that one until now. Please, take this flag:");
        system("cat flag.txt");
    }

    else
    {
        puts("\nGood enough.\n");
    }
}