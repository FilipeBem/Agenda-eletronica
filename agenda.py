import PySimpleGUI as sg

operacoes = []

def adicionar_evento(evento, data_inicio, data_fim):
    if any(evento in operacao for operacao in operacoes):
        print(f"O evento '{evento}' já existe na agenda")
    else:
        print(f"Evento '{evento}' adicionado à agenda de {data_inicio} até {data_fim}")
        operacoes.append(f"{evento} - {data_inicio} até {data_fim}")
        window["EVENTS"].update(values=operacoes)

def remover_evento(evento):
    if any(evento in operacao for operacao in operacoes):
        operacoes[:] = [operacao for operacao in operacoes if evento not in operacao]
        window["EVENTS"].update(values=operacoes)
        print(f"Evento '{evento}' removido da agenda")
    else:
        print(f"O evento '{evento}' não está na agenda")

def editar_evento(evento_antigo, evento_novo, data_inicio, data_fim):
    if any(evento_antigo in operacao for operacao in operacoes):
        index = [i for i, s in enumerate(operacoes) if evento_antigo in s][0]
        operacoes[index] = f"{evento_novo} - {data_inicio} até {data_fim}"
        window["EVENTS"].update(values=operacoes)
        print(f"Evento '{evento_antigo}' editado para '{evento_novo}' na agenda de {data_inicio} até {data_fim}")
    else:
        print(f"O evento '{evento_antigo}' não está na agenda")

layout = [
    [sg.Text("Agenda Eletrônica", size=(30, 1), justification="center", font=("Helvetica", 27))],
    [sg.Text("Digite o nome do evento  ", size=(20, 0), key="ADD_EVENT", justification="center")],
    [sg.Input("", key="EVENT_NAME", size=(40, 1))],
    [sg.Text("Digite o início do evento (dd/mm/aa)      ", size=(30, 0), key="ADD_EVENT", justification="center")],
    [sg.Input("", key="EVENT_DATE", size=(10, 1))],
    [sg.Text("Digite o fim do evento (dd/mm/aa)        ", size=(30, 0), key="ADD_EVENT", justification="center")],
    [sg.Input("", key="EVENT_END", size=(10, 1))],
    [sg.Button("Adicionar", key="ADD", size=(10, 1))],
    [sg.Button("Remover", key="REMOVE", size=(10, 1))],
    [sg.Button("Editar", key="EDIT", size=(10, 1))],
    [sg.Listbox(values=[], key="EVENTS", size=(80, 10), enable_events=True)]
]

window = sg.Window("Agenda Eletrônica", layout)

while True:
    event, values = window.read(timeout=0)
    if event == sg.WIN_CLOSED or event == "EXIT":
        break
    elif event == "ADD":
        adicionar_evento(values["EVENT_NAME"], values["EVENT_DATE"], values["EVENT_END"])
    elif event == "REMOVE":
        remover_evento(values["EVENT_NAME"])
    elif event == "EDIT":
        editar_evento(values["EVENT_NAME"], "Novo Evento", values["EVENT_DATE"], values["EVENT_END"])


window.close()