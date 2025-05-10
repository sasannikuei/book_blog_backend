from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404, render, redirect
import logging
from .forms import BookForm

logger = logging.getLogger(__name__)


class ProductListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    def get(self, request, *args, **kwargs):
        logger.info("Fetching the list of books.")
        return super().get(request, *args, **kwargs)


@api_view(['Get'])
def getProduct(request, pk):
    try:
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        logger.info(f"Book with id {pk} fetched successfully.")
        return Response(serializer.data)
    except Exception as e:
        logger.error(f"Error fetching book with id {pk}: {e}")
        return Response({'error': 'Book not found'}, status=404)


def product_form_view(request):
    try:
        if request.method == "POST":
            logger.info("Processing a new book form.")
            form = BookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                logger.info("Book saved successfully.")
                return redirect('/form')
            else:
                logger.warning("Book form is not valid.")
        else:
            form = BookForm()
    except Exception as e:
        logger.error(f"Error processing book form: {e}")
        raise
    return render(request, 'index.html', {'form': form})