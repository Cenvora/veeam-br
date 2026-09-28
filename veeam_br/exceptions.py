"""Exceptions raised by :class:`veeam_br.client.VeeamClient`.

Both authentication-related errors subclass :class:`PermissionError`, so code written
against earlier releases that catches ``PermissionError`` keeps working. Catch the specific
classes to tell a refused password (prompt the user to re-authenticate) from a session the
server dropped mid-use (the next call logs in again by itself).

Transport failures - an unreachable host, a TLS error, a timeout - are never wrapped in these;
they propagate as the underlying ``httpx.HTTPError``, ``OSError`` or ``TimeoutError``.
"""


class VeeamError(Exception):
    """Base class for errors raised by this library."""


class VeeamAuthenticationError(VeeamError, PermissionError):
    """The server rejected the credentials at password login.

    Raised when the password grant returns something other than a token. Retrying with
    the same credentials will not help; the caller should ask for new ones.
    """


class VeeamSessionError(VeeamError, PermissionError):
    """The server rejected the session while it was in use.

    Raised when a response cannot be decoded, which is how VBR answers a token it no
    longer accepts. The session has already been invalidated and the next call
    authenticates from scratch. This is not proof that the credentials are wrong.
    """
