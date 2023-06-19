
# Results vs. 3.11.0

- fork: python
- ref: 6baddd9fb25e03040c1c
- machine: linux-x86_64
- commit hash: 6baddd9
- commit date: 2023-06-18
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 285 ms: 1.01x faster                                                         |
| docutils       | 2.86 sec                                                     | 2.90 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 84.8 ms: 1.07x faster                                                        |
| pidigits       | 251 ms                                                       | 259 ms: 1.03x slower                                                         |
| float          | 74.2 ms                                                      | 79.1 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.10x faster                                                         |
| regex_v8       | 23.9 ms                                                      | 23.6 ms: 1.02x faster                                                        |
| regex_effbot   | 3.50 ms                                                      | 3.53 ms: 1.01x slower                                                        |
| regex_dna      | 227 ms                                                       | 241 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.31x faster                                                        |
| json_loads           | 28.7 us                                                      | 24.3 us: 1.18x faster                                                        |
| unpickle_pure_python | 241 us                                                       | 209 us: 1.15x faster                                                         |
| xml_etree_parse      | 158 ms                                                       | 151 ms: 1.05x faster                                                         |
| tomli_loads          | 2.26 sec                                                     | 2.18 sec: 1.04x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                       | 105 ms: 1.01x slower                                                         |
| pickle_pure_python   | 319 us                                                       | 324 us: 1.02x slower                                                         |
| xml_etree_process    | 56.5 ms                                                      | 58.5 ms: 1.04x slower                                                        |
| unpickle_list        | 4.53 us                                                      | 4.75 us: 1.05x slower                                                        |
| pickle               | 9.64 us                                                      | 10.3 us: 1.07x slower                                                        |
| pickle_dict          | 30.8 us                                                      | 33.0 us: 1.07x slower                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 86.4 ms: 1.07x slower                                                        |
| unpickle             | 13.4 us                                                      | 14.7 us: 1.10x slower                                                        |
| pickle_list          | 3.83 us                                                      | 4.42 us: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.49 ms: 1.09x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.0 ms: 1.10x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-pythonperf2-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 151 us: 3.46x faster                                                         |
| asyncio_tcp              | 753 ms                                                       | 377 ms: 1.99x faster                                                         |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.56 sec: 1.97x faster                                                       |
| generators               | 56.0 ms                                                      | 35.9 ms: 1.56x faster                                                        |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.31x faster                                                        |
| chaos                    | 80.9 ms                                                      | 63.2 ms: 1.28x faster                                                        |
| fannkuch                 | 429 ms                                                       | 339 ms: 1.26x faster                                                         |
| hexiom                   | 7.13 ms                                                      | 5.81 ms: 1.23x faster                                                        |
| deltablue                | 4.00 ms                                                      | 3.26 ms: 1.23x faster                                                        |
| coroutines               | 27.6 ms                                                      | 22.7 ms: 1.22x faster                                                        |
| richards_super           | 61.0 ms                                                      | 51.5 ms: 1.19x faster                                                        |
| json_loads               | 28.7 us                                                      | 24.3 us: 1.18x faster                                                        |
| scimark_lu               | 115 ms                                                       | 98.9 ms: 1.16x faster                                                        |
| unpickle_pure_python     | 241 us                                                       | 209 us: 1.15x faster                                                         |
| nqueens                  | 103 ms                                                       | 89.9 ms: 1.14x faster                                                        |
| async_tree_memoization   | 630 ms                                                       | 555 ms: 1.14x faster                                                         |
| async_tree_none          | 519 ms                                                       | 460 ms: 1.13x faster                                                         |
| comprehensions           | 24.6 us                                                      | 22.0 us: 1.12x faster                                                        |
| go                       | 164 ms                                                       | 147 ms: 1.12x faster                                                         |
| async_tree_io            | 1.17 sec                                                     | 1.06 sec: 1.10x faster                                                       |
| json                     | 5.65 ms                                                      | 5.12 ms: 1.10x faster                                                        |
| mdp                      | 2.75 sec                                                     | 2.50 sec: 1.10x faster                                                       |
| mako                     | 11.0 ms                                                      | 10.0 ms: 1.10x faster                                                        |
| sqlglot_parse            | 1.53 ms                                                      | 1.40 ms: 1.10x faster                                                        |
| regex_compile            | 158 ms                                                       | 144 ms: 1.10x faster                                                         |
| logging_format           | 8.11 us                                                      | 7.51 us: 1.08x faster                                                        |
| richards                 | 48.3 ms                                                      | 45.1 ms: 1.07x faster                                                        |
| nbody                    | 90.7 ms                                                      | 84.8 ms: 1.07x faster                                                        |
| raytrace                 | 317 ms                                                       | 297 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 705 ms: 1.06x faster                                                         |
| bench_thread_pool        | 1.01 ms                                                      | 952 us: 1.06x faster                                                         |
| sqlglot_transpile        | 1.92 ms                                                      | 1.81 ms: 1.06x faster                                                        |
| sqlglot_normalize        | 126 ms                                                       | 119 ms: 1.06x faster                                                         |
| logging_simple           | 7.19 us                                                      | 6.81 us: 1.06x faster                                                        |
| deepcopy                 | 399 us                                                       | 379 us: 1.05x faster                                                         |
| xml_etree_parse          | 158 ms                                                       | 151 ms: 1.05x faster                                                         |
| meteor_contest           | 131 ms                                                       | 125 ms: 1.04x faster                                                         |
| pycparser                | 1.32 sec                                                     | 1.27 sec: 1.04x faster                                                       |
| logging_silent           | 101 ns                                                       | 96.7 ns: 1.04x faster                                                        |
| dulwich_log              | 68.4 ms                                                      | 65.9 ms: 1.04x faster                                                        |
| tomli_loads              | 2.26 sec                                                     | 2.18 sec: 1.04x faster                                                       |
| deepcopy_memo            | 38.8 us                                                      | 37.8 us: 1.03x faster                                                        |
| spectral_norm            | 93.3 ms                                                      | 91.2 ms: 1.02x faster                                                        |
| deepcopy_reduce          | 3.51 us                                                      | 3.44 us: 1.02x faster                                                        |
| sqlglot_optimize         | 59.8 ms                                                      | 58.6 ms: 1.02x faster                                                        |
| crypto_pyaes             | 83.4 ms                                                      | 81.9 ms: 1.02x faster                                                        |
| regex_v8                 | 23.9 ms                                                      | 23.6 ms: 1.02x faster                                                        |
| 2to3                     | 288 ms                                                       | 285 ms: 1.01x faster                                                         |
| xml_etree_iterparse      | 104 ms                                                       | 105 ms: 1.01x slower                                                         |
| regex_effbot             | 3.50 ms                                                      | 3.53 ms: 1.01x slower                                                        |
| pathlib                  | 19.1 ms                                                      | 19.3 ms: 1.01x slower                                                        |
| docutils                 | 2.86 sec                                                     | 2.90 sec: 1.01x slower                                                       |
| pickle_pure_python       | 319 us                                                       | 324 us: 1.02x slower                                                         |
| pyflate                  | 449 ms                                                       | 458 ms: 1.02x slower                                                         |
| pprint_pformat           | 1.63 sec                                                     | 1.66 sec: 1.02x slower                                                       |
| pidigits                 | 251 ms                                                       | 259 ms: 1.03x slower                                                         |
| xml_etree_process        | 56.5 ms                                                      | 58.5 ms: 1.04x slower                                                        |
| create_gc_cycles         | 1.61 ms                                                      | 1.67 ms: 1.04x slower                                                        |
| pprint_safe_repr         | 784 ms                                                       | 815 ms: 1.04x slower                                                         |
| gc_traversal             | 3.85 ms                                                      | 4.00 ms: 1.04x slower                                                        |
| unpickle_list            | 4.53 us                                                      | 4.75 us: 1.05x slower                                                        |
| scimark_sor              | 111 ms                                                       | 117 ms: 1.05x slower                                                         |
| scimark_monte_carlo      | 68.2 ms                                                      | 72.0 ms: 1.06x slower                                                        |
| telco                    | 6.86 ms                                                      | 7.26 ms: 1.06x slower                                                        |
| regex_dna                | 227 ms                                                       | 241 ms: 1.06x slower                                                         |
| python_startup           | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                                        |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.30 ms: 1.06x slower                                                        |
| float                    | 74.2 ms                                                      | 79.1 ms: 1.07x slower                                                        |
| pickle                   | 9.64 us                                                      | 10.3 us: 1.07x slower                                                        |
| coverage                 | 84.8 ms                                                      | 90.5 ms: 1.07x slower                                                        |
| scimark_fft              | 285 ms                                                       | 305 ms: 1.07x slower                                                         |
| pickle_dict              | 30.8 us                                                      | 33.0 us: 1.07x slower                                                        |
| xml_etree_generate       | 80.5 ms                                                      | 86.4 ms: 1.07x slower                                                        |
| unpack_sequence          | 45.6 ns                                                      | 49.8 ns: 1.09x slower                                                        |
| sqlite_synth             | 2.50 us                                                      | 2.73 us: 1.09x slower                                                        |
| python_startup_no_site   | 7.76 ms                                                      | 8.49 ms: 1.09x slower                                                        |
| unpickle                 | 13.4 us                                                      | 14.7 us: 1.10x slower                                                        |
| pickle_list              | 3.83 us                                                      | 4.42 us: 1.15x slower                                                        |
| async_generators         | 316 ms                                                       | 389 ms: 1.23x slower                                                         |
| dask                     | 410 ms                                                       | 569 ms: 1.39x slower                                                         |
| bench_mp_pool            | 4.62 ms                                                      | 10.1 ms: 2.19x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (2): tornado_http, mypy2
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
