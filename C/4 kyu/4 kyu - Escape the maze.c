// https://www.codewars.com/kata/escape-the-maze/train/c
// My solution
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static char BUFFER_PATH[2048];

typedef struct s_Maze
{
    unsigned    height, width;
    char**      grid;
}   Maze;

void first_position(const Maze *maze, int* x, int *y)
{
    for ( int i = 0; i < maze->height; i++ )
        for ( int j = 0; j < maze->width; j++ )
            if ( maze->grid[i][j] == '^' || maze->grid[i][j] == 'v'
                || maze->grid[i][j] == '>' || maze->grid[i][j] == '<' )
            {
                *x = i;
                *y = j;
                return ;
            }
}

bool walking_by_maze(const Maze *maze, char *passed, char *path, int x, int y, char move)
{
    if ( x < 0 || x >= maze->height || y < 0 || y >= maze->width ) // i escape
        return true;
    if ( maze->grid[x][y] == '#' || passed[x * maze->width + y] ) // i came here before or i cant pass
        return false;
    
    passed[(x * maze->width) + y] = 1;
    
    bool r, l, f, b;
    if( move == '>')
    {
        r = walking_by_maze( maze, passed, path, x+1, y, 'v' );
        l = walking_by_maze( maze, passed, path, x-1, y, '^' );
        f = walking_by_maze( maze, passed, path, x, y+1, '>' );
        b = walking_by_maze( maze, passed, path, x, y-1, '<' );
    }
    else if( move == '<')
    {
        r = walking_by_maze( maze, passed, path, x-1, y, '^' );
        l = walking_by_maze( maze, passed, path, x+1, y, 'v' );
        f = walking_by_maze( maze, passed, path, x, y-1, '<' );
        b = walking_by_maze( maze, passed, path, x, y+1, '>' );
    }
    else if( move == '^')
    {
        r = walking_by_maze( maze, passed, path, x, y+1, '>' );
        l = walking_by_maze( maze, passed, path, x, y-1, '<' );
        b = walking_by_maze( maze, passed, path, x+1, y, 'v' );
        f = walking_by_maze( maze, passed, path, x-1, y, '^' );
    }
    else if( move == 'v')
    {
        r = walking_by_maze( maze, passed, path, x, y-1, '<' );
        l = walking_by_maze( maze, passed, path, x, y+1, '>' );
        b = walking_by_maze( maze, passed, path, x-1, y, '^' );
        f = walking_by_maze( maze, passed, path, x+1, y, 'v' );
    }
    
    if ( f )      strcat( path, "F" );
    else if ( b ) strcat( path, "FB" );
    else if ( r ) strcat( path, "FR" );
    else if ( l ) strcat( path, "FL" );
    
    return f || b || r || l;
}

char* strrev(char* str)
{
    int length = strlen(str);
    for ( int i = 0, j = length - 1; i < j; i++, j-- )
    {
        char tmp = str[i]; // swap
        str[i] = str[j];
        str[j] = tmp;
    }
    return str;
}

char *escape(const Maze *maze)
{
    int x, y;
    first_position( maze, &x, &y );
    
    char *passed = calloc( maze->height * maze->width , sizeof(char) ); // Record where I walk.
    
    BUFFER_PATH[0] = '\0';
    bool can_escape = walking_by_maze( maze, passed, BUFFER_PATH, x, y, maze->grid[x][y] );
    free( passed );
    
    return can_escape ? strrev( strdup( BUFFER_PATH ) ) : NULL;
}

// ...
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct s_Maze
{
    unsigned    height, width;
    char**      grid;
}   Maze;

typedef struct s_Coord
{
    unsigned    i;
    unsigned    j;
}   Coord;

typedef enum e_Direction
{
    top, right, bottom, left
}   Direction;

typedef struct s_Player
{
    Coord       pos;
    Direction   direction;
}   Player;

typedef struct s_CellNode
{
    Player              player;
    char                instruction;
    struct s_CellNode   *prev;
    struct s_CellNode   **next;
    unsigned            nextCount;
}   CellNode;

typedef struct s_DequeNode
{
    CellNode            *content;
    struct s_DequeNode  *prev;
    struct s_DequeNode  *next;
}   DequeNode;

typedef struct s_Deque
{
    DequeNode   *head;
    DequeNode   *tail;
}   Deque;

Coord       *setCoord(Coord *c, unsigned i, unsigned j);

Player      *loadPlayer(Player *p, const Maze *maze);
Player      *setPlayer(Player *p, unsigned i, unsigned j, Direction direction);

CellNode    *newCellNode(CellNode *prev, char instruction);
int         unlinkCellNodes(CellNode *parent, CellNode *child);
void        deleteCellNode(CellNode *node);

DequeNode   *newDequeNode(CellNode *content);
void        deleteDequeNode(DequeNode* n);

Deque       *newDeque();
Deque       *appendDeque(Deque *d, CellNode *content);
CellNode    *shiftDeque(Deque *d);
void        deleteDeque(Deque *d);

char        *pathToNode(const CellNode *node);
char        *escape(const Maze *maze);

Coord   *setCoord(Coord *c, unsigned i, unsigned j)
{
    if (c == NULL)
        return NULL;
    c->i = i;
    c->j = j;
    return c;
}

Player  *setPlayer(Player *p, unsigned i, unsigned j, Direction direction)
{
    if (p == NULL)
        return NULL;
    setCoord(&p->pos, i, j);
    p->direction = direction;
    return p;
}

Player  *loadPlayer(Player *p, const Maze *maze)
{
    unsigned            i;
    unsigned            j;
    char                *spritePtr;
    static const char   *sprites = "^>v<";

    if (maze == NULL || p == NULL)
        return NULL;
    for (i = 0; i < maze->height; ++i)
    {
        for (j = 0; j < maze->width; ++j)
        {
            spritePtr = strchr(sprites, maze->grid[i][j]);
            if (spritePtr != NULL && *spritePtr != '\0')
                return setPlayer(p, i, j, spritePtr - sprites);
        }
    }
    return NULL;
}

CellNode    *newCellNode(CellNode *prev, char instruction)
{
    CellNode    *n;

    n = (CellNode*)malloc(sizeof(CellNode));
    if (n == NULL)
        return NULL;
    // Only the start position can have 4 children.
    n->next = (CellNode**)calloc((prev != NULL) ? 3 : 4, sizeof(CellNode*));
    if (n->next == NULL)
    {
        free(n);
        return NULL;
    }
    n->instruction = instruction;
    n->prev = prev;
    n->nextCount = 0;
    if (prev != NULL)
        prev->next[prev->nextCount++] = n;
    return n;
}

int         unlinkCellNodes(CellNode *parent, CellNode *child)
{
    unsigned    i, j;

    if (parent == NULL || child == NULL || child->prev != parent)
        return 0;
    for (i = 0; i < parent->nextCount; ++i)
    {
        if (parent->next[i] == child)
        {
            child->prev = NULL;
            --parent->nextCount;
            for (j = parent->nextCount; j > i; --j)
                parent->next[j - 1] = parent->next[j];
            /* This should never free firstNode unless there is no exit, but
            ** somehow it seems to do so ever so often. If anyone can tell me
            ** what's going wrong here. ATM I'm using way too much space (the
            ** CellNodes from dead-ends are only freed when the function ends)
            
            if (parent->nextCount == 0)     // If a node has no more children
                deleteCellNode(parent);     // We can delete it!
            */
            return 1;
        }
    }
    return 0;
}

void    deleteCellNode(CellNode *n)
{
    unsigned    i;

    if (n == NULL)
        return;
    if (n->prev != NULL)
        unlinkCellNodes(n->prev, n);
    // Delete all node's children with it.
    if (n->nextCount > 0)
    {
        // We can't access n within the loop because the last iteration deletes n
        for (i = n->nextCount; i > 0; --i)
            deleteCellNode(n->next[i - 1]);
    }
    else
    {
        free(n->next);
        free(n);
    }
}

DequeNode   *newDequeNode(CellNode *content)
{
    DequeNode    *n;

    n = (DequeNode*)malloc(sizeof(DequeNode));
    if (n == NULL)
        return NULL;
    n->content = content;
    n->prev = n->next = NULL;
    return n;
}

void        deleteDequeNode(DequeNode* n)
{
    free(n);
}

Deque       *newDeque()
{
    Deque   *d;

    d = (Deque*)malloc(sizeof(Deque));
    if (d == NULL)
        return NULL;
    d->head = NULL;
    d->tail = NULL;
    return d;
}

void        deleteDeque(Deque *d)
{
    DequeNode    *n;
    DequeNode    *to_del;

    n = d->head;
    while (n != NULL)
    {
        to_del = n;
        n = n->next;
        deleteDequeNode(to_del);
    }
    free(d);
}

Deque       *appendDeque(Deque *d, CellNode *content)
{
    DequeNode   *n;

    if (d == NULL)
        return d;
    n = newDequeNode(content);
    if (n == NULL)
        return NULL;
    if (d->tail != NULL)
        d->tail->next = n;
    else
        d->head = n;
    n->prev = d->tail;
    d->tail = n;
    return d;
}

CellNode    *shiftDeque(Deque *d)
{
    DequeNode   *n;
    CellNode    *content;

    if (d == NULL || d->head == NULL)
        return NULL;
    n = d->head;
    d->head = n->next;
    if (d->head != NULL)
        d->head->prev = NULL;
    else
        d->tail = NULL;
    content = n->content;
    deleteDequeNode(n);
    return content;
}

char        *pathToNode(const CellNode *exit)
{
    char            *path;
    const CellNode  *node;
    size_t          len;

    len = 0;
    node = exit;
    while (node->prev != NULL)
    {
        len += (node->instruction == 'F') ? 1 : 2;
        node = node->prev;
    }
    path = (char*)calloc(len + 1, sizeof(char));
    if (path == NULL)
        return NULL;
    path[len--] = '\0';
    node = exit;
    while (node->prev != NULL)
    {
        path[len--] = 'F';
        if (node->instruction != 'F')
            path[len--] = node->instruction;
        node = node->prev;
    }
    return path;
}

void        delEscapeAlloc(char *seen, Deque *q, CellNode *firstNode)
{
    free(seen);
    deleteDeque(q);
    deleteCellNode(firstNode);
}

char        *escape(const Maze *maze)
{
    static const char   instructions[] = "FRBL";
    unsigned            i2, j2;
    Direction           direction;
    char                *seen;      // Must be freed
    char                *path;      // Not freed (return value)
    Deque               *q;         // Must be freed
    CellNode            *firstNode; // Only node to free at the end
    CellNode            *node;      // All deleted with firstNode
    CellNode            *nextNode;  // All deleted with firstNode
    Player              *player;    // Subpointer of node
    Coord               *pos;       // Subpointer of node

    seen = (char*)calloc(maze->height * maze->width, sizeof(char));
    firstNode = newCellNode(NULL, '\0');
    q = newDeque();
    player = loadPlayer(&firstNode->player, maze);
    if (seen == NULL || q == NULL || firstNode == NULL || player == NULL)
    {
        delEscapeAlloc(seen, q, firstNode);
        return NULL;
    }
    pos = &player->pos;
    if (pos->i == 0 || pos->i == maze->height - 1 || pos->j == 0 || pos->j == maze->width - 1)
    {
        path = (char*)malloc(sizeof(char));
        path[0] = '\0';
        delEscapeAlloc(seen, q, firstNode);
        return path;
    }
    memset(seen, maze->height * maze->width, '\0');
    appendDeque(q, firstNode);
    seen[pos->i * maze->width + pos->j] = 1;    // Start position is visited
    while (q->head != NULL)
    {
        node = shiftDeque(q);
        player = &node->player;
        pos = &player->pos;
        for (direction = top; direction <= left; ++direction)
        {
            i2 = pos->i + (direction == top ? -1 : direction == bottom ? 1 : 0);
            j2 = pos->j + (direction == left ? -1 : direction == right ? 1 : 0);
            // Note: i2 and j2 are unsigned, so -1 == UINT_MAX
            if (i2 >= maze->height || j2 >= maze->width || seen[i2 * maze->width + j2] || maze->grid[i2][j2] != ' ')
                continue;
            nextNode = newCellNode(node, instructions[(direction + 4 - player->direction) % 4]);
            if (nextNode == NULL)
            {
                delEscapeAlloc(seen, q, firstNode);
                return NULL;
            }
            setPlayer(&nextNode->player, i2, j2, direction);
            if (i2 == 0 || i2 == maze->height - 1 || j2 == 0 || j2 == maze->width - 1)
            {   // Found an exit!
                path = pathToNode(nextNode);
                delEscapeAlloc(seen, q, firstNode);
                return path;
            }
            appendDeque(q, nextNode);
            seen[i2 * maze->width + j2] = 1;
        }
    }
    delEscapeAlloc(seen, q, firstNode);
    return NULL;
}