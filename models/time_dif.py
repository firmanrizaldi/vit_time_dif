
from odoo import api, fields, models
import time
import datetime
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)


class time_diff(models.Model):
    _name = 'vit.time_diff'
    
    
    
    depart = fields.Datetime(
        string='Departure',
        default=lambda self: time.strftime("%Y-%m-%d"), 
    )
    
    
    arrive = fields.Datetime(
        string='Arrival',
        default=lambda self: time.strftime("%Y-%m-%d"), 
    )
    
    
    time_diff = fields.Char(
        string='Time Diff',
            compute='_calc_time' 
            )
        
        
    @api.depends('depart','arrive')
    def _calc_time(self):
            
        for record in self:
            
            
            depart_obj = datetime.strptime( str(record.depart), "%Y-%m-%d %H:%M:%S")
            arrive_obj = datetime.strptime( str(record.arrive), "%Y-%m-%d %H:%M:%S")
            
        # import pdb; pdb.set_trace()
            delta = arrive_obj - depart_obj
            
            secs = delta.total_seconds()
            
            d = divmod(secs, 86400)
            _logger.warning(d)
            h = divmod(d[1], 3600)
            _logger.warning(h)
            m = divmod(h[1], 60)
            _logger.warning(m)
            
            if d[0] > 0 :
                ret = "%sd %sh %sm"%(int(d[0]), int(h[0]), int(m[0]))
            else:
                ret = "%sh %sm"%(int(h[0]), int(m[0]))
            
            
            record.time_diff = ret
                
                
    
