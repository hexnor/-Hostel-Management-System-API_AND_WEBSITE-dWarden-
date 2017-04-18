# obj=College.class FilterCollegeByStateList(APIView):

#defaulttoken='token 6d793111878d993460b68dcb78eb618adf20883c'
defaulttoken='token ce3fe9a203703c7ea3da8727ff8fbafec8ddbf44'

def checkauth(usertoken,defaulttoken):
    if usertoken==defaulttoken:
        return 1
    else:
        return 0
#displaying extra fields