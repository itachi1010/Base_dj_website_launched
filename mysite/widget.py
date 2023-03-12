from django_summernote.widgets import SummernoteWidget

class SummernoteWidgetWithCustomToolbar(SummernoteWidget):
    def summernote_settings(self):
        settings = super().summernote_settings()
        settings['toolbar'] = [
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['insert', ['link', 'picture', 'video']],
            ['table', ['table']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['height', ['height']]
        ]
        return settings