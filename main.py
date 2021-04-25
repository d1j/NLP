from google_trans_new import google_translator

import langs


TRANS = google_translator(url_suffix="com")


def translate_input():
    """
        Handles translation from user input flow.
    """
    # Get user input.
    text = input("Please type in the text to translate:\n")

    # Get language to translate from.
    src_lang = input("Type in language code to translate from. \nType 'detect' if you wish to automatically detect source language: \n")
    if (src_lang != "detect") and (src_lang not in langs.SHORT_TO_FULL):
        print("Wrong selection. Please check the list of available languages.") 
        return
    # Get language to translate to.
    tgt_lang = input("Type in language code to translate to:\n")
    if (tgt_lang != "detect") and (tgt_lang not in langs.SHORT_TO_FULL):
        print("Wrong selection. Please check the list of available languages.") 
        return

    # Translate text.
    translated = None
    if src_lang == "detect":
        translated = TRANS.translate(text, lang_tgt=tgt_lang)
    else:
        translated = TRANS.translate(text, lang_src=src_lang, lang_tgt=tgt_lang)    
    
    # Output translated text.
    print(f"Translated text:\n{translated}")


def translate_from_file():
    """
        Handles translation from file flow.
    """
    # Get file name.
    file_name = input("Please type in the name of the file to translate:\n")

    #Open file, print out error msg if file non existent
    try:
    	with open(file_name, 'r') as file:
    		lines = file.readlines()
    		text = ''.join(lines)
    	
    except FileNotFoundError as e:
    	print("Can't find the given file. Please try again.")
    	return


    # Get language to translate from.
    src_lang = input("Type in language code to translate from. \nType 'detect' if you wish to automatically detect source language: \n")
    if (src_lang != "detect") and (src_lang not in langs.SHORT_TO_FULL):
        print("Wrong selection. Please check the list of available languages.") 
        return
    # Get language to translate to.
    tgt_lang = input("Type in language code to translate to:\n")
    if (tgt_lang != "detect") and (tgt_lang not in langs.SHORT_TO_FULL):
        print("Wrong selection. Please check the list of available languages.") 
        return

    # Translate text.
    if src_lang == "detect":
        translated = TRANS.translate(text, lang_tgt=tgt_lang)
    else:
        translated = TRANS.translate(text, lang_src=src_lang, lang_tgt=tgt_lang)    
    
    # Output translated text.
    print(f"Translated text:\n{translated}")


def list_languages():
    """
        Lists available languages for translation.
    """
    lang_list = langs.SHORT_TO_FULL
    print_str = "List of available languages:\n\nCode\tFull name\n-----------------\n"
    for lang in lang_list:
        print_str += f"{lang}\t{lang_list[lang]}\n"
    print(print_str)


def main():
    SELECTION_MSG = \
""" 
Translator menu:
1. Input text to translate.
2. Translate text from file.
3. List available languages.
4. Exit.

Your selection: \
"""
    POWER = True
    # Main loop
    while POWER:
        selection = input(SELECTION_MSG)
        if selection == "1":
            translate_input()
        elif selection == "2":
            translate_from_file()
        elif selection == "3":
            list_languages()
        elif selection == "4":
            print("Exiting...")
            POWER = False
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()