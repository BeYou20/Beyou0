from telegram.ext import CommandHandler

async def admin_category_panel(update, context):
    await update.message.reply_text("إدارة تصنيفات الدورات.")

admin_category_handler = CommandHandler("categories", admin_category_panel)
