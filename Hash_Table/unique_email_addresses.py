class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        return len(set([self.format_email(email) for email in emails]))

    def format_email(self, email: str) -> str:
        return email.split('@')[0].split('+')[0].replace('.', '') \
            + '@' + email.split('@')[1]
