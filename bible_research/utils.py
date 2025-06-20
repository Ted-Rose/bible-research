import uuid


def generate_id(prefix):
    def _generate_id():
        uuid_str = str(uuid.uuid4()).upper().replace('-', '')
        return f"{prefix}{uuid_str[:15]}"
    # To provide uniqueness for bulk create
    return _generate_id
