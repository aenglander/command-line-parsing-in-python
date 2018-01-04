import argparse


def hello():
    parser = argparse.ArgumentParser(description='This says hello a particular number of times.')
    parser.add_argument('name', help='Name to use when saying hello.', type=str)
    parser.add_argument('--times', default=1, help="Number of greetings: 1-5", type=int, choices=range(1, 6))
    args = parser.parse_args()
    for _ in range(args.times):
        print("Hello, {}!".format(args.name))


def goodbye():
    parser = argparse.ArgumentParser(description='"This says goodbye.')
    parser.add_argument('name', help='Name to use when saying goodbye.', type=str, default="Cruel World", nargs="?")
    args = parser.parse_args()
    print("Goodbye, {}!".format(args.name))

