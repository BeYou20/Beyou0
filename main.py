import os
import logging
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from config import BOT_TOKEN
from db_manager import init_db

from handlers.user_handlers import user_reg_handler, start, cancel
from handlers.admin_handlers import (
    admin_msg_handler, admin_user_handler, admin_broadcast_handler,
    show_dev_panel_after_conv
)
from handlers.course_handlers import (
    admin_add_course_handler, admin_edit_course_handler,
    admin_delete_course_handler, admin_move_course_handler,
)
from handlers.category_handlers import admin_category_handler
from handlers.callback_handlers import handle_callback_query, handle_receipt

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

application = Application.builder().token(BOT_TOKEN).build()
app = Flask(__name__)

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.process_update(update)
    return "OK"

@app.route("/")
def home():
    return "Bot is running"

def main() -> None:
    init_db()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(user_reg_handler)
    application.add_handler(admin_msg_handler)
    application.add_handler(admin_user_handler)
    application.add_handler(admin_broadcast_handler)
    application.add_handler(admin_add_course_handler)
    application.add_handler(admin_edit_course_handler)
    application.add_handler(admin_delete_course_handler)
    application.add_handler(admin_move_course_handler)
    application.add_handler(admin_category_handler)
    application.add_handler(CallbackQueryHandler(handle_callback_query))
    application.add_handler(MessageHandler(filters.PHOTO, handle_receipt))

    print("البوت يعمل، ينتظر تحديثات Webhook...")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

if __name__ == "__main__":
    main()
