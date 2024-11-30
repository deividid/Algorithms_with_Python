def form_string(array, lookup, combination):
    if len(array) == 0 or len(lookup) == 0:
        return

    for word in array:
        if word == lookup[:len(word)]:
            combination.append(word)
            form_string(array, lookup[len(word):], combination)

    return combination




words = input().split(', ')
lookup_value = input()
print(' '.join(form_string(words, lookup_value, [])[:-1]))

