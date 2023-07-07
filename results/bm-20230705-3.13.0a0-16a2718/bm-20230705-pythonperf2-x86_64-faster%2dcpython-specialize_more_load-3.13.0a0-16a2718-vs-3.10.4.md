
# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_more_load
- machine: linux-x86_64
- commit hash: 16a2718
- commit date: 2023-07-05
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.92 sec: 1.17x faster                                                                |
| tornado_http   | 152 ms                                                       | 121 ms: 1.26x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 89.1 ms: 1.54x faster                                                                 |
| float          | 110 ms                                                       | 81.3 ms: 1.36x faster                                                                 |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 151 ms: 1.28x faster                                                                  |
| regex_v8       | 26.6 ms                                                      | 24.2 ms: 1.10x faster                                                                 |
| regex_dna      | 259 ms                                                       | 241 ms: 1.08x faster                                                                  |
| regex_effbot   | 2.99 ms                                                      | 3.58 ms: 1.20x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 219 us: 1.47x faster                                                                  |
| pickle_pure_python   | 457 us                                                       | 316 us: 1.45x faster                                                                  |
| json_dumps           | 14.2 ms                                                      | 10.1 ms: 1.41x faster                                                                 |
| xml_etree_process    | 76.0 ms                                                      | 58.8 ms: 1.29x faster                                                                 |
| tomli_loads          | 2.97 sec                                                     | 2.40 sec: 1.24x faster                                                                |
| json_loads           | 30.0 us                                                      | 24.9 us: 1.20x faster                                                                 |
| xml_etree_parse      | 162 ms                                                       | 145 ms: 1.11x faster                                                                  |
| xml_etree_generate   | 94.6 ms                                                      | 85.4 ms: 1.11x faster                                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                                                  |
| unpickle_list        | 4.49 us                                                      | 4.61 us: 1.03x slower                                                                 |
| pickle               | 9.94 us                                                      | 10.2 us: 1.03x slower                                                                 |
| unpickle             | 14.2 us                                                      | 14.6 us: 1.03x slower                                                                 |
| pickle_dict          | 30.0 us                                                      | 31.4 us: 1.05x slower                                                                 |
| pickle_list          | 4.11 us                                                      | 4.34 us: 1.06x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                                 |
| python_startup_no_site | 7.32 ms                                                      | 8.39 ms: 1.15x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 154 us: 3.39x faster                                                                  |
| deltablue                | 7.47 ms                                                      | 3.61 ms: 2.07x faster                                                                 |
| asyncio_tcp              | 782 ms                                                       | 382 ms: 2.05x faster                                                                  |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                                                |
| raytrace                 | 488 ms                                                       | 275 ms: 1.77x faster                                                                  |
| chaos                    | 107 ms                                                       | 61.4 ms: 1.74x faster                                                                 |
| logging_silent           | 166 ns                                                       | 96.5 ns: 1.72x faster                                                                 |
| scimark_lu               | 164 ms                                                       | 98.8 ms: 1.66x faster                                                                 |
| scimark_monte_carlo      | 109 ms                                                       | 67.9 ms: 1.61x faster                                                                 |
| crypto_pyaes             | 118 ms                                                       | 74.1 ms: 1.60x faster                                                                 |
| generators               | 58.0 ms                                                      | 37.1 ms: 1.56x faster                                                                 |
| sqlglot_parse            | 2.26 ms                                                      | 1.45 ms: 1.56x faster                                                                 |
| richards_super           | 90.8 ms                                                      | 58.9 ms: 1.54x faster                                                                 |
| nbody                    | 137 ms                                                       | 89.1 ms: 1.54x faster                                                                 |
| async_tree_none          | 700 ms                                                       | 469 ms: 1.49x faster                                                                  |
| go                       | 259 ms                                                       | 174 ms: 1.49x faster                                                                  |
| async_tree_io            | 1.61 sec                                                     | 1.08 sec: 1.48x faster                                                                |
| hexiom                   | 9.52 ms                                                      | 6.48 ms: 1.47x faster                                                                 |
| unpickle_pure_python     | 321 us                                                       | 219 us: 1.47x faster                                                                  |
| sqlglot_transpile        | 2.71 ms                                                      | 1.85 ms: 1.46x faster                                                                 |
| async_tree_memoization   | 824 ms                                                       | 565 ms: 1.46x faster                                                                  |
| mako                     | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                                                 |
| pickle_pure_python       | 457 us                                                       | 316 us: 1.45x faster                                                                  |
| spectral_norm            | 136 ms                                                       | 96.1 ms: 1.42x faster                                                                 |
| json_dumps               | 14.2 ms                                                      | 10.1 ms: 1.41x faster                                                                 |
| richards                 | 74.1 ms                                                      | 53.0 ms: 1.40x faster                                                                 |
| pyflate                  | 697 ms                                                       | 514 ms: 1.36x faster                                                                  |
| float                    | 110 ms                                                       | 81.3 ms: 1.36x faster                                                                 |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 716 ms: 1.33x faster                                                                  |
| coroutines               | 30.4 ms                                                      | 23.2 ms: 1.31x faster                                                                 |
| logging_simple           | 8.90 us                                                      | 6.83 us: 1.30x faster                                                                 |
| xml_etree_process        | 76.0 ms                                                      | 58.8 ms: 1.29x faster                                                                 |
| logging_format           | 9.57 us                                                      | 7.41 us: 1.29x faster                                                                 |
| deepcopy_memo            | 48.9 us                                                      | 38.1 us: 1.28x faster                                                                 |
| regex_compile            | 194 ms                                                       | 151 ms: 1.28x faster                                                                  |
| unpack_sequence          | 59.5 ns                                                      | 46.8 ns: 1.27x faster                                                                 |
| pprint_pformat           | 2.15 sec                                                     | 1.70 sec: 1.27x faster                                                                |
| pycparser                | 1.66 sec                                                     | 1.31 sec: 1.27x faster                                                                |
| tornado_http             | 152 ms                                                       | 121 ms: 1.26x faster                                                                  |
| mypy2                    | 466 ms                                                       | 371 ms: 1.26x faster                                                                  |
| pprint_safe_repr         | 1.05 sec                                                     | 841 ms: 1.25x faster                                                                  |
| tomli_loads              | 2.97 sec                                                     | 2.40 sec: 1.24x faster                                                                |
| fannkuch                 | 496 ms                                                       | 401 ms: 1.24x faster                                                                  |
| comprehensions           | 26.9 us                                                      | 22.0 us: 1.23x faster                                                                 |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                                                  |
| bench_mp_pool            | 7.18 ms                                                      | 5.93 ms: 1.21x faster                                                                 |
| nqueens                  | 112 ms                                                       | 93.2 ms: 1.21x faster                                                                 |
| scimark_sor              | 177 ms                                                       | 147 ms: 1.21x faster                                                                  |
| json_loads               | 30.0 us                                                      | 24.9 us: 1.20x faster                                                                 |
| deepcopy                 | 454 us                                                       | 381 us: 1.19x faster                                                                  |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.37 ms: 1.19x faster                                                                 |
| sqlglot_optimize         | 70.3 ms                                                      | 59.2 ms: 1.19x faster                                                                 |
| dulwich_log              | 80.1 ms                                                      | 67.7 ms: 1.18x faster                                                                 |
| mdp                      | 3.03 sec                                                     | 2.57 sec: 1.18x faster                                                                |
| deepcopy_reduce          | 4.03 us                                                      | 3.45 us: 1.17x faster                                                                 |
| docutils                 | 3.40 sec                                                     | 2.92 sec: 1.17x faster                                                                |
| bench_thread_pool        | 1.14 ms                                                      | 979 us: 1.16x faster                                                                  |
| json                     | 5.96 ms                                                      | 5.18 ms: 1.15x faster                                                                 |
| scimark_fft              | 359 ms                                                       | 315 ms: 1.14x faster                                                                  |
| xml_etree_parse          | 162 ms                                                       | 145 ms: 1.11x faster                                                                  |
| pathlib                  | 21.7 ms                                                      | 19.6 ms: 1.11x faster                                                                 |
| xml_etree_generate       | 94.6 ms                                                      | 85.4 ms: 1.11x faster                                                                 |
| regex_v8                 | 26.6 ms                                                      | 24.2 ms: 1.10x faster                                                                 |
| sqlite_synth             | 2.97 us                                                      | 2.73 us: 1.09x faster                                                                 |
| create_gc_cycles         | 1.82 ms                                                      | 1.68 ms: 1.09x faster                                                                 |
| async_generators         | 422 ms                                                       | 391 ms: 1.08x faster                                                                  |
| regex_dna                | 259 ms                                                       | 241 ms: 1.08x faster                                                                  |
| meteor_contest           | 137 ms                                                       | 130 ms: 1.06x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                                                  |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                                                  |
| python_startup           | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                                 |
| gc_traversal             | 3.45 ms                                                      | 3.53 ms: 1.02x slower                                                                 |
| unpickle_list            | 4.49 us                                                      | 4.61 us: 1.03x slower                                                                 |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.03x slower                                                                 |
| unpickle                 | 14.2 us                                                      | 14.6 us: 1.03x slower                                                                 |
| pickle_dict              | 30.0 us                                                      | 31.4 us: 1.05x slower                                                                 |
| pickle_list              | 4.11 us                                                      | 4.34 us: 1.06x slower                                                                 |
| telco                    | 7.14 ms                                                      | 7.96 ms: 1.11x slower                                                                 |
| python_startup_no_site   | 7.32 ms                                                      | 8.39 ms: 1.15x slower                                                                 |
| regex_effbot             | 2.99 ms                                                      | 3.58 ms: 1.20x slower                                                                 |
| dask                     | 463 ms                                                       | 590 ms: 1.27x slower                                                                  |
| coverage                 | 64.0 ms                                                      | 89.2 ms: 1.39x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                                          |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
