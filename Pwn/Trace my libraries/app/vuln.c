#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char correct_pass[] = "\xc3\xd2\xc1\xd7\xc2\xfe\xea\xb4\xfc\xa7\xf9\xd4\xf8\xff\xcf\xec\xa3\xce\xe6\xfb\xf1\xca\xfa\xfe\xfa\xeb\xda\xe9\xad\xae\xcd\xc0\xff\xfe\xfd\xfc\xfb\xfa\xf9\xf8\xf7\xf6\xf5\xf4\xf3\xf2\xf1\xf0\xef\xee\xed\xec\xeb\xea\xd4\xe2\xec\xe6\xcd\x88\xe3\xd3\x8d\xfa\x84\x9e\xb6\xab\xa1\x9a\xa4\x8e\xaf\xe7\xba\xa2\x8f\xb9\x9b\xbd\xe3\xac";


char *deobf(char *s)
{
	int i;
	for (i = 0 ; i < strlen(s); i++) {
		s[i] = s[i] ^ 0x80 ^ (i%256);
	}
	return s;
}

int main()
{
	char buf[1000];
	printf("Password: ");
	if (true) {
		char flag[] = "CSCTF{try_again_kiddo}";
	}
	if (fgets(buf, 1000, stdin) == NULL)
		exit(-1);
	buf[strlen(buf) - 1] = '\0';

	if (!strcmp(buf, deobf(correct_pass))) {
		printf("Correct!\n");
	} else
		printf("Nope!\n");

	return 0;
}