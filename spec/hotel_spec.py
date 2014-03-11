import unittest
from should_dsl import should
from hotel import Hotel

class Hotel_spec(unittest.TestCase):

    def it_creates_um_object_hotel(self):
        hotel = Hotel ('001','Softel Jequitimar','www.sbt.com.br','1127338977','R$ 300','3')
        hotel.codHotel |should| equal_to ('001')
        hotel.hotel |should| equal_to ('Softel Jequitimar')
        hotel.site |should| equal_to ('www.sbt.com.br')
        hotel.telefone |should| equal_to ('1127338977')
        hotel.diaria |should| equal_to ('R$ 300')
        hotel.diaHospedado |should| equal_to ('3')

    def it_update(self):
    	hotel = Hotel ('001','Softel Jequitimar','www.sbt.com.br','1127338977','R$ 300','3')
    	hotel.update('Comfort Hotel', 'www.comfort.com.br', '99999999')
    	hotel.hotel |should| equal_to('Comfort Hotel')
    	hotel.site |should| equal_to('www.comfort.com.br')
    	hotel.telefone |should| equal_to('9999999')