import argparse
def parse():
    parser = argparse.ArgumentParser('checker',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--read_path',help="abs read path",default='测试文本/orig.txt')
    parser.add_argument('--checking_path',help='abs checking file path',default='测试文本/orig_0.8_add.txt')
    parser.add_argument('--result_path',help='abs result file path',default='result.txt')
    return parser.parse_args()

if __name__ == '__main__':
    args=parse()
    print(args)