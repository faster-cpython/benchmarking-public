# Results vs. 3.10.4

- fork: faster-cpython
- ref: dynamic_underflow
- machine: linux-x86_64
- commit hash: 6f75dbe
- commit date: 2024-05-04
- overall geometric mean: 1.06x faster
- HPT reliability: 91.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| chameleon      | 9.44 ms                                                      | 8.59 ms: 1.10x faster                                                               |
| tornado_http   | 157 ms                                                       | 141 ms: 1.11x faster                                                                |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 391 ms: 1.77x faster                                                                |
| async_tree_io           | 1.60 sec                                                     | 937 ms: 1.70x faster                                                                |
| async_tree_memoization  | 819 ms                                                       | 496 ms: 1.65x faster                                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 644 ms: 1.45x faster                                                                |
| Geometric mean          | (ref)                                                        | 1.64x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 98.7 ms: 1.13x faster                                                               |
| pidigits       | 271 ms                                                       | 259 ms: 1.04x faster                                                                |
| nbody          | 134 ms                                                       | 130 ms: 1.03x faster                                                                |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 246 ms: 1.06x faster                                                                |
| regex_v8       | 27.2 ms                                                      | 27.0 ms: 1.01x faster                                                               |
| regex_effbot   | 3.09 ms                                                      | 3.58 ms: 1.16x slower                                                               |
| regex_compile  | 190 ms                                                       | 231 ms: 1.22x slower                                                                |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                               |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                                               |
| xml_etree_process    | 75.9 ms                                                      | 68.1 ms: 1.11x faster                                                               |
| xml_etree_parse      | 160 ms                                                       | 147 ms: 1.09x faster                                                                |
| unpickle_list        | 4.65 us                                                      | 4.72 us: 1.02x slower                                                               |
| pickle_pure_python   | 455 us                                                       | 471 us: 1.04x slower                                                                |
| xml_etree_iterparse  | 110 ms                                                       | 116 ms: 1.05x slower                                                                |
| xml_etree_generate   | 92.3 ms                                                      | 99.2 ms: 1.07x slower                                                               |
| pickle_list          | 4.12 us                                                      | 4.44 us: 1.08x slower                                                               |
| pickle               | 9.89 us                                                      | 10.7 us: 1.08x slower                                                               |
| unpickle_pure_python | 312 us                                                       | 338 us: 1.08x slower                                                                |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.10x slower                                                               |
| pickle_dict          | 29.5 us                                                      | 32.9 us: 1.12x slower                                                               |
| tomli_loads          | 2.92 sec                                                     | 3.36 sec: 1.15x slower                                                              |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.0 ms: 1.13x slower                                                               |
| python_startup_no_site | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.18x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 47.5 ms: 1.06x faster                                                               |
| mako            | 14.7 ms                                                      | 14.3 ms: 1.03x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 204 us: 2.63x faster                                                                |
| asyncio_tcp              | 779 ms                                                       | 395 ms: 1.97x faster                                                                |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.60 sec: 1.94x faster                                                              |
| async_tree_none          | 692 ms                                                       | 391 ms: 1.77x faster                                                                |
| async_tree_io            | 1.60 sec                                                     | 937 ms: 1.70x faster                                                                |
| async_tree_memoization   | 819 ms                                                       | 496 ms: 1.65x faster                                                                |
| generators               | 57.3 ms                                                      | 35.6 ms: 1.61x faster                                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 644 ms: 1.45x faster                                                                |
| raytrace                 | 489 ms                                                       | 360 ms: 1.36x faster                                                                |
| chaos                    | 109 ms                                                       | 81.9 ms: 1.33x faster                                                               |
| bench_mp_pool            | 6.37 ms                                                      | 4.90 ms: 1.30x faster                                                               |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                               |
| coroutines               | 30.3 ms                                                      | 23.4 ms: 1.30x faster                                                               |
| thrift                   | 1.18 ms                                                      | 914 us: 1.29x faster                                                                |
| sqlglot_parse            | 2.24 ms                                                      | 1.77 ms: 1.27x faster                                                               |
| crypto_pyaes             | 119 ms                                                       | 94.8 ms: 1.26x faster                                                               |
| logging_format           | 9.64 us                                                      | 7.69 us: 1.25x faster                                                               |
| logging_simple           | 8.88 us                                                      | 7.09 us: 1.25x faster                                                               |
| pylint                   | 566 ms                                                       | 457 ms: 1.24x faster                                                                |
| json_loads               | 30.3 us                                                      | 24.5 us: 1.24x faster                                                               |
| deltablue                | 7.50 ms                                                      | 6.15 ms: 1.22x faster                                                               |
| go                       | 262 ms                                                       | 217 ms: 1.21x faster                                                                |
| sqlglot_transpile        | 2.68 ms                                                      | 2.26 ms: 1.19x faster                                                               |
| pyflate                  | 733 ms                                                       | 632 ms: 1.16x faster                                                                |
| pathlib                  | 21.4 ms                                                      | 18.5 ms: 1.15x faster                                                               |
| richards_super           | 90.6 ms                                                      | 79.8 ms: 1.14x faster                                                               |
| float                    | 111 ms                                                       | 98.7 ms: 1.13x faster                                                               |
| xml_etree_process        | 75.9 ms                                                      | 68.1 ms: 1.11x faster                                                               |
| tornado_http             | 157 ms                                                       | 141 ms: 1.11x faster                                                                |
| scimark_lu               | 167 ms                                                       | 151 ms: 1.10x faster                                                                |
| mdp                      | 3.01 sec                                                     | 2.73 sec: 1.10x faster                                                              |
| chameleon                | 9.44 ms                                                      | 8.59 ms: 1.10x faster                                                               |
| scimark_sor              | 180 ms                                                       | 165 ms: 1.09x faster                                                                |
| xml_etree_parse          | 160 ms                                                       | 147 ms: 1.09x faster                                                                |
| bench_thread_pool        | 1.14 ms                                                      | 1.05 ms: 1.08x faster                                                               |
| pycparser                | 1.67 sec                                                     | 1.55 sec: 1.08x faster                                                              |
| dask                     | 472 ms                                                       | 441 ms: 1.07x faster                                                                |
| json                     | 5.86 ms                                                      | 5.50 ms: 1.07x faster                                                               |
| regex_dna                | 261 ms                                                       | 246 ms: 1.06x faster                                                                |
| django_template          | 50.2 ms                                                      | 47.5 ms: 1.06x faster                                                               |
| pidigits                 | 271 ms                                                       | 259 ms: 1.04x faster                                                                |
| async_generators         | 421 ms                                                       | 403 ms: 1.04x faster                                                                |
| richards                 | 75.1 ms                                                      | 72.0 ms: 1.04x faster                                                               |
| nbody                    | 134 ms                                                       | 130 ms: 1.03x faster                                                                |
| mako                     | 14.7 ms                                                      | 14.3 ms: 1.03x faster                                                               |
| sqlite_synth             | 2.99 us                                                      | 2.93 us: 1.02x faster                                                               |
| regex_v8                 | 27.2 ms                                                      | 27.0 ms: 1.01x faster                                                               |
| asyncio_websockets       | 390 ms                                                       | 395 ms: 1.01x slower                                                                |
| unpickle_list            | 4.65 us                                                      | 4.72 us: 1.02x slower                                                               |
| scimark_monte_carlo      | 107 ms                                                       | 109 ms: 1.02x slower                                                                |
| fannkuch                 | 483 ms                                                       | 497 ms: 1.03x slower                                                                |
| deepcopy_reduce          | 4.01 us                                                      | 4.14 us: 1.03x slower                                                               |
| pickle_pure_python       | 455 us                                                       | 471 us: 1.04x slower                                                                |
| deepcopy                 | 468 us                                                       | 485 us: 1.04x slower                                                                |
| comprehensions           | 26.7 us                                                      | 27.7 us: 1.04x slower                                                               |
| pprint_pformat           | 2.15 sec                                                     | 2.24 sec: 1.04x slower                                                              |
| pprint_safe_repr         | 1.05 sec                                                     | 1.10 sec: 1.05x slower                                                              |
| xml_etree_iterparse      | 110 ms                                                       | 116 ms: 1.05x slower                                                                |
| spectral_norm            | 139 ms                                                       | 147 ms: 1.06x slower                                                                |
| sqlglot_optimize         | 70.1 ms                                                      | 74.6 ms: 1.06x slower                                                               |
| nqueens                  | 115 ms                                                       | 122 ms: 1.06x slower                                                                |
| xml_etree_generate       | 92.3 ms                                                      | 99.2 ms: 1.07x slower                                                               |
| pickle_list              | 4.12 us                                                      | 4.44 us: 1.08x slower                                                               |
| sqlglot_normalize        | 144 ms                                                       | 155 ms: 1.08x slower                                                                |
| meteor_contest           | 138 ms                                                       | 149 ms: 1.08x slower                                                                |
| pickle                   | 9.89 us                                                      | 10.7 us: 1.08x slower                                                               |
| unpickle_pure_python     | 312 us                                                       | 338 us: 1.08x slower                                                                |
| mypy2                    | 933 ms                                                       | 1.01 sec: 1.09x slower                                                              |
| sympy_integrate          | 28.2 ms                                                      | 30.6 ms: 1.09x slower                                                               |
| gunicorn                 | 1.16 ms                                                      | 1.26 ms: 1.09x slower                                                               |
| sympy_sum                | 193 ms                                                       | 211 ms: 1.10x slower                                                                |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.10x slower                                                               |
| aiohttp                  | 1.19 ms                                                      | 1.31 ms: 1.10x slower                                                               |
| logging_silent           | 167 ns                                                       | 185 ns: 1.10x slower                                                                |
| pickle_dict              | 29.5 us                                                      | 32.9 us: 1.12x slower                                                               |
| dulwich_log              | 81.1 ms                                                      | 91.1 ms: 1.12x slower                                                               |
| python_startup           | 11.5 ms                                                      | 13.0 ms: 1.13x slower                                                               |
| tomli_loads              | 2.92 sec                                                     | 3.36 sec: 1.15x slower                                                              |
| hexiom                   | 9.42 ms                                                      | 10.9 ms: 1.15x slower                                                               |
| sympy_str                | 360 ms                                                       | 417 ms: 1.16x slower                                                                |
| regex_effbot             | 3.09 ms                                                      | 3.58 ms: 1.16x slower                                                               |
| sympy_expand             | 600 ms                                                       | 698 ms: 1.16x slower                                                                |
| create_gc_cycles         | 1.76 ms                                                      | 2.06 ms: 1.17x slower                                                               |
| flaskblogging            | 4.39 ms                                                      | 5.19 ms: 1.18x slower                                                               |
| scimark_fft              | 361 ms                                                       | 428 ms: 1.18x slower                                                                |
| regex_compile            | 190 ms                                                       | 231 ms: 1.22x slower                                                                |
| python_startup_no_site   | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                               |
| deepcopy_memo            | 49.8 us                                                      | 61.3 us: 1.23x slower                                                               |
| coverage                 | 63.3 ms                                                      | 78.1 ms: 1.23x slower                                                               |
| telco                    | 7.23 ms                                                      | 9.15 ms: 1.27x slower                                                               |
| gc_traversal             | 3.42 ms                                                      | 4.52 ms: 1.32x slower                                                               |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.82 ms: 1.34x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.06x faster                                                                        |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, docutils, genshi_text, genshi_xml, html5lib, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240504-3.13.0a6+-6f75dbe-PYTHON_UOPS/bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 91.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.13x