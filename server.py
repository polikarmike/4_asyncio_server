import asyncio

# Хост и порт для сервера
HOST = 'localhost'
PORT = 9095

# Асинхронная функция для обработки клиентских подключений
async def handle_echo(reader, writer):
    # Читаем данные от клиента (максимум 100 байт)
    data = await reader.read(100)
    message = data.decode()  # Декодируем данные в строку
    addr = writer.get_extra_info('peername')  # Получаем адрес клиента

    # Выводим полученное сообщение и адрес клиента
    print(f"Received {message!r} from {addr!r}")

    # Отправляем данные обратно клиенту (эхо)
    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()  # Убеждаемся, что все данные отправлены

    # Закрываем соединение
    print("Close the connection")
    writer.close()
    await writer.wait_closed()  # Ждем закрытия соединения

# Асинхронная функция для запуска сервера
async def main():
    # Создаем сервер, который будет использовать функцию handle_echo для обработки подключений
    server = await asyncio.start_server(handle_echo, HOST, PORT)

    # Получаем адрес сервера и выводим его
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    # Запускаем сервер и ждем подключений клиентов
    async with server:
        await server.serve_forever()

# Запускаем основную функцию сервера
asyncio.run(main())
