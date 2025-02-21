from django.contrib import admin
from .models import Reader, Book, BorrowedBook

admin.site.register(Reader)
admin.site.register(Book)

@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ('reader', 'book', 'quantity', )  # Display fields in admin list view
    readonly_fields = ('reader', 'book', 'quantity', )  # Make fields read-only
    actions = None  # Disable bulk actions

    def has_add_permission(self, request):
        return False  # Disable "Add" button

    def has_change_permission(self, request, obj=None):
        return False  # Disable editing

    def has_delete_permission(self, request, obj=None):
        return True  # Allow deletion if needed


