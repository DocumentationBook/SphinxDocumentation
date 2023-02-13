# shellcheck disable=SC2044
for file in $(find docs -name "*.html")
do
    echo $file
    vi -c '%s@_static/@static/@g' -c '%s@_images/@images/@g'  -c 'wq' $file
done

mv docs/_static docs/static
mv docs/_images docs/images
echo _static/ and _images/ are renamed to static/ and images/.
