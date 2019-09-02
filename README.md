# zillow-scraper-by-zpid
Retrieve 125+ attributes of homes and/or rental properties by zpid

Each Zillow property has a ZPID. One way to retrieve this id, is to copy it in the url from a property of interest.  
Zillow used to provide an API to collect these id's, where you would then be able to loop through them (on a timed interval),
but it's been a while since I've used those.

1. You will need python requests and lxml to run this code.  A list of imported modules can be found in the functions file.
2. Copy both files into a local directory and open the file with requests in the title.
3. Replace the ZPID there with one or loop through a set of zpids
4. The get_property function will print out the data that it is collecting and output it to a csv file, named by zpid.


EXAMPLES:

get_property("2083982936")

###############################################

zpids = ['123', '456']

for zpid in zpids:
  get_property(zpid)



EXAMPLE OUTPUT (for some collected attributes):

id UHJvcGVydHk6MjA4Mzk4MjkzNg==
isFeatured False
zpid 2083982936
city Woodland Park
state NJ
streetAddress 43 Mereline Ave
zipcode 07424
neighborhood None
community None
subdivision None
homeStatus FOR_RENT
isListingClaimedByCurrentSignedInUser False
isCurrentSignedInAgentResponsible False
solarPotential None
brokerId 14066
latitude 40.890138
longitude -74.192779
countyFIPS None
parcelId
currency USD
homeType SINGLE_FAMILY
Date available None
Type Single Family
Cooling Central
Heating Baseboard
Pets No
Parking 6 spaces
Laundry None
Deposit & fees None
Price/sqft None
description Large Custom home offers 5 Bedrooms and 4 baths. Features include Central Air, Multi zone heat, hardwood floors, Kitchen with granite and Center Island Stove, 2 car garage, large
backyard. As-Is.
whatILove None
isListedByOwner False
contingentListingType None
building None
timeOnZillow 3 hours
pageViewCount 463
favoriteCount 6
hdpUrl /homedetails/43-Mereline-Ave-Woodland-Park-NJ-07424/2083982936_zpid/
desktopWebHdpImageLink https://photos.zillowstatic.com/p_h/IS3ny02vzw3o5k1000000000.jpg
price 3000
brokerageName REALTY EXECUTIVES EXCEPTIONAL
enhancedBrokerImageUrl https://photos.zillowstatic.com/l_c/IS6yh61bz2xu570000000000.jpg
bathrooms 4
bedrooms 5
