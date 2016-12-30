import datetime
import re

header = """
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <link rel="stylesheet" href="stylesheet.css">
    <title>ICQ-Chat</title>
</head>
<body>
"""

footer = """
</body>
</html>
"""


def convert_xml_to_html(xml):
    xml = xml.replace("<event>", "<div class='event'>")
    xml = xml.replace("<type>0</type>", "")
    xml = xml.replace("<incoming>Yes", "<div class='incoming-yes'>Manu")
    xml = xml.replace("<incoming>No", "<div class='incoming-no'>Joern")
    xml = xml.replace("</incoming>", "")
    xml = xml.replace("<time>", "")
    timestamps = re.findall("\d{10}", xml)
    for timestamp in timestamps:
        xml = xml.replace(timestamp, convert_timestamp(float(timestamp)))
    xml = xml.replace("</time>", "</div>")
    xml = xml.replace("<text>", "<div class='message'>")
    xml = xml.replace("</text>", "</div>")
    xml = xml.replace("</time>", "</div>")
    xml = xml.replace("</event>", "</div>")
    return xml


def convert_timestamp(timestamp):
    time = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return time


def build_index_page(converted_xml):
    return header + converted_xml + footer


def write_index_page(html):
    pass


def main():
    import glob
    filenames = glob.glob("data/*.xml")
    with open('output/xml_input.xml', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

    with open('output/xml_input.xml', 'r') as infile:
        converted_xml = convert_xml_to_html(infile.read().replace('\n', ''))
        index_page = build_index_page(converted_xml)

    with open('output/index.html', 'w') as outfile:
        for line in index_page:
            outfile.write(line)



if __name__ == '__main__':
    assert("2006-08-22 18:16:05" == convert_timestamp(1156270565))
    main()
