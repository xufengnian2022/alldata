package com.dlink.executor;


import org.apache.flink.table.types.DataType;

/**
 * @author wenmo
 * @since 2022/05/08
 **/

public class TableSchemaField {
    private String name;
    private DataType type;

    public TableSchemaField(String name, DataType type) {
        this.name = name;
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public DataType getType() {
        return type;
    }

    public void setType(DataType type) {
        this.type = type;
    }
}
