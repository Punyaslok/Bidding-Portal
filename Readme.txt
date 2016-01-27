IIIT Bidding Portal


A bidding portal targeted mainly at college students looking to buy/sell their stuff to other students within the college. Especially helps graduating students sell some of their belongings like bicycles before leaving.

Platform : web2py

Features :
    1.  Real-time updates on each page about current bidding price.
    2.  Timed bidding, i.e. bidding shuts down automatically after deadline expires.
    3.  After bidding closes, a computer generated e-mail is sent automatically to the winning bidder.

Deployment Link : punyaslokpattnaik.pythonanywhere.com/Bidding_Portal



BUG 1 : Live Search Bar fails to work properly on an individual product's page. Works fine on home and sell pages.

BUG 2 : Live Bidding Information is displayed ONLY after the first bid is placed. It doesn't change from 0 bids to 1 bid. But if the page initially has >=1 bids, it works correctly. ex - if 4th bid is being displayed and a new bid, is made, the bid value will change to the 5th bid.
