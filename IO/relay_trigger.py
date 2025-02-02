import gpiod
import time

CHIP = "/dev/gpiochip0"  # Para Raspberry Pi OS Bookworm
GPIO_PIN = 26  # Pino que controla o relé (e será lido)

# Inicializa o chip
chip = gpiod.Chip(CHIP)

# Configura o pino como saída para controle do relé
line = chip.get_line(GPIO_PIN)
line.request(consumer="relay_control", type=gpiod.LINE_REQ_DIR_OUT)

while True:
    # Liga o relé
    print("Ligando Relé")
    line.set_value(1)
    time.sleep(2)

    # Libera o pino para leitura
    line.release()
    line.request(consumer="relay_status", type=gpiod.LINE_REQ_DIR_IN)

    # Lê o estado do relé
    relay_state = line.get_value()
    print(f"Estado do Relé: {'LIGADO' if relay_state == 1 else 'DESLIGADO'}")

    # Volta para modo de saída e desliga o relé
    line.release()
    line.request(consumer="relay_control", type=gpiod.LINE_REQ_DIR_OUT)
    print("Desligando Relé")
    line.set_value(0)
    time.sleep(2)

    # Libera o pino novamente para leitura
    line.release()
    line.request(consumer="relay_status", type=gpiod.LINE_REQ_DIR_IN)

    # Lê o estado do relé novamente
    relay_state = line.get_value()
    print(f"Estado do Relé: {'LIGADO' if relay_state == 1 else 'DESLIGADO'}")

    # Volta para modo de saída
    line.release()
    line.request(consumer="relay_control", type=gpiod.LINE_REQ_DIR_OUT)
