def send():
    rows = db(db.product_list.status == 'Live').select(orderby=~db.product_list.bid_count)
    for row in rows :
        if row.end_date_time < request.now :
            db(db.product_list.id==row.id).update(status='Expired')
            if row.current_highest_bidder != 'none' :
                rec_email = db(db.auth_user.id == row.current_highest_bidder).select()[0]
                mail.send(to=[rec_email.email],subject='Successfully acquired product.',message='Congratulations '+rec_email.first_name+' '+rec_email.last_name+', you have won the bidding for '+row.product_name+'. You may now contact the seller at his email address.')
            db.commit()
    return 1
from gluon.scheduler import Scheduler
scheduler = Scheduler(db)
