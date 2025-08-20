def main():
  file = input("File name: ")

  if ("." not in file):
    print("application/octet-stream")
    return

  extension = file.split(".")[1]

  match extension.lower():
    case 'gif':
      print("image/gif")
    case 'jpeg' | 'jpg':
      print("image/jpeg")
    case 'png':
      print("image/png")
    case 'pdf':
      print("application/pdf")
    case 'txt':
      print("text/plain")
    case 'zip':
      print("application/zip")
    case _:
      print("application/octet-stream")

main()