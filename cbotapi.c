#include <jansson.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
struct game
{
	json_t *game_state;
	char *botname;
	json_t *move_obj;

};


json_error_t *err;
const char *name="brian";


void constructor(struct game *g,const char *json_text)
{
		g->game_state  = json_object();
		g->move_obj    = json_object();
		g->game_state          = json_loads(json_text,0,err);
		json_t *json_arr    = json_array();
		json_arr            = json_object_get(g->game_state,"bots");
		unsigned int length = json_array_size(json_arr);
		for(int i=0;i<length;i++)
		{
			json_t *bot         = json_object();	
			bot                 = json_array_get(json_arr,i);
			const char *botname = json_string_value(json_object_get(bot,"botname"));
			json_t *move        = json_object();
			char *childno;
			if(strcmp(botname,g->botname)==0)
			{
				snprintf(childno,"%d",json_integer_value(json_object_get(bot,"childno")));
				
				json_object_set_new(move,"childno",json_object_get(bot,"childno"));
				json_object_set_new(move, "relativeangle", json_integer( 0 ) );
				json_object_set_new(move, "ejectmass", json_false());
				json_object_set_new(move, "split", json_false());
				json_object_set_new(move, "pause", json_false());
				json_object_set_new(g->move_obj, childno , move);
				
			}
		
		json_decref(bot);
		json_decref(move);
		}
		
		
}

int main()
{
	
return 0;
}
