#-----------------------FILE DI CONFIGURAZIONE-----------------------#
#questo file contiene le variabili da configurare. 
#Nel modificarlo rispettare quanto scritto nella documentazione


#---------------------VARIABILI CACHE----------------------#

CACHEFOLDER = "Cache\\"
LASTEVENTFILE = CACHEFOLDER + "lastEvent"
USERSFILE = CACHEFOLDER + "usersFile"
RMUSERSFILE = CACHEFOLDER + "rmUsersFile"



#-----------------VARIABILI API TELEGRAM------------------#  
TELEGRAMTOKEN = "756550061:AAHvyaxn_xiDnx8TfI2cYU5EAsycU_s0QqY"



#---------------------VARIABILI BOT-----------------------#
UPDATETIME = 60*60*1000     #1 ora
#UPDATETIME = 15     

INITMSG = "Ciao, mi occupo di tenerti aggiornato sulle news pubblicate sul sito di Ingegneria Informatica di Pisa.\n\n\
Ecco una lista di comandi che possono servirti:\n\
/start - Avvia questo Bot\n\
/help - Visualizza questo messaggio\n\
/iscrivi - Iscrive al sevizio di aggiornamento\n\
/allnews - Visualizza le news attive\n\
/news [categoria] - Visualizza le news attive della categoria indicata\n\
/categorie - Visualizza le categorie disponibili\n"

INVALIDCAT = "Categoria non valida. /categorie per vedere quelle disponibili"
NEWSHEADER = "Ecco le ultime News:"
SUBSCRIBEOK = "Complimenti ora sei iscritto!\nQueste sono le ultime News:"
NOTADMINERROR = "Non sei un amministratore del gruppo e non puoi configurare il bot!"
