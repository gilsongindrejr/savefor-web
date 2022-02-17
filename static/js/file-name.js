let $input = document.getElementById('id_file');
let $filename = document.getElementById('file-name');

console.log($input)
console.log($filename)

$input.addEventListener('change', function(){
    $filename.textContent = this.files[0].name;
});