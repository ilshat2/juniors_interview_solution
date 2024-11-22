import os
import csv
import requests
import time
from bs4 import BeautifulSoup
from collections import defaultdict

def get_animal_counts(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    animal_counts = defaultdict(int)

    categories = soup.select('div.mw-category-group a')

    for category in categories:
        title = category.text.strip()
        if title:
            first_letter = title[0].upper()
            animal_counts[first_letter] += 1

    return animal_counts

def save_to_csv(file_path, data):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Letter', 'Count'])
        for letter, count in sorted(data.items()):
            writer.writerow([letter, count])
    print(f"Results in file: {file_path}")

def main():
    base_url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    current_page_url = base_url
    letter_counts = defaultdict(int)

    output_dir = 'juniors_interview_solution/task2'
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, 'beasts.csv')
    num = 0

    while current_page_url:
        try:
            response = requests.get(current_page_url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error loading page {current_page_url}: {e}")
            break
        
        print(f"The address of the page from which the data is collected: {current_page_url}")
        num += 1
        print("Page number:", num)
        page_counts = get_animal_counts(current_page_url)
        for letter, count in page_counts.items():
            letter_counts[letter] += count

        soup = BeautifulSoup(response.text, 'html.parser')
        next_page_link = soup.find('a', text='Следующая страница')
        if next_page_link and 'href' in next_page_link.attrs:
            current_page_url = f"https://ru.wikipedia.org{next_page_link['href']}"
        else:
            current_page_url = None

    save_to_csv(output_file_path, letter_counts)
    print(f"Total pages processed: {num}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Function execution time: {elapsed_time:.2f} seconds")
