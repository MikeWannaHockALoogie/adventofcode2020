'''
pseudo:
1.) load input into pandas df 
2.) select data with appropriate fields as not Null 

'''
import pandas as pd
import re
file = 'day_4_passport_processing_input.txt'

def load_data(file)->list:
    '''
    load file into pands data frame for use as database
    '''
    passports ={'byr':[] ,'iyr':[] ,'eyr':[] ,'hgt':[] ,'hcl':[] ,'ecl':[] ,'pid':[] ,'cid':[] }

    with open(file) as f:
        f= f.read().split('\n\n')
        # split entries where wever thier is a double line break
        for entry in f:
            # replace all other line breaks and spaces with ',' for easy spliting
            entry = entry.replace('\n',',')
            entry = entry.replace(' ',',')
            entry = entry.split(',')
            passport = {}
            # create passport var for loading into passports dict
            for field in range(len(entry)):
                entry[field] = entry[field].split(':')
                passport[entry[field][0]]=entry[field][1]
                #print(passport)
            for key in passports.keys():
                # check for values input NONe if no values found 
                if key in passport.keys():
                    passports[key].append(passport[key])
                else:
                    passports[key].append(None)
        return pd.DataFrame.from_dict(passports)
    




data = load_data(file)
# select data for solution one by excluding 'cid' and dropping any null values 
l = [x for x in data.columns[:-1]]
s1 = data[l]
s1 = s1.dropna()
 # select data for solution two with logic from readme.txt    
s2 =s1[
    s1.byr.between('1920','2002')
    & s1.iyr.between('2010','2020', inclusive = True)
    & s1.eyr.between('2020','2030', inclusive = True)
    & (
        s1.hgt.str.fullmatch('(15[0-9]|16[0-9]|17[0-9]|18[0-9]|19[0-6])cm') | s1.hgt.str.match('(59|6[0-9]|7[0-6])in') 
    )
    & s1.hcl.str.fullmatch('#[0-9a-f]{6}')
    & s1.ecl.isin(['amb','blu','brn','gry','grn','hzl','oth'])
    & s1.pid.str.fullmatch('\d{9}') 

]
# solutions for part one and two 
print(s1.shape)
print(s2.shape)



