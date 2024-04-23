#This function will find the last number of the pyramid in the file
def max_nombre(file_name):
    max_nombre =0

    with open(file_name, 'r') as file:

        for line in file:
            num_string, _ = line.strip().split(' ')
            num = int(num_string)
            if num > max_nombre:
                max_nombre = num

    return max_nombre

#This function will return the list of all the last numbers of the pyramid
def derniers_nombre_triangle(max_nombre):
    dereniers_nombres = []

    nombre = 0

    while nombre < max_nombre:
        ligne_nombre = len(dereniers_nombres) + 1
        premier_nombre = (ligne_nombre * (ligne_nombre - 1)) // 2 + 1
        dernier_nombre = premier_nombre + ligne_nombre - 1
        dereniers_nombres.append(dernier_nombre)
        nombre = dernier_nombre

    return dereniers_nombres

#This function will build the final sentence using the previous functions
def phrase_construction(file_name, input_list):
    mots_phrase = {}

    with open(file_name, 'r') as file:
        for line in file:
            num_str, mot = line.strip().split(' ')
            num = int(num_str)
            if num in input_list:
                mots_phrase[num] = mot.lower()

    phrase = ' '.join(mots_phrase[num] for num in input_list)

    return phrase

# We replace with the file name and we print the result
file_name = "coding_qual_input.txt"
# print(derniers_nombre_triangle(max_nombre(file_name)))
print(phrase_construction(file_name,derniers_nombre_triangle(max_nombre(file_name))))