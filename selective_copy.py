import os
import shutil


def img_copy():
    """Copy .jpg images in the directory tree to a backup directory."""

    path = "."
    full_path = os.path.abspath(path)
    dest_dir = os.path.join(full_path, "pictures_backup/")
    file_count = 0
    for root, directories, files in os.walk(full_path):
        for filename in files:
            full_filename = os.path.join(root, filename)
            if filename.endswith(".jpg"):
                # Execute this when the dest_dir does not exist.
                if not os.path.exists(dest_dir):
                    print "The destination directory could not be found, \
                        creating %s now." % dest_dir
                    try:
                        os.makedirs(dest_dir)
                        shutil.copy(os.path.abspath(full_filename), dest_dir)
                        file_count += 1
                    except OSError as os_err:
                        print "An error occurred:", os_err
                    except shutil.Error as sh_err:
                        print "An error occurred while \
                            copying %s:" % filename, sh_err
                else:
                    # Execute when the dest_dir does not exist.
                    dest_filename = os.path.join(dest_dir, filename)
                    if os.path.exists(dest_filename):
                        continue  # Don't copy the same file twice.
                    else:
                        try:
                            shutil.copy(
                                os.path.abspath(full_filename), dest_dir)
                            file_count += 1
                        except shutil.Error as copy_err:
                            print "An error has occurred:", copy_err
    if file_count == 0:
        print "No new .jpg files found."
    else:
        print "Copied %d .jpg file(s) to %s." % (file_count, dest_dir)


img_copy()