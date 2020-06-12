'''
Lesk algorithms 

Lesk algoritması, anlamların içindeki kelime benzeriliğine bakarak cümlelerin benzer olup olmadığını saptamak
1) Her iki cümle için tokenization işlemi uygulanır.
2) Her iki cümle için sadeleşme uygulanır.(to, a, or, in... veya noktalama işaretlerden kurtulurur)
3) Her iki cümle için Lemmatization işlemi uygulanır.
4) Birinci cümle ve ikinci cümle için ortak olan kelimelerin sayısı birden fazla ise bu iki cümle benzerdir diyebiliriz.

EX:
warn = "to make someone realize a possible danger or problem, especially one in the future"
alert = "quick to realize a possible danger, understand, and act in a particular situation"

1)TOKANIZATION
warn = ['quick', 'to', 'realize', 'a', 'possible', 'danger', ',', 'understand', ',', 'and', 'act', 'in', 'a', 'particular', 'situation']
alert = ['to', 'make', 'someone', 'realize', 'a', 'possible', 'danger', 'or', 'problem', ',', 'especially', 'one', 'in', 'the', 'future']

2) COMMON USING WORD IGNORE
warn = ['quick', 'realize', 'possible', 'danger', 'understand', 'act', 'particular', 'situation']
alert = ['make', 'someone', 'realize', 'possible', 'danger', 'problem', 'especially', 'one', 'future']

3) LEMMATİZATİON
warn = ['quick', 'realize', 'possible', 'danger', 'understand', 'act', 'particular', 'situation']
alert = ['make', 'someone', 'realize', 'possible', 'danger', 'problem', 'especially', 'one', 'future']

---CATCH SAME WORD---
warn alert ['danger', 'possible', 'realize']
same word number =  3
'''

from nltk import tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# words
def words(s1, s2):
    amazing = "making someone feel extremely surprised"
    incredible = "impossible, or very difficult, to believe"
    bad = "worse, worst unpleasant and causing difficulties or harm"
    worse = "more unpleasant, difficult, or severe than before"
    beautiful = "having an attractive quality that gives pleasure to those who experience it or think about it"
    nice = "used to describe a person who is kind, friendly, and pleasant to be with"
    big = "large in size or amount"
    enormous = "extremely large"
    dangerous = "a person, animal, thing, or activity could harm you"
    perilous = "extremely activity could harm you"
    end = "the final part of something such as a period of time, activity, or story"
    finish = "to complete something or come to the end of an activity"
    false = "not true, but made to seem true in order to deceive people"
    fake = "an object that is made to look real or valuable in order to deceive people"
    fast = "moving or happening quickly, or able to move or happen quickly"
    quick = "happening or done with great speed, or lasting only a short time"
    good = "very satisfactory, enjoyable, pleasant, or interesting"
    fine = "good or good enough; healthy and well"
    hate = "to dislike someone or something very much"
    dislike = "to not like someone or something"
    warn = "to make someone realize a possible danger or problem, especially one in the future"
    alert = "quick to realize a possible danger, understand, and act in a particular situation"

    if s1 == "alert":
        s1 = alert
    elif s1 == "warn":
        s1 = warn
    elif s1 == "dislike":
        s1 = dislike
    elif s1 == "hate":
        s1 = hate
    elif s1 == "fine":
        s1 = fine
    elif s1 == "good":
        s1 = good
    elif s1 == "quick":
        s1 = quick
    elif s1 == "fake":
        s1 = fake
    elif s1 == "fast":
        s1 = fast
    elif s1 == "false":
        s1 = false
    elif s1 == "finish":
        s1 = finish
    elif s1 == "end":
        s1 = end
    elif s1 == "perilous":
        s1 = perilous
    elif s1 == "dangerous":
        s1 = dangerous
    elif s1 == "enormous":
        s1 = enormous
    elif s1 == "big":
        s1 = big
    elif s1 == "nice":
        s1 = nice
    elif s1 == "beautiful":
        s1 = beautiful
    elif s1 == "worse":
        s1 = worse
    elif s1 == "incredible":
        s1 = incredible
    elif s1 == "bad":
        s1 = bad
    elif s1 == "amazing":
        s1 = amazing

    if s2 == "alert":
        s2 = alert
    elif s2 == "warn":
        s2 = warn
    elif s2 == "dislike":
        s2 = dislike
    elif s2 == "hate":
        s2 = hate
    elif s2 == "fine":
        s2 = fine
    elif s2 == "good":
        s2 = good
    elif s2 == "quick":
        s2 = quick
    elif s2 == "fake":
        s2 = fake
    elif s2 == "fast":
        s2 = fast
    elif s2 == "false":
        s2 = false
    elif s2 == "finish":
        s2 = finish
    elif s2 == "end":
        s2 = end
    elif s2 == "perilous":
        s2 = perilous
    elif s2 == "dangerous":
        s2 = dangerous
    elif s2 == "enormous":
        s2 = enormous
    elif s2 == "big":
        s2 = big
    elif s2 == "nice":
        s2 = nice
    elif s2 == "beautiful":
        s2 = beautiful
    elif s2 == "worse":
        s2 = worse
    elif s2 == "incredible":
        s2 = incredible
    elif s2 == "bad":
        s2 = bad
    elif s2 == "amazing":
        s2 = amazing
    return s1, s2


word1 = input()

# make words tokenization
def word_tokenization(word1, word2):
    word1_tokenizetion = tokenize.word_tokenize(word1)
    word2_tokenizetion = tokenize.word_tokenize(word2)
    return word2_tokenizetion, word1_tokenizetion

# punctuation escape and common using word ignore
def word_ignore(word1, word2):
    word1, word2 = word_tokenization(word1, word2)

    # remove punctuation
    word_punctuation1 = [w1 for w1 in word1 if w1.isalpha()]
    word_punctuation2 = [w2 for w2 in word2 if w2.isalpha()]


# common using word ignore
    s_word = stopwords.words('english')
    word_p1 = word_punctuation1[:]
    word_p2 = word_punctuation2[:]
    for w in word_punctuation1:
            if w in s_word:
               word_p1.remove(w)
    for w in word_punctuation2:
            if w in s_word:
               word_p2.remove(w)
    return word_p1, word_p2

# make lemmatization
def lemma(word1, word2):
    w_1, w_2 = word_ignore(word1, word2)
    lemmatizer = WordNetLemmatizer()

    # non-element cluster identification
    word1_lemma = []
    word2_lemma = []

    # word length
    index_word1 = len(w_1)
    index_word2 = len(w_2)

    # non-element cluster insert element
    for w in range(index_word1):
        word_l = lemmatizer.lemmatize(w_1[w])
        word1_lemma.insert(w, word_l)
    for w in range(index_word2):
        word_2 = lemmatizer.lemmatize(w_2[w])
        word2_lemma.insert(w, word_2)

    return word1_lemma, word2_lemma

# make catch same word
def catchword(word1, word2):
    c_word1, c_word2 = lemma(word1, word2)
    f = []
    index = 0
    for c1 in c_word1:
        for c2 in c_word2:
            if c1 in c2:
                f.insert(0, c1)
                index = index + 1
    return index, f


d1 = ["alert", "warn", "dislike", "hate", "fine", "good", "quick", "fake", "fast", "false", "finish", "end",
      "perilous", "enormous", "big", "nice", "beautiful", "worse", "incredible", "bad", "amazing", ]
word1 = word1.lower()
d1.remove(word1)
for i in range(len(d1)):
    word2 = d1[i]
    word2 = word2.lower()

    w1, w2 = words(word1, word2)

    # remove number
    r_word1 = ''.join([i for i in w1 if not i.isdigit()])
    r_word2 = ''.join([i for i in w2 if not i.isdigit()])

    # make small character
    word1_s = r_word1.lower()
    word2_s = r_word2.lower()

    index, f1 = catchword(w1, w2)

    if index > 2:
        print("\n", word1, " and ", word2, "similar word")

        print("\n ----------------------- \n")
        print("Show details (yes \ no)")
        C = input()
        c = C.lower()

        if c == 'yes':
            print("-----TOKANIZATION-----")
            w_tokanize = word_tokenization(word1_s, word2_s)
            for t in range(2):
                print(w_tokanize[t])
            print("\n")

            print("-----COMMON USING WORD IGNORE-----")
            w_punctuation = word_ignore(word1_s, word2_s)
            for p in range(2):
                print(w_punctuation[p])
            print("\n")

            print("---LEMMATİZATİON---")
            w_lemmatization = lemma(word1_s, word2_s)
            for l in range(2):
                print(w_lemmatization[l])
            print("\n")

            print("---CATCH SAME WORD---")
            print(word1, word2, f1)
            print("same word number = ", index)

        elif c ==  'no':
            print("No details")