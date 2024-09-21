import argparse
from glob import glob
from os.path import join

from halo import Halo
import imageio
from tqdm import tqdm

VALID_EXTENSIONS = ("png", "jpg")


def make_gif(filenames, duration, output_path):
    images = []
    for filename in tqdm(filenames, "Reading images"):
        images.append(imageio.imread(filename))

    spinner = Halo(text="Saving GIF...")
    spinner.start()
    imageio.mimsave(output_path, images, duration=duration)
    spinner.stop()
    print(f"GIF saved to: {output_path}")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--input-path", help="Path to directory of images", required=True
    )
    parser.add_argument("-d", "--duration", help="Duration of GIF", required=True)
    parser.add_argument("-o", "--output-path", help="Path to save GIF", required=True)
    return parser.parse_args()


def main():
    args = parse_args()

    duration = float(args.duration)
    filenames = []
    for ext in VALID_EXTENSIONS:
        filenames.extend(glob(join(args.input_path, f"*.{ext}")))

    make_gif(filenames, duration, args.output_path)


if __name__ == "__main__":
    main()
