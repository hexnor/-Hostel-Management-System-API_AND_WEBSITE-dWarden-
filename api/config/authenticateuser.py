# obj=College.class FilterCollegeByStateList(APIView):

#defaulttoken='token 6d793111878d993460b68dcb78eb618adf20883c'
defaulttoken='token 7a8c23b3442a54a99b4c2a4441dcc2b79f4b05eb'

def checkauth(usertoken,defaulttoken):
    if usertoken==defaulttoken:
        return 1
    else:
        return 0
#displaying extra fields