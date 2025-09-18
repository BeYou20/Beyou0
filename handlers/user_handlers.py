from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from db_manager import add_user, get_all_admins
from handlers.callback_handlers import (
    start_registration, get_name, get_gender, get_age,
    get_country, get_city, get_phone, get_email, show_main_menu
)

GET_NAME, GET_GENDER, GET_AGE, GET_COUNTRY, GET_CITY, GET_PHONE, GET_EMAIL = range(7)

async def start(update, context):
    user = update.effective_user
    user_id = user.id
    is_new_user = add_user(user_id)
    if is_new_user:
        admin_ids_to_notify = [admin_id for admin_id in get_all_admins() if admin_id != user_id]
        if admin_ids_to_notify:
            message_to_admin = (
                f"**🔔 مستخدم جديد دخل البوت!**\n\n"
                f"**الاسم:** {user.first_name} {user.last_name or ''}\n"
                f"**المعرف (@):** {user.username or 'لا يوجد'}\n"
                f"**معرف المستخدم (ID):** `{{user_id}}`"
            )
            for admin_id in admin_ids_to_notify:
                await context.bot.send_message(
                    chat_id=admin_id,
                    text=message_to_admin,
                    parse_mode='Markdown'
                )
    await update.message.reply_text("أهلاً بك في بوت الدورات التدريبية!", reply_markup=ReplyKeyboardRemove())
    await show_main_menu(update, context)

async def cancel(update, context):
    await update.message.reply_text('تم إلغاء العملية.', reply_markup=ReplyKeyboardRemove())
    await show_main_menu(update, context)
    return ConversationHandler.END

user_reg_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(start_registration, pattern=r"^register_\\d+$")],
    states={
        GET_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
        GET_GENDER: [CallbackQueryHandler(get_gender, pattern=r"^gender_")],
        GET_AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_age)],
        GET_COUNTRY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_country)],
        GET_CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_city)],
        GET_PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
        GET_EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_email)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)
