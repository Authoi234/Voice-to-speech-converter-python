import tkinter as tk, speech_recognition as sr, pyperclip

def copy_text():
    text = T.get("1.0", tk.END)
    pyperclip.copy(text)

def VoiceCommand():
    voice_btn.config(text="Listening...", bg="yellow", fg="white")

    with sr.Microphone() as source:
        root.update()

        try:
            audio =  sr.Recognizer().listen(source, timeout=2, phrase_time_limit=10)
            sr.Recognizer().recognize_google(audio, language='bn-BD')
            text = sr.Recognizer().recognize_google(audio, language='bn-BD')
            T.insert(tk.END, text + " ")
            output_label.config(text="Completed")
        except sr.UnknownValueError:
            output_label.config(text="Not Understandable")
        except sr.RequestError:
            output_label.config(text="Request Error")
        finally:
            voice_btn.config(text="Voice", bg="#AD8FE5", fg="white")

root = tk.Tk()
root.title("Bangla speech to text converter By Authoi")
T=tk.Text(root)
T.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

btn_frame = tk.Frame(root)
btn_frame.pack(side=tk.TOP, fill=tk.X)

copy_btn = tk.Button(btn_frame, text="Copy Text", bg="red", fg="white",font=("Helvetica", 10), width=20, height=2 , command=copy_text)
copy_btn.pack(side=tk.TOP,   padx=15, pady=15)

voice_btn = tk.Button(btn_frame, text="Voice", bg="#AD8FE5", fg="white",font=("Helvetica", 10), width=20, height=2 , command=VoiceCommand)
voice_btn.pack(side=tk.TOP,   padx=15, pady=15)

output_label = tk.Label(root, text="Output", font=("Helvetica", 16))
output_label.pack(side=tk.BOTTOM)

tk.mainloop()