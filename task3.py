"""
Create micro library that allows users to work with notes about ukrainian films. Note should contain film_name, note, rating (rating - is 1 - 5 rating of the film) Micro lib should contain the next funcitonality:
Read notes from .csv file
Add note to .csv file
Remove note from .csv file
Print notes to console
Get films with the highest rating
Get films with the lowest rating
Get average rating among all films
"""
import csv


def read_notes_from_csv():
    with open("ukr_films.csv", "r") as file:
        f = csv.DictReader(file)
        for note in f:
            print(note['note'])


def add_notes_to_csv(note):
    with open("ukr_films.csv", "a") as file:
        file.write(f',{note},')


def highest_rate_films():
    with open("ukr_films.csv", "r") as file:
        f = csv.DictReader(file)
        for rate in f:
            try:
                if int(rate['rating']) > 4:
                    print(rate['film_name'])
            except:
                print(end='')


def lowest_rate_films():
    with open("ukr_films.csv", "r") as file:
        f = csv.DictReader(file)
        for rate in f:
            try:
                if int(rate['rating']) <= 2:
                    print(rate['film_name'])
            except:
                print(end='')


def average_rate_of_all_films():
    with open("ukr_films.csv", "r") as file:
        f = csv.DictReader(file)
        counter = 0
        avg = 0
        for i in f:
            avg += int(i["rating"])
            counter += 1
        print(round(avg/counter, 2))


read_notes_from_csv()
add_notes_to_csv("Film Director")
highest_rate_films()
lowest_rate_films()
average_rate_of_all_films()
