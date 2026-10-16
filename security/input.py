import re

class InputSecurity:
    @staticmethod
    def detect_injection(input : str):
        injection_patterns = [
                r"ignore (all )?previous instructions",
                r"system override",
                r"you are now a",
                r"assistant: ",
                r"<\|system\|>",
                r"new rule:"
            ]
        for pattern in injection_patterns:
            if re.search(pattern, input, re.IGNORECASE):
                return True
        return False

    @staticmethod
    def detect_pii(input : str):
        pii_patterns = [
                r"\b\d{16}\b",  
                r"\b((\+420)|(00420))*\d{3}\s*\d{3}\s*\d{3}\b",  
                r"\b\S+@\S+\.\S+\b",  
                r"\b\d{6}/?\d{4}\b"
            ]
        for pattern in pii_patterns:
            if re.search(pattern, input):
                return True
        return False

    @staticmethod
    def detect_user_specific_sensitive_info(input : str):
        sensitive_info_patterns = [
                r"veronikacalkovska|veronika\.calkovska",  

            ]
        for pattern in sensitive_info_patterns:
            if re.search(pattern, input):
                return True
        return False