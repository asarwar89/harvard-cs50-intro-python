import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]|([1-9]\d)|(1\d{2})|(2[0-5]{2}))(\.([0-9]|([1-9]\d)|(1\d{2})|(2[0-5]{2}))){3}$", ip):
        return True
    else:
        return False
#   matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)

#   if not matches:
#       return False

#   for group in matches.groups():
#       # Check for valid range
#       if not 0 <= int(group) <= 255:
#           return False
#       # Check for leading zeros (except for '0')
#       if len(group) > 1 and group.startswith('0'):
#           return False

#   return True


if __name__ == "__main__":
    main()