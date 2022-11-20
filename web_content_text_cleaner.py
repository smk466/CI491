from web_scrape_classes import LinkContent

"""
TODO
This will clean the texts before searching names with spacy as spacy can't fully recognize
the texts directly from the extracted web contents

This script will run after web_content_retrieve.py and before find_names_and_emails.py

Plan to do:
1. Remove new lines in each link content
2. Remove any special characters in content text
3. Try to eliminate any combined texts
"""

def remove_new_lines(content: list[LinkContent]) -> list[LinkContent]:
    cleanedContent: list[LinkContent] = []
    for webObj in content:
        webObj.content = " ".join(webObj.content.split("\n"))
        cleanedContent.append(webObj)
    # tempContent = remove_none_string(tempContent)
    write_cleaned_content_text_to_file(cleanedContent)
    return cleanedContent
    
# def remove_special_characters():
    
# def remove_none_string(tempContent: list[str]) -> list[str]:
#     noneString = "none"
#     while (noneString in tempContent):
#         tempContent.remove(noneString)
#     return tempContent
    
def write_cleaned_content_text_to_file(tempContent: list[LinkContent]) -> None:
    with open("output_cleaned_contents.txt", "w", encoding="utf-8-sig") as f:
        for webObj in tempContent:
            #print(f'Link: {webObj.link}\n\n{webObj.content}\n\n', file=f)
            print(webObj, file=f)
    f.close