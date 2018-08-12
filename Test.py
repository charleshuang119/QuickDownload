import item

soup = item.find_search_content("https://www.youtube.com/results?search_query=python")
print(item.page_bar(soup))
