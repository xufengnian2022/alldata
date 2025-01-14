//
//! Copyright 2020 Alibaba Group Holding Limited.
//!
//! Licensed under the Apache License, Version 2.0 (the "License");
//! you may not use this file except in compliance with the License.
//! You may obtain a copy of the License at
//!
//! http://www.apache.org/licenses/LICENSE-2.0
//!
//! Unless required by applicable law or agreed to in writing, software
//! distributed under the License is distributed on an "AS IS" BASIS,
//! WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//! See the License for the specific language governing permissions and
//! limitations under the License.

use maxgraph_store::api::{DataType, LabelId, PropId};

pub trait Schema: Send + Sync {
    fn get_prop_id(&self, name: &str) -> Option<PropId>;
    fn get_prop_type(&self, label: LabelId, prop_id: PropId) -> Option<DataType>;
    fn get_prop_name(&self, prop_id: PropId) -> Option<String>;
    fn get_label_id(&self, name: &str) -> Option<LabelId>;
    fn get_label_name(&self, label: LabelId) -> Option<String>;
    fn to_proto(&self) -> Vec<u8>;
}
