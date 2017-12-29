from bs4 import BeautifulSoup
import urllib.request


def d(x):
    display(HTML(str(x)))


def soupify(url):
    with urllib.request.urlopen(url) as f:
        html_doc = f.read()
    return BeautifulSoup(html_doc, 'html.parser')


def clear_all(things):
    for i in things:
        i.clear()


def parse_hunter():
    snow_report = soupify('https://m.huntermtn.com/mountain-info/snow-report/')
    lift_trails = soupify("https://m.huntermtn.com/mountain-info/lifts-terrain/#snow-report-lifts")

    css = """
    .hm-status svg {
        width: 1.5em;
        height: 1.5em;
        margin-right: 0.75em;
    }
    
    .hm-legend_icon svg {
        width: 1.5rem;
        height: 1.5rem;
        margin-right: 0.75rem;
    }
    
    .hm-status {
        display: -ms-flexbox;
        display: flex;
        padding: 0.875em 0;
        border-bottom: 1px solid #fffef7;
    }
    
    .hm-status-lift {
        width: calc(50% - 1.5em);
        margin-right: 1.5em;
        padding-left: 0.5em;
        padding-right: 0.5em;
        float: left;
    }
    .hm-status-lift:nth-child(4n-3), .hm-status-lift:nth-child(4n-2) {
        background: #fffef7;
    }
    """

    snow_report.find("div", "swiper-button-prev").clear()
    snow_report.find("div", "swiper-button-next").clear()

    clear_all(lift_trails.find_all("svg", "icon_util_right_thin"))
    clear_all(lift_trails.find_all("button", "hm-status_heading"))

    snow_report_finished = snow_report.find("div", "dynamicCodeInsert sortableModule snow-report-data no-edit-bar")
    lift_report_finished = lift_trails.find("div", "hm-content pb-area")
    output = "<style>{}</style>{}<br>{}".format(str(css), str(snow_report_finished), str(lift_report_finished))
    return output

if __name__ == "__main__":
    print(parse_hunter())
