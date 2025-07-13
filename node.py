VERSION = "1.0.0"
import argparse

def main():
    try:
        if args.hello:
        if args.goodbye:
        if args.version:
        if not any(vars(args).values()):
            print("No arguments provided.")
            print("Version:", VERSION)
            print(f"Goodbye, {args.goodbye}!")
            print(f"Hello, {args.hello}!")
    parser = argparse.ArgumentParser(description='Simple CLI')
    parser.add_argument("--version", action="store_true", help="Show version")
    parser.add_argument("--hello", help="Say hello")
    parser.add_argument("--goodbye", help="Say goodbye")
    args = parser.parse_args()

    except Exception as e:
        print("Error:", e)
if __name__ == '__main__':
    main()
# CLI complete
