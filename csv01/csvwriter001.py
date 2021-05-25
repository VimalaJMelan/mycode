
import csv 

def main():

    #create a dataframe called superdf from our csv data
    with open('superbirthday.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        writer = csv.writer(file_out)
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}') # python3.6 way
                if row["heroname"]
                    
                ## to do things
                print('Column names are {}'.format(", ".join(row)))
                line_count += 1
            # print(f'\t{row["name"]} aka {row["heroname"]} was born in {row["birthday month"]}.')
            # above is the python3.6+ way to do things
            print('\t{} aka {} was born in {}.'.format(row["name"],row["heroname"],row["birthday month"]))
            line_count += 1



    # uncomment the line below if you need to see what we are looping across
    # orient = 'records' prevents to_dict() from using the index value
    #print(superdf.to_dict(orient='records'))



    


    
if __name__ == "__main__":
    main()

