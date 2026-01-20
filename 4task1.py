try:
    fh=open("sample.txt","r")
    content1 = fh.readline()
    content2 = fh.readline()

    print(f"line1: {content1}")
    print(f"line2: {content2}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


