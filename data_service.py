import urllib.request as request
import json
import os

class DataService:
    def __init__(self, api_url):
        self.api_url=api_url
        self.file=open(os.path.join(os.getcwd(),"api_nbp.json"), "r")
        self.save_to_json_file()

    def get_data_from_nbp(self):
        response=request.urlopen(self.api_url)
        if response.getcode()==200:
            source = response.read()
            data = json.loads(source)
            tab_currency=[]
            for i in range(len(data[0]['rates'])):
                tab_currency.append(data[0]['rates'][i]['currency'])
        else:
            tab_currency=[]
            data = json.load(self.file)
            for i in data["rates"]:
                tab_currency.append(data["rates"][i]["name"])
        return tab_currency

    def get_currency_values_from_nbp(self):
        response = request.urlopen(self.api_url)
        if response.getcode()==200:
            source = response.read()
            data = json.loads(source)
            tab_currency_values = []
            for i in range(len(data[0]['rates'])):
                tab_currency_values.append(data[0]['rates'][i]['mid'])
        else:
            tab_currency_values = []
            data = json.load(self.file)
            for i in range(len(data['rates'])):
                tab_currency_values.append(data['rates'][i]["mid"])
        return tab_currency_values

    def get_code_currency_from_nbp(self):
        response = request.urlopen(self.api_url)
        if response.getcode()==200:
            source = response.read()
            data = json.loads(source)
            tab_code_values = []
            for i in range(len(data[0]['rates'])):
                tab_code_values.append(data[0]['rates'][i]['code'])
        else:
            tab_code_values = []
            data = json.load(self.file)
            for i in range(len(data['rates'])):
                tab_code_values.append(data['rates'][i]["code"])
        return tab_code_values

    def save_to_json_file(self):
        with open('api_nbp.json', 'w') as json_file:
            tabela_walut=self.get_data_from_nbp()
            tabela_code=self.get_code_currency_from_nbp()
            tabela_nazw=self.get_currency_values_from_nbp()
            data={}
            data['rates']=[]
            for i in range(len(tabela_walut)):
                data['rates'].append({'name':tabela_walut[i],
                                     'code':tabela_code[i],
                                     'mid':tabela_nazw[i]})
            json.dump(data, json_file)


