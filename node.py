import argparse

def main():
        if args.hello:
            print(f"Hello, {args.hello}!")
    parser = argparse.ArgumentParser(description='Simple CLI')
    parser.add_argument("--hello", help="Say hello")
    args = parser.parse_args()

if __name__ == '__main__':
    main()
