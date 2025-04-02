   return s[::-1]


def decrypt(s, noise_level=512)
    s = reverse(s)

    return s[::noise_level + 1]


if __name__ == '__main__':

    try:
        with open (sys.argv[1], 'r') as encryted_file:
            encrypted_message = encrypted_file.read()
            message = decrypt(encryted_message)

        with open(sys.argv[1], 'w') as message_file:
            message_file.write(message)

    except FileNotFoundError:
        print('File not found')
    except IndexError:
        print('Please enter a message file name')  