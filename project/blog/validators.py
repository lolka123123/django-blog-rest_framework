from django.core.validators import ValidationError

def validator_file_size(file):
    max_size_kb = 2500

    # if file.size > max_size_kb * 1024:
    #     raise ValidationError(f'Файл не может быть более {max_size_kb}KB!')