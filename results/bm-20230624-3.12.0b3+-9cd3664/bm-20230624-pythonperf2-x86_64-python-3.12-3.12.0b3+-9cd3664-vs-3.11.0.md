
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 9cd3664
- commit date: 2023-06-24
- overall geometric mean: 1.08x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 283 ms: 1.02x faster                                         |
| docutils       | 2.86 sec                                                     | 2.88 sec: 1.01x slower                                       |
| tornado_http   | 122 ms                                                       | 120 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 85.0 ms: 1.07x faster                                        |
| float          | 74.2 ms                                                      | 77.0 ms: 1.04x slower                                        |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                        | 1.00x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 143 ms: 1.10x faster                                         |
| regex_v8       | 23.9 ms                                                      | 23.8 ms: 1.01x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.57 ms: 1.02x slower                                        |
| regex_dna      | 227 ms                                                       | 247 ms: 1.09x slower                                         |
| Geometric mean | (ref)                                                        | 1.00x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.1 ms: 1.33x faster                                        |
| unpickle_pure_python | 241 us                                                       | 208 us: 1.16x faster                                         |
| json_loads           | 28.7 us                                                      | 25.0 us: 1.15x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 147 ms: 1.07x faster                                         |
| tomli_loads          | 2.26 sec                                                     | 2.19 sec: 1.03x faster                                       |
| pickle_pure_python   | 319 us                                                       | 318 us: 1.00x faster                                         |
| xml_etree_process    | 56.5 ms                                                      | 58.3 ms: 1.03x slower                                        |
| pickle_dict          | 30.8 us                                                      | 32.0 us: 1.04x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.77 us: 1.05x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 85.1 ms: 1.06x slower                                        |
| pickle               | 9.64 us                                                      | 10.3 us: 1.06x slower                                        |
| unpickle             | 13.4 us                                                      | 14.5 us: 1.08x slower                                        |
| pickle_list          | 3.83 us                                                      | 4.36 us: 1.14x slower                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.44 ms: 1.09x slower                                        |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 9.91 ms: 1.11x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 149 us: 3.52x faster                                         |
| asyncio_tcp              | 753 ms                                                       | 376 ms: 2.00x faster                                         |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.56 sec: 1.97x faster                                       |
| generators               | 56.0 ms                                                      | 36.6 ms: 1.53x faster                                        |
| json_dumps               | 13.4 ms                                                      | 10.1 ms: 1.33x faster                                        |
| chaos                    | 80.9 ms                                                      | 62.3 ms: 1.30x faster                                        |
| fannkuch                 | 429 ms                                                       | 340 ms: 1.26x faster                                         |
| mypy2                    | 451 ms                                                       | 363 ms: 1.24x faster                                         |
| deltablue                | 4.00 ms                                                      | 3.22 ms: 1.24x faster                                        |
| hexiom                   | 7.13 ms                                                      | 5.81 ms: 1.23x faster                                        |
| richards_super           | 61.0 ms                                                      | 49.9 ms: 1.22x faster                                        |
| coroutines               | 27.6 ms                                                      | 22.6 ms: 1.22x faster                                        |
| scimark_lu               | 115 ms                                                       | 97.2 ms: 1.18x faster                                        |
| unpickle_pure_python     | 241 us                                                       | 208 us: 1.16x faster                                         |
| json_loads               | 28.7 us                                                      | 25.0 us: 1.15x faster                                        |
| async_tree_memoization   | 630 ms                                                       | 549 ms: 1.15x faster                                         |
| async_tree_none          | 519 ms                                                       | 456 ms: 1.14x faster                                         |
| go                       | 164 ms                                                       | 144 ms: 1.14x faster                                         |
| comprehensions           | 24.6 us                                                      | 21.9 us: 1.13x faster                                        |
| nqueens                  | 103 ms                                                       | 91.8 ms: 1.12x faster                                        |
| sqlglot_parse            | 1.53 ms                                                      | 1.37 ms: 1.12x faster                                        |
| async_tree_io            | 1.17 sec                                                     | 1.06 sec: 1.11x faster                                       |
| mako                     | 11.0 ms                                                      | 9.91 ms: 1.11x faster                                        |
| logging_format           | 8.11 us                                                      | 7.34 us: 1.11x faster                                        |
| regex_compile            | 158 ms                                                       | 143 ms: 1.10x faster                                         |
| logging_silent           | 101 ns                                                       | 91.6 ns: 1.10x faster                                        |
| mdp                      | 2.75 sec                                                     | 2.50 sec: 1.10x faster                                       |
| richards                 | 48.3 ms                                                      | 44.0 ms: 1.10x faster                                        |
| json                     | 5.65 ms                                                      | 5.19 ms: 1.09x faster                                        |
| sqlglot_transpile        | 1.92 ms                                                      | 1.77 ms: 1.08x faster                                        |
| logging_simple           | 7.19 us                                                      | 6.65 us: 1.08x faster                                        |
| sqlglot_normalize        | 126 ms                                                       | 117 ms: 1.08x faster                                         |
| deepcopy                 | 399 us                                                       | 372 us: 1.07x faster                                         |
| xml_etree_parse          | 158 ms                                                       | 147 ms: 1.07x faster                                         |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 700 ms: 1.07x faster                                         |
| raytrace                 | 317 ms                                                       | 297 ms: 1.07x faster                                         |
| nbody                    | 90.7 ms                                                      | 85.0 ms: 1.07x faster                                        |
| bench_thread_pool        | 1.01 ms                                                      | 953 us: 1.06x faster                                         |
| deepcopy_memo            | 38.8 us                                                      | 36.6 us: 1.06x faster                                        |
| pycparser                | 1.32 sec                                                     | 1.25 sec: 1.06x faster                                       |
| spectral_norm            | 93.3 ms                                                      | 88.5 ms: 1.05x faster                                        |
| dulwich_log              | 68.4 ms                                                      | 65.1 ms: 1.05x faster                                        |
| deepcopy_reduce          | 3.51 us                                                      | 3.37 us: 1.04x faster                                        |
| sqlglot_optimize         | 59.8 ms                                                      | 57.7 ms: 1.04x faster                                        |
| tomli_loads              | 2.26 sec                                                     | 2.19 sec: 1.03x faster                                       |
| pyflate                  | 449 ms                                                       | 435 ms: 1.03x faster                                         |
| scimark_monte_carlo      | 68.2 ms                                                      | 66.3 ms: 1.03x faster                                        |
| meteor_contest           | 131 ms                                                       | 128 ms: 1.02x faster                                         |
| 2to3                     | 288 ms                                                       | 283 ms: 1.02x faster                                         |
| scimark_sor              | 111 ms                                                       | 110 ms: 1.01x faster                                         |
| gc_traversal             | 3.85 ms                                                      | 3.79 ms: 1.01x faster                                        |
| tornado_http             | 122 ms                                                       | 120 ms: 1.01x faster                                         |
| crypto_pyaes             | 83.4 ms                                                      | 82.7 ms: 1.01x faster                                        |
| pathlib                  | 19.1 ms                                                      | 18.9 ms: 1.01x faster                                        |
| regex_v8                 | 23.9 ms                                                      | 23.8 ms: 1.01x faster                                        |
| pickle_pure_python       | 319 us                                                       | 318 us: 1.00x faster                                         |
| pprint_pformat           | 1.63 sec                                                     | 1.64 sec: 1.00x slower                                       |
| docutils                 | 2.86 sec                                                     | 2.88 sec: 1.01x slower                                       |
| create_gc_cycles         | 1.61 ms                                                      | 1.64 ms: 1.02x slower                                        |
| regex_effbot             | 3.50 ms                                                      | 3.57 ms: 1.02x slower                                        |
| telco                    | 6.86 ms                                                      | 7.01 ms: 1.02x slower                                        |
| pprint_safe_repr         | 784 ms                                                       | 803 ms: 1.02x slower                                         |
| xml_etree_process        | 56.5 ms                                                      | 58.3 ms: 1.03x slower                                        |
| float                    | 74.2 ms                                                      | 77.0 ms: 1.04x slower                                        |
| pickle_dict              | 30.8 us                                                      | 32.0 us: 1.04x slower                                        |
| pidigits                 | 251 ms                                                       | 261 ms: 1.04x slower                                         |
| coverage                 | 84.8 ms                                                      | 88.2 ms: 1.04x slower                                        |
| unpickle_list            | 4.53 us                                                      | 4.77 us: 1.05x slower                                        |
| xml_etree_generate       | 80.5 ms                                                      | 85.1 ms: 1.06x slower                                        |
| python_startup           | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                        |
| pickle                   | 9.64 us                                                      | 10.3 us: 1.06x slower                                        |
| scimark_fft              | 285 ms                                                       | 305 ms: 1.07x slower                                         |
| unpickle                 | 13.4 us                                                      | 14.5 us: 1.08x slower                                        |
| python_startup_no_site   | 7.76 ms                                                      | 8.44 ms: 1.09x slower                                        |
| regex_dna                | 227 ms                                                       | 247 ms: 1.09x slower                                         |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.41 ms: 1.09x slower                                        |
| sqlite_synth             | 2.50 us                                                      | 2.74 us: 1.10x slower                                        |
| unpack_sequence          | 45.6 ns                                                      | 50.3 ns: 1.10x slower                                        |
| pickle_list              | 3.83 us                                                      | 4.36 us: 1.14x slower                                        |
| bench_mp_pool            | 4.62 ms                                                      | 5.53 ms: 1.20x slower                                        |
| async_generators         | 316 ms                                                       | 391 ms: 1.24x slower                                         |
| dask                     | 410 ms                                                       | 558 ms: 1.36x slower                                         |
| Geometric mean           | (ref)                                                        | 1.08x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
