import sys

print("spam")
sys.stdout.write("spam" + "\n")
print("spam", "ham")
sys.stdout.write(str("spam") + " " + str("ham") + "\n")

print("We have a problem", file=sys.stderr)

