import filecmp
import sys

# e.g.
# python3 extract_diff_path.py bbb aaa |xargs -I{} cp --parents -r {} extract/
def main(a, b):

  def fn(dcmp,current_dir=a, buf=[]):
    # Combines the current directory path and object name
    buf.extend([f"{current_dir}/{x}" for x in dcmp.left_only])
    buf.extend([f"{current_dir}/{x}" for x in dcmp.diff_files])
    items = dcmp.subdirs.items()
    # No directory under which there is a difference exists
    if not items:
      return 
    for k,v in items:
      fn(v,f"{current_dir}/{k}",buf)
    return buf

  return fn(filecmp.dircmp(a, b))

if __name__ == '__main__':
  for x in main(sys.argv[1], sys.argv[2]):
    print(x)
