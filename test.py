import requests
from bs4 import BeautifulSoup


def fetch_google_doc(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    return response.text


def parse_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')
    data = []

    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 3:
            try:
                x = int(cells[0].get_text().strip())
                char = cells[1].get_text().strip()
                y = int(cells[2].get_text().strip())
                data.append((x, char, y))
            except ValueError:
                # Skip rows where conversion to int fails
                continue

    return data


def print_grid(data):
    # Find max x and y to determine grid size
    max_x = max(x for x, _, _ in data)
    max_y = max(y for _, _, y in data)

    # Create a grid initialized with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill in the grid with the characters
    for x, char, y in data:
        grid[y][x] = char

    # Print the grid
    for row in grid:
        print(''.join(row))


def main(url):
    html = fetch_google_doc(url)
    data = parse_data(html)
    print_grid(data)

# URL of the Google Doc
doc_url = 'https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub'
main(doc_url)
