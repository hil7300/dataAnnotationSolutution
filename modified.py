import requests
from bs4 import BeautifulSoup


url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"


def print_unicode_grid(url):
    # Fetch the content of the Google Doc
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the text content
    content = soup.get_text()

    # Parse the content and extract character information
    lines = content.split('\n')
    characters = []
    max_x, max_y = 0, 0

    for line in lines:
        if line.strip():
            parts = line.split()
            if len(parts) == 3:
                x, char, y = int(parts[0]), parts[1], int(parts[2])
                characters.append((char, x, y))
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    # Create the grid
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill the grid with characters
    for char, x, y in characters:
        grid[y][x] = char

    # Print the grid
    for row in reversed(grid):  # Reverse the rows to match the coordinate system
        print(''.join(row))

# Use the function with the provided URL

print_unicode_grid(url)
