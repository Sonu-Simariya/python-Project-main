import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mlp
print('---------------------'*8)
##print('Enter this type of path')
print(str('Enter this type path:  C:/users/sonu/downloads/insurance.csv'))
print('---------------------'*8)
b=input('Enter a path: ')
df=pd.read_csv(b)
print('Your file is')
print('---------------------'*8)
print(df)
print('---------------------'*8)
print('The columns are:  ',df.keys())
for a in df:
    print('---------------------'*8)
    print('Enter 1 to show barplot')
    print('---------------------'*8)
    c=int(input('Enter your choice '))
    print('---------------------'*8)
    print('The columns are:    ',df.keys())
    print('---------------------'*8)
    if c == 1:
        d = input('Enter a Column to show Bar ')
        f= df[d].value_counts().values
        sns.barplot(y=df[d].value_counts().values,x=df[d].value_counts().index,hue=f)
        mlp.rcParams["figure.figsize"]=(50,50)
        mlp.xticks(rotation=45,fontsize=10)
        mlp.yticks(rotation=45,fontsize=10)
        print(mlp.show())
        print('---------------------'*8)
        z=int(input('Enter 1 to continue with same link '))
        print('---------------------'*8)
        if z==1:
            continue
        else:
            print('Exit run again for new path.')
            break
else:
    print('Exit: Run Again.')
















