import requests
import sys
from lxml import html


def download(url):
    """Returns the HTML source code from the given URL
        :param url: URL to get the source from.
    """
    r = requests.get(url)
    if r.status_code != 200:
        sys.stderr.write("! Error {} retrieving url {}\n".format(r.status_code, url))
        return None

    return r


if __name__ == '__main__':
    sys.stdout.write("=============================\n")
    sys.stdout.write("== Lingwars - Scrape XPath ==\n")
    sys.stdout.write("=============================\n")

    url = "http://www.juntadeandalucia.es/medioambiente/atmosfera/informes_siva/feb17/gr170215.htm"

    page = download(url)
    if page:
        sys.stdout.write("\n\n1) Download text from {}\n".format(url))
        sys.stdout.write(page.text[:200])

        # Parse the text to XML structures
        sys.stdout.write("\n\n2) Let's try some XPath expresions:")
        tree = html.fromstring(page.content)

        # Execute xpath over retrieved html content
        xpath_string = '//a/@href'
        results = tree.xpath(xpath_string)
        sys.stdout.write('\n\t'.join(results))

    else:
        sys.stdout.write("Nothing was retrieved.")
