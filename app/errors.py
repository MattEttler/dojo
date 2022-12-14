"""Custom Project Generator Exceptions."""

class NoCategoriesFoundError(ValueError):
    """Indicates the lack of a categories made available to the Project Generator.
Typically this is controlled by a configuration file."""

class NoAttributesFoundError(ValueError):
    """Indicates the lack of attributes made available to the Project Generator.
Typically this is controlled by a configuration file."""
