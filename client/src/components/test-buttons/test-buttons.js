import React, { useState } from "react";
import { Button, InputNumber, Radio } from "antd";
import axios from "axios";

const TestButtons = () => {
  const [op_a, set_op_a] = useState(0);
  const [op_b, set_op_b] = useState(0);
  const [oper, set_oper] = useState(0);
  const [result, set_result] = useState();

  const update_op_a = value => {
    set_op_a(value);
  };

  const update_op_b = value => {
    set_op_b(value);
  };

  const update_oper = value => {
    set_oper(value);
  };

  const calculate = () => {
    let post_data = {
      op_a: op_a,
      op_b: op_b,
      oper: oper
    };

    let response = axios.post("http://localhost:8083/calc", post_data);
    set_result(response.answer);
  };

  return (
    <div>
      Op A
      <InputNumber value={op_a} onChange={update_op_a} />
      Op B
      <InputNumber value={op_b} onChange={update_op_b} />
      Operator
      <Radio.Group onChange={update_oper} value={oper}>
        <Radio value={0}>+</Radio>
        <Radio value={1}>-</Radio>
        <Radio value={2}>*</Radio>
        <Radio value={3}>/</Radio>
      </Radio.Group>
      <Button type="primary" onClick={calculate}>
        Calculate
      </Button>
      <div>
        Result:
        <div>{result}</div>
      </div>
    </div>
  );
};

export default TestButtons;
