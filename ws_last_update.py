import requests
import optparse
import sys
from lxml import html


def check_update_date(modid):
    r = requests.get('https://steamcommunity.com/sharedfiles/filedetails/?id='
                     + modid)
    if r.status_code == 200:
        return extract_update_date(r.content)
    return None


def extract_update_date(content):
    dom = html.fromstring(content)
    update = dom.xpath('/html/body/div[1]/div[7]/div[2]/div[1]/div[4]/div[10]/div/div[2]/div[4]/div[2]/div[3]/text()')
    if len(update) == 1:
        return update[0]
    return None


if __name__ == '__main__':
    parser = optparse.OptionParser()

    parser.add_option('-m', '--mod-id',
                      action="store", dest="modid",
                      help="ID of the mod", default="0")

    options, args = parser.parse_args()

    if options.modid == "0":
        print("Specify Steam Workshop ID with --mod-id=<ID> option")
        sys.exit(2)

    res = check_update_date(options.modid)
    if res is None:
        print("Failed to check update date")
        sys.exit(2)
    print(res)
