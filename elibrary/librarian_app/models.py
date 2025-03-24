from django.db import models

class Book(models.Model):
    accession_number = models.CharField(max_length=50, unique=True)  # Unique book identifier
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publish_date = models.DateField()
    edition = models.CharField(max_length=50)
    pdf_file = models.FileField(upload_to='books_pdfs/')  # Stored inside MEDIA_ROOT/books_pdfs/
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.accession_number})"
