#!/usr/bin/python
# -*- coding:UTF-8 -*-
import json
def calculate():
    fin=open("/home/jin/graduate/predict/result.json",'r',encoding='utf8')
    line=fin.readline()
    CoverLaw=0
    OwnLaw=0
    while line:
        cnt=0
        d=json.loads(line)
        predict_law=d['predict_law']
        true_law=d['true_law']
        for e in true_law:
            if e in predict_law:
                cnt+=1
        CoverLaw+=cnt/len(true_law)*1.0
        OwnLaw+=cnt/len(predict_law)*1.0
        line=fin.readline()
    CoverLaw_avg=CoverLaw/6832*1.0
    OwnLaw_avg=OwnLaw/6832*1.0
    print("平均CoverLaw_avg为%.4f"%CoverLaw_avg)
    print("平均OwnLaw_avg为%.4f"%OwnLaw_avg)
    EvalLaw=(2.0*CoverLaw_avg*OwnLaw_avg)/(CoverLaw_avg+OwnLaw_avg)*1.0
    print("EvalLaw为%.4f" % EvalLaw)

if __name__=='__main__':
    calculate()