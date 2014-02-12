About this product
==================

This product makes it possible for customers to register on the website and add an RMA.
Customers are able to follow the status of their RMA.
Employees can see all RMA's and add status updates.

Tested on:
* Plone 4.0.1 (Unified installer)

How to use ?
============

After installing the package, restart Zope.

Go to Plone configuration menu "Add/Remove product", select the product and install it.

Two new content types are added: 'RMA' and 'RMA folder'.

Have fun !

What does this product add to a default Plone site?
===================================================

* Two content types: 'RMA' and 'RMA folder'.
* Four new roles: 'Customer', 'Employee general', 'Warehouse employee' and 'Mechanic'.
* New fields for the member registration
* A custom workflow for the new content types
* A portlet showing new RMA's

Todo
====

* Include tests
* Add mailing option
* Make producttype dropdown list configurable
* Configure roles correctly, only employee is used
* Create portlet
* And probably much more!

