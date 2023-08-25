
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: bef1c87
- commit date: 2023-06-25
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-pythonperf2-x86_64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                      |
| tornado_http   | 152 ms                                                       | 121 ms: 1.26x faster                                        |
| Geometric mean | (ref)                                                        | 1.22x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-pythonperf2-x86_64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 137 ms                                                       | 92.5 ms: 1.48x faster                                       |
| float          | 110 ms                                                       | 79.0 ms: 1.40x faster                                       |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-pythonperf2-x86_64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 144 ms: 1.34x faster                                        |
| regex_v8       | 26.6 ms                                                      | 24.4 ms: 1.09x faster                                       |
| regex_dna      | 259 ms                                                       | 249 ms: 1.04x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.56 ms: 1.19x slower                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-pythonperf2-x86_64-python-main-3.13.0a0-bef1c87 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 216 us: 1.49x faster                                        |
| pickle_pure_python   | 457 us                                                       | 323 us: 1.42x faster                                        |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                       |
| tomli_loads          | 2.97 sec                                                     | 2.25 sec: 1.32x faster                                      |
| xml_etree_process    | 76.0 ms                                                      | 59.2 ms: 1.28x faster                                       |
| json_loads           | 30.0 us                                                      | 24.2 us: 1.24x faster                                       |
| xml_etree_generate   | 94.6 ms                                                      | 86.3 ms: 1.10x faster                                       |
| xml_etree_parse      | 162 ms                                                       | 152 ms: 1.06x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                        |
| pickle               | 9.94 us                                                      | 10.0 us: 1.01x slower                                       |
| unpickle             | 14.2 us                                                      | 14.5 us: 1.03x slower                                       |
| pickle_dict          | 30.0 us                                                      | 31.7 us: 1.06x slower                                       |
| unpickle_list        | 4.49 us                                                      | 4.86 us: 1.08x slower                                       |
| pickle_list          | 4.11 us                                                      | 4.45 us: 1.08x slower                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-pythonperf2-x86_64-python-main-3.13.0a0-bef1c87 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.2 ms: 1.02x faster                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.33 ms: 1.14x slower                                       |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-pythonperf2-x86_64-python-main-3.13.0a0-bef1c87 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-pythonperf2-x86_64-python-main-3.13.0a0-bef1c87 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 153 us: 3.42x faster                                        |
| deltablue                | 7.47 ms                                                      | 3.22 ms: 2.32x faster                                       |
| asyncio_tcp              | 782 ms                                                       | 379 ms: 2.06x faster                                        |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                      |
| raytrace                 | 488 ms                                                       | 270 ms: 1.81x faster                                        |
| chaos                    | 107 ms                                                       | 60.6 ms: 1.77x faster                                       |
| logging_silent           | 166 ns                                                       | 93.9 ns: 1.76x faster                                       |
| scimark_lu               | 164 ms                                                       | 93.0 ms: 1.76x faster                                       |
| go                       | 259 ms                                                       | 147 ms: 1.76x faster                                        |
| richards_super           | 90.8 ms                                                      | 52.2 ms: 1.74x faster                                       |
| scimark_sor              | 177 ms                                                       | 107 ms: 1.66x faster                                        |
| hexiom                   | 9.52 ms                                                      | 5.81 ms: 1.64x faster                                       |
| richards                 | 74.1 ms                                                      | 45.4 ms: 1.63x faster                                       |
| sqlglot_parse            | 2.26 ms                                                      | 1.41 ms: 1.60x faster                                       |
| scimark_monte_carlo      | 109 ms                                                       | 69.7 ms: 1.57x faster                                       |
| generators               | 58.0 ms                                                      | 37.0 ms: 1.57x faster                                       |
| pyflate                  | 697 ms                                                       | 445 ms: 1.57x faster                                        |
| spectral_norm            | 136 ms                                                       | 88.1 ms: 1.55x faster                                       |
| sqlglot_transpile        | 2.71 ms                                                      | 1.81 ms: 1.50x faster                                       |
| async_tree_io            | 1.61 sec                                                     | 1.08 sec: 1.49x faster                                      |
| async_tree_none          | 700 ms                                                       | 469 ms: 1.49x faster                                        |
| unpickle_pure_python     | 321 us                                                       | 216 us: 1.49x faster                                        |
| nbody                    | 137 ms                                                       | 92.5 ms: 1.48x faster                                       |
| async_tree_memoization   | 824 ms                                                       | 563 ms: 1.46x faster                                        |
| crypto_pyaes             | 118 ms                                                       | 82.0 ms: 1.44x faster                                       |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                       |
| pickle_pure_python       | 457 us                                                       | 323 us: 1.42x faster                                        |
| fannkuch                 | 496 ms                                                       | 353 ms: 1.40x faster                                        |
| float                    | 110 ms                                                       | 79.0 ms: 1.40x faster                                       |
| json_dumps               | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                       |
| coroutines               | 30.4 ms                                                      | 21.9 ms: 1.39x faster                                       |
| regex_compile            | 194 ms                                                       | 144 ms: 1.34x faster                                        |
| logging_simple           | 8.90 us                                                      | 6.65 us: 1.34x faster                                       |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 713 ms: 1.33x faster                                        |
| tomli_loads              | 2.97 sec                                                     | 2.25 sec: 1.32x faster                                      |
| logging_format           | 9.57 us                                                      | 7.24 us: 1.32x faster                                       |
| pycparser                | 1.66 sec                                                     | 1.28 sec: 1.29x faster                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                      |
| xml_etree_process        | 76.0 ms                                                      | 59.2 ms: 1.28x faster                                       |
| deepcopy_memo            | 48.9 us                                                      | 38.1 us: 1.28x faster                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 820 ms: 1.28x faster                                        |
| mypy2                    | 466 ms                                                       | 369 ms: 1.27x faster                                        |
| tornado_http             | 152 ms                                                       | 121 ms: 1.26x faster                                        |
| nqueens                  | 112 ms                                                       | 89.8 ms: 1.25x faster                                       |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.25x faster                                        |
| comprehensions           | 26.9 us                                                      | 21.7 us: 1.24x faster                                       |
| json_loads               | 30.0 us                                                      | 24.2 us: 1.24x faster                                       |
| scimark_fft              | 359 ms                                                       | 296 ms: 1.21x faster                                        |
| sqlglot_optimize         | 70.3 ms                                                      | 57.9 ms: 1.21x faster                                       |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.29 ms: 1.21x faster                                       |
| mdp                      | 3.03 sec                                                     | 2.52 sec: 1.21x faster                                      |
| bench_thread_pool        | 1.14 ms                                                      | 955 us: 1.19x faster                                        |
| dulwich_log              | 80.1 ms                                                      | 67.3 ms: 1.19x faster                                       |
| deepcopy                 | 454 us                                                       | 382 us: 1.19x faster                                        |
| unpack_sequence          | 59.5 ns                                                      | 50.3 ns: 1.18x faster                                       |
| json                     | 5.96 ms                                                      | 5.06 ms: 1.18x faster                                       |
| docutils                 | 3.40 sec                                                     | 2.89 sec: 1.18x faster                                      |
| deepcopy_reduce          | 4.03 us                                                      | 3.44 us: 1.17x faster                                       |
| create_gc_cycles         | 1.82 ms                                                      | 1.62 ms: 1.12x faster                                       |
| pathlib                  | 21.7 ms                                                      | 19.7 ms: 1.10x faster                                       |
| xml_etree_generate       | 94.6 ms                                                      | 86.3 ms: 1.10x faster                                       |
| regex_v8                 | 26.6 ms                                                      | 24.4 ms: 1.09x faster                                       |
| sqlite_synth             | 2.97 us                                                      | 2.73 us: 1.09x faster                                       |
| async_generators         | 422 ms                                                       | 389 ms: 1.08x faster                                        |
| meteor_contest           | 137 ms                                                       | 127 ms: 1.08x faster                                        |
| xml_etree_parse          | 162 ms                                                       | 152 ms: 1.06x faster                                        |
| regex_dna                | 259 ms                                                       | 249 ms: 1.04x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                        |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| python_startup           | 11.5 ms                                                      | 11.2 ms: 1.02x faster                                       |
| pickle                   | 9.94 us                                                      | 10.0 us: 1.01x slower                                       |
| telco                    | 7.14 ms                                                      | 7.28 ms: 1.02x slower                                       |
| unpickle                 | 14.2 us                                                      | 14.5 us: 1.03x slower                                       |
| gc_traversal             | 3.45 ms                                                      | 3.54 ms: 1.03x slower                                       |
| pickle_dict              | 30.0 us                                                      | 31.7 us: 1.06x slower                                       |
| unpickle_list            | 4.49 us                                                      | 4.86 us: 1.08x slower                                       |
| pickle_list              | 4.11 us                                                      | 4.45 us: 1.08x slower                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.33 ms: 1.14x slower                                       |
| regex_effbot             | 2.99 ms                                                      | 3.56 ms: 1.19x slower                                       |
| coverage                 | 64.0 ms                                                      | 91.2 ms: 1.43x slower                                       |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x
