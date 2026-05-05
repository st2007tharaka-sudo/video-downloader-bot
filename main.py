import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# මෙතනට ඔයාගේ Token එක දාන්න
TOKEN =8558595291:AAGj_Gra5N74n_W3FQWtDLAFfYTL2o_QKcc

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ඕනෑම වීඩියෝ ලින්ක් එකක් එවන්න, මම ඒක download කරලා දෙන්නම්! 📥⚡️")

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text("වීඩියෝ එක සකසමින් පවතිනවා, මොහොතක් රැඳී සිටින්න...⏳")
    
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'video.mp4',
            'max_filesize': 45 * 1024 * 1024, # 45MB ට අඩු ඒවා පමණයි
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        await update.message.reply_video(video=open('video.mp4', 'rb'))
        os.remove('video.mp4')
    except Exception as e:
        await update.message.reply_text("වැරදීමක් සිදුවුණා. ලින්ක් එක නිවැරදිද බලන්න. ❌")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), download_video))
    app.run_polling()
