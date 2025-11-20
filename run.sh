docker run -d --rm -p 6100:5000 -v $(pwd)/:/app  -v $(pwd)/../:/data markdown_reader:latest python markdown_reader.py --target_folder /data/markdown
