import argparse

def main():
        if args.hello:
        if args.goodbye:
            print(f"Goodbye, {args.goodbye}!")
            print(f"Hello, {args.hello}!")
    parser = argparse.ArgumentParser(description='Simple CLI')
    parser.add_argument("--hello", help="Say hello")
    parser.add_argument("--goodbye", help="Say goodbye")
    args = parser.parse_args()

if __name__ == '__main__':
    main()
