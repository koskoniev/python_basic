import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

        html = html[html.find("<body>") + len("<body>"):html.find("</body>")]

        # while html.count("<a class") > 0:
        #     html = html.replace(html[html.find("<a class"):html.find("/a>") + 3], '')
        #
        # while html.count(">") > 0:
        #     html = html.replace(html[html.find("<"):html.find(">") + 1], "")
        #
        # html = html.split("\n")
        # outlet = str()

        # for i in range(len(html)):
        #     if html[i].count(" ") == len(html[i]):
        #         continue
        #     else:
        #         outlet += html[i] + "\n"

    with codecs.open(result_file, 'w', 'utf-8') as result:
        result.write(html)

    return True


html_text = "D:\\PycharmProjects\\python_basic\\Lessons\\draft.html"
# html_text = "..\\Lessons\\draft.html"
print(html_text)
print(delete_html_tags(html_text))
