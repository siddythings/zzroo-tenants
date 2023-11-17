import os
import requests
import json


class APICls:
    def backend_call(self, end_point, request_obj):
        URL = os.getenv("zzrooBackendApp", "") + end_point
        headers = {"Content-Type": "application/json",
                   "request-id": "qwerty", "email": "qwerty", "account-id": "qwerty"}
        print(request_obj, "request obj")
        # response = requests.post(url=URL, data=json.dumps(
        #     request_obj), headers=headers)
        # responseCode = response.status_code
        responseCode = 200
        response = {
            "status": "success",
            "message": "OTP sent successfully"
        }
        if responseCode == 200:
            response_data = response
            print(response_data)
            return response_data
        else:
            if response.json():
                return response.json()
            raise ('Error occurred while updating bill')

    def send_otp(self, request_obj):
        end_point = "/send_otp"
        self.backend_call(end_point, request_obj)

    def otp_validation(self, request_obj):
        end_point = "/otp_validation"
        self.backend_call(end_point, request_obj)

    def user_profle(self, request_obj):
        end_point = "/user_profle"
        self.backend_call(end_point, request_obj)


API = APICls()
