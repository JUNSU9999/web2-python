# positional formating
print(
    "to {}. Lorem ipsum dolor sit amet, consectetur adipsisicing elit, sed do eiusmod tempor incidiunt ut labore et dolore magna aliqua. Ut enim ad minim apple veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. {} Duis aute irure dolor {} in reprehenderit apple computer in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui {} officia deserunt mollit anim id est laborum.".format(
        "JUNSU", 12, "JUNSU", "JUNSU"
    )
)

# Named placeholder
print(
    "to {name}. Lorem ipsum dolor sit amet, consectetur adipsisicing elit, sed do eiusmod tempor incidiunt ut labore et dolore magna aliqua. Ut enim ad minim apple veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. {age:d} Duis aute irure dolor {name} in reprehenderit apple computer in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui {name} officia deserunt mollit anim id est laborum.".format(
        name="JUNSU", age=12
    )
)
