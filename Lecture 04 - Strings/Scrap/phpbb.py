import re
import requests

tag_pattern = re.compile(r'<[^>]*>')
br_pattern = re.compile(r'<br\s*/>')

patterns_replacement_list = [(tag_pattern, ''), (br_pattern, "\n")]


def send_request(url: str) -> str:
    response = requests.get(url)
    html_content = response.text
    return html_content


def select_posts_content(html_content: str) -> list:
    # pattern to find every <div class="content"> </div>, there should be post content inside it
    div_content_pattern = re.compile(r'<div class="content">(.+?)</div>\n', re.DOTALL)
    content = div_content_pattern.findall(html_content)
    return content


def replace_unnecessary_tags(post: str) -> str:
    for pattern_replacement in patterns_replacement_list:
        pattern = pattern_replacement[0]
        replacement = pattern_replacement[1]

        post = pattern.sub(replacement, post)

        return post


def write_in_file(file_name: str, content: list) -> None:
    with open(file_name, 'w') as file:
        for index, post in enumerate(content):
            post = replace_unnecessary_tags(post)

            formated_post = f"{index + 1}. [{post}]\n"
            file.write(formated_post)
            print(formated_post)


def main():
    url = 'http://www.phpbb.com/community/viewtopic.php?f=46&t=2159437'
    html_content = send_request(url)
    posts_content = select_posts_content(html_content)

    write_in_file('phpbb.txt', posts_content)


if __name__ == '__main__':
    main()
