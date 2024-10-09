import sys
import re

if len(sys.argv) != 2:
    print("Unesite ime datoteke")
    sys.exit(1)

file = sys.argv[1]

with open(file, "r") as f:
    lines = f.read()

entries = re.findall(r'@book{([^\}]*)}', lines, re.DOTALL)

books = []
for entry in entries:
    id = re.search(r'^([^,]*)', entry).group(1)
    author_match = re.search(r'author\s*=\s*["{]([^"}]*)["}]', entry, re.IGNORECASE)
    author = author_match.group(1) if author_match else ""
    publisher_match = re.search(r'publisher\s*=\s*["{]([^"}]*)["}]', entry, re.IGNORECASE)
    publisher = publisher_match.group(1) if publisher_match else ""
    title_match = re.search(r'title\s*=\s*["{]([^"}]*)["}]', entry, re.IGNORECASE)
    title = title_match.group(1) if title_match else ""
    year_match = re.search(r'year\s*=\s*["{]([^"}]*)["}]', entry, re.IGNORECASE)
    year = year_match.group(1) if year_match else ""
    books.append((id, author, publisher, title, year))


print("<UL>")
for book in books:
    print(f'  <LI> {book[1]}, <I>{book[3]}</I>, {book[2]}, {book[4]} ({book[0]}) </LI>')
print("</UL>")