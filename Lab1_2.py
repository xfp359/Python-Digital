pages = 100
lines_per_page = 50
characters_per_line = 25
bytes_per_character = 4

total_characters = pages * lines_per_page * characters_per_line
total_information_volume_in_bytes = total_characters * bytes_per_character
diskette_volume_in_mb = 1.44
diskette_volume_in_bytes = diskette_volume_in_mb * 1024 * 1024
books = diskette_volume_in_bytes // total_information_volume_in_bytes
print(f"Количество книг, которые можно поместить на дискету: {books}")