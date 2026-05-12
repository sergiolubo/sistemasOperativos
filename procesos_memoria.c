#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int hijos = 3;
    size_t memoria_mb = 50;
    size_t bytes = memoria_mb * 1024 * 1024;
    printf("Proceso padre: PID=%d\n", getpid());
    for (int i = 0; i < hijos; i++) {
        pid_t pid = fork();
        if (pid == 0) {
            char *memoria = malloc(bytes);
            if (memoria == NULL) {
                perror("Error reservando memoria");
                exit(1);
            }
            for (size_t j = 0; j < bytes; j += 4096) {
                memoria[j] = 1;
            }
            printf("Hijo %d: PID=%d, PPID=%d, memoria reservada=%zu MB\n",
                   i + 1, getpid(), getppid(), memoria_mb);
            sleep(20);
            free(memoria);
            printf("Hijo %d: PID=%d finaliza y libera memoria\n", i + 1, getpid());
            exit(0);
        }
    }
    sleep(3);
    printf("\nProcesos relacionados:\n");
    system("ps -o pid,ppid,state,%mem,%cpu,cmd");
    for (int i = 0; i < hijos; i++) {
        wait(NULL);
    }
    printf("Proceso padre finaliza: PID=%d\n", getpid());
    return 0;
}
