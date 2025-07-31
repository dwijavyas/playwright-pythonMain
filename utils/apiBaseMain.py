from playwright.sync_api import Playwright

ordersPayLoad={"orders":[{"country":"India","productOrderedId":"67a8dde5c0d3e6622a297cc8"}]}

class APIUtils:

    #to get the token variable, need to login and get the token from it
    #every login has its own token generated
    def getToken(self, playwright: Playwright, user_credentials, url_data):

        #
        user_email = user_credentials["user_email"]
        user_password = user_credentials["user_password"]

        api_request_context = playwright.request.new_context(base_url=url_data["url1"])
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail":user_email,"userPassword":user_password})
        
        assert response.ok
        print(response.json())
        #take json response into 1 dict and extract "token" at whatever index 
        responseBody = response.json()
        return responseBody["token"]


    def createOrder(self, playwright: Playwright, user_credentials, url_data):
        token = self.getToken(playwright, user_credentials, url_data)
        api_request_context = playwright.request.new_context(base_url=url_data["url1"])
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=ordersPayLoad,
                                            headers={"Authorization": token,
                                                     "Content-Type": "application/json"})
        
        print(response.json())
        response_body = response.json()
        #extracting order id from the json response, at 0 index bcz order id is in a list and there can be multiple orders in the list
        orderID = response_body["orders"][0]
        return orderID
        