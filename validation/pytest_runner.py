import sys
import tempfile
from absl import flags
from absl.testing import absltest
import pytest

with tempfile.TemporaryDirectory(prefix='absl-validation-') as directory:
    flags.FLAGS(['validation', '--test_tmpdir=' + directory])
    sys.exit(pytest.main(sys.argv[1:]))
