# Results

- fork: Fidget-Spinner
- version: 3.12.0a7+
- commit hash: [dfd6b01](https://github.com/Fidget%2dSpinner/cpython/commit/dfd6b01)
- commit date: 2023-04-27T17:34:38+08:00
- commit merge base: [dff8e5dc8d0758d1f9c55fdef308e44aefebe1a2](https://github.com/Fidget%2dSpinner/cpython/commit/dff8e5dc8d0758d1f9c55fdef308e44aefebe1a2)
- ref: call_function_ex_inl

## linux x86_64 (azure)

- [pystats raw](bm-20230427-azure-x86_64-Fidget%252dSpinner-call_function_ex_inl-3.12.0a7%2B-dfd6b01-pystats.json)
- [pystats table](bm-20230427-azure-x86_64-Fidget%252dSpinner-call_function_ex_inl-3.12.0a7%2B-dfd6b01-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4823675939)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230427-linux-x86_64-Fidget%252dSpinner-call_function_ex_inl-3.12.0a7%2B-dfd6b01.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster \* (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230427-linux-x86_64-Fidget%252dSpinner-call_function_ex_inl-3.12.0a7%2B-dfd6b01-vs-3.10.4.md)
- [plot](bm-20230427-linux-x86_64-Fidget%252dSpinner-call_function_ex_inl-3.12.0a7%2B-dfd6b01-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.01x slower \* (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230427-linux-x86_64-Fidget%252dSpinner-call_function_ex_inl-3.12.0a7%2B-dfd6b01-vs-3.11.0.md)
- [plot](bm-20230427-linux-x86_64-Fidget%252dSpinner-call_function_ex_inl-3.12.0a7%2B-dfd6b01-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.81%, 1.00x slower at 99th %ile)
- [table](bm-20230427-linux-x86_64-Fidget%252dSpinner-call_function_ex_inl-3.12.0a7%2B-dfd6b01-vs-base.md)
- [plot](bm-20230427-linux-x86_64-Fidget%252dSpinner-call_function_ex_inl-3.12.0a7%2B-dfd6b01-vs-base.png)

