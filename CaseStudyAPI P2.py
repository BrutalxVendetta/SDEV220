from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book
import json

@csrf_exempt
def book_list(request):
    # /books/  -> GET = list, POST = create
    if request.method == 'GET':
        books = Book.objects.all()
        data = []
        for b in books:
            data.append({
                "id": b.id,
                "book_name": b.book_name,
                "author": b.author,
                "publisher": b.publisher
            })
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        body = request.body.decode('utf-8')
        data = json.loads(body)

        book = Book(
            book_name=data.get("book_name", ""),
            author=data.get("author", ""),
            publisher=data.get("publisher", "")
        )
        book.save()

        return JsonResponse({
            "id": book.id,
            "book_name": book.book_name,
            "author": book.author,
            "publisher": book.publisher
        }, status=201)


@csrf_exempt
def book_detail(request, id):
    # /books/<id>/  -> GET = one, PUT = update, DELETE = delete
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return JsonResponse({"message": "Book not found"}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            "id": book.id,
            "book_name": book.book_name,
            "author": book.author,
            "publisher": book.publisher
        })

    if request.method == 'PUT':
        body = request.body.decode('utf-8')
        data = json.loads(body)

        if "book_name" in data:
            book.book_name = data["book_name"]
        if "author" in data:
            book.author = data["author"]
        if "publisher" in data:
            book.publisher = data["publisher"]

        book.save()

        return JsonResponse({
            "id": book.id,
            "book_name": book.book_name,
            "author": book.author,
            "publisher": book.publisher
        })

    if request.method == 'DELETE':
        book.delete()
        return JsonResponse({"message": "Book deleted"})
