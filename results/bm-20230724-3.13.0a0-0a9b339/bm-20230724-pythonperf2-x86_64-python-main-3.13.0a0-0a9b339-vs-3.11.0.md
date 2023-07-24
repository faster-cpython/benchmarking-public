
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 0a9b339
- commit date: 2023-07-24
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                      |
| tornado_http   | 122 ms                                                       | 123 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 88.2 ms: 1.03x faster                                       |
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                        |
| float          | 74.2 ms                                                      | 81.0 ms: 1.09x slower                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 151 ms: 1.04x faster                                        |
| regex_v8       | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                       |
| regex_dna      | 227 ms                                                       | 245 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                       |
| json_loads           | 28.7 us                                                      | 24.1 us: 1.19x faster                                       |
| xml_etree_parse      | 158 ms                                                       | 143 ms: 1.11x faster                                        |
| unpickle_pure_python | 241 us                                                       | 222 us: 1.08x faster                                        |
| pickle_pure_python   | 319 us                                                       | 316 us: 1.01x faster                                        |
| tomli_loads          | 2.26 sec                                                     | 2.34 sec: 1.04x slower                                      |
| xml_etree_process    | 56.5 ms                                                      | 59.0 ms: 1.05x slower                                       |
| pickle               | 9.64 us                                                      | 10.2 us: 1.06x slower                                       |
| unpickle_list        | 4.53 us                                                      | 4.83 us: 1.06x slower                                       |
| unpickle             | 13.4 us                                                      | 14.5 us: 1.08x slower                                       |
| xml_etree_generate   | 80.5 ms                                                      | 87.1 ms: 1.08x slower                                       |
| pickle_dict          | 30.8 us                                                      | 33.3 us: 1.08x slower                                       |
| pickle_list          | 3.83 us                                                      | 4.29 us: 1.12x slower                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.42 ms: 1.09x slower                                       |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 156 us: 3.35x faster                                        |
| asyncio_tcp              | 753 ms                                                       | 369 ms: 2.04x faster                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                      |
| generators               | 56.0 ms                                                      | 37.4 ms: 1.50x faster                                       |
| chaos                    | 80.9 ms                                                      | 62.1 ms: 1.30x faster                                       |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                       |
| mypy2                    | 451 ms                                                       | 372 ms: 1.21x faster                                        |
| json_loads               | 28.7 us                                                      | 24.1 us: 1.19x faster                                       |
| coroutines               | 27.6 ms                                                      | 23.5 ms: 1.17x faster                                       |
| scimark_lu               | 115 ms                                                       | 98.7 ms: 1.16x faster                                       |
| crypto_pyaes             | 83.4 ms                                                      | 73.4 ms: 1.14x faster                                       |
| raytrace                 | 317 ms                                                       | 284 ms: 1.12x faster                                        |
| json                     | 5.65 ms                                                      | 5.08 ms: 1.11x faster                                       |
| xml_etree_parse          | 158 ms                                                       | 143 ms: 1.11x faster                                        |
| async_tree_memoization   | 630 ms                                                       | 570 ms: 1.11x faster                                        |
| nqueens                  | 103 ms                                                       | 93.0 ms: 1.11x faster                                       |
| comprehensions           | 24.6 us                                                      | 22.3 us: 1.10x faster                                       |
| async_tree_none          | 519 ms                                                       | 472 ms: 1.10x faster                                        |
| hexiom                   | 7.13 ms                                                      | 6.56 ms: 1.09x faster                                       |
| unpickle_pure_python     | 241 us                                                       | 222 us: 1.08x faster                                        |
| async_tree_io            | 1.17 sec                                                     | 1.09 sec: 1.08x faster                                      |
| fannkuch                 | 429 ms                                                       | 399 ms: 1.07x faster                                        |
| mdp                      | 2.75 sec                                                     | 2.56 sec: 1.07x faster                                      |
| logging_format           | 8.11 us                                                      | 7.56 us: 1.07x faster                                       |
| deltablue                | 4.00 ms                                                      | 3.74 ms: 1.07x faster                                       |
| mako                     | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                       |
| deepcopy                 | 399 us                                                       | 375 us: 1.06x faster                                        |
| sqlglot_parse            | 1.53 ms                                                      | 1.45 ms: 1.06x faster                                       |
| sqlglot_normalize        | 126 ms                                                       | 120 ms: 1.05x faster                                        |
| regex_compile            | 158 ms                                                       | 151 ms: 1.04x faster                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 718 ms: 1.04x faster                                        |
| deepcopy_memo            | 38.8 us                                                      | 37.2 us: 1.04x faster                                       |
| logging_silent           | 101 ns                                                       | 97.1 ns: 1.04x faster                                       |
| sqlglot_transpile        | 1.92 ms                                                      | 1.86 ms: 1.03x faster                                       |
| bench_thread_pool        | 1.01 ms                                                      | 979 us: 1.03x faster                                        |
| nbody                    | 90.7 ms                                                      | 88.2 ms: 1.03x faster                                       |
| logging_simple           | 7.19 us                                                      | 7.00 us: 1.03x faster                                       |
| deepcopy_reduce          | 3.51 us                                                      | 3.45 us: 1.02x faster                                       |
| richards_super           | 61.0 ms                                                      | 60.3 ms: 1.01x faster                                       |
| pickle_pure_python       | 319 us                                                       | 316 us: 1.01x faster                                        |
| meteor_contest           | 131 ms                                                       | 130 ms: 1.00x faster                                        |
| regex_v8                 | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                       |
| spectral_norm            | 93.3 ms                                                      | 94.1 ms: 1.01x slower                                       |
| pycparser                | 1.32 sec                                                     | 1.34 sec: 1.01x slower                                      |
| dulwich_log              | 68.4 ms                                                      | 69.3 ms: 1.01x slower                                       |
| scimark_monte_carlo      | 68.2 ms                                                      | 69.1 ms: 1.01x slower                                       |
| tornado_http             | 122 ms                                                       | 123 ms: 1.01x slower                                        |
| docutils                 | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                      |
| pathlib                  | 19.1 ms                                                      | 19.5 ms: 1.02x slower                                       |
| gc_traversal             | 3.85 ms                                                      | 3.95 ms: 1.03x slower                                       |
| create_gc_cycles         | 1.61 ms                                                      | 1.66 ms: 1.03x slower                                       |
| coverage                 | 84.8 ms                                                      | 87.3 ms: 1.03x slower                                       |
| pprint_pformat           | 1.63 sec                                                     | 1.69 sec: 1.03x slower                                      |
| bench_mp_pool            | 4.62 ms                                                      | 4.79 ms: 1.04x slower                                       |
| tomli_loads              | 2.26 sec                                                     | 2.34 sec: 1.04x slower                                      |
| pidigits                 | 251 ms                                                       | 260 ms: 1.04x slower                                        |
| xml_etree_process        | 56.5 ms                                                      | 59.0 ms: 1.05x slower                                       |
| pprint_safe_repr         | 784 ms                                                       | 825 ms: 1.05x slower                                        |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.28 ms: 1.06x slower                                       |
| python_startup           | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                       |
| pickle                   | 9.64 us                                                      | 10.2 us: 1.06x slower                                       |
| unpickle_list            | 4.53 us                                                      | 4.83 us: 1.06x slower                                       |
| scimark_fft              | 285 ms                                                       | 305 ms: 1.07x slower                                        |
| regex_dna                | 227 ms                                                       | 245 ms: 1.08x slower                                        |
| unpickle                 | 13.4 us                                                      | 14.5 us: 1.08x slower                                       |
| go                       | 164 ms                                                       | 177 ms: 1.08x slower                                        |
| xml_etree_generate       | 80.5 ms                                                      | 87.1 ms: 1.08x slower                                       |
| pickle_dict              | 30.8 us                                                      | 33.3 us: 1.08x slower                                       |
| python_startup_no_site   | 7.76 ms                                                      | 8.42 ms: 1.09x slower                                       |
| float                    | 74.2 ms                                                      | 81.0 ms: 1.09x slower                                       |
| sqlite_synth             | 2.50 us                                                      | 2.76 us: 1.10x slower                                       |
| pickle_list              | 3.83 us                                                      | 4.29 us: 1.12x slower                                       |
| telco                    | 6.86 ms                                                      | 7.70 ms: 1.12x slower                                       |
| richards                 | 48.3 ms                                                      | 54.6 ms: 1.13x slower                                       |
| pyflate                  | 449 ms                                                       | 513 ms: 1.14x slower                                        |
| unpack_sequence          | 45.6 ns                                                      | 53.3 ns: 1.17x slower                                       |
| async_generators         | 316 ms                                                       | 399 ms: 1.26x slower                                        |
| scimark_sor              | 111 ms                                                       | 147 ms: 1.33x slower                                        |
| dask                     | 410 ms                                                       | 591 ms: 1.44x slower                                        |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                |

Benchmark hidden because not significant (3): sqlglot_optimize, regex_effbot, xml_etree_iterparse
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
