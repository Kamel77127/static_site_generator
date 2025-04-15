from textnode import TextNode,TextTypes


def main():
    random = TextNode("This is some anchor text", TextTypes.LINK, "https://www.boot.dev")
    print(random)
    

if __name__ == "__main__":
    main()