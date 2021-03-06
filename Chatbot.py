import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola, bienvenido al chatbot ITLA', ['hola', 'klk', 'saludos', 'buenas'], single_response = True)
        response('En que podemos ayudarle?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Estamos ubicados en la caleta, junto a la ciudad tecnologica', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
        response('Para conocer los documentos de inscripcon, ingrese a Orbi.edu.com/registro', ['inscripcion', 'requisitos', 'documentos', 'informacion'], single_response=True)
        response('Las fechas de admision estan descritas en Orbi.edu.com/admisiones', ['adminision', 'ingreso', 'cuando', 'fecha'], single_response=True)
        response('La seleccion de materias esta disponible en Orbi.edu.do', ['materias', 'seleccion', 'donde', 'como'], single_response=True)
        response('Dentro del campus ITLA no tenemos un codigo de vestimenta especifico, pero si velamos por la vestimenta decente', ['vestimenta', 'codigo', 'tienen', 'algun'], single_response=True)
        response('Toda la informacion acerca de nuestros precios esta en Orbi.edu.com/precios', ['precio', 'inscripcion', 'mensualidad', 'creditos', 'precios', 'detalles'], single_response=True)
        response('Nuestra biblioteca esta ubicada en el edificio 3.', ['biblioteca', 'libros', 'tienen', 'virtuales'], single_response=True)
        response('Siempre a la orden, gracias por utilizar nuestros servicios', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'b??scalo en google a ver que tal'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))