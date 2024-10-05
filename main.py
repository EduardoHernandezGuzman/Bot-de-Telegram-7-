import telebot
import random
from dotenv import load_dotenv
import os
from telebot import types  

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

chistes = [
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
    "¿Por qué estuvo el libro de matemáticas en el hospital? ¡Porque tenía muchos problemas!",
    "¿Qué le dice una iguana a su hermana gemela? Somos iguanitas.",
    "¿Qué hace una impresora en la playa? ¡Saca copias de seguridad!",
    "¿Qué hace una abeja en el cine? ¡Zum-bido!",
    "¿Qué le dice un jardinero a otro jardinero? ¡Estamos en las mismas ramas!",
    "¿Por qué los pájaros no usan Facebook? ¡Porque ya tienen Twitter!",
    "¿Cómo se llama el campeón de buceo japonés? ¡Tokofondo!",
    "¿Cuál es el colmo de un electricista? ¡Que su esposa le sea infiel con el hijo de un cortocircuito!",
    "¿Por qué los pájaros no usan zapatos? ¡Porque tienen tenis!",
    "¿Qué le dice un árbol a otro? ¡Nos vemos en el bosque!",
    "¿Cómo se dice dios en japonés? ¡Kamisama!",
    "¿Por qué llora el libro de matemáticas? ¡Porque tiene muchos problemas!",
    "¿Qué le dice un huevo a una sartén? ¡Me tienes frito!",
    "¿Cuál es el animal más antiguo? ¡La cebra porque está en blanco y negro!",
    "¿Qué hace un pez en un árbol? ¡Nada, porque los peces no trepan!",
     "¿Por qué los esqueletos no pelean entre ellos? ¡Porque no tienen agallas!",
    "¿Qué le dijo una pared a la otra? ¡Nos vemos en la esquina!",
    "¿Cuál es el colmo de Aladdín? ¡Tener mal genio!",
    "¿Qué le dice un semáforo a otro? ¡No me mires que me estoy cambiando!",
    "¿Por qué el libro de historia está siempre deprimido? ¡Porque su pasado es terrible!",
    "¿Cómo organizan una fiesta los planetas? ¡Invitan a Neptuno!",
    "¿Por qué los fantasmas son malos para contar chistes? ¡Porque te dejan helado!",
    "¿Qué hace una escoba en el gimnasio? ¡Barre los récords!",
    "¿Cuál es el animal más trabajador? ¡La hormiga, porque siempre está en su trabajo!",
    "¿Por qué los vampiros no pueden comer sopa? ¡Porque les da escalofríos!"
]

adivinanzas = [
    "Blanco por dentro, verde por fuera. Si quieres que te lo diga, espera.",
    "Aunque no hablo, siempre cuento. Sin mí, nunca sabes el monto.",
    "Del cielo bajo, del suelo subo, y en un cofre me encierro.",
    "Dos hermanitos muy unidos que siempre van de la mano. Cuando los quiere el señor, les corta la cabeza, y los manda a freír.",
    "Vuela sin alas, llora sin ojos. Sin boca te habla y sin lengua te nombra.",
    "Un palacio muy plateado, con muchas damas dentro bailando.",
    "Roja por dentro, verde por fuera. Si quieres que te lo diga, espera.",
    "Viste de verde, amarillo y rojo, y en las vacaciones, se transforma en fuego.",
    "Con agujas y sin hilo, viajo por todo el mundo y siempre vuelvo al mismo sitio.",
    "Cuando menos lo piensas, algo suena. Si algo te dice, algo responde.",
     "Oro parece, plata no es. Quien no lo adivine, bien tonto es.",
    "Tengo dientes y no muerdo, y también tengo pies, pero no me muevo.",
    "Tiene corona pero no es rey, tiene escamas pero no es pez.",
    "Sube llena y baja vacía, y si no te das prisa, la sopa se enfría.",
    "Vuelo de noche, duermo en el día, y nunca verás plumas en ala mía.",
    "Llevo siglos en el mar, y no sé nadar.",
    "En el agua nací, en el agua he de vivir, no sé nadar ni andar, pero sé flotar.",
    "Si me nombras desaparezco. ¿Quién soy?",
    "Adivina, adivinador: por el día soy muy pequeñita, y por la noche crezco sin parar.",
    "Cien agujeros tengo y por uno me sostengo."
]

who_urls = {
    "Pennywise": "https://s1.ppllstatics.com/diariosur/www/multimedia/201909/05/media/cortadas/Pennywise-knlC-U90651765752iF-1248x770@Diario%20Sur.jpg",
    "El Jinete sin Cabeza": "https://cdn.atomix.vg/wp-content/uploads/2022/06/jinete.jpg",
    "Un selenita": "https://www.turismodeestrellas.com/media/files/6343_habitante-la-luna.png",
    "Un ser venido de otro planeta":"https://inboxlatinonyhome.files.wordpress.com/2019/07/img_6593.jpg?w=730",
    "Godzilla":"https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/media/image/2016/05/592268-godzilla-2-godzilla-vs-kong-retraso-fechas-estreno.jpg?tf=3840x",
    "Drácula":"https://4.bp.blogspot.com/-7GdQ1lmu7mQ/XtUK9YuXo4I/AAAAAAAAOK8/VtItg2XfTNoIpS-F8MJE2tB3b2SCeoYDwCK4BGAYYCw/s640/lugosidracula.jpg",
    "Cthulhu":"https://static.wikia.nocookie.net/lovecraft/images/7/72/Lovecraft-cthulhu.jpg/revision/latest?cb=20140210145556&path-prefix=es",
    "El Hombre Lobo":"https://static.wikia.nocookie.net/seres-mitologicos/images/4/4b/Werewolf.jpg/revision/latest/scale-to-width-down/1200?cb=20141212161948&path-prefix=es",
    "El Yeti":"https://ichef.bbci.co.uk/ace/ws/640/cpsprodpb/4ea3/live/8686b820-9b57-11ee-84bb-07160cedaa67.jpg",
    "La Momia":"https://t2.uc.ltmcdn.com/es/posts/9/5/5/como_hacer_un_disfraz_de_momia_21559_600.jpg",
    "El Fantasma de la Ópera":"https://lamanodelextranjero.files.wordpress.com/2018/08/el-escalofriante-maquillaje-de-lon-chaney-para-el-fantasma-de-la-opera.jpg",
    "La Bruja":"https://images.ecestaticos.com/BT3jtmRxFE6LW2sHzN4HflB70VY=/0x0:1607x904/1200x900/filters:fill(white):format(jpg)/f.elconfidencial.com%2Foriginal%2Ffa9%2Fa39%2F558%2Ffa9a39558637f505a4cc28136cb13c9e.jpg",
    "El Monstruo del Lago Ness":"https://eldiariony.com/wp-content/uploads/sites/2/2023/08/Ilustracion-del-huevo-de-flamenco-descubierto-en-Mexico.-1.jpg?w=2600",
    "El Hombre Invisible":"https://externos.uma.es/cultura/fancine/2016/wp-content/uploads/2016/10/hombreinvisible.jpg",
    "El Alienígena":"https://us.123rf.com/450wm/vikaviktoria007/vikaviktoria0072310/vikaviktoria007231001201/216291294-pesadilla-de-ciencia-ficci%C3%B3n-invasor-alien%C3%ADgena-en-la-tierra.jpg?ver=6",
    "La Criatura del Pantano":"https://static.wikia.nocookie.net/arrow/images/2/2d/Cosa_del_Pantano.jpg/revision/latest?cb=20200331232140&path-prefix=es",
    "El Vampiro":"https://static.wikia.nocookie.net/mangakaart/images/c/cc/Vampiro.jpg/revision/latest?cb=20130411164312&path-prefix=es",
    "El Demonio":"https://img.freepik.com/fotos-premium/demonio-cuernos_855892-1004.jpg",
    "El Zombi":"https://img.europapress.es/fotoweb/fotonoticia_20220822152105_1200.jpg"

    
}

action = [
    "comió",
    "destruyó",
    "quemó",
    "desintegró",
    "pulverizó",
    "escondió",
    "partió",
    "trituró",
    "devoró",
    "aplastó",
    "rompió",
    "hundió",
    "robo",
    "consumió",
    "abdujo",
    "derritió",
    "borró",
    "contaminó",
    "envenenó"
]

what = [
    "las llaves de mi casa",
    "el tejado del vecino",
    "mi coche nuevo",
    "las gafas de mi abuela",
    "los apuntes de HTML",
    "el monopatín de mi hermano pequeño",
    "el teléfono móvil",
    "el ordenador portátil",
    "el control remoto de la televisión",
    "la carta de amor",
    "el pastel de cumpleaños",
    "el libro de hechizos",
    "la lámpara mágica",
    "el trofeo del torneo",
    "la joya del museo",
    "la fórmula secreta",
    "el mapa del tesoro",
    "la varita mágica",
    "la poción de la juventud"
]

when = [
    "después del almuerzo",
    "justo a tiempo",
    "después del concierto",
    "durante el viaje de fin de curso",
    "después de las clases",
    "durante la misa del domingo",
    "durante la proyección de la película",
    "en plena noche",
    "al amanecer",
    "en pleno día",
    "en la hora de la siesta",
    "durante la cena",
    "en la hora punta",
    "durante la tormenta",
    "en la luna llena",
    "en pleno eclipse",
    "en el momento más inesperado",
    "en el peor momento posible",
    "justo antes de la boda"
]

caracteres = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "!", "@", "#", "$", "%", "&", "*", "+", "-"
]


@bot.message_handler(commands=['start'])
def send_start(message):
    start_text = """
    ¡Hola! Bienvenido a uno de mis primeros bots de Telegram.
    
    Puedes usar los botones a continuación para interactuar conmigo:
    """
    markup = types.ReplyKeyboardMarkup(row_width=2)
    chiste_button = types.KeyboardButton('/chiste')
    adivinanza_button = types.KeyboardButton('/adivinanza')
    excusa_button = types.KeyboardButton('/excusa')
    password_button = types.KeyboardButton('/password')
    help_button = types.KeyboardButton('/help') 
    about_button = types.KeyboardButton('/about') 
    markup.add(chiste_button, adivinanza_button, excusa_button, password_button, help_button, about_button)

    bot.send_message(message.chat.id, start_text, reply_markup=markup)

@bot.message_handler(commands=['help']) 
def send_help(message):
    bot.reply_to(message, "Usa los botones para ver chistes, adivinanzas o más.")

@bot.message_handler(commands=['about'])
def send_about(message):
    about_text = """
    Soy un sencillo bot de Telegram creado por EduardoHernandezGuzman.
    """
    bot.reply_to(message, about_text)

@bot.message_handler(commands=['chiste'])
def send_random_joke(message):
    random_joke = random.choice(chistes)
    bot.reply_to(message, random_joke)

@bot.message_handler(commands=['adivinanza'])
def send_random_riddle(message):
    random_riddle = random.choice(adivinanzas)
    bot.reply_to(message, random_riddle)

@bot.message_handler(commands=['excusa'])
def send_random_excuse(message):
    random_who = random.choice(list(who_urls.keys())) 
    random_action = random.choice(action)
    random_what = random.choice(what)
    random_when = random.choice(when)
    random_excuse = f"{random_who} {random_action} {random_what} {random_when}."

    if random_who in who_urls:
        image_url = who_urls[random_who]
        bot.send_photo(message.chat.id, image_url)

    bot.reply_to(message, random_excuse)

@bot.message_handler(commands=['password'])
def contraseña(message):
    valor = 9
    nueva_contraseña = ''.join(random.choice(caracteres) for _ in range(valor))
    bot.reply_to(message, f"Tu nueva contraseña es: {nueva_contraseña}")

if __name__ == "__main__":
    bot.polling(none_stop=True)