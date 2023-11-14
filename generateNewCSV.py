# import pandas as pd

# csv = pd.read_csv(
#     "./Testicular Cancer Dataset.csv",
#     # names=[*cancer_type_columns, "Disease Free (Months)"]
#     # usecols=[*cancer_type_columns, 'Disease Free (Months)', 'Postoperative tx', 'Disease Free Status'],
#     na_values=['NA'],
#     keep_default_na=False
# )

# withCancer = csv.loc[csv['Disease Free Status'] == '1:Recurred/Progressed']

# print(withCancer)

# for i in [1/3, 2/3, 4/3, 5/3]:
#     current = withCancer.copy()
#     current['Disease Free (Months)'] = current['Disease Free (Months)'] * i
#     if i < 1:
#         current['Disease Free Status'] = '0:DiseaseFree'
#     print(current)
#     csv += current

#     for rowIndex in range(len(current)):
#         csv.loc[len(csv.index)] = current.iloc[rowIndex].squeeze()

# csv.to_csv('Expanded TCD.csv')

with open('./Testicular Cancer Dataset.csv', 'r') as f:
    lines = [f.readline()]
    
    while line := f.readline():
        # 19 e Disease Free (Months), 20 e Disease Free Status

        line = line.split(',')

        # print(line[20])
        if line[20] == '0:DiseaseFree':
            # Skip dem som ikke har fått kreft igjen
            lines.append(','.join(line))
            continue

        # print(line[19].replace('.', ''), line[19].replace('.', '').isnumeric())

        if line[19].replace('.', '').isnumeric():
            for i in [i/10 for i in range(1, 20, 1)]:
                lineCopy = line.copy()
                lineCopy[19] = str(round(float(line[19]) * i, 2))
                if i < 1:
                    lineCopy[20] = '0:DiseaseFree'
        
                lines.append(','.join(lineCopy))
    
    with open('./Expanded TCD.csv', 'w') as out:
        out.write(''.join(lines))
