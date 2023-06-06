#include <nan.h>
#include "mbus-master.h"

NAN_MODULE_INIT(InitModule) {
    MbusMaster::Init(target);
}

NAN_MODULE_WORKER_ENABLED(mbus, InitModule);