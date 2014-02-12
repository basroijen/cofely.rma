from smtplib import SMTPRecipientsRefused
from Products.CMFCore.utils import getToolByName
from email import message_from_string
from zope.component import getUtility

def mailStatusUpdate(self, REQUEST, mail_template=None):
    """ Email a forgotten password to a member.
    
    o Raise an exception if user ID is not found.
    
    """
    utils = getToolByName(self, 'plone_utils')
    if not utils.validateSingleEmailAddress(email):
        raise ValueError, 'The email address did not validate'
    try:
        encoding = getUtility(ISiteRoot).getProperty('email_charset', 'utf-8')
 #       if mail_template is None:
 #           mail_template = self.rma_mail_template

#        mail_text = mail_template(self,
#                                  REQUEST,
#                                  member=member,
#                                  member_id=forgotten_userid,
#                                  member_email=email,
#                                  charset=email_charset,
#                                  reset=reset)
        # mail_text is a string
        mail_text = 'From: "Bas Roijen" <bas.roijen@cofely-gdfsuez.nl>\nTo: bas.roijen@cofely-gdfsuez.nl\nSubject: Aanvraag wachtwoord wijzigen\nPrecedence: bulk\n\nIemand heeft gevraagd om het wachtwoord van uw account op \'Een korte titel voor de website. Deze zal worden getoond in de titel van het browser scherm op iedere pagina.\' te wijzigen. Als u dit niet bent geweest, dan kunt u deze e-mail negeren. Als u door wilt gaan en uw wachtwoord wilt wijzigen, bezoek dan dit adres: http://localhost:8080/Plone/passwordreset/085f417a24ec7ea47616d4cafe41365d\n\n(Deze link is 168 uur geldig)\n\nAls deze email voor u onverwacht komt, kunt u deze negeren. Uw wachtwoord is niet gewijzigd. Verzoek gemaakt vanaf IP adres \n\n'

        if isinstance(mail_text, unicode):
            mail_text = mail_text.encode(encoding)

        message_obj = message_from_string(mail_text)
        subject = message_obj['Subject']
        m_to = message_obj['To']
        m_from = message_obj['From']
        host = getToolByName(self, 'MailHost')

        host.send( mail_text, m_to, m_from, subject=subject,
                   charset=encoding)
    except SMTPRecipientsRefused:
        # Don't disclose email address on failure
        raise SMTPRecipientsRefused(_(u'Recipient address rejected by server.'))
