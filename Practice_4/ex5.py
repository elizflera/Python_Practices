class HTML:
    s = ""

    def get_code(self):
        return (self.s)

    class body:
        def __enter__(self):
            HTML.s += "<body>\n"

        def __exit__(self, exc_type, exc_val, exc_tb):
            HTML.s += "</body>\n"

    class div:
        def __enter__(self):
            HTML.s += "<div>\n"

        def __exit__(self, exc_type, exc_val, exc_tb):
            HTML.s += "</div>\n"

    class p():
        def __init__(self, ps):
            HTML.s += "<p>" + ps + "</p>\n"


html = HTML()
html.div()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')
print(html.get_code())
