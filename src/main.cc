#include <nan.h>
#include "mbus-master.h"

NAN_MODULE_INIT(InitModule) {
    MbusMaster::Init(target);
}

#if NODE_MAJOR_VERSION >= 10
NAN_MODULE_WORKER_ENABLED(mbus, InitModule)
#else
NODE_MODULE(mbus, InitModule)
#endif