import os, time
import pandas as pd

from api import GeneralApi


class Processing:
    def __init__(self, config, prompt, path, save_path) -> None:
        self.path = path
        self.save_path = save_path

        self.config = config
        self.prompt = prompt
        # self.message = message
        self.data = self._read_csv()
        # self.data = data
        # self.data_list = [data for i in range(len(self.data)/)]

        self.gpt = GeneralApi(self.config)
    
    def run(self, n=1):
        self.result = []
        # while i < len(self.data):
        #     message = self.data[i:i + n]
        #     i += n
        #     input_message = ''
        #     for mess in message:
        #         input_message += '{} '.format(mess)
        for i, input_message in enumerate(self.data):
            print('original:',input_message)
            res = self.gpt.run(input_message, self.prompt)
            print('summary:{}\n'.format(res))
            self.result.append([input_message, res])
            # if i % (1*n) == 0:
            self._save_csv()
            if i %2000 == 0:
                time.sleep(2*60*60)

    def _read_csv(self):
        df = pd.read_csv(self.path)
        data = df.loc[:,'0']
        return list(data)

    def _save_csv(self):
        df = pd.DataFrame(self.result)
        df.to_csv(self.save_path, mode='w')


if __name__ == "__main__":
    # key = 'sk-D28MPhpzU4CY0HpYDb4f1a95E6564fC2Ac9a23D7551c99D7'
    # key_gpt4 = 'sk-bqJtCvo4vEWDxp2UD3F249377e694cCa9e5b89244963E305'
    config_kimi = {
        'platform':'kimi',
        'key':'sk-kbu7EmPCaRi0xJnH5NJRR0lLfE03cf2BwBBenHysWyMSY0we',
        'api_base': "https://api.moonshot.cn/v1",
        'model':"moonshot-v1-8k",
    }

    config_gpt = {
        'platform':'openai',
        'key':'sk-D28MPhpzU4CY0HpYDb4f1a95E6564fC2Ac9a23D7551c99D7',
        'api_base': "https://api.kwwai.top/v1",
        'model':"gpt-3.5-turbo",
    }

    prompt = "你是一个医疗不良事件处理机器人，你将以文本的形式回复下文中医疗不良事件的摘要，摘要由20字以内的事件简述和10字以内的事件处理组成，事件简述包括时间、病症、治疗手段和不良事件，全部摘要不超过40字，无项目符号。"
    # message = '患者因急性上呼吸道感染、肺炎住院治疗，2023.6.12日护士遵医嘱为患者采集动脉血标本，使用该产品，打开包装后发现其针栓处断开，立即更换。未对患者造成不良影响。 2023.5.26 14时护士给予病人抽取胰岛素时，发现针头弯曲，立即给与更换新注射器，检查无误后完成此次操作，未对患者造成二次伤害。2023.06.08 患者行肝门胆管癌手术，术中监测体温，显示未连接传感器，体温测不出，重新更换新体温探头，完成体温监测，未对患者造成伤害。2023.6.5 17：36护士遵医嘱给予患者心电监护，取用心电极片时，发现一个电极扣松动，立即给予更换新电极片，检查无误后完成此次操作，未对患者造成二次伤害患者因膝关节骨性关节炎入院行手术治疗，2023-6-29日8:00分主管医生准备为患者进行刀口换药，打开一次性使用换药包，发现包内碘伏棉球包装渗漏且污染其它用物，无法使用，立即更换新的换药包，未对患者造成不良后果。患者因膝关节骨性关节炎入院行手术治疗，2023-6-28日10:00分护士准备使用静脉留置针为患者进行穿刺输液，打开后发现留置针中间断裂，无法继续使用，立即更换新的留置针，未对患者造成不良后果。2023.05.17 护士取用时发现棉签包装未封口，立即更换新棉签，检查无误，未对患者造成伤害。'
    # message = '患者因急性上呼吸道感染、肺炎住院治疗，2023.6.12日护士遵医嘱为患者采集动脉血标本，使用该产品，打开包装后发现其针栓处断开，立即更换。未对患者造成不良影响。'
    path = './data/data.csv'
    save_path = './data/summary.csv'

    # df = pd.read_csv(path)
    # data_all = list(df.loc[:,'0'])
    # print(len(data_all))
    # for i in range(10):
    #     if (i+1)*2000 > len(data_all):
    #         data = data_all[i*2000:]
    #     else:
    #         data = data_all[i*2000:(i+1)*2000]
    #     # print(data)
    Processing(config_gpt, prompt, path, save_path).run(n=1)
        # time.sleep(2*60*60)
