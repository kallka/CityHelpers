# Author: Karina Kallas
# Description: Change names of pdf docs available in each surveyor book on LA County Surveyor site.
#  example book name: https://dpw.lacounty.gov/smpm/landrecords/List.aspx?type=survey&book=277
#  example file name: https://pw.lacounty.gov/sur/nas/landrecords/survey/RS277/RS277-001.pdf
#   - File names always end in 001-100
#

# Save Path Name and Index
main_path = 'https://pw.lacounty.gov/sur/nas/landrecords/survey/RS277/RS277-001.pdf'
index = 65
next_path = main_path

for tens in range(0, 10):
    for ones in range(0, 10):
        if tens == 0 and ones == 0:
            continue
        else:
            next_path = next_path[:index] + chr(ones + 48) + next_path[index + 1:]
            if tens >= 1:
                next_path = next_path[:index-1] + chr(tens + 48) + next_path[index:]
            print(next_path)