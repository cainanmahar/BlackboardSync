"""
Blackboard Exception Classes

a set of exception classes thrown by library api abstractions
"""

class BlackboardAPIError(Exception):
    pass

class BBAuthError(BlackboardAPIError):
    pass

class BBPrivateCourseError(BlackboardAPIError):
    pass