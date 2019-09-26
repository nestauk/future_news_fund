import pandas as pd
import os
import json

TOPDIR = "/mnt/c/Users/aotubusen/Documents/DS Projects/future_news_fund/data/raw/opname_csv_gb"
HEADER_PATH = os.path.join(TOPDIR,'DOC','OS_Open_Names_Header.csv')

def extract_tree(df, levels, ilvl=0):
    lvl = levels[ilvl]
    entities = []
    for group, grouped in df.groupby(lvl):
        try:
            children = extract_tree(grouped, levels, ilvl+1)
        except IndexError:
            children = grouped[['LOCAL_TYPE','NAME1']].to_dict(orient='records')
            children = [{'type': child['LOCAL_TYPE'], 'name':child['NAME1']}
                        for child in children]
        entity = {'type':lvl, 'name':group}
        if len(children) > 0:
            entity['contains'] = children
        entities.append(entity)
    return entities


header = list(pd.read_csv(HEADER_PATH).columns)
data = []
cols = ['NAME1','LOCAL_TYPE','POSTCODE_DISTRICT','DISTRICT_BOROUGH','COUNTY_UNITARY','REGION','COUNTRY']

for filename in os.listdir(os.path.join(TOPDIR,'DATA')):
    path = os.path.join(TOPDIR,'DATA',filename)
    df = pd.read_csv(path, header=None, names=header, low_memory=False)
    # Get non-postcode areas
    _df = df.loc[df.TYPE == 'populatedPlace']
    data += _df[cols].to_dict(orient='records')
    # Get postcode areas
    postcode_with_name = (df.LOCAL_TYPE == 'Postcode') & (~pd.isnull(df.POPULATED_PLACE))
    _df = df.loc[postcode_with_name].copy()
    _df['POSTCODE_DISTRICT'] = list(map(lambda x: x.split()[0], _df.NAME1))
    _df['NAME1'] = _df.POPULATED_PLACE
    data += _df[cols].to_dict(orient='records')
    del df
    del _df

df = pd.DataFrame(data)
df.drop_duplicates(inplace=True)
levels = ['COUNTRY','REGION','COUNTY_UNITARY','POSTCODE_DISTRICT','DISTRICT_BOROUGH']

tree = extract_tree(df, levels)

with open('/mnt/c/Users/aotubusen/Documents/DS Projects/future_news_fund/data/interim/britain_place_tree.json','w') as f:
    f.write(json.dumps(tree))
