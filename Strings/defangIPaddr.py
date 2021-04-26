def defangIPaddr(address):
    # O(n^2) Time, O(1) space ?
    i = 0
    while i < len(address):
        if address[i] == ".":
            address = address[:i] + "[.]" + address[i+1:]
            i += 3
        i += 1
    return address


def defangIPaddr2(address):
    # O(n) Time, O(1) space?
    address = address.split('.')  # O(n) Time, O(1) space?
    address = '[.]'.join(address)  # O(n) Time, O(1) space?
    return address


print(defangIPaddr("255.100.50.0"))
print(defangIPaddr2("255.100.50.0"))
