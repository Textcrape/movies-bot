# MIT License 
 # Copyright (c) 2022 Charlie
 import os, re 
 search = re.compile(r'^.\d+$') 
 def is_enabled(value, default): 
     if value.lower() in ["true", "yes", "1", "enable", "y"]: 
         return True 
     elif value.lower() in ["false", "no", "0", "disable", "n"]: 
         return False 
     else: 
         return default 
  
  
 # Creator 
 CREATOR_NAME = os.environ.get("CREATOR_NAME", "CHARLEY") 
 CREATOR_USERNAME = os.environ.get("CREATOR_USERNAME", "OBSTREPEROUS_20") 
  
 # Account 
 API_HASH = os.environ.get("API_HASH", "a319f80ac07376f1043a5a09d9baad3c") 
 API_ID = os.environ.get("API_ID", "13358890") 
 # About Bot 
 BOT_TOKEN = os.environ.get("BOT_TOKEN", "5511952184:AAFXbSGw_KLdfR-WWzwi-C_y09g_GwbPu2g") 
 PICS = os.environ.get("PICS", "https://telegra.ph/file/034d53b5ed1d920ecab8b.jpg") 
 # Database 
 DATABASE_NAME = os.environ.get("DATABASE_NAME", "LuciferMoringstar-Robot") 
 DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://{Username}:{Passs}@cluster0.{clusterID}.mongodb.net/myFirstDatabase?retryWrites=true{iD}=majority") 
 # Chats & Users 
 ADMINS = os.environ.get("ADMINS", "1142482938 5179879782") 
 SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "HO_Tech_Group") 
 AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1001600984322") 
 CHANNELS = [int(ch) if search.search(ch) else ch for ch in os.environ.get("CHANNELS", "-1001784382279").split()] 
 LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001590063851") 
 GET_FILECHANNEL = os.environ.get("GET_FILECHANNEL", "-1001570208190") 
 FILTER_DEL_SECOND = int(os.environ.get("FILTER_DEL_SECOND", "600")) 
  
 # AutoFilter 
 AUTH_GROUPS = os.environ.get("AUTH_GROUPS", "") 
 AUTH_USERS = [int(user) if search.search(user) else user for user in os.environ.get('AUTH_USERS', '').split()] 
 FILTER_BUTTONS = os.environ.get("FILTER_BUTTONS", "10") 
 PROTECT_FILES = is_enabled((os.environ.get('PROTECT_FILES', "True")), True) 
