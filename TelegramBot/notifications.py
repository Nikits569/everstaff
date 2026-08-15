from .bot import bot
from .db import get_active_subscribers
from .handlers import *


async def send_message(name_surname, email, title, text, country, city):
    for i in get_active_subscribers():
        try:
            final_text = f"""
            📩 <b>Новий запит з сайту</b>
            
            👤 <b>Ім'я:</b> {name_surname}
            📧 <b>Email:</b> {email}
            🌍 <b>Країна:</b> {country}
            🏙 <b>Місто:</b> {city}
            
            📌 <b>Тема:</b> {title}
            💬 <b>Повідомлення:</b>
            {text}
            """
            await bot.send_message(i[0], text=final_text, parse_mode="HTML")
        except Exception as e:
            print(e)
