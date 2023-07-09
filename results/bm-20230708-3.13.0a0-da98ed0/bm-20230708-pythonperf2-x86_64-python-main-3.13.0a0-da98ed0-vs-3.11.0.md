
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: da98ed0
- commit date: 2023-07-08
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf2-x86_64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf2-x86_64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 87.5 ms: 1.04x faster                                       |
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                        |
| float          | 74.2 ms                                                      | 80.0 ms: 1.08x slower                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf2-x86_64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 151 ms: 1.04x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.53 ms: 1.01x slower                                       |
| regex_v8       | 23.9 ms                                                      | 24.2 ms: 1.01x slower                                       |
| regex_dna      | 227 ms                                                       | 241 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf2-x86_64-python-main-3.13.0a0-da98ed0 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                       |
| json_loads           | 28.7 us                                                      | 24.6 us: 1.17x faster                                       |
| unpickle_pure_python | 241 us                                                       | 223 us: 1.08x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 147 ms: 1.08x faster                                        |
| pickle_dict          | 30.8 us                                                      | 31.0 us: 1.01x slower                                       |
| pickle_pure_python   | 319 us                                                       | 323 us: 1.01x slower                                        |
| xml_etree_iterparse  | 104 ms                                                       | 107 ms: 1.03x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.67 us: 1.03x slower                                       |
| xml_etree_process    | 56.5 ms                                                      | 59.0 ms: 1.05x slower                                       |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                       |
| tomli_loads          | 2.26 sec                                                     | 2.39 sec: 1.06x slower                                      |
| xml_etree_generate   | 80.5 ms                                                      | 85.0 ms: 1.06x slower                                       |
| unpickle             | 13.4 us                                                      | 14.5 us: 1.08x slower                                       |
| pickle_list          | 3.83 us                                                      | 4.29 us: 1.12x slower                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf2-x86_64-python-main-3.13.0a0-da98ed0 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.36 ms: 1.08x slower                                       |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf2-x86_64-python-main-3.13.0a0-da98ed0 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf2-x86_64-python-main-3.13.0a0-da98ed0 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 152 us: 3.43x faster                                        |
| asyncio_tcp              | 753 ms                                                       | 381 ms: 1.97x faster                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                      |
| generators               | 56.0 ms                                                      | 36.3 ms: 1.55x faster                                       |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                       |
| chaos                    | 80.9 ms                                                      | 62.4 ms: 1.30x faster                                       |
| mypy2                    | 451 ms                                                       | 371 ms: 1.22x faster                                        |
| coroutines               | 27.6 ms                                                      | 23.1 ms: 1.20x faster                                       |
| json_loads               | 28.7 us                                                      | 24.6 us: 1.17x faster                                       |
| scimark_lu               | 115 ms                                                       | 99.2 ms: 1.15x faster                                       |
| raytrace                 | 317 ms                                                       | 277 ms: 1.14x faster                                        |
| deltablue                | 4.00 ms                                                      | 3.53 ms: 1.13x faster                                       |
| async_tree_memoization   | 630 ms                                                       | 561 ms: 1.12x faster                                        |
| async_tree_none          | 519 ms                                                       | 465 ms: 1.12x faster                                        |
| nqueens                  | 103 ms                                                       | 92.8 ms: 1.11x faster                                       |
| comprehensions           | 24.6 us                                                      | 22.2 us: 1.11x faster                                       |
| hexiom                   | 7.13 ms                                                      | 6.50 ms: 1.10x faster                                       |
| json                     | 5.65 ms                                                      | 5.17 ms: 1.09x faster                                       |
| fannkuch                 | 429 ms                                                       | 392 ms: 1.09x faster                                        |
| async_tree_io            | 1.17 sec                                                     | 1.08 sec: 1.09x faster                                      |
| mako                     | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                       |
| logging_format           | 8.11 us                                                      | 7.45 us: 1.09x faster                                       |
| mdp                      | 2.75 sec                                                     | 2.53 sec: 1.09x faster                                      |
| unpickle_pure_python     | 241 us                                                       | 223 us: 1.08x faster                                        |
| bench_thread_pool        | 1.01 ms                                                      | 939 us: 1.08x faster                                        |
| xml_etree_parse          | 158 ms                                                       | 147 ms: 1.08x faster                                        |
| gc_traversal             | 3.85 ms                                                      | 3.58 ms: 1.08x faster                                       |
| sqlglot_normalize        | 126 ms                                                       | 118 ms: 1.07x faster                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 713 ms: 1.05x faster                                        |
| richards_super           | 61.0 ms                                                      | 58.3 ms: 1.05x faster                                       |
| deepcopy                 | 399 us                                                       | 381 us: 1.05x faster                                        |
| logging_simple           | 7.19 us                                                      | 6.88 us: 1.05x faster                                       |
| regex_compile            | 158 ms                                                       | 151 ms: 1.04x faster                                        |
| sqlglot_parse            | 1.53 ms                                                      | 1.47 ms: 1.04x faster                                       |
| deepcopy_memo            | 38.8 us                                                      | 37.3 us: 1.04x faster                                       |
| logging_silent           | 101 ns                                                       | 97.0 ns: 1.04x faster                                       |
| nbody                    | 90.7 ms                                                      | 87.5 ms: 1.04x faster                                       |
| deepcopy_reduce          | 3.51 us                                                      | 3.41 us: 1.03x faster                                       |
| dulwich_log              | 68.4 ms                                                      | 66.7 ms: 1.03x faster                                       |
| sqlglot_transpile        | 1.92 ms                                                      | 1.88 ms: 1.02x faster                                       |
| pycparser                | 1.32 sec                                                     | 1.31 sec: 1.01x faster                                      |
| sqlglot_optimize         | 59.8 ms                                                      | 59.4 ms: 1.01x faster                                       |
| meteor_contest           | 131 ms                                                       | 130 ms: 1.00x faster                                        |
| crypto_pyaes             | 83.4 ms                                                      | 83.7 ms: 1.00x slower                                       |
| pickle_dict              | 30.8 us                                                      | 31.0 us: 1.01x slower                                       |
| regex_effbot             | 3.50 ms                                                      | 3.53 ms: 1.01x slower                                       |
| regex_v8                 | 23.9 ms                                                      | 24.2 ms: 1.01x slower                                       |
| pickle_pure_python       | 319 us                                                       | 323 us: 1.01x slower                                        |
| docutils                 | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                      |
| pprint_pformat           | 1.63 sec                                                     | 1.68 sec: 1.03x slower                                      |
| xml_etree_iterparse      | 104 ms                                                       | 107 ms: 1.03x slower                                        |
| unpickle_list            | 4.53 us                                                      | 4.67 us: 1.03x slower                                       |
| pathlib                  | 19.1 ms                                                      | 19.6 ms: 1.03x slower                                       |
| coverage                 | 84.8 ms                                                      | 87.7 ms: 1.03x slower                                       |
| pidigits                 | 251 ms                                                       | 260 ms: 1.04x slower                                        |
| xml_etree_process        | 56.5 ms                                                      | 59.0 ms: 1.05x slower                                       |
| pprint_safe_repr         | 784 ms                                                       | 820 ms: 1.05x slower                                        |
| python_startup           | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                       |
| pickle                   | 9.64 us                                                      | 10.1 us: 1.05x slower                                       |
| tomli_loads              | 2.26 sec                                                     | 2.39 sec: 1.06x slower                                      |
| xml_etree_generate       | 80.5 ms                                                      | 85.0 ms: 1.06x slower                                       |
| go                       | 164 ms                                                       | 173 ms: 1.06x slower                                        |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.28 ms: 1.06x slower                                       |
| regex_dna                | 227 ms                                                       | 241 ms: 1.06x slower                                        |
| scimark_monte_carlo      | 68.2 ms                                                      | 72.5 ms: 1.06x slower                                       |
| spectral_norm            | 93.3 ms                                                      | 99.9 ms: 1.07x slower                                       |
| python_startup_no_site   | 7.76 ms                                                      | 8.36 ms: 1.08x slower                                       |
| float                    | 74.2 ms                                                      | 80.0 ms: 1.08x slower                                       |
| unpickle                 | 13.4 us                                                      | 14.5 us: 1.08x slower                                       |
| richards                 | 48.3 ms                                                      | 52.5 ms: 1.09x slower                                       |
| scimark_fft              | 285 ms                                                       | 312 ms: 1.10x slower                                        |
| sqlite_synth             | 2.50 us                                                      | 2.74 us: 1.10x slower                                       |
| pickle_list              | 3.83 us                                                      | 4.29 us: 1.12x slower                                       |
| telco                    | 6.86 ms                                                      | 7.72 ms: 1.13x slower                                       |
| pyflate                  | 449 ms                                                       | 510 ms: 1.14x slower                                        |
| unpack_sequence          | 45.6 ns                                                      | 54.5 ns: 1.19x slower                                       |
| async_generators         | 316 ms                                                       | 399 ms: 1.26x slower                                        |
| scimark_sor              | 111 ms                                                       | 146 ms: 1.31x slower                                        |
| dask                     | 410 ms                                                       | 589 ms: 1.44x slower                                        |
| bench_mp_pool            | 4.62 ms                                                      | 6.74 ms: 1.46x slower                                       |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                |

Benchmark hidden because not significant (2): tornado_http, create_gc_cycles
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
