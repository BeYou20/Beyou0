from telegram import ReplyKeyboardMarkup
from telegram.ext import CallbackContext

# أمثلة توضيحية لدوال الكولباك
async def start_registration(update, context):
    await update.callback_query.message.reply_text("أدخل اسمك:")

async def get_name(update, context):
    await update.message.reply_text("اختر جنسك:", reply_markup=ReplyKeyboardMarkup([['ذكر', 'أنثى']], one_time_keyboard=True))

async def get_gender(update, context):
    await update.callback_query.message.reply_text("أدخل عمرك:")

async def get_age(update, context):
    await update.message.reply_text("اكتب دولتك:")

async def get_country(update, context):
    await update.message.reply_text("اكتب مدينتك:")

async def get_city(update, context):
    await update.message.reply_text("رقم هاتفك:")

async def get_phone(update, context):
    await update.message.reply_text("بريدك الإلكتروني:")

async def get_email(update, context):
    await update.message.reply_text("تم التسجيل بنجاح!")

async def show_main_menu(update, context):
    await update.message.reply_text("القائمة الرئيسية للبوت.")

async def handle_callback_query(update, context):
    await update.callback_query.answer("تم استقبال الأمر.")

async def handle_receipt(update, context):
    await update.message.reply_text("تم استلام صورة التحويل، سنراجعها قريباً.")
