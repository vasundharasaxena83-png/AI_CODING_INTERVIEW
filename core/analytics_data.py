import pandas as pd

def get_topic_dataframe(company):

    data = {
        "Google": {
            "Topic": ["Array","Graph","DP","Tree","String","Heap"],
            "Probability (%)": [30,20,15,15,10,10]
        },
        "Amazon": {
            "Topic": ["Array","Tree","Graph","DP","Heap","String"],
            "Probability (%)": [25,20,20,15,10,10]
        },
        "Meta": {
            "Topic": ["Array","String","Graph","DP","Tree","Heap"],
            "Probability (%)": [35,20,15,15,10,5]
        },
        "Microsoft": {
            "Topic": ["Array","Tree","DP","Graph","Heap","String"],
            "Probability (%)": [25,20,20,15,10,10]
        }
    }

    return pd.DataFrame(data[company])