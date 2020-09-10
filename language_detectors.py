#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import chardet
import langid
from textblob import TextBlob
from polyglot.text import Text, Word
from langdetect import detect, DetectorFactory, detect_langs


def text_blob():
    """
    Detect language with text_blob

    :return: True
    :rtype: bool
    """
    with open("./inputfile.txt", "r") as sentences:
        try:
            for sentence in sentences:
                sentence = sentence.strip()
                blob = TextBlob(sentence)
                result = blob.detect_language()
                with open("./output/textBlobResult.short.txt", "w") as output:
                    output.write(sentence, ":", result)
        except:
            pass
    return True


def polyglot():
    """
    Detect language with polyglot

    :return: True
    :rtype: bool
    """
    with open("./inputfile.txt", "r") as sentences:
        try:
            for sentence in sentences:
                sentence = sentence.strip()
                result = Text(sentence)
                print(sentence, "Language Detected: Code={}, Name={}\n".format(result.language.code,
                                                                               result.language.name),
                      file=open("./output/polyglotResult.short.txt", "a"))
        except:
            pass
    return True


def chardet_export():
    """
    Detect language with chardet

    :return: True
    :rtype: bool
    """
    with open("./inputfile.txt", "r") as sentences:
        try:
            for sentence in sentences:
                sentence = sentence.strip()
                result = chardet.detect(sentence.encode('utf-8'))
                print(sentence, result, file=open("./output/chardetResult.short.txt", "a"))
        except:
            pass
    return True


def lang_detect():
    """
    Detect language with chardet

    :return: True
    :rtype: bool
    """
    with open("./inputfile.txt", "r") as sentences:
        try:
            for sentence in sentences:
                sentence = sentence.strip()
                result = detect_langs(sentence)
                print(sentence, ":", result, file=open("./output/langDedectResult.short.txt", "a"))
        except:
            pass
    return True


def langid():
    """
    Detect language with guess_language

    :return: True
    :rtype: bool
    """
    with open("./inputfile.txt", "r") as sentences:
        for sentence in sentences:
            try:
                sentence = sentence.strip()
                result = langid.classify(sentence)
                print(sentence, ":", result, file=open("./output/langidResult.short.txt", "a"))
            except:
                pass
    return True


if __name__ == '__main__':
    text_blob()
    polyglot()
    chardet_export()
    lang_detect()
    langid()
