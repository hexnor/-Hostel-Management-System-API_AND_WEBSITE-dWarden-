# obj=College.class FilterCollegeByStateList(APIView):

#defaulttoken='token 6d793111878d993460b68dcb78eb618adf20883c'


def checkauth(usertoken,defaulttoken):
    if usertoken==defaulttoken:
        return 1
    else:
        return 0
#displaying extra fields
