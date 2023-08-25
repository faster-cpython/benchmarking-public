
# Results vs. 3.10.4

- fork: faster-cpython
- ref: micro_op_jump_if_non
- machine: linux-x86_64
- commit hash: 66a6bc3
- commit date: 2023-07-10
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.93 sec: 1.16x faster                                                                |
| tornado_http   | 152 ms                                                       | 124 ms: 1.23x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 92.7 ms: 1.48x faster                                                                 |
| float          | 110 ms                                                       | 82.2 ms: 1.34x faster                                                                 |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 152 ms: 1.27x faster                                                                  |
| regex_v8       | 26.6 ms                                                      | 23.8 ms: 1.12x faster                                                                 |
| regex_dna      | 259 ms                                                       | 242 ms: 1.07x faster                                                                  |
| regex_effbot   | 2.99 ms                                                      | 3.56 ms: 1.19x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 319 us: 1.43x faster                                                                  |
| unpickle_pure_python | 321 us                                                       | 224 us: 1.43x faster                                                                  |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                                 |
| xml_etree_process    | 76.0 ms                                                      | 59.2 ms: 1.28x faster                                                                 |
| tomli_loads          | 2.97 sec                                                     | 2.33 sec: 1.27x faster                                                                |
| json_loads           | 30.0 us                                                      | 25.6 us: 1.17x faster                                                                 |
| xml_etree_generate   | 94.6 ms                                                      | 87.1 ms: 1.09x faster                                                                 |
| xml_etree_parse      | 162 ms                                                       | 150 ms: 1.07x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 107 ms: 1.03x faster                                                                  |
| unpickle             | 14.2 us                                                      | 14.4 us: 1.01x slower                                                                 |
| pickle               | 9.94 us                                                      | 10.4 us: 1.05x slower                                                                 |
| unpickle_list        | 4.49 us                                                      | 4.71 us: 1.05x slower                                                                 |
| pickle_list          | 4.11 us                                                      | 4.38 us: 1.07x slower                                                                 |
| pickle_dict          | 30.0 us                                                      | 32.7 us: 1.09x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                                 |
| python_startup_no_site | 7.32 ms                                                      | 8.38 ms: 1.14x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 155 us: 3.37x faster                                                                  |
| asyncio_tcp              | 782 ms                                                       | 385 ms: 2.03x faster                                                                  |
| deltablue                | 7.47 ms                                                      | 3.71 ms: 2.01x faster                                                                 |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                                                |
| raytrace                 | 488 ms                                                       | 284 ms: 1.72x faster                                                                  |
| chaos                    | 107 ms                                                       | 62.8 ms: 1.71x faster                                                                 |
| logging_silent           | 166 ns                                                       | 98.2 ns: 1.69x faster                                                                 |
| scimark_lu               | 164 ms                                                       | 97.9 ms: 1.67x faster                                                                 |
| generators               | 58.0 ms                                                      | 35.9 ms: 1.61x faster                                                                 |
| crypto_pyaes             | 118 ms                                                       | 75.8 ms: 1.56x faster                                                                 |
| bench_mp_pool            | 7.18 ms                                                      | 4.63 ms: 1.55x faster                                                                 |
| sqlglot_parse            | 2.26 ms                                                      | 1.48 ms: 1.52x faster                                                                 |
| async_tree_none          | 700 ms                                                       | 465 ms: 1.51x faster                                                                  |
| scimark_monte_carlo      | 109 ms                                                       | 73.1 ms: 1.50x faster                                                                 |
| richards_super           | 90.8 ms                                                      | 61.0 ms: 1.49x faster                                                                 |
| async_tree_io            | 1.61 sec                                                     | 1.08 sec: 1.49x faster                                                                |
| nbody                    | 137 ms                                                       | 92.7 ms: 1.48x faster                                                                 |
| go                       | 259 ms                                                       | 177 ms: 1.46x faster                                                                  |
| async_tree_memoization   | 824 ms                                                       | 564 ms: 1.46x faster                                                                  |
| hexiom                   | 9.52 ms                                                      | 6.58 ms: 1.45x faster                                                                 |
| mako                     | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                                 |
| sqlglot_transpile        | 2.71 ms                                                      | 1.89 ms: 1.43x faster                                                                 |
| pickle_pure_python       | 457 us                                                       | 319 us: 1.43x faster                                                                  |
| spectral_norm            | 136 ms                                                       | 95.3 ms: 1.43x faster                                                                 |
| unpickle_pure_python     | 321 us                                                       | 224 us: 1.43x faster                                                                  |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                                                 |
| richards                 | 74.1 ms                                                      | 55.0 ms: 1.35x faster                                                                 |
| pyflate                  | 697 ms                                                       | 518 ms: 1.35x faster                                                                  |
| float                    | 110 ms                                                       | 82.2 ms: 1.34x faster                                                                 |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 716 ms: 1.33x faster                                                                  |
| coroutines               | 30.4 ms                                                      | 22.9 ms: 1.33x faster                                                                 |
| deepcopy_memo            | 48.9 us                                                      | 37.3 us: 1.31x faster                                                                 |
| xml_etree_process        | 76.0 ms                                                      | 59.2 ms: 1.28x faster                                                                 |
| logging_simple           | 8.90 us                                                      | 6.96 us: 1.28x faster                                                                 |
| regex_compile            | 194 ms                                                       | 152 ms: 1.27x faster                                                                  |
| tomli_loads              | 2.97 sec                                                     | 2.33 sec: 1.27x faster                                                                |
| logging_format           | 9.57 us                                                      | 7.55 us: 1.27x faster                                                                 |
| pycparser                | 1.66 sec                                                     | 1.32 sec: 1.26x faster                                                                |
| mypy2                    | 466 ms                                                       | 372 ms: 1.25x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 1.72 sec: 1.25x faster                                                                |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.16 ms: 1.25x faster                                                                 |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                                                  |
| fannkuch                 | 496 ms                                                       | 399 ms: 1.24x faster                                                                  |
| pprint_safe_repr         | 1.05 sec                                                     | 846 ms: 1.24x faster                                                                  |
| tornado_http             | 152 ms                                                       | 124 ms: 1.23x faster                                                                  |
| comprehensions           | 26.9 us                                                      | 22.1 us: 1.22x faster                                                                 |
| scimark_sor              | 177 ms                                                       | 146 ms: 1.21x faster                                                                  |
| nqueens                  | 112 ms                                                       | 93.9 ms: 1.20x faster                                                                 |
| bench_thread_pool        | 1.14 ms                                                      | 951 us: 1.19x faster                                                                  |
| sqlglot_optimize         | 70.3 ms                                                      | 58.9 ms: 1.19x faster                                                                 |
| mdp                      | 3.03 sec                                                     | 2.56 sec: 1.18x faster                                                                |
| deepcopy                 | 454 us                                                       | 384 us: 1.18x faster                                                                  |
| json_loads               | 30.0 us                                                      | 25.6 us: 1.17x faster                                                                 |
| dulwich_log              | 80.1 ms                                                      | 68.4 ms: 1.17x faster                                                                 |
| deepcopy_reduce          | 4.03 us                                                      | 3.46 us: 1.17x faster                                                                 |
| docutils                 | 3.40 sec                                                     | 2.93 sec: 1.16x faster                                                                |
| scimark_fft              | 359 ms                                                       | 313 ms: 1.15x faster                                                                  |
| json                     | 5.96 ms                                                      | 5.19 ms: 1.15x faster                                                                 |
| unpack_sequence          | 59.5 ns                                                      | 52.5 ns: 1.13x faster                                                                 |
| create_gc_cycles         | 1.82 ms                                                      | 1.61 ms: 1.13x faster                                                                 |
| regex_v8                 | 26.6 ms                                                      | 23.8 ms: 1.12x faster                                                                 |
| pathlib                  | 21.7 ms                                                      | 19.6 ms: 1.10x faster                                                                 |
| xml_etree_generate       | 94.6 ms                                                      | 87.1 ms: 1.09x faster                                                                 |
| xml_etree_parse          | 162 ms                                                       | 150 ms: 1.07x faster                                                                  |
| async_generators         | 422 ms                                                       | 393 ms: 1.07x faster                                                                  |
| regex_dna                | 259 ms                                                       | 242 ms: 1.07x faster                                                                  |
| sqlite_synth             | 2.97 us                                                      | 2.77 us: 1.07x faster                                                                 |
| meteor_contest           | 137 ms                                                       | 129 ms: 1.06x faster                                                                  |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 107 ms: 1.03x faster                                                                  |
| python_startup           | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                                 |
| unpickle                 | 14.2 us                                                      | 14.4 us: 1.01x slower                                                                 |
| gc_traversal             | 3.45 ms                                                      | 3.57 ms: 1.03x slower                                                                 |
| pickle                   | 9.94 us                                                      | 10.4 us: 1.05x slower                                                                 |
| unpickle_list            | 4.49 us                                                      | 4.71 us: 1.05x slower                                                                 |
| pickle_list              | 4.11 us                                                      | 4.38 us: 1.07x slower                                                                 |
| telco                    | 7.14 ms                                                      | 7.76 ms: 1.09x slower                                                                 |
| pickle_dict              | 30.0 us                                                      | 32.7 us: 1.09x slower                                                                 |
| python_startup_no_site   | 7.32 ms                                                      | 8.38 ms: 1.14x slower                                                                 |
| regex_effbot             | 2.99 ms                                                      | 3.56 ms: 1.19x slower                                                                 |
| dask                     | 463 ms                                                       | 592 ms: 1.28x slower                                                                  |
| coverage                 | 64.0 ms                                                      | 86.9 ms: 1.36x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                          |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x
