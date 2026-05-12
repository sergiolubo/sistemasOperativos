#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    printf("Proceso padre iniciado. PID=%d\n", getpid());

    for (int i = 0; i < 3; i++) {
        pid_t pid = fork();

        if (pid == 0) {
            printf("Proceso hijo %d creado. PID=%d PPID=%d\n",
                   i + 1, getpid(), getppid());

            sleep(10);

            printf("Proceso hijo %d finalizando. PID=%d\n",
                   i + 1, getpid());

            exit(0);
        }
    }

    sleep(2);

    printf("\nProcesos observados:\n");
    system("ps -o pid,ppid,state,cmd");

    for (int i = 0; i < 3; i++) {
        wait(NULL);
    }

    printf("Proceso padre finalizado.\n");

    return 0;
}
