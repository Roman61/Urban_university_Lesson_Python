import serial

# Настройка COM-порта
ser = serial.Serial(
    port='COM2',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

# Отправка данных
data = b"Hello, serial port!"
ser.write(data)

# Закрытие порта
ser.close()

