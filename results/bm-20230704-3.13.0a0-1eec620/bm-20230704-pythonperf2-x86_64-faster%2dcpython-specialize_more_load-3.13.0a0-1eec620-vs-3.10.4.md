
# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_more_load
- machine: linux-x86_64
- commit hash: 1eec620
- commit date: 2023-07-04
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.93 sec: 1.16x faster                                                                |
| tornado_http   | 152 ms                                                       | 122 ms: 1.25x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 89.6 ms: 1.53x faster                                                                 |
| float          | 110 ms                                                       | 80.3 ms: 1.37x faster                                                                 |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 149 ms: 1.30x faster                                                                  |
| regex_v8       | 26.6 ms                                                      | 24.9 ms: 1.07x faster                                                                 |
| regex_dna      | 259 ms                                                       | 246 ms: 1.05x faster                                                                  |
| regex_effbot   | 2.99 ms                                                      | 3.65 ms: 1.22x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 220 us: 1.46x faster                                                                  |
| pickle_pure_python   | 457 us                                                       | 314 us: 1.46x faster                                                                  |
| json_dumps           | 14.2 ms                                                      | 10.0 ms: 1.42x faster                                                                 |
| xml_etree_process    | 76.0 ms                                                      | 58.4 ms: 1.30x faster                                                                 |
| tomli_loads          | 2.97 sec                                                     | 2.34 sec: 1.27x faster                                                                |
| json_loads           | 30.0 us                                                      | 24.7 us: 1.21x faster                                                                 |
| xml_etree_parse      | 162 ms                                                       | 146 ms: 1.11x faster                                                                  |
| xml_etree_generate   | 94.6 ms                                                      | 85.8 ms: 1.10x faster                                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                                                  |
| unpickle             | 14.2 us                                                      | 14.6 us: 1.03x slower                                                                 |
| pickle               | 9.94 us                                                      | 10.2 us: 1.03x slower                                                                 |
| unpickle_list        | 4.49 us                                                      | 4.65 us: 1.03x slower                                                                 |
| pickle_list          | 4.11 us                                                      | 4.36 us: 1.06x slower                                                                 |
| pickle_dict          | 30.0 us                                                      | 31.9 us: 1.06x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                                 |
| python_startup_no_site | 7.32 ms                                                      | 8.37 ms: 1.14x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 151 us: 3.47x faster                                                                  |
| deltablue                | 7.47 ms                                                      | 3.57 ms: 2.09x faster                                                                 |
| asyncio_tcp              | 782 ms                                                       | 383 ms: 2.04x faster                                                                  |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                                                |
| raytrace                 | 488 ms                                                       | 275 ms: 1.78x faster                                                                  |
| chaos                    | 107 ms                                                       | 61.7 ms: 1.74x faster                                                                 |
| logging_silent           | 166 ns                                                       | 97.5 ns: 1.70x faster                                                                 |
| scimark_lu               | 164 ms                                                       | 98.8 ms: 1.66x faster                                                                 |
| crypto_pyaes             | 118 ms                                                       | 73.6 ms: 1.61x faster                                                                 |
| sqlglot_parse            | 2.26 ms                                                      | 1.43 ms: 1.58x faster                                                                 |
| generators               | 58.0 ms                                                      | 37.6 ms: 1.54x faster                                                                 |
| scimark_monte_carlo      | 109 ms                                                       | 71.5 ms: 1.53x faster                                                                 |
| nbody                    | 137 ms                                                       | 89.6 ms: 1.53x faster                                                                 |
| richards_super           | 90.8 ms                                                      | 59.7 ms: 1.52x faster                                                                 |
| go                       | 259 ms                                                       | 172 ms: 1.51x faster                                                                  |
| async_tree_none          | 700 ms                                                       | 466 ms: 1.50x faster                                                                  |
| async_tree_io            | 1.61 sec                                                     | 1.08 sec: 1.49x faster                                                                |
| sqlglot_transpile        | 2.71 ms                                                      | 1.85 ms: 1.47x faster                                                                 |
| hexiom                   | 9.52 ms                                                      | 6.49 ms: 1.47x faster                                                                 |
| async_tree_memoization   | 824 ms                                                       | 562 ms: 1.47x faster                                                                  |
| unpickle_pure_python     | 321 us                                                       | 220 us: 1.46x faster                                                                  |
| pickle_pure_python       | 457 us                                                       | 314 us: 1.46x faster                                                                  |
| mako                     | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                                                 |
| spectral_norm            | 136 ms                                                       | 94.5 ms: 1.44x faster                                                                 |
| json_dumps               | 14.2 ms                                                      | 10.0 ms: 1.42x faster                                                                 |
| richards                 | 74.1 ms                                                      | 53.5 ms: 1.38x faster                                                                 |
| float                    | 110 ms                                                       | 80.3 ms: 1.37x faster                                                                 |
| pyflate                  | 697 ms                                                       | 513 ms: 1.36x faster                                                                  |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 713 ms: 1.33x faster                                                                  |
| deepcopy_memo            | 48.9 us                                                      | 36.8 us: 1.33x faster                                                                 |
| coroutines               | 30.4 ms                                                      | 23.2 ms: 1.31x faster                                                                 |
| xml_etree_process        | 76.0 ms                                                      | 58.4 ms: 1.30x faster                                                                 |
| regex_compile            | 194 ms                                                       | 149 ms: 1.30x faster                                                                  |
| logging_simple           | 8.90 us                                                      | 6.94 us: 1.28x faster                                                                 |
| tomli_loads              | 2.97 sec                                                     | 2.34 sec: 1.27x faster                                                                |
| unpack_sequence          | 59.5 ns                                                      | 46.9 ns: 1.27x faster                                                                 |
| logging_format           | 9.57 us                                                      | 7.59 us: 1.26x faster                                                                 |
| pprint_pformat           | 2.15 sec                                                     | 1.71 sec: 1.26x faster                                                                |
| mypy2                    | 466 ms                                                       | 371 ms: 1.26x faster                                                                  |
| pycparser                | 1.66 sec                                                     | 1.33 sec: 1.25x faster                                                                |
| tornado_http             | 152 ms                                                       | 122 ms: 1.25x faster                                                                  |
| pprint_safe_repr         | 1.05 sec                                                     | 840 ms: 1.25x faster                                                                  |
| fannkuch                 | 496 ms                                                       | 397 ms: 1.25x faster                                                                  |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.23x faster                                                                  |
| bench_mp_pool            | 7.18 ms                                                      | 5.86 ms: 1.22x faster                                                                 |
| comprehensions           | 26.9 us                                                      | 22.0 us: 1.22x faster                                                                 |
| scimark_sor              | 177 ms                                                       | 145 ms: 1.22x faster                                                                  |
| deepcopy                 | 454 us                                                       | 373 us: 1.22x faster                                                                  |
| json_loads               | 30.0 us                                                      | 24.7 us: 1.21x faster                                                                 |
| nqueens                  | 112 ms                                                       | 92.9 ms: 1.21x faster                                                                 |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.37 ms: 1.19x faster                                                                 |
| bench_thread_pool        | 1.14 ms                                                      | 956 us: 1.19x faster                                                                  |
| mdp                      | 3.03 sec                                                     | 2.55 sec: 1.19x faster                                                                |
| sqlglot_optimize         | 70.3 ms                                                      | 59.2 ms: 1.19x faster                                                                 |
| dulwich_log              | 80.1 ms                                                      | 67.6 ms: 1.18x faster                                                                 |
| deepcopy_reduce          | 4.03 us                                                      | 3.42 us: 1.18x faster                                                                 |
| docutils                 | 3.40 sec                                                     | 2.93 sec: 1.16x faster                                                                |
| json                     | 5.96 ms                                                      | 5.17 ms: 1.15x faster                                                                 |
| scimark_fft              | 359 ms                                                       | 317 ms: 1.14x faster                                                                  |
| pathlib                  | 21.7 ms                                                      | 19.4 ms: 1.12x faster                                                                 |
| xml_etree_parse          | 162 ms                                                       | 146 ms: 1.11x faster                                                                  |
| xml_etree_generate       | 94.6 ms                                                      | 85.8 ms: 1.10x faster                                                                 |
| create_gc_cycles         | 1.82 ms                                                      | 1.66 ms: 1.09x faster                                                                 |
| sqlite_synth             | 2.97 us                                                      | 2.72 us: 1.09x faster                                                                 |
| async_generators         | 422 ms                                                       | 392 ms: 1.08x faster                                                                  |
| regex_v8                 | 26.6 ms                                                      | 24.9 ms: 1.07x faster                                                                 |
| regex_dna                | 259 ms                                                       | 246 ms: 1.05x faster                                                                  |
| meteor_contest           | 137 ms                                                       | 131 ms: 1.04x faster                                                                  |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                                                  |
| python_startup           | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                                 |
| unpickle                 | 14.2 us                                                      | 14.6 us: 1.03x slower                                                                 |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.03x slower                                                                 |
| unpickle_list            | 4.49 us                                                      | 4.65 us: 1.03x slower                                                                 |
| telco                    | 7.14 ms                                                      | 7.57 ms: 1.06x slower                                                                 |
| pickle_list              | 4.11 us                                                      | 4.36 us: 1.06x slower                                                                 |
| pickle_dict              | 30.0 us                                                      | 31.9 us: 1.06x slower                                                                 |
| gc_traversal             | 3.45 ms                                                      | 3.77 ms: 1.09x slower                                                                 |
| python_startup_no_site   | 7.32 ms                                                      | 8.37 ms: 1.14x slower                                                                 |
| regex_effbot             | 2.99 ms                                                      | 3.65 ms: 1.22x slower                                                                 |
| dask                     | 463 ms                                                       | 588 ms: 1.27x slower                                                                  |
| coverage                 | 64.0 ms                                                      | 92.8 ms: 1.45x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                                          |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x
