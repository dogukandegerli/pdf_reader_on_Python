import pyttsx3
import PyPDF2

hikaye_yolu = r"C:\Users\Doğukan Değerli\Desktop\TheShortStory_10001379.pdf"

with open(hikaye_yolu, "rb") as hikaye:
    pdfOkuyucu = PyPDF2.PdfReader(hikaye)

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    for sayfa_numarasi in range(len(pdfOkuyucu.pages)):
        sayfa = pdfOkuyucu.pages[sayfa_numarasi]
        yazi = sayfa.extract_text()  # extractText yerine extract_text kullanıyoruz
        engine.say(yazi)
        engine.runAndWait()

        if sayfa_numarasi == 1:  # Örneğin, 5. sayfada durdur
            break
