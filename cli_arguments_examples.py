from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()

    parser.add_argument('required-arg', default='Default value of my required arg', 
                        help='Help to display when calling program wiht -h or --help')
    parser.add_argument('')