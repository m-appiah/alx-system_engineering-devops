#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop
 *
 * Return: int
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - the starting point
 *
 * Return: success(0)
 */
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid == 0)
			exit(0);
		else if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(2);
		}
		else
		{
			perror("Fork failed");
			exit(2);
		}
	}
	infinite_while();
	return (0);
}
