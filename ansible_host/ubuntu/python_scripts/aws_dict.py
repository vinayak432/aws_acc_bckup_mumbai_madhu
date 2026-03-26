policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::11112222333:oidc-provider/auth.example.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "auth.example.com:sub": "Administrator",
                    "auth.example.com:aud": "MyappWebIdentity"
                }
            }
        }
    ]
}

print("*******keys*****")
for key in policy.keys():
    print(key)

print("********values******")
for value in policy.values():
    print(value)

for key, value in policy["Statement"][0]["Principal"].items():
    print("Key:", key)
    print("Value:", value)

