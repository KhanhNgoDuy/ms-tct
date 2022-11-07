import argparse

parser = argparse.ArgumentParser(description='testing script')
parser.add_argument('--mode', type=str, help='rgb or flow')
parser.add_argument('--load_model', type=str, help='rgb or flow')
parser.add_argument('--root', type=str, help='root folder')
parser.add_argument('--gpu', type=str)
parser.add_argument('--save_dir', type=str, help='save folder')

args = parser.parse_args()

# if '__name__' == '__main__':
for key in args.__dict__:
	print("{} {}".format(key, args.__dict__[key]))

