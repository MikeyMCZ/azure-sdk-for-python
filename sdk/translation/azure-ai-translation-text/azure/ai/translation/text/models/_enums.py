# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class LanguageDirectionality(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Language Directionality."""

    LEFT_TO_RIGHT = "ltr"
    """Language is written left to right."""
    RIGHT_TO_LEFT = "rtl"
    """Language is written right to left."""


class ProfanityAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Translator profanity actions."""

    NO_ACTION = "NoAction"
    """No Action is taken on profanity"""
    MARKED = "Marked"
    """Profanity is marked."""
    DELETED = "Deleted"
    """Profanity is deteled from the translated text."""


class ProfanityMarker(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Translator profanity markers."""

    ASTERISK = "Asterisk"
    """Profanity is marked with asterisk."""
    TAG = "Tag"
    """Profanity is marked with the tags."""


class TextType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Translation text type."""

    PLAIN = "Plain"
    HTML = "Html"
