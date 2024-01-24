from gtts import gTTS
import PyPDF2


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text


def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    return tts


def save_audio(tts, output_path):
    tts.save(output_path)


def pdf_to_audiobook(pdf_path, output_path):
    text = extract_text_from_pdf(pdf_path)
    tts = text_to_speech(text)
    save_audio(tts, output_path)


if __name__ == "__main__":
    # Get input PDF file path from the user
    pdf_input_path = input("Enter the path to the input PDF file,removing any quotation marks: ")

    # Get output audiobook file path from the user
    audio_output_path = input("Enter the path for the output audiobook file (e.g., output.mp3),removing any quotation marks: ")

    pdf_to_audiobook(pdf_input_path, audio_output_path)



