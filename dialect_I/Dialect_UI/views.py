from django.shortcuts import render
from django.http import HttpResponse
import speech_recognition as sr
from googletrans import Translator
from .models import ContactUs
# from googletrans import LANGUAGES 
# # Create your views here.
# print(LANGUAGES)
def speech_lang():
    language = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani',
     'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano',
      'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian',
       'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 
       'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 
       'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 
       'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 
       'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 
       'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 
       'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 
       'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 
       'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 
       'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 
       'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 
       'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 
       'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
    return language

def translator(request):
    language=speech_lang()
    # result=translation()
    prams={'languages': language}
    return render(request, 'Dialect/translator.html',prams)



def translated(request):
    text = request.POST['text']
    lang = request.POST['lang']
    #print('text: ',text, "lang: ",lang)
    result,u_lang=translation(text,lang)
    prams={'res': result, 'u_lang': u_lang, 't_lang': lang }
    return render(request, 'Dialect/translated.html',prams)


def voice_rec(request):
    language=speech_lang()
    # result=translation()
    prams={'languages': language}
    return render(request, 'Dialect/voice_rec.html',prams)

def home_page(request):
    return render(request, 'Dialect/Menu_DI.html')

def contact(request):
    #return HttpResponse('this is contact page')
    if request.method=="POST":
        #print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        #print(name,email,phone,desc)
        contact=ContactUs(username=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,"Dialect/contact.html")

def about(request):
    return render(request,"Dialect/about.html")

def translation(query,lan):
    trans=Translator()
    dt=trans.detect('query')
    dt2=dt.lang
    k=trans.translate(query,dest=lan)
    translated=str(k.text)
    return translated , dt2
