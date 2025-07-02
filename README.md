1. Place your Chrome `Bookmarks` JSON file in the root of this project.

2. Build the image:
docker build -t bookmarks-converter .

3. Run the image:
docker run -it --rm -v "$(pwd)":/app bookmarks-converter Bookmarks
