import requests
import re

tag_pattern = re.compile(r'<[^>]*>')
bracket_pattern1 = re.compile(r'&#91;')
bracket_pattern2 = re.compile(r'&#93;')
quote_pattern = re.compile(r'&quot;')
pattern_list = [(tag_pattern, ''), (bracket_pattern1, '['), (bracket_pattern2, ']'), (quote_pattern, '"')]


def send_request(url: str) -> str:
    response = requests.get(url)
    html_content = response.text
    return html_content


def remove_unnecessary_tags(html_content: str) -> str:
    unnecessary_info_pattern = re.compile(r'<div class="post-signature(.*?)<div class="h-flex-spacer h-margin-top-16">', re.DOTALL)
    html_content = unnecessary_info_pattern.sub('', html_content)

    return html_content


def select_post(html_content: str) -> list:
    div_content_pattern = re.compile(
        r'js-post__content-text restore h-wordwrap" itemprop="text">(.+?)<div class="b-post__footer h-hide--on-preview">', re.DOTALL)

    post_content = div_content_pattern.findall(html_content)
    return post_content


def replace_characters(post: str) -> str:
    for pattern_tuple in pattern_list:
        pattern = pattern_tuple[0]
        replacement = pattern_tuple[1]

        post = pattern.sub(replacement, post)

    post = re.sub(r'([\t\r])', r'', post).strip()
    post = re.sub(r'\n\s*\n', '\n', post)

    return post


def write_in_file(filename: str, content: list) -> None:
    with open(filename, 'w') as file:
        for index, post in enumerate(content):
            post = replace_characters(post)
            formated_line = f"{index + 1}. [{post}]\n"
            file.write(formated_line)
            print(formated_line)


def main():
    url = 'https://forum.vbulletin.com/forum/vbulletin-3-8/vbulletin-3-8-questions-problems-and-troubleshooting/414325-www-vs-non-www-url-causing-site-not-to-login'
    html_content = send_request(url)
    html_content = remove_unnecessary_tags(html_content)
    posts_content = select_post(html_content)
    write_in_file('vbulletin.txt', posts_content)


if __name__ == '__main__':
    main()
