import pandas as pd
df = pd.read_csv("C://Users//RAMMYAHSHREE//Downloads//test_file.csv")
print(df.to_string())
print(df)

dataset = {"vehicle": ["verna", "himalaya", "royal enfield"], "type": ["car", "bike", "bike"]}
data_frame = pd.DataFrame(dataset)
print(data_frame)
print(data_frame.loc[0])
print(data_frame.loc[[0], ["vehicle"]])
print(data_frame.loc[:, ["vehicle"]])
print(data_frame.loc[[0, 1], ["vehicle"]])
print(data_frame.loc[[0, 1]])
# print(data_frame.loc[[]])

# frame_ind = pd.DataFrame(dataset, index=["row0", "row1"])
# print(frame_ind)

# lst = [1, 4, 7]
# ser = pd.Series(lst)
# print(ser)

# data = {"day1": "sunday", "day2": "monday"}
# ser_data = pd.Series(data)
# print(ser_data)

