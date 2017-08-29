#
# contains list of data used to generate various random data in real world examples
#

DAYS_IN_YEAR = 365
HOURS_IN_YEAR = DAYS_IN_YEAR * 24
MINUTES_IN_YEAR = HOURS_IN_YEAR * 60
MONTHS_IN_YEAR = 12
MAX_DIMENSION = 300
MIN_VALUE = 10000.00
MAX_VALUE = 100000.00

#
# taken from some of my favorite shows, if main character does not have a last name - the name is smith
# only first name and last name (array of arrays)
#
CAST_OF_CHARACTERS = [
    ['Dave', 'Nelson'],          ['Jimmy', 'James'],         ['Matthew', 'Brock'],    ['Lisa', 'Miller'],
    ['Joe', 'Garrelli'],         ['Beth', 'Smith'],          ['Bill', 'McNeal'],      ['Catherine', 'Duke'],
    ['Max', 'Lewis'],            ['Johnny', 'Johnson'],      ['Walt', 'Smith'],       ['Ed', 'Harlow'],
    ['Sandi', 'Angelini'],       ['Melanie', 'Sanders'],     ['Frank', 'Westford'],   ['Bob', 'Costas'],
    ['Don', 'Green'],            ['Jane', 'Robertson'],      ['Scott', 'Barker'],     ['Jerry', 'Seinfeld'],
    ['Ron', 'Jarek'],            ['Tom', 'Baxter'],          ['Marty', 'Jackson'],    ['Eddie', 'Chambers'],
    ['Steve', 'Johnson'],        ['Carl', 'Jackson'],        ['Kevin', 'Sparks'],     ['Adam', 'West'],
    ['John', 'Bush'],            ['James', 'Caan'],          ['Katie', 'Couric'],     ['Matt', 'Lauer'],
    ['Jack', 'Carter'],          ['Allison', 'Blake'],       ['Jo', 'Lupo'],          ['Douglas', 'Fargo'],
    ['Henry', 'Deacon'],         ['Vincent', 'Smith'],       ['Zoe', 'Carter'],       ['Zane', 'Donovan'],
    ['Nathan', 'Stark'],         ['Beverly', 'Barlowe'],     ['Grace', 'Monroe'],     ['Larry', 'Haberman'],
    ['Holly', 'Marten'],         ['Andy', 'Smith'],          ['Jim', 'Taggart'],      ['Kevin', 'Blake'],
    ['Eva', 'Thorne'],           ['Lexi', 'Carter'],         ['John', 'Mansfield'],   ['Michaela', 'Wen'],
    ['Spencer', 'Martin'],       ['Pilar', 'Smith'],         ['William', 'Shaw'],     ['Callie', 'Curie'],
    ['Seth', 'Osbourne'],        ['warren', 'Hughes'],       ['Jenna', 'Blake'],      ['Adam', 'Barlowe'],
    ['Abby', 'Carter'],          ['Noah', 'Drummer'],        ['Julia', 'Golden'],     ['Duncan', 'Smith'],
    ['Nick', 'Fowler'],          ['Walter', 'Perkins'],      ['Anne', 'Young'],       ['Susan', 'Perkins'],
    ['Carol', 'Taylor'],         ['Maria', 'Leonardo'],      ['Jasper', 'Cole'],      ['Brian', 'Perkins'],
    ['Doris', 'Gilmer'],         ['Bruce', 'Manlius'],       ['Irvin', 'Thatcher'],   ['Pierre', 'Fargo'],
    ['Claudia', 'Donovan'],      ['Marcus', 'Blake'],        ['Jason', 'Anderson'],   ['Callister', 'Raynes'],
    ['Jane', 'Harrington'],      ['Andre', 'Sandrov'],       ['Diane', 'Lancaster'],  ['Michael', 'Clark'],
    ['Carl', 'Carlson'],         ['Dylan', 'Hartwell'],      ['Pete', 'Puhlman'],     ['Emily', 'Glenn'],
    ['Christopher', 'Dactylos'], ['Ray', 'Darlton'],         ['Max', 'Dillon'],       ['William', 'Cobb'],
    ['Milton', 'Houk'],          ['Jake', 'Wyatt'],          ['Sam', 'Lovejoy'],      ['Wendy', 'Whiticus'],
    ['Leo', 'Weinbrenner'],      ['Tracy', 'Fox'],           ['Mary-Beth', 'Curtis'], ['Toby', 'Bismark'],
    ['Jacob', 'Stefano'],        ['Lisa', 'Wheeler'],        ['Louis', 'Glazer'],     ['Walter', 'Perkins'],
    ['Belle', 'St John'],        ['Paul', 'Suenos'],         ['Aaron', 'Finn'],       ['Steven', 'Whiticus'],
    ['Teri', 'Wallace'],         ['Sebastian', 'Marx'],      ['Ethan', 'Edison'],     ['Bella', 'Pagani'],
    ['Yuri', 'Gregor'],          ['H.J', 'Johnson'],         ['Norman', 'Gregor'],    ['Judy', 'Stone'],
    ['Derek', 'Bowers'],         ['Lily', 'Morgan'],         ['Ryan', 'Brock'],       ['Bob', 'Stone'],
    ['Eileen', 'Michaels'],      ['Rick', 'Wallace'],        ['Tanya', 'Zimmer'],     ['Kevin', 'Blake'],
    ['Bob', 'Nobb'],             ['Mark', 'Timmons'],        ['Neil', 'Baxter'],      ['Jessica', 'Lansky'],
    ['Pete', 'Lattimer'],        ['Myka', 'Bering'],         ['Artie', 'Nielson'],    ['Claudia', 'Donovan'],
    ['Leena', 'Smith'],          ['Steve', 'Jinks'],         ['Irene', 'Frederic'],   ['H.G', 'Wells'],
    ['Daniel', 'Dickenson'],     ['Adwin', 'Kosan'],         ['Marcus', 'Diamond'],   ['James', 'MacPherson'],
    ['Adrian', 'Smith'],         ['Kelly', 'Hernandez'],     ['Abigail', 'Chow'],     ['Jane', 'Lattimer'],
    ['Vanessa', 'Calder'],       ['Benedict', 'Valda'],      ['Joshua', 'Donovan'],   ['Walter', 'Sykes'],
    ['Chorlotte', 'Dupres'],     ['Sally', 'Stukowski'],     ['Hugo', 'Miller'],      ['Nick', 'Powell'],
    ['Sam', 'Martino'],          ['Claire', 'Donovan'],      ['Tyler', 'Struhl'],     ['Kate', 'Logan'],
    ['Rebecca', 'St Clair'],     ['Douglas', 'Fargo'],       ['Amanda', 'Lattimer'],  ['Jeannie', 'Bering'],
    ['Rebecca', 'St Claire'],    ['Walter', 'Sykes'],        ['Bonnie', 'Belski'],    ['Izzy', 'Weisfelt'],
    ['Lily', 'Abbott'],          ['Liam', 'Napier'],         ['Gary', 'Whitman'],     ['Gilbert', 'Radburn'],
    ['Jesslyn', 'Henjik'],       ['Larry', 'Newley'],        ['Lauren', 'Andrews'],   ['Mike', 'Madden'],
    ['Emma', 'Jinks'],           ['Jesse', 'Ashton'],        ['Autumn', 'Radnor'],    ['Arnold', 'Cassell'],
    ['Nana', 'Hernandez'],       ['Emily', 'Krueger'],       ['Jillian', 'Whitman'],  ['Eric', 'Marsden'],
    ['Jeff', 'Weaver'],          ['Warren', 'Bering'],       ['John', 'Hill'],        ['Kurt', 'Smoller'],
    ['Charlie', 'Martin'],       ['Michael', 'Martin'],      ['Dwayne', 'Maddox'],    ['Cody', 'Bell'],
    ['Ethan', 'Ellis'],          ['Judy', 'Giltoy'],         ['Joe', 'Barton'],       ['Evan', 'Smith'],
    ['Rebecca', 'Carson'],       ['Janice', 'Mallow'],       ['Diane', 'Hewlett'],    ['Scott', 'Mohr'],
    ['Alice', 'Liddell'],        ['Stephanie', 'Goodison'],  ['Reggie', 'Hinton'],    ['Corinne', 'Huggins'],
    ['Jonah', 'Raitt'],          ['Damian', 'Jardin'],       ['Garry', 'Gross'],      ['Lenny', 'Malone'],
    ['Amy', 'Gillian'],          ['Zach', 'Adanto'],         ['Lester', 'Holt'],      ['Brady', 'Miller'],
    ['Deb', 'Staley'],           ['Larry', 'Kemp'],          ['Anthony', 'Bishop'],   ['Thomas', 'Roberts'],
    ['Rick', 'Davis'],           ['Lisa', 'Da Vinci'],       ['Jed', 'Fissel'],       ['William', 'Freitag'],
    ['Beth', 'Raitt'],           ['Aaron', 'Sawyer'],        ['Gibson', 'Rice'],      ['Gil', 'Moorpark'],
    ['Ed', 'Schultz'],           ['Christina', 'Robertson'], ['Val', 'Preston'],      ['Terry', 'Chambers'],
    ['Ed', 'Marzotto'],          ['Bobby', 'Busecki'],       ['Jeff', 'Canning'],     ['Geoffery', 'Cedolia'],
    ['Manuel', 'Flores'],        ['Jerry', 'Hoffler'],       ['Nina', 'Golden'],      ['Hank', 'Siskel'],
    ['Joel', 'Lambeth'],         ['Ritchie', 'Purcell'],     ['Cody', 'Thomas'],      ['Tamara', 'Resnick'],
    ['Lee', 'Donaldson'],        ['Isabella', 'Fuentes'],    ['Buck', 'Mendell'],     ['Joe', 'Sweetwood'],
    ['Charles', 'Well'],         ['Kevin', 'Munroe'],        ['Colin', 'Shreve'],     ['Courtney', 'Moore'],
    ['Sam', 'Garity'],           ['Anja', 'Steinbruck'],     ['Barry', 'Byck'],       ['Rex', 'Simmons'],
    ['Haddon', 'Lockhart'],      ['Ricky', 'Johnson'],       ['Caspian', 'Barnabas'], ['Kyle', 'Barton'],
    ['Charlie', 'Battes'],       ['Regent', 'Gans'],         ['Choi', 'Pak'],         ['Jeff', 'Russell'],
    ['Will', 'Fox'],             ['John', 'Donley'],         ['Philo', 'Farnsworth'], ['Sutton', 'Harris'],
    ['Daniel', 'Varley'],        ['Halley', 'Newell'],       ['Eric', 'Bell'],        ['Lisa', 'Bernardo'],
    ['Johann', 'Steinbruck'],    ['Charlie', 'Bell'],        ['Jonah', 'Roth'],       ['Isaac', 'Weisfelt'],
    ['Liam', 'McShane'],         ['Jeff', 'McMasters'],      ['Daniel', 'Varley'],    ['Philip', 'Petrov'],
    ['Karl', 'Steinbruck'],      ['Tim', 'Watts'],           ['Anthony', 'Seklir'],   ['Laura', 'Roth'],
    ['Gavin', 'Tager'],          ['Greg', 'Permut'],         ['Minnie', 'Harris'],    ['Nora', 'Varley'],
    ['Monica', 'Hopper'],        ['Lenny', 'Bukowski'],      ['Karl', 'Irving'],      ['Donny', 'Shultz'],
    ['Charlie', 'Stanton'],      ['Jason', 'Kinser'],        ['Peg', 'Myer'],         ['Gwen', 'Ashton'],
    ['Karen', 'Miller'],         ['Owen', 'Larsen'],         ['Jordan', 'Tivoli'],    ['Gerry', 'Labelle'],
    ['Rose', 'Meyer'],           ['Hank', 'Conway'],         ['Adam', 'Griff'],       ['Doug', 'Varley'],
    ['Vincent', 'Crowley'],      ['Janet', 'Conway'],        ['Nancy', 'Malloy'],     ['Julia', 'Helmsworth'],
    ['Ralph', 'Brunsky'],        ['Jeff', 'Green'],          ['Justine', 'Pounder'],  ['Gordon', 'Letanik'],
    ['Chet', 'Greenfield'],      ['Lorna', 'Soliday'],       ['Grace', 'Ellen'],      ['Jake', 'Stone'],
    ['Cassandra', 'Cillian'],    ['Ezekiel', 'Jones'],       ['Eve', 'Baird'],        ['Flynn', 'Carsen']
]

INTERNET_DOMAINS = [
    'google.com',   'gmail.com',     'yahoo.com',    'msn.com',     'microsoft.com', '10gen.com',
    'mongodb.com',  'aol.com',       'excite.com',   'lycos.com',   'usa.net',       'netscape.net',
    'hotmail.com',  'live.com',      'juno.com',     'netzero.com', 'fastmail.com',  'runbox.com',
    'postmark.com', 'planetall.com', 'poboxes.info', 'uunet.com',   'cern.ch',       'mail.com'
]

REPS = [
    '*',   'MDZ', 'PTL', 'PNO', 'POA', 'MRS', 'MGX', 'M3C', 'XVK', 'PJD', 'PLS', 'PFW', 'TLZ', 'P44', 'P57',
    'IQU', 'PJM', 'M9D', 'C08', 'MZB', 'PV8', 'PWB', 'P9K', 'MFH', 'COR'
]

ACCT_TYPES = [
    '*', 'Single', 'Joint', 'IRA', 'Trust', 'Roth IRA', 'Rollover IRA'
]

ACCT_STATUSES = [
    '*', 'Existing', 'Closures', 'New'
]

STATES = [
    '*',  'CT', 'NB', 'NH', 'SC', 'MB', 'MT', 'OH', 'NE', 'NC', 'LA', 'MD', 'NF', 'MA', 'SD', 'NM', 'NT',
    'IN', 'ME', 'NV', 'NU', 'AR', 'FL', 'IA', 'DE', 'TN', 'TX', 'AZ', 'DC', 'MN', 'MS', 'NJ', 'ND', 'GA'
]

DOB_YRS = [
    '*',    '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969',
    '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979',
    '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989'
]

DIRECTIONS = ['In', 'Out', '*']

