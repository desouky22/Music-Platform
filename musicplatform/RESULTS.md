# 1- Create some artists

    from artists.models import Artist
    from albums.models import Album
    artist1 = Artist()
    artist1.stage_name="Raze"
    artist1.social_link="https://www.google.com/raze"
    artist1.save()

    artist2 = Artist()
    artist2.stage_name="Brimstone"
    artist2.social_link="https://www.google.com/Brim"
    artist2.save()

    artist3 = Artist()
    artist3.stage_name="Sage"
    artist3.social_link="https://www.google.com/Sage"
    artist3.save()

    artist4 = Artist()
    artist4.stage_name="Astra"
    artist4.social_link="https://www.google.com/astra"
    artist4.save()

# 2- List down all artists

    Artist.objects.all()

# 3- List down all artists sorted by name

    Artist.objects.all().order_by('stage_name')

# 4- List down all artists whose name starts with a

    Artist.objects.filter(stage_name\_\_startswith='a')

# 5- in 2 different ways, create some albums and assign them to any artists

    (a)
    from artists.models import Artist
    from albums.models import Album
    from datetime import datetime
    album1 = Album()
    album1.name="Breeze"
    artist1=Artist.objects.get(pk=1)
    album1.artist=artist1
    album1.release_date=datetime(2019,1,1)
    album1.cost=100
    album1.save()


    (b)
    from artists.models import Artist
    from albums.models import Album
    from datetime import datetime
    album2 = Album.objects.create(artist=Artist.objects.get(pk=2), name="IceBox", release_date=datetime(2020,5,5), cost=200)
    album3 = Album.objects.create(artist=Artist.objects.get(pk=2), name="Ascent1", release_date=datetime(2022,10,6), cost=250)
    album4 = Album.objects.create(artist=Artist.objects.get(pk=2), name="Ascent2", release_date=datetime(2022,10,6), cost=250)
    album5 = Album.objects.create(artist=Artist.objects.get(pk=2), name="Bind", release_date=datetime(2022,10,6), cost=250)
    album6 = Album.objects.create(artist=Artist.objects.get(pk=2), name="Fracture", release_date=datetime(2022,10,6), cost=250)

# 6- get the latest released album

    latest_album = Album.objects.all().order_by('-release_date').first()

# 7- get all albums released before today

    before_today=Album.objects.filter(release_date__day__lt=datetime.now().day)

# 8- get all albums released today or before but not after today

    before_or_today=Album.objects.filter(release_date__day__lte=datetime.now().day)

# 9- count the total number of albums (hint: count in an optimized manner)

    Album.objects.count()

# 10- in 2 different ways, for each artist, list down all of his/her albums (hint: use objects manager and use the related object reference)

    (a) => this is with better performance because of using join in
    q=Artist.objects.prefetch_related('album_set').all()
    lst=[]
    for artist in q:
        lst.append((artist,artist.album_set.all()))

    (b)
    lst=[]
    for artist in Artist.objects.all():
        albums = Album.objects.filter(artist_id=artist.id)
        lst.append((artist, albums))

# 11- list down all albums ordered by cost then by name (cost has the higher priority)

    Album.objects.all().order_by('cost', 'name')
