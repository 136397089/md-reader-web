SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPTS_DIR")"
DATA_DIR="$(dirname "$PROJECT_DIR")"

docker run -d --rm -p 6100:5000 \
  -v "$PROJECT_DIR":/app \
  -v "$DATA_DIR":/data \
  markdown_reader:latest python src/markdown_reader.py --target_folder /data/markdown
