#!/usr/bin/bash

cat > .git/hooks/pre-commit << 'END'
#!/usr/bin/env bash

. ./test.sh
END
