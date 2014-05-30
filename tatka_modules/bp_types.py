# bp_types.py
# Data types for BackProj

class Trigger():
    def __init__(self,
                 eventid=None,
                 x=None, y=None, z=None,
                 i=None, j=None, k=None,
                 max_grid=None,
                 beg_win=None, end_win=None,
                 center_win=None):
        self.x = x
        self.y = y
        self.z = z
        self.i = i
        self.j = j
        self.k = k
        self.max_grid = max_grid
        self.beg_win = beg_win
        self.end_win = end_win
        self.center_win = center_win
        self.lat = None
        self.lon = None
        self.origin_time = None

    def __str__(self):
        s = 'X %s ' % self.x
        s += 'Y %s ' % self.y
        s += 'Z %s ' % self.z
        s += 'MaxStack %s ' % (self.max_grid)
        s += 'BEG %s ' % self.beg_win
        s += 'END %s ' % self.end_win
        if (self.lat is not None and
            self.lon is not None):
            s += ' LAT %s LON %s' % (self.lat, self.lon)
        if (self.origin_time is not None):
            s += ' T_ORIG %s' % (self.origin_time)
        return s
    
class Pick():
    def __init__(self,
                 evtid=None,station=None,
                 arrival_type=None):
        
        self.evtid = evtid
        self.station = station
        self.arrival_type = arrival_type
        self.theor_time = []

    def __str__(self):
        s = ''
        for sta,tt in zip(self.station,self.theor_time):
            s += '  %s ' % sta
            s += '  %s ' % self.arrival_type
            s += '  %s ' % tt
            s += '\n'
        return s
