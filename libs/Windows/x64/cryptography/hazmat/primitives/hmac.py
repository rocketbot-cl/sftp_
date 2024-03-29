# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.


import typing

from cryptography import utils
from cryptography.exceptions import (
    AlreadyFinalized,
)
from cryptography.hazmat.backends.openssl.hmac import _HMACContext
from cryptography.hazmat.primitives import hashes

AlreadyFinalized_MESSAGE = "Context was already finalized."


class HMAC(hashes.HashContext):
    _ctx: typing.Optional[_HMACContext]

    def __init__(
        self,
        key: bytes,
        algorithm: hashes.HashAlgorithm,
        backend: typing.Any = None,
        ctx=None,
    ):
        if not isinstance(algorithm, hashes.HashAlgorithm):
            raise TypeError("Expected instance of hashes.HashAlgorithm.")
        self._algorithm = algorithm

        self._key = key
        if ctx is None:
            from cryptography.hazmat.backends.openssl.backend import (
                backend as ossl,
            )

            self._ctx = ossl.create_hmac_ctx(key, self.algorithm)
        else:
            self._ctx = ctx

    @property
    def algorithm(self) -> hashes.HashAlgorithm:
        return self._algorithm

    def update(self, data: bytes) -> None:
        if self._ctx is None:
            raise AlreadyFinalized(AlreadyFinalized_MESSAGE)
        utils._check_byteslike("data", data)
        self._ctx.update(data)

    def copy(self) -> "HMAC":
        if self._ctx is None:
            raise AlreadyFinalized(AlreadyFinalized_MESSAGE)
        return HMAC(
            self._key,
            self.algorithm,
            ctx=self._ctx.copy(),
        )

    def finalize(self) -> bytes:
        if self._ctx is None:
            raise AlreadyFinalized(AlreadyFinalized_MESSAGE)
        digest = self._ctx.finalize()
        self._ctx = None
        return digest

    def verify(self, signature: bytes) -> None:
        utils._check_bytes("signature", signature)
        if self._ctx is None:
            raise AlreadyFinalized(AlreadyFinalized_MESSAGE)

        ctx, self._ctx = self._ctx, None
        ctx.verify(signature)
