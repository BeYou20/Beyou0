from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, CallbackQueryHandler, filters

async def admin_panel(update, context):
    await update.message.reply_text("لوحة تحكم المشرف.")

async def show_dev_panel_after_conv(update, context):
    await update.message.reply_text("تم الرجوع للوحة الإدارة.")

admin_msg_handler = CommandHandler("adminpanel", admin_panel)
admin_user_handler = CommandHandler("adminusers", lambda u, c: u.message.reply_text("إدارة المستخدمين"))
admin_broadcast_handler = CommandHandler("broadcast", lambda u, c: u.message.reply_text("إرسال رسالة جماعية"))
