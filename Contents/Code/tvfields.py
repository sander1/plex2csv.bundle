####################################################################################################
#	Helper file for Plex2CSV
# Written by dane22 on the Plex Forums, UKDTOM on GitHub
#
# This one contains the valid fields and attributes for tv-shows
# 
# To disable a field not needed, simply put a # sign in front of the line, and it'll be ommited.
# After above, a PMS restart is sadly req. though
# Note though, that this will be overwritten, if/when this plugin is updated
#
# If level has the number 666 in it, a column named 'PMS Media Path' will
# automaticly be added to the end
####################################################################################################

# Fields that contains a timestamp and should return a date
dateTimeFields = ['addedAt', 'updatedAt', 'lastViewedAt', 'originallyAvailableAt']

# Fields that contains a timestamp and should return a time
timeFields =['duration']

# Levels that only req. a single call towards PMS
singleCall = ['Level 1', 'Level 2', 'Level 3']

# Define rows and element name for level 1 (Single call)
Level_1 = [
	('TV Show ID' , '@ratingKey'),
	('Series Title' , '@grandparentTitle'),
	('Episode Sort Title' , '@titleSort'),
	('Episode Title' , '@title'),
	('Year' , '@year'),
	('Season' , '@parentIndex'),
	('Episode' , '@index'),
	('Content Rating' , '@contentRating'),
	('Summary' , '@summary'),	
	('Rating' , '@rating')
	]

Level_2 = [
		('Studio' , '@studio'),
		('Originally Aired' , '@originallyAvailableAt'),
		('Directors' , 'Director/@tag'),
		('Writers' , 'Writer/@tag'),
		('Duration' , '@duration'),
		('Added' , '@addedAt'),
		('Updated' , '@updatedAt'),
		('Poster url' , '@thumb'),
		('Collection', ''),
		('Locked Fields', 'Field/@name')
	]
	
Level_3 = [
		('Media Video Resolution' , 'Media/@videoResolution'),
		('Media Video Duration' , 'Media/@duration'),
		('Media Video Bitrate' , 'Media/@bitrate'),
		('Media Video Width' , 'Media/@width'),
		('Media Video Height' , 'Media/@height'),
		('Media Video Aspect Ratio' , 'Media/@aspectRatio'),
		('Media Video Audio Channels' , 'Media/@audioChannels'),
		('Media Video Audio Codec' , 'Media/@audioCodec'),
		('Media Video Video Codec' , 'Media/@videoCodec'),
		('Media Video Container' , 'Media/@container'),
		('Media Video FrameRate' , 'Media/@videoFrameRate'),
		('Media Video Profile' , 'Media/@videoProfile'),
		('Media Video Title' , 'Media/@title')
	]

Level_4 = [
		('MetaDB Link' , '@guid'),
		('Part File' , 'Media/Part/@file'),
		('Part Duration' , 'Media/Part/@duration'),
		('Part Size' , 'Media/Part/@size'),
		('Part Size as Bytes' , 'Media/Part/@size'),
		('Part Container' , 'Media/Part/@container'),
		('Part Video Profile' , 'Media/Part/@videoProfile'),
		('Part Optimized for Streaming' , 'Media/Part/@optimizedForStreaming'),
		('Part Indexed' , 'Media/Part/@indexes'),
		('Extras' , 'Extras/@size'),
		('Accessible' , 'Media/Part/@accessible'),	
		('Exists' , 'Media/Part/@exists')	
	]

Level_5 = [
	('Video Stream Title' , 'Media/Part/Stream[@streamType=1]/@title'),
	('Video Stream Default' , 'Media/Part/Stream[@streamType=1]/@default'),
	('Video Stream Codec' , 'Media/Part/Stream[@streamType=1]/@codec'),
	('Video Stream Index' , 'Media/Part/Stream[@streamType=1]/@index'),
	('Video Stream Bitrate' , 'Media/Part/Stream[@streamType=1]/@bitrate'),
	('Video Stream Language' , 'Media/Part/Stream[@streamType=1]/@language'),
	('Video Stream Language Code' , 'Media/Part/Stream[@streamType=1]/@languageCode'),
	('Video Stream Bit Depth' , 'Media/Part/Stream[@streamType=1]/@bitDepth'),
	('Video Stream Cabac' , 'Media/Part/Stream[@streamType=1]/@cabac'),
	('Video Stream Chroma Sub Sampling' , 'Media/Part/Stream[@streamType=1]/@chromaSubsampling'),
	('Video Stream Codec ID' , 'Media/Part/Stream[@streamType=1]/@codecID'),
	('Video Stream Color Range' , 'Media/Part/Stream[@streamType=1]/@colorRange'),
	('Video Stream Color Space' , 'Media/Part/Stream[@streamType=1]/@colorSpace'),
	('Video Stream Duration' , 'Media/Part/Stream[@streamType=1]/@duration'),
	('Video Stream Frame Rate' , 'Media/Part/Stream[@streamType=1]/@frameRate'),
	('Video Stream Frame Rate Mode' , 'Media/Part/Stream[@streamType=1]/@frameRateMode'),
	('Video Stream Has Scaling Matrix' , 'Media/Part/Stream[@streamType=1]/@hasScalingMatrix'),
	('Video Stream Height' , 'Media/Part/Stream[@streamType=1]/@height'),
	('Video Stream Width' , 'Media/Part/Stream[@streamType=1]/@width'),
	('Video Stream Level' , 'Media/Part/Stream[@streamType=1]/@level'),
	('Video Stream Pixel Format' , 'Media/Part/Stream[@streamType=1]/@pixelFormat'),
	('Video Stream Profile' , 'Media/Part/Stream[@streamType=1]/@profile'),
	('Video Stream Ref Frames' , 'Media/Part/Stream[@streamType=1]/@refFrames'),
	('Video Stream Scan Type' , 'Media/Part/Stream[@streamType=1]/@scanType')
	]

Level_6 = [
	('Audio Stream Selected' , 'Media/Part/Stream[@streamType=2]/@selected'),
	('Audio Stream Default' , 'Media/Part/Stream[@streamType=2]/@default'),
	('Audio Stream Codec' , 'Media/Part/Stream[@streamType=2]/@codec'),
	('Audio Stream Index' , 'Media/Part/Stream[@streamType=2]/@index'),
	('Audio Stream Channels' , 'Media/Part/Stream[@streamType=2]/@channels'),
	('Audio Stream Bitrate' , 'Media/Part/Stream[@streamType=2]/@bitrate'),
	('Audio Stream Language' , 'Media/Part/Stream[@streamType=2]/@language'),
	('Audio Stream Language Code' , 'Media/Part/Stream[@streamType=2]/@languageCode'),
	('Audio Stream Audio Channel Layout' , 'Media/Part/Stream[@streamType=2]/@audioChannelLayout'),
	('Audio Stream Bit Depth' , 'Media/Part/Stream[@streamType=2]/@bitDepth'),
	('Audio Stream Bitrate Mode' , 'Media/Part/Stream[@streamType=2]/@bitrateMode'),
	('Audio Stream Codec ID' , 'Media/Part/Stream[@streamType=2]/@codecID'),
	('Audio Stream Duration' , 'Media/Part/Stream[@streamType=2]/@duration'),
	('Audio Stream Profile' , 'Media/Part/Stream[@streamType=2]/@profile'),
	('Audio Stream Sampling Rate' , 'Media/Part/Stream[@streamType=2]/@samplingRate'),
	('Subtitle Stream Codec' , 'Media/Part/Stream[@streamType=3]/@codec'),
	('Subtitle Stream Forced' , 'Media/Part/Stream[@streamType=3]/@forced'),
	('Subtitle Stream Index' , 'Media/Part/Stream[@streamType=3]/@index'),
	('Subtitle Stream Language' , 'Media/Part/Stream[@streamType=3]/@language'),
	('Subtitle Stream Language Code' , 'Media/Part/Stream[@streamType=3]/@languageCode'),
	('Subtitle Stream Codec ID' , 'Media/Part/Stream[@streamType=3]/@codecID'),
	('Subtitle Stream Format' , 'Media/Part/Stream[@streamType=3]/@format'),
	('Subtitle Stream Title' , 'Media/Part/Stream[@streamType=3]/@title'),
	('Subtitle Stream Selected' , 'Media/Part/Stream[@streamType=3]/@selected')
	]

Level_7 = [
	]

Level_8 = [
	]

Level_9 = [
	]

Level_666 = [
	]

# Define rows and element name for Show Only level 1 (one call for all shows....Note that this level only export on show level!, but is very fast)
Show_1 = [
	('Title' , '@title'),
	('Sort Title' , '@titleSort'),
	('Original Title', '@originalTitle'),
	('Summary' , '@summary'),
	('Originally Aired' , '@originallyAvailableAt'),
	('Year' , '@year'),
	('Rating' , '@rating'),
	('Content Rating' , '@contentRating'),
	('Studio' , '@studio'),
	('Poster url' , '@thumb')
	]

# Define rows and element name for Show Only level 2 (two call for all shows....Note that this level only export on show level!)
Show_2 = [
	('MetaDB Link' , '@guid')
	]

