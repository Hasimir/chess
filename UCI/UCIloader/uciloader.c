#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
 
int main()
{
  FILE *f = fopen("wrapper.ini", "r");
  char buf[1024], exe_name[1024];
  if(!f) return -1;
  fscanf(f, "%[^\n]", exe_name); fclose(f);
  snprintf(buf, 1024, "/opt/local/bin/wine %s/%s", get_current_dir_name(), exe_name);
  system(buf);
  return 0;
} 
