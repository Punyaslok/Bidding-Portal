@auth.requires_login()
def ref_func_bid_value():
    return dict(retval=(db(db.product_list.id==request.args[0]).select())[0])

@auth.requires_login()
def ref_func_name_details():
    return dict(retval=(db(db.product_list.id==request.args[0]).select())[0])


@auth.requires_login()
def searchresults():
    searchstring = args[0]
    rows = db(db.product_list).select(orderby=~db.product_list.bid_count)
    return locals()
