import matplotlib.pyplot as plt
import numpy as np

'''Type of reporting vs Nos'''
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph



def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')

def get_plot(x,y):
    plt.switch_backend ('AGG')
    plt.figure(figsize=(5,4))
    plt.title("Quality Issue Type of reporting")
    plt.bar(x,y)
    addlabels(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Type_of_Reporting')
    plt.tight_layout()
    graph=get_graph()
    return graph
   
    