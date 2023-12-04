import threading
import time

class SemafaroSimples:
    def __init__(self):
        self.semaforo = threading.Semaphore(1)

    def secao_critica(self):
        with self.semaforo:
            # Seção crítica - código que precisa ser protegido
            print(f"{threading.current_thread().name} está na seção crítica.")
            time.sleep(2)
            print(f"{threading.current_thread().name} saiu da seção crítica.")

def tarefa(sem):
    sem.secao_critica()

# Criar uma instância do semáforo simples
semaforo = SemafaroSimples()

# Criar várias threads para simular acesso concorrente
threads = []
for i in range(5):
    t = threading.Thread(target=tarefa, args=(semaforo,), name=f"Thread-{i+1}")
    threads.append(t)
    t.start()

# Aguardar que todas as threads terminem
for thread in threads:
    thread.join()

print("Todas as threads terminaram.")
