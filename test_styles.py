import pytest

def test_font_family():
    # Ellenőrizzük, hogy a body tagben talpatlan betűtípus van beállítva
    with open('styles.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'font-family: sans-serif;' in content, "A talpatlan betűtípus nincs beállítva az egész weboldalon!"

def test_h1_background_color():
    # Ellenőrizzük, hogy az egyes szintű fejezetcím háttérszíne aqua
    with open('styles.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'background-color: aqua;' in content, "Az egyes szintű fejezetcím háttérszíne nem aqua!"

def test_h1_text_color():
    # Ellenőrizzük, hogy az egyes szintű fejezetcím szövege navy színű
    with open('styles.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'color: navy;' in content, "Az egyes szintű fejezetcím szövege nem navy!"

def test_first_sentence_second_word_font_size():
    # Ellenőrizzük, hogy az első mondat második szava 24 pixel méretű
    with open('styles.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'font-size: 24px;' in content, "Az első mondat második szava nem 24 pixel méretű!"

def test_first_sentence_third_word_underline():
    # Ellenőrizzük, hogy az első mondat harmadik szava alá van húzva
    with open('styles.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'text-decoration: underline;' in content, "Az első mondat harmadik szava nem aláhúzott!"

def test_third_and_fourth_sentence_strike_through():
    # Ellenőrizzük, hogy a harmadik és negyedik mondat áthúzott
    with open('styles.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'text-decoration: line-through;' in content, "A harmadik és negyedik mondat nem áthúzott!"

def test_third_and_fourth_sentence_yellow_color():
    # Ellenőrizzük, hogy a harmadik és negyedik mondat sárga színű
    with open('styles.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'color: yellow;' in content, "A harmadik és negyedik mondat nem sárga színű!"

def test_fourth_sentence_background_and_text_color():
    # Ellenőrizzük, hogy a negyedik mondat háttérszíne kék, szöveg színe fehér
    with open('styles.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'background-color: blue;' in content, "A negyedik mondat háttérszíne nem kék!"
        assert 'color: white;' in content, "A negyedik mondat szöveg színe nem fehér!"
