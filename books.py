from fastapi import FastAPI

app = FastAPI()


BOOKS = [
     {'title': 'Title one' , 'author':'Autor one','category' : 'Science'},
     {'title': 'Title two','author':'Autor two','category':'Maths'},
     {'title': 'Title three','author':'Autor three','category':'Bio'},
     {'title': 'Title four','author':'Autor four','category':'Chem'},
     {'title': 'Title five','author':'Autor five','category':'Hindi'},
     {'title': 'Title six','author':'Autor two','category':'English'}
 ]
@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_books(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold == book_title.casefold():
            return book


@app.get("books/byauthor/{author}")
async def read_books_by_author_path(authoe:str):
    books_to_return=[]
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
        return books_to_return