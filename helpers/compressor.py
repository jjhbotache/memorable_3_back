import gzip

def compress_to_gzip(file_path, output_path):
  file_name = file_path.split("/")[-1].split(".")[0]
  final_output_path = output_path + file_name + ".gz"
  
  with open(file_path, 'rb') as file:
    with gzip.open(final_output_path, 'wb') as gzip_file:
      gzip_file.writelines(file)
      
    
def uncompress_ai_design_from_gzip(file_path, output_path):
  file_name = file_path.split("/")[-1].split(".")[0]
  final_output_path = output_path + file_name + ".ai"
  
  with gzip.open(file_path, 'rb') as file:
    with open(final_output_path, 'wb') as gzip_file:
      gzip_file.writelines(file)

