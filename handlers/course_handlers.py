from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, CallbackQueryHandler, filters

async def admin_add_course(update, context):
    await update.message.reply_text("إضافة دورة جديدة.")

async def admin_edit_course(update, context):
    await update.message.reply_text("تعديل دورة.")

async def admin_delete_course(update, context):
    await update.message.reply_text("حذف دورة.")

async def admin_move_course(update, context):
    await update.message.reply_text("نقل دورة لتصنيف آخر.")

admin_add_course_handler = CommandHandler("addcourse", admin_add_course)
admin_edit_course_handler = CommandHandler("editcourse", admin_edit_course)
admin_delete_course_handler = CommandHandler("delcourse", admin_delete_course)
admin_move_course_handler = CommandHandler("movecourse", admin_move_course)
