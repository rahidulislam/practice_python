from enum import Enum,auto
from pprint import pprint
from functools import total_ordering
import json
import enum


class Color(Enum):
    RED = 1
    CRIMSON = 1
    GREEN = 2
    BLUE = 3


print(type(Color.RED))

print(isinstance(Color.RED, Color))
print(Color.RED.name, Color.RED.value)

# if Color.YELLOW in Color:
#     print("Color.RED is a member of Color")
# else:
#     print('Not Found')

if Color.RED == 1:
    print("Color.RED == 1")
else:
    print("Color.RED != 1")

print(Color.RED == Color.CRIMSON)
print(Color["RED"])
print(Color(1))
print(Color.RED == Color(1))

for color in Color:
    print(color)
print(list(Color))
# Color.YELLOW = 4
# Color.RED = 100
pprint(Color.__members__)


class ResponseStatus(Enum):
    PENDING = "pending"
    FULFILLED = "fulfilled"
    REJECTED = "rejected"


response = """{
    "status": "fulfilled"
    }"""

data = json.loads(response)
status = data["status"]
try:
    print(ResponseStatus(status))
except ValueError:
    print("ValueError")


# print(ResponseStatus(status))
@enum.unique
class Day(Enum):
    MON = "Monday"
    TUE = "Tuesday"
    WED = "Wednesday"
    THU = "Thursday"
    FRI = "Friday"
    SAT = "Saturday"
    SUN = "Sunday"


@total_ordering
class PaymentStatus(Enum):
    PENDING = 1
    COMPLETED = 2
    REFUNDED = 3

    def __str__(self):
        return f"{self.name.lower()}({self.value})"

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        if isinstance(other, PaymentStatus):
            return self is other

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other
        if isinstance(other, PaymentStatus):
            return self.value < other.value
        return False

    def __bool__(self):
        if self is self.COMPLETED:
            return True
        return False


print(PaymentStatus.PENDING)
if PaymentStatus.PENDING == 1:
    print("PaymentStatus.PENDING == 1")
status = 1
if status < PaymentStatus.COMPLETED:
    print("status has not completed")
for member in PaymentStatus:
    print(member, bool(member))


@total_ordering
class OrderedEnum(Enum):
    def __lt__(self, other):
        if isinstance(other, OrderedEnum):
            return self.value < other.value
        return NotImplemented


class ApprovalStatus(OrderedEnum):
    # def _generate_next_value_(name,start,count,last_values):
    #     return name.lower()

    PENDING = auto()
    APPROVED = auto()
    REJECTED = auto()

    


status = ApprovalStatus(1)
if status < ApprovalStatus.APPROVED:
    print("status has not approved")

for member in ApprovalStatus:
    print(member.name, member.value)
