import csv

dict_from_csv = {}
dict_from_csv_2 = {}
final_dict = {}
final_dict_values = list()
def test(infile1, infile2):
    with open(infile1, mode ='r') as inp:
        reader = csv.reader(inp, delimiter = "\t")
        dict_from_csv = {rows[0]:rows[4] for rows in reader}
    #print(dict_from_csv)

    with open(infile2, mode = 'r') as inp:
        reader = csv.reader(inp, delimiter = "\t")
        dict_from_csv_2 = {rows[0]:rows[5] for rows in reader}
        for key, value in dict_from_csv_2.items():
            value = list(value.split(", "))
            dict_from_csv_2[key] = value
    #print(dict_from_csv_2)

    del dict_from_csv_2["scaffold"]

    print(dict_from_csv_2)
    for key, value in dict_from_csv_2.items():
        for vog in value:
            if vog not in dict_from_csv:
                print(vog + " not annotated")
                #I literally do not know what else to do, if you run this, you will get a key error
            final_dict_values.append(dict_from_csv[vog])
        final_dict[key] = final_dict_values
    print(final_dict)

test('vog.annotations copy.tsv', 'assemblies.phigaro copy.tsv')

