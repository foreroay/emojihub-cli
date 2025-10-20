import argparse
from src.api import (
    get_random_emoji, 
    get_all_groups, 
    get_emojis_by_group, 
    search_emojis
)

def _format_emoji(emoji: dict) -> str:
    """Formats emoji data into a readable string."""
    name = emoji.get('name', 'N/A')
    html = emoji.get('htmlCode', ['N/A'])[0]
    category = emoji.get('category', 'N/A')
    group = emoji.get('group', 'N/A')
    return f"{html}  {name} (Group: {group}, Category: {category})"

def main():
    """Main CLI handler."""
    parser = argparse.ArgumentParser(description="A CLI for the EmojiHub API 😺")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Command: random
    subparsers.add_parser("random", help="Get a random emoji")

    # Command: list-groups
    subparsers.add_parser("list-groups", help="List all available emoji groups")

    # Command: by-group
    group_parser = subparsers.add_parser("by-group", help="Get emojis from a group")
    group_parser.add_argument("group_name", type=str, help="e.g., 'face-positive'")

    # Command: search
    search_parser = subparsers.add_parser("search", help="Search for emojis")
    search_parser.add_argument("query", type=str, help="e.g., 'cat'")

    args = parser.parse_args()

    if args.command == "random":
        emoji = get_random_emoji()
        if emoji:
            print("Your random emoji:")
            print(_format_emoji(emoji))

    elif args.command == "list-groups":
        groups = get_all_groups()
        if groups:
            print("--- Available Emoji Groups ---")
            for group in groups:
                print(f"- {group}")

    elif args.command == "by-group":
        emojis = get_emojis_by_group(args.group_name)
        if emojis:
            print(f"--- Emojis in group '{args.group_name}' ---")
            for emoji in emojis:
                print(_format_emoji(emoji))
        else:
            print(f"No emojis found for group '{args.group_name}'.")

    elif args.command == "search":
        emojis = search_emojis(args.query)
        if emojis:
            print(f"--- Search results for '{args.query}' ---")
            for emoji in emojis:
                print(_format_emoji(emoji))
        else:
            print(f"No emojis found for query '{args.query}'.")

if __name__ == "__main__":
    main()
