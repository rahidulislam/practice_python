import csv
# f = open("test.csv",'r',encoding='utf-8')
# csv_reader = csv.reader(f)
# for line in csv_reader:
#     print(line)
# f.close()
# total_area = 0
# with open('/media/rahidulislam/Personal/Work/practice_python/practice_python/country.csv', 'r',encoding='utf-8') as f:
#     csv_reader =csv.reader(f)
    # for line_no,line_in in enumerate(csv_reader,1):
        # if line_no == 1:
        #     print("Header:")
        #     print(line_in)
        #     print('data: ')
        # else:
        #     print(line_in)

    # skip header
#     next(csv_reader)
#     for line in csv_reader:
#         total_area +=float(line[1])

# print(total_area)
fieldnames = ['country_name', 'area', 'code2', 'code3']
with open('/media/rahidulislam/Personal/Work/practice_python/practice_python/country.csv', 'r',encoding='utf-8') as f:
    csv_reader =csv.DictReader(f,fieldnames)

    # skip the header
    header = next(csv_reader)
    print(header)
    for line in csv_reader:
        print(f"The area of {line['country_name']} is {line['area']} km2")

# f = open("test.csv","w",encoding="utf-8")
# writer = csv.writer(f)
# writer.writerow(["country","area","code2","code3"])
# writer.writerow(["Afghanistan","652230","AF","AFG"])
# f.close()
header = ['name', 'area', 'country_code2', 'country_code3']
# data = ["Afghanistan","652230","AF","AFG"]
data = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]
with open("test.csv","w",encoding="utf-8",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

# Writing to CSV files using the DictWriter class
fieldnames = ['name', 'area', 'country_code2','country_code3']
rows =[
    {'name': 'Albania',
    'area': 28748,
    'country_code2': 'AL',
    'country_code3': 'ALB'},
    {'name': 'Algeria',
    'area': 2381741,
    'country_code2': 'DZ',
    'country_code3': 'DZA'},
    {'name': 'American Samoa',
    'area': 199,
    'country_code2': 'AS',
    'country_code3': 'ASM'}
]

with open("test2.csv","w") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)