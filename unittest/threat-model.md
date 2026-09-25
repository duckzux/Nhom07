# Threat Model - json_search() (STRIDE)

## (a) Actors / Roles
| Role     | Muc dich goi ham                                     |
|----------|------------------------------------------------------|
| admin    | Toan quyen: xem ca credential (apiKey, managementIp) |
| operator | Van hanh: xem su co + IP thiet bi                    |
| viewer   | Chi xem tom tat su co (issueSummary)                 |
| unknown  | Role khong hop le / gia mao -> bi tu choi            |

## (b) Tai san nhay cam (Assets)
- apiKey: chuoi xac thuc SNMP (truong "apiKey" trong deviceDetails) - Critical
- managementIpAddress: IP quan ly thiet bi trong mang noi bo - High
- issueSummary, category, ...: thong tin van hanh thong thuong - Low

## (c) Trust boundary bi bo qua
Ranh gioi giua "nguoi goi json_search() voi bat ky role nao" va "du lieu tho
tu API giam sat Cisco DNA Center". Neu ham khong kiem tra role -> moi caller
nhan duoc toan bo du lieu, bao gom credential.

## (d) Threats
| ID | STRIDE                 | Mo ta                                                         | Giam thieu              |
|----|------------------------|---------------------------------------------------------------|-------------------------|
| T1 | Information Disclosure | viewer goi json_search("apiKey") -> nhan duoc SNMP credential | Kiem tra role theo policy.py |
| T2 | Information Disclosure | viewer goi json_search("managementIpAddress") -> lo IP noi bo  | Kiem tra role theo policy.py |
| T3 | Elevation of Privilege | Truyen role gia ("root", "hacker") -> vuot kiem tra           | Fail-closed: role la -> tra [] |
