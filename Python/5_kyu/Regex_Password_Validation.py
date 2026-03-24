"""You need to write regex that will validate a password to make sure it meets the following criteria:
    At least six characters long
    contains a lowercase letter
    contains an uppercase letter
    contains a digit
    only contains alphanumeric characters (note that '_' is not alphanumeric)
"""
regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z0-9]{6,}$'

"""
^ / $ — start and end anchors (match the whole string)
(?=.*[a-z]) — lookahead: must contain at least one lowercase letter
(?=.*[A-Z]) — lookahead: must contain at least one uppercase letter
(?=.*\d) — lookahead: must contain at least one digit
[a-zA-Z0-9]{6,} — only alphanumeric characters, 6 or more

"""