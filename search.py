import itunes
import sys

track = itunes.search_song(" ".join(sys.argv[1:]))[0]
album = track.get_album()

title = track.get_name()
album_title = album.get_name()
artists = track.get_artist().get_name()
release_date = track.get_release_date()
track_number = track.get_disc_number()
total_tracks = album.get_track_count()
genre = track.get_genre()
album_artist = album.get_artist().get_name()
disc_number = track.get_disc_number()
total_discs = 1
duration = track.get_duration()
minutes = int(duration / 60)
seconds = int(duration / 60 % 1 * 100)

print "Title: " + title
print "Album: " + album_title
print "Artists: " + artists
print "Release Date: " + release_date 
print "Track number: " + str(track_number) + "/" + str(total_tracks)
print "Genre: " + genre
print "Album Artist: " + album_artist
print "Disc Number: " + str(disc_number) + "/" + str(total_discs)
print "Duration: " + str(minutes) + "m " + str(seconds) + "s"

print "\nAvailable Artworks:"
artworks = track.get_artwork()
for index, artwork in enumerate(artworks):
	print "Artwork #" + str(index + 1) + " (" + str(artwork) + "x" + str(artwork) + "):"
	print artworks[artwork] + "\n"