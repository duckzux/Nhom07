# Security Requirements - json_search()

SR1: Ham chi tra ve ket qua cua key X cho role nam trong POLICY[X] (policy.py).
SR2: apiKey chi duoc tra ve cho role "admin".
SR3: managementIpAddress chi duoc tra ve cho "admin" va "operator".
SR4: issueSummary duoc tra ve cho "admin", "operator", "viewer".
SR5: Role khong nam trong danh sach hop le (admin/operator/viewer) -> tra ve [].
SR6: Khong truyen role -> mac dinh la viewer (least privilege).
