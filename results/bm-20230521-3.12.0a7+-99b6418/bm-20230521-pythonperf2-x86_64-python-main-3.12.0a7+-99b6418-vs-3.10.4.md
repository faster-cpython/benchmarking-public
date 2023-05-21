
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 99b6418
- commit date: 2023-05-21
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                         |
| docutils       | 3.40 sec                                                     | 2.87 sec: 1.19x faster                                       |
| tornado_http   | 152 ms                                                       | 115 ms: 1.32x faster                                         |
| Geometric mean | (ref)                                                        | 1.25x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 88.7 ms: 1.55x faster                                        |
| float          | 110 ms                                                       | 80.4 ms: 1.37x faster                                        |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.30x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 144 ms: 1.34x faster                                         |
| regex_v8       | 26.6 ms                                                      | 23.9 ms: 1.11x faster                                        |
| regex_dna      | 259 ms                                                       | 240 ms: 1.08x faster                                         |
| regex_effbot   | 2.99 ms                                                      | 3.47 ms: 1.16x slower                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 210 us: 1.53x faster                                         |
| pickle_pure_python   | 457 us                                                       | 321 us: 1.42x faster                                         |
| tomli_loads          | 2.97 sec                                                     | 2.15 sec: 1.38x faster                                       |
| json_dumps           | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                        |
| xml_etree_process    | 76.0 ms                                                      | 58.9 ms: 1.29x faster                                        |
| json_loads           | 30.0 us                                                      | 24.0 us: 1.25x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 147 ms: 1.10x faster                                         |
| xml_etree_generate   | 94.6 ms                                                      | 86.4 ms: 1.09x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                         |
| pickle               | 9.94 us                                                      | 10.4 us: 1.05x slower                                        |
| unpickle             | 14.2 us                                                      | 14.9 us: 1.05x slower                                        |
| pickle_list          | 4.11 us                                                      | 4.38 us: 1.07x slower                                        |
| unpickle_list        | 4.49 us                                                      | 4.82 us: 1.07x slower                                        |
| pickle_dict          | 30.0 us                                                      | 32.8 us: 1.09x slower                                        |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7+-99b6418 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.5 ms: 1.00x slower                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.52 ms: 1.16x slower                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7+-99b6418 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7+-99b6418 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 146 us: 3.58x faster                                         |
| deltablue                | 7.47 ms                                                      | 3.26 ms: 2.29x faster                                        |
| asyncio_tcp              | 782 ms                                                       | 380 ms: 2.06x faster                                         |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.57 sec: 1.97x faster                                       |
| richards_super           | 90.8 ms                                                      | 50.7 ms: 1.79x faster                                        |
| go                       | 259 ms                                                       | 149 ms: 1.74x faster                                         |
| logging_silent           | 166 ns                                                       | 96.2 ns: 1.72x faster                                        |
| chaos                    | 107 ms                                                       | 64.1 ms: 1.67x faster                                        |
| generators               | 58.0 ms                                                      | 35.5 ms: 1.63x faster                                        |
| richards                 | 74.1 ms                                                      | 45.5 ms: 1.63x faster                                        |
| sqlglot_parse            | 2.26 ms                                                      | 1.40 ms: 1.61x faster                                        |
| scimark_sor              | 177 ms                                                       | 110 ms: 1.61x faster                                         |
| scimark_lu               | 164 ms                                                       | 102 ms: 1.61x faster                                         |
| raytrace                 | 488 ms                                                       | 303 ms: 1.61x faster                                         |
| hexiom                   | 9.52 ms                                                      | 5.96 ms: 1.60x faster                                        |
| pyflate                  | 697 ms                                                       | 446 ms: 1.56x faster                                         |
| nbody                    | 137 ms                                                       | 88.7 ms: 1.55x faster                                        |
| unpickle_pure_python     | 321 us                                                       | 210 us: 1.53x faster                                         |
| scimark_monte_carlo      | 109 ms                                                       | 72.0 ms: 1.52x faster                                        |
| bench_mp_pool            | 7.18 ms                                                      | 4.73 ms: 1.52x faster                                        |
| async_tree_none          | 700 ms                                                       | 461 ms: 1.52x faster                                         |
| async_tree_io            | 1.61 sec                                                     | 1.06 sec: 1.51x faster                                       |
| sqlglot_transpile        | 2.71 ms                                                      | 1.81 ms: 1.50x faster                                        |
| spectral_norm            | 136 ms                                                       | 91.4 ms: 1.49x faster                                        |
| async_tree_memoization   | 824 ms                                                       | 554 ms: 1.49x faster                                         |
| mako                     | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                        |
| fannkuch                 | 496 ms                                                       | 345 ms: 1.44x faster                                         |
| crypto_pyaes             | 118 ms                                                       | 82.8 ms: 1.43x faster                                        |
| pickle_pure_python       | 457 us                                                       | 321 us: 1.42x faster                                         |
| tomli_loads              | 2.97 sec                                                     | 2.15 sec: 1.38x faster                                       |
| coroutines               | 30.4 ms                                                      | 22.1 ms: 1.37x faster                                        |
| float                    | 110 ms                                                       | 80.4 ms: 1.37x faster                                        |
| json_dumps               | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                        |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 706 ms: 1.35x faster                                         |
| pycparser                | 1.66 sec                                                     | 1.24 sec: 1.35x faster                                       |
| regex_compile            | 194 ms                                                       | 144 ms: 1.34x faster                                         |
| logging_simple           | 8.90 us                                                      | 6.65 us: 1.34x faster                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                       |
| tornado_http             | 152 ms                                                       | 115 ms: 1.32x faster                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 794 ms: 1.32x faster                                         |
| deepcopy_memo            | 48.9 us                                                      | 37.1 us: 1.32x faster                                        |
| logging_format           | 9.57 us                                                      | 7.36 us: 1.30x faster                                        |
| xml_etree_process        | 76.0 ms                                                      | 58.9 ms: 1.29x faster                                        |
| nqueens                  | 112 ms                                                       | 89.9 ms: 1.25x faster                                        |
| json_loads               | 30.0 us                                                      | 24.0 us: 1.25x faster                                        |
| comprehensions           | 26.9 us                                                      | 21.8 us: 1.24x faster                                        |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                         |
| 2to3                     | 350 ms                                                       | 284 ms: 1.23x faster                                         |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.25 ms: 1.22x faster                                        |
| dulwich_log              | 80.1 ms                                                      | 65.8 ms: 1.22x faster                                        |
| deepcopy                 | 454 us                                                       | 373 us: 1.22x faster                                         |
| mdp                      | 3.03 sec                                                     | 2.50 sec: 1.21x faster                                       |
| sqlglot_optimize         | 70.3 ms                                                      | 58.2 ms: 1.21x faster                                        |
| bench_thread_pool        | 1.14 ms                                                      | 948 us: 1.20x faster                                         |
| deepcopy_reduce          | 4.03 us                                                      | 3.39 us: 1.19x faster                                        |
| docutils                 | 3.40 sec                                                     | 2.87 sec: 1.19x faster                                       |
| unpack_sequence          | 59.5 ns                                                      | 50.6 ns: 1.18x faster                                        |
| scimark_fft              | 359 ms                                                       | 307 ms: 1.17x faster                                         |
| json                     | 5.96 ms                                                      | 5.12 ms: 1.17x faster                                        |
| pathlib                  | 21.7 ms                                                      | 19.4 ms: 1.12x faster                                        |
| sqlite_synth             | 2.97 us                                                      | 2.66 us: 1.11x faster                                        |
| regex_v8                 | 26.6 ms                                                      | 23.9 ms: 1.11x faster                                        |
| create_gc_cycles         | 1.82 ms                                                      | 1.66 ms: 1.10x faster                                        |
| xml_etree_parse          | 162 ms                                                       | 147 ms: 1.10x faster                                         |
| xml_etree_generate       | 94.6 ms                                                      | 86.4 ms: 1.09x faster                                        |
| async_generators         | 422 ms                                                       | 386 ms: 1.09x faster                                         |
| regex_dna                | 259 ms                                                       | 240 ms: 1.08x faster                                         |
| meteor_contest           | 137 ms                                                       | 127 ms: 1.08x faster                                         |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                         |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                         |
| python_startup           | 11.5 ms                                                      | 11.5 ms: 1.00x slower                                        |
| telco                    | 7.14 ms                                                      | 7.26 ms: 1.02x slower                                        |
| pickle                   | 9.94 us                                                      | 10.4 us: 1.05x slower                                        |
| unpickle                 | 14.2 us                                                      | 14.9 us: 1.05x slower                                        |
| pickle_list              | 4.11 us                                                      | 4.38 us: 1.07x slower                                        |
| unpickle_list            | 4.49 us                                                      | 4.82 us: 1.07x slower                                        |
| pickle_dict              | 30.0 us                                                      | 32.8 us: 1.09x slower                                        |
| gc_traversal             | 3.45 ms                                                      | 3.99 ms: 1.16x slower                                        |
| regex_effbot             | 2.99 ms                                                      | 3.47 ms: 1.16x slower                                        |
| python_startup_no_site   | 7.32 ms                                                      | 8.52 ms: 1.16x slower                                        |
| dask                     | 463 ms                                                       | 559 ms: 1.21x slower                                         |
| coverage                 | 64.0 ms                                                      | 90.5 ms: 1.42x slower                                        |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                 |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
