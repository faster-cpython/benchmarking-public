
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 99b6418
- commit date: 2023-05-21
- overall geometric mean: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 284 ms: 1.01x faster                                         |
| docutils       | 2.86 sec                                                     | 2.87 sec: 1.00x slower                                       |
| tornado_http   | 122 ms                                                       | 115 ms: 1.06x faster                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 88.7 ms: 1.02x faster                                        |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                         |
| float          | 74.2 ms                                                      | 80.4 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.09x faster                                         |
| regex_effbot   | 3.50 ms                                                      | 3.47 ms: 1.01x faster                                        |
| regex_dna      | 227 ms                                                       | 240 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7+-99b6418 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                        |
| json_loads           | 28.7 us                                                      | 24.0 us: 1.20x faster                                        |
| unpickle_pure_python | 241 us                                                       | 210 us: 1.14x faster                                         |
| xml_etree_parse      | 158 ms                                                       | 147 ms: 1.07x faster                                         |
| tomli_loads          | 2.26 sec                                                     | 2.15 sec: 1.05x faster                                       |
| pickle_pure_python   | 319 us                                                       | 321 us: 1.01x slower                                         |
| xml_etree_process    | 56.5 ms                                                      | 58.9 ms: 1.04x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.82 us: 1.06x slower                                        |
| pickle_dict          | 30.8 us                                                      | 32.8 us: 1.07x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 86.4 ms: 1.07x slower                                        |
| pickle               | 9.64 us                                                      | 10.4 us: 1.08x slower                                        |
| unpickle             | 13.4 us                                                      | 14.9 us: 1.11x slower                                        |
| pickle_list          | 3.83 us                                                      | 4.38 us: 1.14x slower                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7+-99b6418 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.52 ms: 1.10x slower                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7+-99b6418 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.0 ms: 1.10x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7+-99b6418 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 146 us: 3.58x faster                                         |
| asyncio_tcp              | 753 ms                                                       | 380 ms: 1.98x faster                                         |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                       |
| generators               | 56.0 ms                                                      | 35.5 ms: 1.58x faster                                        |
| json_dumps               | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                        |
| chaos                    | 80.9 ms                                                      | 64.1 ms: 1.26x faster                                        |
| coroutines               | 27.6 ms                                                      | 22.1 ms: 1.24x faster                                        |
| fannkuch                 | 429 ms                                                       | 345 ms: 1.24x faster                                         |
| deltablue                | 4.00 ms                                                      | 3.26 ms: 1.23x faster                                        |
| richards_super           | 61.0 ms                                                      | 50.7 ms: 1.20x faster                                        |
| hexiom                   | 7.13 ms                                                      | 5.96 ms: 1.20x faster                                        |
| json_loads               | 28.7 us                                                      | 24.0 us: 1.20x faster                                        |
| unpickle_pure_python     | 241 us                                                       | 210 us: 1.14x faster                                         |
| nqueens                  | 103 ms                                                       | 89.9 ms: 1.14x faster                                        |
| async_tree_memoization   | 630 ms                                                       | 554 ms: 1.14x faster                                         |
| comprehensions           | 24.6 us                                                      | 21.8 us: 1.13x faster                                        |
| scimark_lu               | 115 ms                                                       | 102 ms: 1.13x faster                                         |
| async_tree_none          | 519 ms                                                       | 461 ms: 1.13x faster                                         |
| json                     | 5.65 ms                                                      | 5.12 ms: 1.10x faster                                        |
| async_tree_io            | 1.17 sec                                                     | 1.06 sec: 1.10x faster                                       |
| go                       | 164 ms                                                       | 149 ms: 1.10x faster                                         |
| logging_format           | 8.11 us                                                      | 7.36 us: 1.10x faster                                        |
| mako                     | 11.0 ms                                                      | 10.0 ms: 1.10x faster                                        |
| mdp                      | 2.75 sec                                                     | 2.50 sec: 1.10x faster                                       |
| sqlglot_parse            | 1.53 ms                                                      | 1.40 ms: 1.09x faster                                        |
| regex_compile            | 158 ms                                                       | 144 ms: 1.09x faster                                         |
| logging_simple           | 7.19 us                                                      | 6.65 us: 1.08x faster                                        |
| sqlglot_normalize        | 126 ms                                                       | 117 ms: 1.08x faster                                         |
| pycparser                | 1.32 sec                                                     | 1.24 sec: 1.07x faster                                       |
| xml_etree_parse          | 158 ms                                                       | 147 ms: 1.07x faster                                         |
| deepcopy                 | 399 us                                                       | 373 us: 1.07x faster                                         |
| bench_thread_pool        | 1.01 ms                                                      | 948 us: 1.07x faster                                         |
| sqlglot_transpile        | 1.92 ms                                                      | 1.81 ms: 1.06x faster                                        |
| richards                 | 48.3 ms                                                      | 45.5 ms: 1.06x faster                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 706 ms: 1.06x faster                                         |
| tornado_http             | 122 ms                                                       | 115 ms: 1.06x faster                                         |
| tomli_loads              | 2.26 sec                                                     | 2.15 sec: 1.05x faster                                       |
| logging_silent           | 101 ns                                                       | 96.2 ns: 1.05x faster                                        |
| deepcopy_memo            | 38.8 us                                                      | 37.1 us: 1.05x faster                                        |
| raytrace                 | 317 ms                                                       | 303 ms: 1.04x faster                                         |
| dulwich_log              | 68.4 ms                                                      | 65.8 ms: 1.04x faster                                        |
| deepcopy_reduce          | 3.51 us                                                      | 3.39 us: 1.04x faster                                        |
| meteor_contest           | 131 ms                                                       | 127 ms: 1.03x faster                                         |
| sqlglot_optimize         | 59.8 ms                                                      | 58.2 ms: 1.03x faster                                        |
| nbody                    | 90.7 ms                                                      | 88.7 ms: 1.02x faster                                        |
| spectral_norm            | 93.3 ms                                                      | 91.4 ms: 1.02x faster                                        |
| scimark_sor              | 111 ms                                                       | 110 ms: 1.01x faster                                         |
| 2to3                     | 288 ms                                                       | 284 ms: 1.01x faster                                         |
| regex_effbot             | 3.50 ms                                                      | 3.47 ms: 1.01x faster                                        |
| pprint_pformat           | 1.63 sec                                                     | 1.62 sec: 1.01x faster                                       |
| crypto_pyaes             | 83.4 ms                                                      | 82.8 ms: 1.01x faster                                        |
| docutils                 | 2.86 sec                                                     | 2.87 sec: 1.00x slower                                       |
| pickle_pure_python       | 319 us                                                       | 321 us: 1.01x slower                                         |
| pprint_safe_repr         | 784 ms                                                       | 794 ms: 1.01x slower                                         |
| pathlib                  | 19.1 ms                                                      | 19.4 ms: 1.02x slower                                        |
| create_gc_cycles         | 1.61 ms                                                      | 1.66 ms: 1.03x slower                                        |
| pidigits                 | 251 ms                                                       | 261 ms: 1.04x slower                                         |
| gc_traversal             | 3.85 ms                                                      | 3.99 ms: 1.04x slower                                        |
| xml_etree_process        | 56.5 ms                                                      | 58.9 ms: 1.04x slower                                        |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.25 ms: 1.05x slower                                        |
| scimark_monte_carlo      | 68.2 ms                                                      | 72.0 ms: 1.05x slower                                        |
| regex_dna                | 227 ms                                                       | 240 ms: 1.06x slower                                         |
| telco                    | 6.86 ms                                                      | 7.26 ms: 1.06x slower                                        |
| unpickle_list            | 4.53 us                                                      | 4.82 us: 1.06x slower                                        |
| sqlite_synth             | 2.50 us                                                      | 2.66 us: 1.07x slower                                        |
| pickle_dict              | 30.8 us                                                      | 32.8 us: 1.07x slower                                        |
| coverage                 | 84.8 ms                                                      | 90.5 ms: 1.07x slower                                        |
| python_startup           | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                        |
| xml_etree_generate       | 80.5 ms                                                      | 86.4 ms: 1.07x slower                                        |
| scimark_fft              | 285 ms                                                       | 307 ms: 1.08x slower                                         |
| pickle                   | 9.64 us                                                      | 10.4 us: 1.08x slower                                        |
| float                    | 74.2 ms                                                      | 80.4 ms: 1.08x slower                                        |
| python_startup_no_site   | 7.76 ms                                                      | 8.52 ms: 1.10x slower                                        |
| unpack_sequence          | 45.6 ns                                                      | 50.6 ns: 1.11x slower                                        |
| unpickle                 | 13.4 us                                                      | 14.9 us: 1.11x slower                                        |
| pickle_list              | 3.83 us                                                      | 4.38 us: 1.14x slower                                        |
| async_generators         | 316 ms                                                       | 386 ms: 1.22x slower                                         |
| dask                     | 410 ms                                                       | 559 ms: 1.36x slower                                         |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                 |

Benchmark hidden because not significant (5): pyflate, regex_v8, xml_etree_iterparse, mypy2, bench_mp_pool
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
