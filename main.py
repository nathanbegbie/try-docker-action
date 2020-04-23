import os

def main():
    print(os.getenv("AN_ENV_VARIABLE"))
    print(os.getenv("who-to-greet"))

if __name__ == "__main__":
    main()
