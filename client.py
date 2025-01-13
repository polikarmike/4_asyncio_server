import asyncio

# Хост и порт для подключения клиента
HOST = 'localhost'
PORT = 9095


# Асинхронная функция для клиентской части
async def tcp_echo_client(message):
    # Устанавливаем соединение с сервером
    reader, writer = await asyncio.open_connection(HOST, PORT)

    print(f'Send: {message!r}')  # Выводим отправляемое сообщение
    writer.write(message.encode())  # Отправляем сообщение на сервер
    await writer.drain()  # Убеждаемся, что все данные отправлены

    # Читаем ответ от сервера (максимум 100 байт)
    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')  # Выводим полученные данные

    print("Close the connection")  # Сообщаем о закрытии соединения
    writer.close()  # Закрываем соединение
    await writer.wait_closed()  # Ждем, пока соединение полностью закроется


# Асинхронная функция для запуска клиента
async def main():
    await tcp_echo_client("Hello, asyncio!")  # Отправляем сообщение серверу


# Запускаем клиентскую часть
asyncio.run(main())
