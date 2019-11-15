import pandas as pd
def data_clean():
    df = pd.read_csv('DC_Properties_Clean')
    return df

quadrant = ['Northwest', 'Northeast', 'Southeast', 'Southwest']

ward = ['Ward 1','Ward 2','Ward 3','Ward 4','Ward 5','Ward 6','Ward 7','Ward 8']

neighborhood = ['Old City 1','Columbia Heights','Petworth','Deanwood','Old City 2','Chevy Chase','Brookland',
'Brightwood','Congress Heights','Capitol Hill','Trinidad','Fort Dupont Park','Randle Heights','Woodridge',
'American University','Riggs Park','Hillcrest','Eckington','16th Street Heights','Georgetown','Mt. Pleasant',
'Anacostia','Ledroit Park','Marshall Heights','Lily Ponds','Glover Park','Shepherd Heights','Chillum','Brentwood',
'North Cleveland Park','Michigan Park','Palisades','Cleveland Park','Burleith','Crestwood','Takoma Park','Fort Lincoln',
'Kent','Spring Valley','Forest Hills','Colonial Village','Garfield','Wesley Heights','Berkley','Foxhall','Kalorama','Wakefield',
'Barry Farms','Southwest Waterfront','Observatory Circle','Hawthorne','Foggy Bottom','Woodley','Central-tri 1',
'Massachusetts Avenue Heights']

style = ['2 Story','3 Story','2.5 Story Fin','1 Story','1.5 Story Fin','2.5 Story Unfin',
'Split Level','Split Foyer','4 Story','3.5 Story Fin','1.5 Story Unfin','Default','Bi-Level',
'4.5 Story Fin','3.5 Story Unfin','Vacant','4.5 Story Unfin']

structure = ['Row Inside','Single','Semi-Detached','Row End','Multi','Town Inside','Town End','Default']

extwall = ['Common Brick','Brick/Siding','Vinyl Siding','Wood Siding','Stucco',
'Shingle','Aluminum','Brick Veneer','Brick/Stucco','Brick/Stone','Stone','Face Brick',
'Stone/Siding','Stone Veneer','Stone/Stucco','Hardboard','Concrete','Concrete Block','Metal Siding',
'Stucco Block','Default','Plywood','Adobe','SPlaster']

intwall = ['Hardwood','Hardwood/Carp','Wood Floor','Carpet','Lt Concrete','Ceramic Tile',
'Default','Parquet','Vinyl Comp','Vinyl Sheet','Resiliant','Terrazo']

roof = ['Built Up','Metal- Sms','Comp Shingle','Slate','Neopren','Shake','Clay Tile','Shingle',
'Metal- Pre','Typical','Composition Ro','Metal- Cpr','Water Proof','Wood- FS','Concrete Tile','Concrete']

qualified = ['Q','U']

grade = ['Average','Above Average','Good Quality','Very Good','Excellent',
'Superior','Exceptional-A','Fair Quality','Exceptional-B','Exceptional-C','Low Quality']

condition = ['Good', 'Average', 'Very Good', 'Fair', 'Excellent', 'Poor']

ac = ['Y','N']

heat = ['Air Exchng','Air-Oil','Elec Base Brd','Electric Rad','Evp Cool','Forced Air','Gravity Furnac',
'Hot Water Rad','Ht Pump','Ind Unit','Wall Furnace','Warm Cool','Water Base Brd']

property_type = ['Condominium', 'Apartment', 'Serviced Residence',
       'Terrace/Link House', 'Townhouse', 'Flat', 'Semi-detached House',
       'Bungalow']