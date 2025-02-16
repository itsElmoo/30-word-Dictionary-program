WORDS = {
    "BAYAMBANG": "a municipality in the province of the philippines.",
    "LIMIT": "a point or level beyond which something does not or may not extend or pass.",
    "MAXIMUM": "as great, high, or intense as possible or permitted.",
    "MINIMUM": "the least or smallest amount or quantity possible, attainable, oe required.",
    "REPETITION": "the action of repeating something.",
    "SET": "a group of things belong together.",
    "OFFLINE": "out of operation or existence.",
    "ONLINE": "in or into operation or existence.",
    "TOOLS": "something(such as instrument or apparatus) used in performing an operation.",
    "MESSAGE": "a communication or statement conveyed from one person or group to other.",
    "APPLICATION": "the action o f putting something into operation.",
    "VIEW": "the ablity to see something or to be seen from a particular place.",
    "GREEN": "is a color between blue and yellow in the spectrum",
    "PLOT": "secretly make plans to carry out (an illegal or harmful action).",
    "VALENTINE": "a card sent, often anonymously, on St. Valentine's Day (February 14) to a person one loves or is attracted to.",
    "DESIGN": "a plan or drawing produced to show the look and function or workings of a building, garment, or other object before it is built or made.",
    "LEATHER": " strong, flexible and durable material obtained from the tanning, or chemical treatment, of animal skins and hides to prevent decay.",
    "LEADER": "the person who leads or commands a group, organization, or country.",
    "WALLET": "a pocket-sized flat folding case for holding money and plastic cards.",
    "PHONE": "a telephone.",
    "BATTERY": "a fortified emplacement for heavy guns.",
    "NOTIFICATION": "the action of notifying someone or something.",
    "BOTTLE": "a container, typically made of glass or plastic and with a narrow neck, used for storing drinks or other liquids.",
    "BREAD": "a usually baked and leavened food made of a mixture whose basic constituent is flour or meal.",
    "BACKSPACE": "a reference work on a particular subject, the items of which are typically arranged in alphabetical order.",
    "DICTIONARY": "a reference work on a particular subject, the items of which are typically arranged in alphabetical order.",
    "IPHONE": "a smartphone made by Apple that combines a phone, camera, music player, and computer into one device.",
    "CHOCOLATE": "a food made from cocoa beans that can be eaten or used as a flavoring.",
    "PESO": "the basic monetary unit of Mexico, several other Latin American countries, and the Philippines, equal to 100 centésimos in Uruguay and 100 centavos elsewhere.",
    "SHOES": "a covering for the foot, typically made of leather, having a sturdy sole and not reaching above the ankle."
}

print("Hiluh ludzz! Wilkam sa Diksyunari q!")
print("Ikaw hanap meaning words?? Pili k jan ludz kng anu usto mue:")
print(", ".join(WORDS.keys()))

while True:
    word = input("\nSay: ")
       
    if word == "EXIT":
        print("Paalam ludz!")
        break
    
    print(f"\nThe definition of {word}:")
    print(f"'{WORDS.get(word, 'Mali man nilagay mo lude, shek mue spiling mue ang laki mue n pati spiling mali?? hayst')}'\n")

