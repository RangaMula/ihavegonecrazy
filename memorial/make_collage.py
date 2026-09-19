"""Build a side-by-side memorial collage from two photos, matched to equal height."""
import sys
from PIL import Image

def collage(left_path, right_path, out_path, height=1000, gap=18, margin=28, bg=(12, 12, 12)):
    left = Image.open(left_path).convert("RGB")
    right = Image.open(right_path).convert("RGB")
    def fit(im):
        w = round(im.width * height / im.height)
        return im.resize((w, height), Image.LANCZOS)
    left, right = fit(left), fit(right)
    canvas = Image.new("RGB", (margin * 2 + left.width + gap + right.width, margin * 2 + height), bg)
    canvas.paste(left, (margin, margin))
    canvas.paste(right, (margin + left.width + gap, margin))
    canvas.save(out_path, "JPEG", quality=93, subsampling=0)
    return canvas.size

if __name__ == "__main__":
    a, b, out = sys.argv[1:4]
    print(out, collage(a, b, out))
