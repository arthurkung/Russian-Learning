OT_string = '''1. Genesis
2. Exodus
3. Leviticus
4. Numbers
5. Deuteronomy
6. Joshua
7. Judges
8. Ruth
9. 1 Samuel
10. 2 Samuel
11. 1 Kings
12. 2 Kings
13. 1 Chronicles
14. 2 Chronicles
15. Ezra
16. Nehemiah
17. Esther
18. Job
19. Psalms
20. Proverbs
21. Ecclesiastes
22. Song of Solomon
23. Isaiah
24. Jeremiah
25. Lamentations
26. Ezekiel
27. Daniel
28. Hosea
29. Joel
30. Amos
31. Obadiah
32. Jonah
33. Micah
34. Nahum
35. Habakkuk
36. Zephaniah
37. Haggai
38. Zechariah
39. Malachi'''

NT_string='''1. Matthew
2. Mark
3. Luke
4. John
5. Acts (of the Apostles)
6. Romans
7. 1 Corinthians
8. 2 Corinthians
9. Galatians
10. Ephesians
11. Philippians
12. Colossians
13. 1 Thessalonians
14. 2 Thessalonians
15. 1 Timothy
16. 2 Timothy
17. Titus
18. Philemon
19. Hebrews
20. James
21. 1 Peter
22. 2 Peter
23. 1 John
24. 2 John
25. 3 John
26. Jude
27. Revelation'''

OT_list = OT_string.split('\n')
OT_list = [string.split('. ') for string in OT_list]
OT_dict ={int(book[0]):book[1] for book in OT_list}

NT_list = NT_string.split('\n')
NT_list = [string.split('. ') for string in NT_list]
NT_dict ={int(book[0])+39:book[1] for book in NT_list}
Bible_book_list = {**OT_dict, **NT_dict}

def give_full_verse_name(verse_name):
    try:
        book, chapter, verse = verse_name.split('-')
        last_book_char = book[-1]
        if not last_book_char.isdigit():
            book = book[:-1]
        book_name = Bible_book_list[int(book)]

        return book_name+' '+chapter+':'+verse
    except:
        raise Exception('versename has to be in format: booknum-chapternum-versenum')

