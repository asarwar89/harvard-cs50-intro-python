def playback():
    str = input("Enter the string? ").split(" ")
    print(*str, sep="...")

playback()