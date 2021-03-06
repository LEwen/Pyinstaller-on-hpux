AR = ['/usr/bin/ar']
ARFLAGS = ['rcs']
BINDIR = '/usr/local/bin'
CC = ['/usr/local/bin/gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o', '']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '2', '3')
CFLAGS = ['-milp32', '-O2', '-Wdeclaration-after-statement', '-Wimplicit-function-declaration', '-Werror']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC', '-DPIC']
COMPILER_CC = 'gcc'
CPPPATH_ST = '-I%s'
DEFINES = ['_REENTRANT', '_BSD_SOURCE', 'HPUX', 'HAVE_UNSETENV=1', 'NDEBUG', 'WINDOWED']
DEFINES_ST = '-D%s'
DEFINE_COMMENTS = {'HAVE_MKDTEMP': '', 'HAVE_UNSETENV': ''}
DEST_BINFMT = 'elf'
DEST_CPU = 'ia'
DEST_OS = 'hpux'
HAVE_UNSETENV = 1
LIBDIR = '/usr/local/lib'
LIBPATH = ['/usr/local/lib/hpux32']
LIBPATH_ST = '-L%s'
LIB_DL = ['dl']
LIB_M = ['m']
LIB_PTHREAD = ['pthread']
LIB_ST = '-l%s'
LIB_Z = ['z']
LINKFLAGS = ['-milp32']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['/usr/local/bin/gcc']
PREFIX = '/usr/local'
PYI_ARCH = '32bit'
PYI_SYSTEM = 'HP-UX'
RPATH_ST = '-Wl,-rpath,%s'
SHLIB_MARKER = []
SONAME_ST = '-Wl,-h,%s'
STATICLIBPATH = ['/usr/local/lib/hpux32']
STLIBPATH_ST = '-L%s'
STLIB_MARKER = []
STLIB_ST = '-l%s'
STRIP = ['/usr/local/bin/strip']
STRIPFLAGS = ['']
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.sl'
cstlib_PATTERN = 'lib%s.a'
define_key = ['HAVE_UNSETENV', 'HAVE_MKDTEMP']
macbundle_PATTERN = '%s.bundle'
