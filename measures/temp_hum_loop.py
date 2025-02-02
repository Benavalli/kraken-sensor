import gpiod
import time

CHIP = "/dev/gpiochip0"  # Para Raspberry Pi OS Bookworm
GPIO_PIN = 18  # Defina o GPIO correto do DHT11

# Inicializa o chip GPIO
chip = gpiod.Chip(CHIP)

def read_dht11():
    global chip  # Garante que estamos sempre usando o mesmo chip

    try:
        # ✅ Libera o pino ANTES de qualquer coisa, para evitar conflitos
        line = chip.get_line(GPIO_PIN)
        try:
            line.release()
        except OSError:
            pass  # Se já estiver liberado, ignora o erro

        # 1️⃣ Configura GPIO como saída para iniciar comunicação
        line.request(consumer="dht11_control", type=gpiod.LINE_REQ_DIR_OUT)
        line.set_value(0)  # Pulso baixo
        time.sleep(0.018)  # Aguarda 18ms
        line.set_value(1)  # Retorna para HIGH
        time.sleep(0.00004)
        line.release()  # ✅ Libera o GPIO ANTES de mudar para leitura

        # 2️⃣ Configura GPIO como entrada para receber dados
        line.request(consumer="dht11_status", type=gpiod.LINE_REQ_DIR_IN)

        # 3️⃣ Aguarda a resposta do sensor
        start_time = time.time()
        while line.get_value() == 1:
            if time.time() - start_time > 0.1:
                print("Timeout ao aguardar início da resposta")
                line.release()
                return None, None

        # 4️⃣ Lê os 40 bits de dados
        data = []
        for _ in range(40):
            start_time = time.time()
            while line.get_value() == 0:
                if time.time() - start_time > 0.1:
                    print("Timeout ao aguardar transição LOW-HIGH")
                    line.release()
                    return None, None

            start_time = time.time()
            while line.get_value() == 1:
                if time.time() - start_time > 0.1:
                    print("Timeout ao aguardar transição HIGH-LOW")
                    line.release()
                    return None, None

            duration = time.time() - start_time
            data.append(1 if duration > 0.00005 else 0)

        line.release()  # ✅ Libera o pino após leitura

        # 5️⃣ Converte os dados lidos
        humidity = int("".join(map(str, data[0:8])), 2)
        temperature = int("".join(map(str, data[16:24])), 2)

        return temperature, humidity

    except OSError as e:
        print(f"Erro ao acessar o GPIO: {e}")
        return None, None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None, None

# Loop principal
while True:
    temp, hum = read_dht11()
    if temp is not None and hum is not None:
        print(f"Temperatura: {temp}°C, Umidade: {hum}%")
    else:
        print("Erro ao ler o sensor. Tentando novamente...")
        time.sleep(3)  # ✅ Tempo maior para evitar erros consecutivos

    time.sleep(2)
