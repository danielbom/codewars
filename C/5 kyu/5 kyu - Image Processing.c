// https://www.codewars.com/kata/image-processing/train/c
// My solution
typedef struct xRGBPixel {
    unsigned char unused;
    unsigned char red;
    unsigned char green;
    unsigned char blue;
} xRGBPixel;

unsigned char *processImage (const unsigned char *imageData, int height, int width, void* weights, int n) {
    int x, y, h = n / 2, dy, dx;
    xRGBPixel **img = calloc(height + n, sizeof(xRGBPixel *));  // /*
    for (y = 0; y < height + n; ++y)                            // * Criando a matriz de pixels
        img[y] = calloc(width + n, sizeof(xRGBPixel));          // */

    for (y = 0; y < height; ++y) {                              // /*
        for (x = 0; x < width; ++x) {                           // *
            img[y+h][x+h].red = *(imageData++);                 // *
            img[y+h][x+h].green = *(imageData++);               // *
            img[y+h][x+h].blue = *(imageData++);                // * Inicializando a matrix de
        }                                                       // * pixels
        for (x = 0; x < h; ++x) {                               // *
            img[y+h][x] = img[y+h][h];                          // *
            img[y+h][width+h+x] = img[y+h][width+h-1];          // *
        }                                                       // *
    }                                                           // */

    for (y = 0; y < h; ++y){                                    // /*
        for (x = 0; x < width + n; ++x) {                       // *
            img[y][x] = img[h][x];                              // *
            img[height+h+y][x] = img[height+h-1][x];            // *
        }                                                       // *
    }                                                           // */

    float* ws = (float*)weights;                                // /*
    float **wts = calloc(n, sizeof(float *));                   // *
    for (y = 0; y < n; ++y) {                                   // * Transformando o vetor peso
        wts[y] = calloc(n, sizeof(float));                      // * em uma matrix
        for (x = 0; x < n; ++x)                                 // *
            wts[y][x] = *(ws++);                                // *
    }                                                           // */

    unsigned char *ret = calloc(height, width * 3), *r = ret;
    for (y = 0; y < height; ++y) for (x = 0; x < width; ++x) {
        float red = 0, green = 0, blue = 0;
        for (dy = -h; dy <= h; ++dy){
            for (dx = -h; dx <= h; ++dx) {
                red   += wts[h+dy][h+dx] * img[y+h+dy][x+h+dx].red;
                green += wts[h+dy][h+dx] * img[y+h+dy][x+h+dx].green;
                blue  += wts[h+dy][h+dx] * img[y+h+dy][x+h+dx].blue;
            }
        }
        *(r++) =   red < 0 ? 0 : 255 <   red ? 255 : red;
        *(r++) = green < 0 ? 0 : 255 < green ? 255 : green;
        *(r++) =  blue < 0 ? 0 : 255 <  blue ? 255 : blue;
    }
    for (y = 0; y < height + n; ++y)
        free(img[y]);
    for (y = 0; y < n; ++y)
        free(wts[y]);          
    free(img);
    free(wts);
    return ret;
}

// ...
/* Per pixel basis convolution */
unsigned char convolution(const unsigned char *imgColor, int im_y, int im_x, int w, int h, float *kernel, int n) {
  int row, col, im_row, im_col, elmt, ctr = n/2; float pixel = 0;
  unsigned char imgExd[w+2*ctr][h+2*ctr]; float (*k)[n] = kernel;
    
  // ctr = radius of the kernel (rounded down)
  // which is how far the image is extended out:
  // (extended radius = kernel radius + image radius)
    
  /* Extend Image */
  for (row = 0; row < h+2*ctr; row++) {
    for (col = 0; col < w+2*ctr; col++) {
      im_row = row < ctr || row >= ctr+h ? (row < ctr? 0 : h-1) : row-ctr; // if row outside image radius: become extended row
      im_col = col < ctr || col >= ctr+w ? (col < ctr? 0 : w-1) : col-ctr; // same for column
      imgExd[row][col] = imgColor[im_row*w + im_col];
    }
  }
  
  /* Apply convolution */
  for (row = 0; row < n; row++)
    for (col = 0; col < n; col++)
      pixel += imgExd[im_y+row][im_x+col] * k[row][col]; // sum matrix multiplicative values

  /* Adjust to pixel value boundaries */
  pixel = pixel < 0 || pixel > 255 ? ( pixel < 0 ? 0 : 255 ) : pixel;
  
  return (char) ((int)(pixel+0.5));
}

/* Process image function */
unsigned char *processImage (const unsigned char *imageData, int height, int width, void* weights, int n) {
    int row, col;
    unsigned char *imgFltr = (char*)malloc(3*width*height);
    unsigned char imgRed[width*height];
    unsigned char imgGrn[width*height];
    unsigned char imgBlu[width*height];
    
    /* Break Image into rgb */
    for (row = 0; row < height; row++) {
        for (col = 0; col < width; col++) {
            imgRed[row*width + col] = imageData[row*width*3 + col*3 + 0]; // Red   = 0 (for clarity)
            imgGrn[row*width + col] = imageData[row*width*3 + col*3 + 1]; // Blue  = 1
            imgBlu[row*width + col] = imageData[row*width*3 + col*3 + 2]; // Green = 2
        }
    }
    
    /* Apply weights to each pixel color */
    for (row = 0; row < height; row++) {
        for (col = 0; col < width; col++) { // convolution() returns a pixel color char
            imgFltr[row*width*3 + col*3 + 0] = convolution(imgRed, row, col, width, height, weights, n);
            imgFltr[row*width*3 + col*3 + 1] = convolution(imgGrn, row, col, width, height, weights, n);
            imgFltr[row*width*3 + col*3 + 2] = convolution(imgBlu, row, col, width, height, weights, n);
        }
    }
    
    /* Complete!
    * #FilteredImage
    * #OnMyWay5BeInstagramFamous
    */
    
    putImageData(imgFltr, height, width, 200, 200); // show off your new pic!
    
    return imgFltr;
}

// ...
typedef unsigned char byte;

static byte filterSample
(byte *window,float *weight,int size)
{
    float sample, sum = 0.5;
    int idx;
    for(idx=0;idx<size;idx++)
    {
        sample = window[idx];
        sum += sample*weight[idx];
    }
    if(sum<0.0)
        return 0;
    if(sum>255.0)
        return 255;
    return sum;
}

static int nearest
(int v_offset,int h_offset,int v_pos,int h_pos,int height,int width)
{
    if(v_pos+v_offset<0)
        v_offset = -v_pos; 
    if(v_pos+v_offset>=height)
        v_offset = height-1-v_pos; 
    if(h_pos+h_offset<0)
        h_offset = -h_pos; 
    if(h_pos+h_offset>=width)
        h_offset = width-1-h_pos;
    return 3*(v_offset*width+h_offset);
}

static void buildWindow
(byte *window,byte *input,int height,int width,int v_pos,int h_pos,int n)
{
    int col, row, center = n>>1;
    for(row=0;row<n;row++)
        for(col=0;col<n;col++)
            *window++ = input[nearest(row-center,col-center,v_pos,h_pos,height,width)];
}

static void filterImage
(byte *output, byte *input, int height, int width, float *weight, int n)
{
    int col, row;
    byte window[n*n];

    for(row=0;row<height;row++)
        for(col=0;col<width;col++)
        {
            buildWindow(window,input,height,width,row,col,n);
            *output = filterSample(window,weight,n*n);
            input += 3;
            output += 3;
        }
}

static void readWeight
(float *output, void* weights, int n)
{
    int row, col;
    float (*w)[n] = weights;
    for(row=0;row<n;row++)
        for(col=0;col<n;col++)
            *output++ = w[row][col];
}

unsigned char *processImage
(const unsigned char *imageData, int height, int width, void* weights, int n) {
    float weight[n*n];
    int component;
    byte *output = (byte *)malloc(3*height*width);
    readWeight(weight,weights,n);
    for(component=0;component<3;component++)
        filterImage(output+component,imageData+component,height,width,weight,n);
    return output;
}

// ...
#define UC unsigned char *
#define pt(x, y, o) imageData[((x) + (y) * width) * 3 + (o)]
#define rpt(x, y, o) ret[((x) + (y) * width) * 3 + (o)]

int min(int x, int y) {
  return x < y ? x : y;
}

int max(int x, int y) {
  return x > y ? x : y;
}

UC processImage (const UC imageData,
                 int height,
                 int width,
                 void* weights,
                 int n) {
    float (*w)[n] = weights;
    UC ret = (UC) malloc(width * height * 3 * sizeof(unsigned char));
    int i, j, a, b, c;
    fprintf(stdout, "%d %d %d\n\n", width, height, n);
    double res = 0;
    for (a = 0; a < n; ++a) for (b = 0; b < n; ++b) res += w[a][b];
        printf("%.3f\n\n", res);

    for (c = 0; c < 3; ++c)
        for (i = 0; i < width; ++i) {
            for (j = 0; j < height; ++j) {
                float x = 0;
                for (a = 0; a < n; ++a) {
                    for (b = 0; b < n; ++b) {
                        int x_val = min(width - 1, max(0, i + a - (n >> 1)));
                        int y_val = min(height - 1, max(0, j + b - (n >> 1)));
                        x += pt(x_val, y_val, c) * w[a][b];
                    }
                }
                if (x < 0) x = 0;
                if (x > 255) x = 255;
                rpt(i, j, c) = (int) (x + 0.5);
            }
        }
    putImageData(ret, height, width, 200, 200);
    return ret;
}

// ...
#define  COL       3
#define  round(X)  (((X) * 2 + 1) / 2)
#define  cut(X,A)  (((X) < 0) ? 0 : (((X) > (A)) ? (A) : (X)))

unsigned char *processImage (const unsigned char *imageData, int height, int width, void* weights, int n) {
    float (*w)[n] = weights;

    float value[COL];
    int cx, cy;
    unsigned char *tmp;

    if ((tmp = malloc(width * height * COL)) == NULL)
        return tmp;

    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            value[0] = value[1] = value[2] = 0;
            for (int ky = 0; ky < n; ky++) {
                for (int kx = 0; kx < n; kx++) {
                    cy = cut(y - n / 2 + ky, height - 1);
                    cx = cut(x - n / 2 + kx, width - 1);
                    value[0] += imageData[(cy * width + cx) * COL]     * w[ky][kx];
                    value[1] += imageData[(cy * width + cx) * COL + 1] * w[ky][kx];
                    value[2] += imageData[(cy * width + cx) * COL + 2] * w[ky][kx];
                }
            }
            tmp[(y * width + x) * COL]     = round(cut(value[0], 255));
            tmp[(y * width + x) * COL + 1] = round(cut(value[1], 255));
            tmp[(y * width + x) * COL + 2] = round(cut(value[2], 255));
        }
    }

    return tmp;
}

// ...
#define fitinto(min, max, n) (((n) > (max)) ? ((max)) : (((n) < (min)) ? ((min)) : ((n))))

unsigned char *processImage (const unsigned char *imageData, int height, int width, void* weights, int n) {
    float (*w)[n] = weights;
    int i, j, ki, kj, ch;
    int kr = n / 2;
    const unsigned char (*img)[width][3] = (void *)imageData;
    unsigned char (*retimg)[width][3];
    float sum;
    
    retimg = malloc(height * width * 3 * sizeof(unsigned char));
    for (i = 0; i < height; i++) {
        for (j = 0; j < width; j++) {
            for (ch = 0; ch < 3; ch++) {
                sum = 0.0;
                for (ki = -kr; ki <= kr; ki++) {
                    for (kj = -kr; kj <= kr; kj++) {
                        sum += w[ki + kr][kj + kr] * img[fitinto(0, height - 1, i + ki)][fitinto(0, width - 1, j + kj)][ch];
                    }
                }
                retimg[i][j][ch] = fitinto(0, 255, (int)roundf(sum));
            }
        }
    }
    return retimg;
}

// ...
unsigned char truncate(float val){
  unsigned char x;
  (val < 0) ? (x = 0) : ((val >255) ? (x = 255) : (x = (int)round(val)));
  return x;
}
unsigned char *processImage (const unsigned char *imageData, int height, int width, void* weights, int n) {
    float (*w)[n] = weights;

    //3 arrays for storing processed R , G or B value in each pixel
    float red [height*width], green[height*width], blue[height*width];

    //Extending the edges according to weights matrix size(n)
    unsigned char extended[height+n-1][width+n-1];
    int extension = (n-1)/2, ro = 0, go = 0, bo = 0;

    //Stoing values 3 times per pixel (for RGB). c==0 is Red, ==1 is Green, ==2 is Blue
    for(int c = 0; c <3;c++){

        //Filling the extended 2d array...
        int w_end = width + extension -1,  h_end = height + extension -1;
        for(int x = 0; x < height + n - 1; x++ ){
            for(int y = 0; y < width + n -1;y++){      
                int set_x, set_y;
                (x < extension) ? (set_x =0): ((x > h_end )? (set_x = h_end-extension) : (set_x = x - extension));
                (y < extension) ? (set_y =0): ((y > w_end )? (set_y = w_end-extension) : (set_y = y - extension));
                int pixel_number = set_x * width + set_y, element_number = 3* pixel_number + c;
                extended[x][y] = imageData[element_number];  
            }
        }
        //Processing the extended array with weights matrix
        for(int x = extension; x <= extension + height -1; x++){
            for(int y = extension; y<= extension + width -1; y++){
                int s = x - extension, t = y - extension;
                float ret = 0;
                for(int i = 0; i < n; i++){
                    for(int j = 0; j<n;j++){
                        ret += w[i][j] * (float)extended[s+i][t+j];
                    }
                }     
                //Storing the values to R,G or B arrays
                (c == 0) ? (red[ro] = ret, ro++) : ((c == 1) ? (green[go] = ret, go++) : (blue[bo] = ret, bo++));    
            }
        }  
    }
    unsigned char * ret = malloc(height*width*3*sizeof(unsigned char));
    float tem[height*width*3];
    int r1 = 0, g1=0, b1 = 0;
    for(int x = 0; x < height*width*3;x++){
        (x%3 == 0) ? (tem[x] = red[r1], r1++) : ((x%3 == 1) ? (tem[x] = green[g1], g1++) : (tem[x] = blue[b1],b1++));
        ret[x] = truncate(tem[x]);
    }
    return ret;
}

// ...
int clip (int lower, int value, int upper) { return value < lower ? lower : value > --upper ? upper : value; }

unsigned char *processImage (const unsigned char *imageData, int height, int width, void* weights, int n) {
    float (*w)[n] = weights, sum;
    int k = n/2, r, c;
    unsigned char *processed = malloc (3 * height * width), *p = processed;
    for (int y = 0; y < height; ++y)
        for (int x = 0; x < width; ++x)
            for (int rgb = 0; rgb < 3; ++rgb, *p++ = clip (0, sum + 0.5, 256))
                for (sum = 0, r = -k; r <= k; ++r)
                    for (c = -k; c <= k; ++c)
                        sum += w[r+k][c+k] * imageData[3*(clip (0, y+r, height)*width + clip (0, x+c, width)) + rgb];
  return processed;
}