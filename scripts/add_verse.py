# Inside the Django shell
from bible.models import Verse


verse1 = Verse.objects.create(
    book="John",
    chapter=3,
    verse=17,
)
print(verse1)
john_16 = Verse.objects.get(book="John", chapter=3, verse=17)
print(john_16.verse)
