#!/usr/bin/env python3
import requests
import csv


response = requests.get('https://jsonplaceholder.typicode.com/posts/')


def fetch_and_print_posts():
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        data = response.json()

        for post in data:
            print(post['title'])
    else:
        print("Fail")


def fetch_and_save_posts():

    print("Status code: {}".format(response.status_code))

    if response.status_code == 200:
        data = response.json()
        struct_data = []
        for post in data:
            dict_posts = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            struct_data.append(dict_posts)

        with open("posts.csv", mode="w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()

            for user_id in struct_data:
                writer.writerow(user_id)
    else:
        print("Fail")
