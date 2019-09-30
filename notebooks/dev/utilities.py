def get_example(df,number,length,var='long_description'):
    '''
    Gets random examples in a field
    
    Args:
        Df is the dataframe we want to use
        number is the number of examples we want
        length is the length of the examples
    
    '''
    
    choose = random.sample(list(df.index),number)
    
    for x in df.loc[choose][var]:
        
        print(x[:length])
        print('\n')