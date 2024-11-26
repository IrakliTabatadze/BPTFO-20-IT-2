import json

movies_lst = []


def read_file(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)

        return data


def write_file(file_name):
    with open(file_name, 'w') as json_file:
        json.dump(movies_lst, json_file, indent=4)


def parse_movies(page):
    for movie in page:
        release_year = int(movie['release_date'][:4])
        genres = movie['genres']

        if release_year > 2000 and 'Crime' in genres:
            movie['genres'].remove('Crime')
            movie['genres'].append('New_Crime')
        elif release_year < 2000 and 'Drama' in genres:
            movie['genres'].remove('Drama')
            movie['genres'].append('Old_Drama')
        elif release_year == 2000:
            movie['genres'].append('New_Century')

        movies_lst.append(movie)


def read_pages(json_data):
    for page in json_data:
        # print(page['results'])
        parse_movies(page['results'])


if __name__ == '__main__':
    filename = 'movies.json'
    json_data = read_file(filename)
    read_pages(json_data)
    write_file(filename)
