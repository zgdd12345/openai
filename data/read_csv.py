import os
import pandas as pd

root_path = './data'

path1 = '2023上半年数据-测试.xls'
path2 = '使用单位、经营企业医疗器械不良事件报告 (22).xls'
path3 = '使用单位、经营企业医疗器械不良事件报告 (22).xls'
path4 = '使用单位、经营企业医疗器械不良事件报告 (22).xls'
path5 = '使用单位、经营企业医疗器械不良事件报告 (22).xls'

save_name = 'data.csv'


def read(path):
    events = []
    length = 0
    df = pd.read_excel(os.path.join(root_path, path), sheet_name='{}'.format('Sheet0'))
    # print(df)
    for i in df.index:
        print('num:{}, length:{}'.format(i, len(df['使用过程'][i])))
        length += len(df['使用过程'][i])
        events.append(df['使用过程'][i])
    return events, length

all_events = []
length = 0
for path in [path1, path2, path3, path4, path5]:
    events_, l = read(path)
    length += l
    all_events.extend(events_)

print('The number of char:', length)

all_events = [event for event in all_events if len(event) >= 50]

df = pd.DataFrame(all_events)
# print('value:', df.values[:3])

df.to_csv(os.path.join(root_path, save_name))
