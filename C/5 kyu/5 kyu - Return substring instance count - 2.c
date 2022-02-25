// https://www.codewars.com/kata/return-substring-instance-count-2/train/c
// My solution
#include <stdbool.h>

int searching(const char* p, const char* f, char* s, bool ov, int i, int n){
    return !s ? i : ( ov ? searching(s+1, f, strstr(p, f), ov, i+1, n): searching(s+n, f, strstr(p, f), ov, i+1, n));
}
int search_substr(const char *text, const char *search, bool overlap) {
    return strlen(search) == 0? 0: searching(text, search, strstr(text, search), overlap, 0, strlen(search))/2;
}

// And
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int search_substr(const char *full_text, const char *search_text, bool allow_overlap){
    int n = strlen(search_text);
    if(n == 0) return 0;
    int cont;
    char *p = full_text;
    char *s;
    for(cont = 0; s = strstr (p, search_text) ; cont++){
        if(allow_overlap) p = s + 1;
        else              p = s + n;
    }
    return cont;
}

// ...
#include <stdbool.h>
#include <string.h>

int search_substr(const char *full_text, const char *search_text, bool allow_overlap) {
    int sub_len = strlen(search_text);
    if ( sub_len == 0 || sub_len > strlen(full_text) ) return 0;
    int count = 0;
    char * res = strstr(full_text, search_text);
    if ( allow_overlap ) {
        while( res != NULL ) {
            count += 1;
            res = strstr(res + 1, search_text);
        }
    }
    else {
        while( res != NULL ) {
            count += 1;
            res = strstr(res + sub_len, search_text);
        }
    }
    return count;
}

// ...
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

typedef struct vertex {
  int32_t next[0xff];
  int32_t go[0xff];
  int32_t p;
  int32_t link;
  int32_t count_by_link;
  bool leaf;
  char pch;
  char padding[2];
} vertex_t;

typedef struct graph {
  int sz;
  vertex_t *t;
} graph_t;
///////////////////////////////////////////////////////

#define UNINITIALIZED -1

static void vert_init(vertex_t *v) {
  int i;
  for (i = 0; i < 0xff; ++i)
    v->next[i] = v->go[i] = UNINITIALIZED;
}
///////////////////////////////////////////////////////

static graph_t gr_init(const char *str) {
  graph_t gr = {.sz = 0, .t = NULL};
  int nmax = strlen(str) + 1;
  gr.t = malloc(sizeof(vertex_t)*nmax); //all symbols are different
  memset(gr.t, 0xff, sizeof(vertex_t)*nmax);
  gr.t[0].p = gr.t[0].link = UNINITIALIZED;
  gr.t[0].leaf = false;
  memset(gr.t[0].next, 0xff, sizeof(gr.t[0].next));
  memset(gr.t[0].go, 0xff, sizeof(gr.t[0].go));
  vert_init(&gr.t[0]);
  gr.sz = 1;
  return gr;
}
///////////////////////////////////////////////////////

static void gr_add_string (graph_t *gr, const char *s) {
  int v = 0;
  for (; *s; ++s) {
    if (gr->t[v].next[(int)*s] == UNINITIALIZED) {
      memset(gr->t[gr->sz].next, 0xff, sizeof(gr->t[gr->sz].next));
      memset(gr->t[gr->sz].go, 0xff, sizeof(gr->t[gr->sz].go));
      gr->t[gr->sz].leaf = false;
      gr->t[gr->sz].link = UNINITIALIZED;
      gr->t[gr->sz].count_by_link = UNINITIALIZED;
      gr->t[gr->sz].p = v;
      gr->t[gr->sz].pch = *s;
      gr->t[v].next[(int)*s] = gr->sz++;
    }
    v = gr->t[v].next[(int)*s];
  }
  gr->t[v].leaf = true;
}
///////////////////////////////////////////////////////

static int gr_go (graph_t *gr, int v, char c);
static int gr_get_link (graph_t *gr, int v) {
  if (gr->t[v].link == UNINITIALIZED) {
    if (v == 0 || gr->t[v].p == 0) {
      gr->t[v].link = 0;
    } else {
      gr->t[v].link = gr_go(gr, gr_get_link(gr, gr->t[v].p), gr->t[v].pch);
    }
  }
  return gr->t[v].link;
}
///////////////////////////////////////////////////////

int gr_go (graph_t *gr, int v, char c) {
  if (gr->t[v].go[(int)c] == -1) {
    if (gr->t[v].next[(int)c] != -1) {
      gr->t[v].go[(int)c] = gr->t[v].next[(int)c];
    } else {
      gr->t[v].go[(int)c] = v==0 ? 0 : gr_go (gr, gr_get_link(gr, v), c);
    }
  }
  return gr->t[v].go[(int)c];
}
///////////////////////////////////////////////////////

static int smart_solution(const char *ft,
              const char *st,
              bool ol) {
  int count = 0;
  graph_t gr = gr_init(st);
  int cs = 0;

  gr_add_string(&gr, st);
  for (; *ft; ++ft) {
    cs = gr_go(&gr, cs, *ft);
    if (!gr.t[cs].leaf)
      continue;
    ++count;
    if (!ol) cs = 0;
    cs *= ol ? 1 : 0;
  }

  free(gr.t);
  return count;
}
///////////////////////////////////////////////////////

int search_substr(const char *full_text,
                  const char *search_text,
                  bool allow_overlap) {
  if (strcmp(search_text, "") == 0) return 0;
  return smart_solution(full_text, search_text, allow_overlap);
}
///////////////////////////////////////////////////////

// ...
#include <stdbool.h>

int search_substr(const char *haystack, const char *needle, bool allow_overlap) 
{
    int i, j, occurances = 0;
    
    for (i = 0; haystack[i]; ++i) {
        for (j = 0; needle[j]; ++j)
            if (haystack[i + j] != needle[j])
                break;
        
        if (needle[j] == '\0' && j > 0) {
            occurances++;
            if (!allow_overlap)
                i += j - 1;
        }
    }
   
    return occurances;
}

