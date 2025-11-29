# Create a program that: Opens a file in append mode, Adds a new log entry and Opens the file in read mode and prints all logs...

with open("log.txt", "a") as f:
    f.write("Program run successfully\n")

with open("log.txt", "r") as f:
    logs = f.read()
    print(logs)


# i moved the files that are created outside into the lecture-05 folder