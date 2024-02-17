# def longestNiceSubstring(s: str):
#     nice_string = ""
#     current_string = ""
#     set1 = set(s)
#     for i in range(len(s)):
#         if s[i] == s[i].lower():
#             if s[i].upper() in set1:
#                 current_string += s[i]
#             else:
#                 new_string_fraction = s[i+1:]
#                 set1 = set(new_string_fraction)
#                 current_string = ""
#         else:
#             if s[i].lower() in set1:
#                 current_string += s[i]
#         if len(current_string) > len(nice_string):
#             nice_string = current_string
#
#     return nice_string
#

def is_nice(substring):
    lowercase_set = set(substring.lower())
    uppercase_set = set(substring.upper())
    return lowercase_set == uppercase_set


def longestNiceSubstring(s: str):
    nice_string = ""
    for i in range(len(s)):
        for j in range(i + len(nice_string), len(s)):
            substring = s[i:j + 1]
            if is_nice(substring) and len(substring) > len(nice_string):
                nice_string = substring

    return nice_string



print(longestNiceSubstring("YazaAay"))

