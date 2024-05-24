import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    __html_filename = "index.html"
    __css_filename = "style.css"

    def __get_html_content(self):
        with open(self.__html_filename, "r", encoding="utf-8") as fd:
            return fd.read()

    def __get_css_content(self):
        with open(self.__css_filename, "r", encoding="utf-8") as fd:
            return fd.read()

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        if self.path == f"/{self.__css_filename}":
            mime_type = "text/css"
            content = self.__get_css_content()
        else:
            mime_type = "text/html"
            content = self.__get_html_content()

        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", mime_type)  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(content, "utf-8"))  # Тело ответа


if __name__ == "__main__":
    load_dotenv()
    host_name = os.getenv('HOST', "localhost")  # Адрес для доступа по сети
    server_port = int(os.getenv('PORT', "8080")) # Порт для доступа по сети

    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    web_server = HTTPServer((host_name, server_port), MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        web_server.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    web_server.server_close()
    print("Server stopped.")
