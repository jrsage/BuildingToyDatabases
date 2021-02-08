import sqlite3

id = [x for x in range (1,51)]

state = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID',
    'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS',
    'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
    'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV',
    'WI', 'WY' ]

taxRate = [.04, 0, .056, .065, .0725, .0290, .0635, 0, .06, .04, .04, .06,
    .0625, .07, .06, .065, .06, .0445, .055, .0625, .06, .06, .06875, .07,
    .04225, 0, .0475, .05, 0, .06625, .05125, .04, .055, .0685, .0575, .045,
    0, .06, .07, .06, .045, .07, .0625, .061, .053, .06, .06, .065, .05, .04]

data = list(zip(id, state, taxRate))

conn = sqlite3.connect('toyRetail.db')
c = conn.cursor()

c.executemany('INSERT INTO tax VALUES (?, ?, ?)', data)
conn.commit()
conn.close()
