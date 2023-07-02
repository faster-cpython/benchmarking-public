
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 18b1fde
- commit date: 2023-07-01
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf2-x86_64-python-main-3.13.0a0-18b1fde |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.93 sec: 1.03x slower                                      |
| Geometric mean | (ref)                                                        | 1.02x slower                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf2-x86_64-python-main-3.13.0a0-18b1fde |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                        |
| float          | 74.2 ms                                                      | 80.8 ms: 1.09x slower                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf2-x86_64-python-main-3.13.0a0-18b1fde |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                       |
| regex_compile  | 158 ms                                                       | 152 ms: 1.04x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.57 ms: 1.02x slower                                       |
| regex_dna      | 227 ms                                                       | 245 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf2-x86_64-python-main-3.13.0a0-18b1fde |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                       |
| json_loads           | 28.7 us                                                      | 25.6 us: 1.12x faster                                       |
| unpickle_pure_python | 241 us                                                       | 224 us: 1.08x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 148 ms: 1.07x faster                                        |
| pickle_pure_python   | 319 us                                                       | 321 us: 1.01x slower                                        |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.02x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.71 us: 1.04x slower                                       |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                       |
| tomli_loads          | 2.26 sec                                                     | 2.42 sec: 1.07x slower                                      |
| xml_etree_process    | 56.5 ms                                                      | 60.6 ms: 1.07x slower                                       |
| pickle_dict          | 30.8 us                                                      | 33.2 us: 1.08x slower                                       |
| unpickle             | 13.4 us                                                      | 14.6 us: 1.09x slower                                       |
| xml_etree_generate   | 80.5 ms                                                      | 88.4 ms: 1.10x slower                                       |
| pickle_list          | 3.83 us                                                      | 4.31 us: 1.13x slower                                       |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf2-x86_64-python-main-3.13.0a0-18b1fde |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.38 ms: 1.08x slower                                       |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf2-x86_64-python-main-3.13.0a0-18b1fde |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf2-x86_64-python-main-3.13.0a0-18b1fde |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 157 us: 3.34x faster                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                      |
| asyncio_tcp              | 753 ms                                                       | 385 ms: 1.95x faster                                        |
| generators               | 56.0 ms                                                      | 37.5 ms: 1.49x faster                                       |
| chaos                    | 80.9 ms                                                      | 61.8 ms: 1.31x faster                                       |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                       |
| mypy2                    | 451 ms                                                       | 375 ms: 1.20x faster                                        |
| coroutines               | 27.6 ms                                                      | 23.2 ms: 1.19x faster                                       |
| raytrace                 | 317 ms                                                       | 274 ms: 1.15x faster                                        |
| scimark_lu               | 115 ms                                                       | 100 ms: 1.14x faster                                        |
| deltablue                | 4.00 ms                                                      | 3.55 ms: 1.13x faster                                       |
| json_loads               | 28.7 us                                                      | 25.6 us: 1.12x faster                                       |
| nqueens                  | 103 ms                                                       | 92.0 ms: 1.12x faster                                       |
| async_tree_memoization   | 630 ms                                                       | 566 ms: 1.11x faster                                        |
| async_tree_none          | 519 ms                                                       | 470 ms: 1.11x faster                                        |
| comprehensions           | 24.6 us                                                      | 22.4 us: 1.10x faster                                       |
| hexiom                   | 7.13 ms                                                      | 6.56 ms: 1.09x faster                                       |
| async_tree_io            | 1.17 sec                                                     | 1.08 sec: 1.08x faster                                      |
| logging_format           | 8.11 us                                                      | 7.51 us: 1.08x faster                                       |
| mdp                      | 2.75 sec                                                     | 2.54 sec: 1.08x faster                                      |
| mako                     | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                       |
| json                     | 5.65 ms                                                      | 5.23 ms: 1.08x faster                                       |
| unpickle_pure_python     | 241 us                                                       | 224 us: 1.08x faster                                        |
| xml_etree_parse          | 158 ms                                                       | 148 ms: 1.07x faster                                        |
| bench_thread_pool        | 1.01 ms                                                      | 952 us: 1.06x faster                                        |
| fannkuch                 | 429 ms                                                       | 407 ms: 1.05x faster                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 715 ms: 1.05x faster                                        |
| sqlglot_normalize        | 126 ms                                                       | 120 ms: 1.05x faster                                        |
| logging_simple           | 7.19 us                                                      | 6.89 us: 1.04x faster                                       |
| regex_v8                 | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                       |
| regex_compile            | 158 ms                                                       | 152 ms: 1.04x faster                                        |
| sqlglot_parse            | 1.53 ms                                                      | 1.49 ms: 1.03x faster                                       |
| richards_super           | 61.0 ms                                                      | 59.3 ms: 1.03x faster                                       |
| deepcopy                 | 399 us                                                       | 388 us: 1.03x faster                                        |
| logging_silent           | 101 ns                                                       | 98.3 ns: 1.03x faster                                       |
| deepcopy_reduce          | 3.51 us                                                      | 3.44 us: 1.02x faster                                       |
| crypto_pyaes             | 83.4 ms                                                      | 81.7 ms: 1.02x faster                                       |
| sqlglot_transpile        | 1.92 ms                                                      | 1.89 ms: 1.01x faster                                       |
| deepcopy_memo            | 38.8 us                                                      | 38.3 us: 1.01x faster                                       |
| pycparser                | 1.32 sec                                                     | 1.31 sec: 1.01x faster                                      |
| dulwich_log              | 68.4 ms                                                      | 67.8 ms: 1.01x faster                                       |
| meteor_contest           | 131 ms                                                       | 130 ms: 1.01x faster                                        |
| pickle_pure_python       | 319 us                                                       | 321 us: 1.01x slower                                        |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.02x slower                                        |
| regex_effbot             | 3.50 ms                                                      | 3.57 ms: 1.02x slower                                       |
| pathlib                  | 19.1 ms                                                      | 19.5 ms: 1.02x slower                                       |
| docutils                 | 2.86 sec                                                     | 2.93 sec: 1.03x slower                                      |
| create_gc_cycles         | 1.61 ms                                                      | 1.65 ms: 1.03x slower                                       |
| pidigits                 | 251 ms                                                       | 260 ms: 1.04x slower                                        |
| unpickle_list            | 4.53 us                                                      | 4.71 us: 1.04x slower                                       |
| coverage                 | 84.8 ms                                                      | 88.1 ms: 1.04x slower                                       |
| pprint_pformat           | 1.63 sec                                                     | 1.70 sec: 1.04x slower                                      |
| spectral_norm            | 93.3 ms                                                      | 97.5 ms: 1.04x slower                                       |
| go                       | 164 ms                                                       | 171 ms: 1.05x slower                                        |
| python_startup           | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                       |
| pickle                   | 9.64 us                                                      | 10.1 us: 1.05x slower                                       |
| pprint_safe_repr         | 784 ms                                                       | 829 ms: 1.06x slower                                        |
| gc_traversal             | 3.85 ms                                                      | 4.09 ms: 1.06x slower                                       |
| tomli_loads              | 2.26 sec                                                     | 2.42 sec: 1.07x slower                                      |
| xml_etree_process        | 56.5 ms                                                      | 60.6 ms: 1.07x slower                                       |
| regex_dna                | 227 ms                                                       | 245 ms: 1.08x slower                                        |
| pickle_dict              | 30.8 us                                                      | 33.2 us: 1.08x slower                                       |
| python_startup_no_site   | 7.76 ms                                                      | 8.38 ms: 1.08x slower                                       |
| float                    | 74.2 ms                                                      | 80.8 ms: 1.09x slower                                       |
| unpickle                 | 13.4 us                                                      | 14.6 us: 1.09x slower                                       |
| richards                 | 48.3 ms                                                      | 52.7 ms: 1.09x slower                                       |
| sqlite_synth             | 2.50 us                                                      | 2.74 us: 1.10x slower                                       |
| xml_etree_generate       | 80.5 ms                                                      | 88.4 ms: 1.10x slower                                       |
| scimark_monte_carlo      | 68.2 ms                                                      | 75.1 ms: 1.10x slower                                       |
| pickle_list              | 3.83 us                                                      | 4.31 us: 1.13x slower                                       |
| scimark_fft              | 285 ms                                                       | 323 ms: 1.14x slower                                        |
| telco                    | 6.86 ms                                                      | 7.80 ms: 1.14x slower                                       |
| pyflate                  | 449 ms                                                       | 511 ms: 1.14x slower                                        |
| bench_mp_pool            | 4.62 ms                                                      | 5.33 ms: 1.15x slower                                       |
| unpack_sequence          | 45.6 ns                                                      | 53.2 ns: 1.17x slower                                       |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.88 ms: 1.21x slower                                       |
| async_generators         | 316 ms                                                       | 397 ms: 1.26x slower                                        |
| scimark_sor              | 111 ms                                                       | 146 ms: 1.32x slower                                        |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                |

Benchmark hidden because not significant (3): nbody, sqlglot_optimize, tornado_http
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
