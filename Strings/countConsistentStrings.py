def countConsistentStrings():
    for val in ["string", "bing", "the"]:
        for char in val:
            if char == "i":
                break
            print(val)


print("The end")
countConsistentStrings()
