#!/usr/bin/bash

cat > .git/hooks/pre-commit << 'END'
#!/usr/bin/env bash

. ./test.sh
END

chmod 755 .git/hooks/pre-commit
