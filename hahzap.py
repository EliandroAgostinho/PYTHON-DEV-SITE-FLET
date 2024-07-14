# Título: hashzap 
# Botão Iniciar chat
    # popup/modal/alerta
        #Título: Bem vindo ao hashzap
        #Campo de texto: Escreva seu nome no chat
        #Botão: Entrar no chat 
                # Sumir com o título e o botão inicial
                # Fechar o popup
                # Criar o chat (com a mensagem de "nome do usuário entrou no")
                # Em baixo do chat: 
                        # Campo de texto: Digite a sua mensagem
                        # Botão: Enviar
                                # Vai aparecer a mensagem no chat com o nome do usúario
                                
# framework Flet -> aplicativo/site/programa de computador                                
import flet as ft

# Criar a função principal do sistema
def main(pagina):
    # Criar alguma coisa
    # Criar o título
    
    titulo = ft.Text("Hashzap")
    
    
    ##############################################################################################
    ##############################################################################################
    
    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        print(mensagem)
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel)# Cria o tunel de comunicação    
            
            
    
    titulo_janela = ft.Text("Bem vindo ao Hashzap!")
    
    campo_utilizador = ft.TextField(label="Digite o seu nome do chat") 
    
    ################################################################################################
    ################################################################################################

    def enviar_mensagem(evento):
        texto = f"{campo_utilizador.value}: {texto_mensagem.value}"    
        # Enviar a mensagem no chat
                # Utlizador: mensagem 
        #chat.controls.append(ft.Text(texto))   
        
        #Enviar mensagem no tunel
        pagina.pubsub.send_all(texto)
             
        # Limpar o campo de mensagem  
        texto_mensagem.value = ""
        pagina.update()      
    
    
    texto_mensagem = ft.TextField(label="Digite a sua mensagem",on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar",on_click=enviar_mensagem)
    
    # Colunas e linhas
    linha_mensaegm = ft.Row([texto_mensagem,botao_enviar])
    chat = ft.Column()
    
    
    ##############################################################################################
    ##############################################################################################
    
    def entrar_chat(evento):
        # Tirar o titulo da pagina
        pagina.remove(titulo)
        
        # Tirar o botao inciar
        pagina.remove(botao_iniciar)
        
        # Fechar o botao popup/janela
        janela.open = False
        
        # Criar o chat
        pagina.add(chat)
        
        # adicionar linha mensaegem
        pagina.add(linha_mensaegm)
        
        # Criar o campo de texto de enviar mensagem
        pagina.add(texto_mensagem)
        
        # Criar o botao de enviar mensagem    
        pagina.add(botao_enviar)
        
        # Escrever a mensaegm o utilizador entrou no chat
        
        texto_entrou_chat = f"{campo_utilizador.value} entrou no chat"
        pagina.pubsub.send_all(texto_entrou_chat)
        #chat.controls.append(ft.Text(texto_entrou_chat))
        
        pagina.upadte()
    
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    
    janela = ft.AlertDialog(title=titulo_janela,content=campo_utilizador,actions=[botao_entrar])
    
    
    ######################################################################################################
    ######################################################################################################
    
    def abrir_popup(evento): # Toda função que é chamada ao acionar de um botão deve passar o evento como parametro
        pagina.dialog = janela
        janela.open = True
        pagina.update()
    
    
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)    
    
    # Criar essa coisa na pagina
    # adicionar o titulo na pagina
    pagina.add(titulo)        
    pagina.add(botao_iniciar)
