import codecs
import string


def delete_html_tags(html_file, result_file='D:\\PycharmProjects\\python_basic\\DZ\\cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

        html = html[html.find("<body>"):html.find("</body>")]

        while html.count("<a class") > 0:
            html = html.replace(html[html.find("<a class"):html.find("</a>") + 4], '')

        while html.count(">") > 0:
            html = html.replace(html[html.find("<"):html.find(">") + 1], "")

        html = html.split("\n")
        outlet = str()
        for i, e in enumerate(html):
            if e.count(" ") != len(e):
                outlet += e + "\n"
        html = outlet

    with codecs.open(result_file, 'w', 'utf-8') as result:
        result.write(html)
        file.close()
        result.close()

    return True


html_text = "D:\\PycharmProjects\\python_basic\\Lessons\\draft.html"
# print(html_text)
delete_html_tags(html_text)
