from container import Container
from pprint import pprint
cont = Container()

# single
#data = {"bins": [{"w": 10, "h": 10, "d": 10, "max_wg": 0, "id": "Bin1"}], "items": [{"w": 5, "h": 3, "d": 2, "q": 2, "vr": 1, "wg": 0, "id": "Item1"},{"w": 3, "h": 3, "d": 3, "q": 3, "vr": 1, "wg": 0, "id": "Item2"}], "params": {"images_background_color": "255,255,255", "images_bin_border_color": "59,59,59", "images_bin_fill_color": "230,230,230", "images_item_border_color": "214,79,79", "images_item_fill_color": "177,14,14", "images_item_back_border_color": "215,103,103", "images_sbs_last_item_fill_color": "99,93,93", "images_sbs_last_item_border_color": "145,133,133", "images_width": 100, "images_height": 100, "images_source": "file", "images_sbs": 1, "stats": 1, "item_coordinates": 1, "images_complete": 1, "images_separated": 1}}
#cont.single(data)

# multi 
#data = {"bins": [{"w": 5, "h": 5, "d": 5, "max_wg": 0, "id": "Bin1", "q": None},{"w": 3, "h": 3, "d": 3, "max_wg": 0, "id": "Bin2"}], "items": [{"w": 5, "h": 3, "d": 2, "q": 2, "vr": 1, "wg": 0, "id": "Item1"},{"w": 3, "h": 3, "d": 3, "q": 3, "vr": 1, "wg": 0, "id": "Item2"}], "params": {"images_background_color": "255,255,255", "images_bin_border_color": "59,59,59", "images_bin_fill_color": "230,230,230", "images_item_border_color": "214,79,79", "images_item_fill_color": "177,14,14", "images_item_back_border_color": "215,103,103", "images_sbs_last_item_fill_color": "99,93,93", "images_sbs_last_item_border_color": "145,133,133", "images_width": 100, "images_height": 100, "images_source": "file", "images_sbs": 1, "stats": 1, "item_coordinates": 1, "images_complete": 1, "images_separated": 1}}
#pprint(cont.multi(data))

# find
#data = {"bins": [{"w": 5, "h": 0, "d": 5, "id": "Bin1", "find": "h"},{"w": 3, "h": 30, "d": 3, "id": "Bin2", "find": "h"}], "items": [{"w": 5, "h": 3, "d": 2, "q": 2, "vr": 1, "id": "Item1"},{"w": 3, "h": 3, "d": 3, "q": 3, "vr": 1, "id": "Item2"}], "params": {"images_background_color": "255,255,255", "images_bin_border_color": "59,59,59", "images_bin_fill_color": "230,230,230", "images_item_border_color": "214,79,79", "images_item_fill_color": "177,14,14", "images_item_back_border_color": "215,103,103", "images_sbs_last_item_fill_color": "99,93,93", "images_sbs_last_item_border_color": "145,133,133", "images_width": 100, "images_height": 100, "images_source": "file", "images_sbs": 1, "stats": 1, "item_coordinates": 1, "images_complete": 1, "images_separated": 1}}
#pprint(cont.find(data))

# adjustment
#data = {"bins": [{"w": 0, "h": 0, "d": 0, "id": "Bin1"}], "items": [{"w": 5, "h": 3, "d": 2, "q": 2, "vr": 1, "id": "Item1"},{"w": 3, "h": 3, "d": 3, "q": 3, "vr": 1, "id": "Item2"}], "params": {"images_background_color": "255,255,255", "images_bin_border_color": "59,59,59", "images_bin_fill_color": "230,230,230", "images_item_border_color": "214,79,79", "images_item_fill_color": "177,14,14", "images_item_back_border_color": "215,103,103", "images_sbs_last_item_fill_color": "99,93,93", "images_sbs_last_item_border_color": "145,133,133", "images_width": 100, "images_height": 100, "images_source": "file", "images_sbs": 1, "stats": 1, "item_coordinates": 1, "images_complete": 1, "images_separated": 1}}
#pprint(cont.adjustment(data))

# maximum
#data = {"bins": [{"w": 5, "h": 5, "d": 5, "max_wg": 0, "id": "Bin1"},{"w": 3, "h": 3, "d": 3, "max_wg": 0, "id": "Bin2"}], "items": [{"w": 5, "h": 3, "d": 2, "vr": 1, "wg": 0, "id": "Item1"},{"w": 3, "h": 3, "d": 3, "vr": 1, "wg": 0, "id": "Item2"}], "params": {"images_background_color": "255,255,255", "images_bin_border_color": "59,59,59", "images_bin_fill_color": "230,230,230", "images_item_border_color": "214,79,79", "images_item_fill_color": "177,14,14", "images_item_back_border_color": "215,103,103", "images_sbs_last_item_fill_color": "99,93,93", "images_sbs_last_item_border_color": "145,133,133", "images_width": 100, "images_height": 100, "images_source": "file", "images_sbs": 1, "stats": 1, "item_coordinates": 1, "images_complete": 1, "images_separated": 1}}
#pprint(cont.maximum(data))