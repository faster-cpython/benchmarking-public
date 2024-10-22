# Results vs. 3.13.0

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: linux-x86_64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 282 ms: 1.03x faster                                                           |
| docutils       | 2.81 sec                                                     | 2.96 sec: 1.05x slower                                                         |
| html5lib       | 71.9 ms                                                      | 74.0 ms: 1.03x slower                                                          |
| tornado_http   | 120 ms                                                       | 117 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 389 ms: 1.18x faster                                                           |
| async_tree_none            | 372 ms                                                       | 320 ms: 1.16x faster                                                           |
| async_tree_memoization     | 452 ms                                                       | 397 ms: 1.14x faster                                                           |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                                           |
| async_tree_io              | 847 ms                                                       | 803 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 571 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 548 ms: 1.05x faster                                                           |
| async_tree_io_tg           | 819 ms                                                       | 784 ms: 1.04x faster                                                           |
| asyncio_tcp                | 380 ms                                                       | 368 ms: 1.03x faster                                                           |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                         |
| async_generators           | 359 ms                                                       | 362 ms: 1.01x slower                                                           |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                           |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 80.3 ms: 1.02x faster                                                          |
| pidigits       | 253 ms                                                       | 254 ms: 1.01x slower                                                           |
| nbody          | 88.0 ms                                                      | 92.6 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                           |
| regex_v8       | 26.2 ms                                                      | 27.1 ms: 1.03x slower                                                          |
| regex_effbot   | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                                          |
| regex_dna      | 244 ms                                                       | 255 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 11.0 ms                                                      | 10.6 ms: 1.04x faster                                                          |
| xml_etree_parse      | 145 ms                                                       | 142 ms: 1.02x faster                                                           |
| pickle_pure_python   | 318 us                                                       | 313 us: 1.02x faster                                                           |
| xml_etree_process    | 60.9 ms                                                      | 60.2 ms: 1.01x faster                                                          |
| xml_etree_generate   | 85.3 ms                                                      | 85.8 ms: 1.01x slower                                                          |
| unpickle_pure_python | 214 us                                                       | 218 us: 1.02x slower                                                           |
| json_loads           | 24.0 us                                                      | 24.9 us: 1.04x slower                                                          |
| tomli_loads          | 2.41 sec                                                     | 2.51 sec: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                          |
| python_startup_no_site | 8.94 ms                                                      | 9.04 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 24.1 ms: 1.10x faster                                                          |
| genshi_xml      | 57.3 ms                                                      | 52.2 ms: 1.10x faster                                                          |
| mako            | 10.4 ms                                                      | 10.3 ms: 1.01x faster                                                          |
| django_template | 38.9 ms                                                      | 40.5 ms: 1.04x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 290 us: 1.37x faster                                                           |
| deepcopy_memo              | 39.5 us                                                      | 30.2 us: 1.31x faster                                                          |
| deepcopy_reduce            | 3.54 us                                                      | 2.92 us: 1.21x faster                                                          |
| async_tree_memoization_tg  | 461 ms                                                       | 389 ms: 1.18x faster                                                           |
| async_tree_none            | 372 ms                                                       | 320 ms: 1.16x faster                                                           |
| generators                 | 33.5 ms                                                      | 29.3 ms: 1.14x faster                                                          |
| async_tree_memoization     | 452 ms                                                       | 397 ms: 1.14x faster                                                           |
| genshi_text                | 26.6 ms                                                      | 24.1 ms: 1.10x faster                                                          |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                          |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                                           |
| genshi_xml                 | 57.3 ms                                                      | 52.2 ms: 1.10x faster                                                          |
| richards_super             | 59.8 ms                                                      | 55.7 ms: 1.07x faster                                                          |
| raytrace                   | 289 ms                                                       | 270 ms: 1.07x faster                                                           |
| richards                   | 52.7 ms                                                      | 49.6 ms: 1.06x faster                                                          |
| scimark_sor                | 126 ms                                                       | 118 ms: 1.06x faster                                                           |
| scimark_fft                | 314 ms                                                       | 298 ms: 1.05x faster                                                           |
| async_tree_io              | 847 ms                                                       | 803 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 571 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 548 ms: 1.05x faster                                                           |
| telco                      | 8.58 ms                                                      | 8.19 ms: 1.05x faster                                                          |
| bench_thread_pool          | 901 us                                                       | 862 us: 1.04x faster                                                           |
| async_tree_io_tg           | 819 ms                                                       | 784 ms: 1.04x faster                                                           |
| pyflate                    | 492 ms                                                       | 472 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.12 ms: 1.04x faster                                                          |
| bench_mp_pool              | 4.65 ms                                                      | 4.48 ms: 1.04x faster                                                          |
| json_dumps                 | 11.0 ms                                                      | 10.6 ms: 1.04x faster                                                          |
| 2to3                       | 291 ms                                                       | 282 ms: 1.03x faster                                                           |
| asyncio_tcp                | 380 ms                                                       | 368 ms: 1.03x faster                                                           |
| thrift                     | 877 us                                                       | 853 us: 1.03x faster                                                           |
| bpe_tokeniser              | 5.10 sec                                                     | 4.96 sec: 1.03x faster                                                         |
| tornado_http               | 120 ms                                                       | 117 ms: 1.03x faster                                                           |
| logging_simple             | 6.40 us                                                      | 6.24 us: 1.02x faster                                                          |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                           |
| logging_format             | 7.07 us                                                      | 6.92 us: 1.02x faster                                                          |
| spectral_norm              | 97.4 ms                                                      | 95.3 ms: 1.02x faster                                                          |
| float                      | 81.9 ms                                                      | 80.3 ms: 1.02x faster                                                          |
| xml_etree_parse            | 145 ms                                                       | 142 ms: 1.02x faster                                                           |
| hexiom                     | 6.33 ms                                                      | 6.22 ms: 1.02x faster                                                          |
| coverage                   | 81.1 ms                                                      | 79.7 ms: 1.02x faster                                                          |
| sympy_integrate            | 23.3 ms                                                      | 23.0 ms: 1.02x faster                                                          |
| pickle_pure_python         | 318 us                                                       | 313 us: 1.02x faster                                                           |
| sqlglot_optimize           | 59.7 ms                                                      | 58.8 ms: 1.01x faster                                                          |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                           |
| pycparser                  | 1.26 sec                                                     | 1.24 sec: 1.01x faster                                                         |
| scimark_lu                 | 97.8 ms                                                      | 96.5 ms: 1.01x faster                                                          |
| deltablue                  | 3.41 ms                                                      | 3.37 ms: 1.01x faster                                                          |
| sympy_str                  | 296 ms                                                       | 292 ms: 1.01x faster                                                           |
| xml_etree_process          | 60.9 ms                                                      | 60.2 ms: 1.01x faster                                                          |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                          |
| mako                       | 10.4 ms                                                      | 10.3 ms: 1.01x faster                                                          |
| sympy_sum                  | 154 ms                                                       | 153 ms: 1.01x faster                                                           |
| chaos                      | 61.7 ms                                                      | 61.2 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                         |
| crypto_pyaes               | 72.8 ms                                                      | 72.4 ms: 1.00x faster                                                          |
| mdp                        | 2.52 sec                                                     | 2.52 sec: 1.00x faster                                                         |
| python_startup             | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                          |
| pidigits                   | 253 ms                                                       | 254 ms: 1.01x slower                                                           |
| xml_etree_generate         | 85.3 ms                                                      | 85.8 ms: 1.01x slower                                                          |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                          |
| nqueens                    | 88.2 ms                                                      | 88.9 ms: 1.01x slower                                                          |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.01x slower                                                         |
| async_generators           | 359 ms                                                       | 362 ms: 1.01x slower                                                           |
| python_startup_no_site     | 8.94 ms                                                      | 9.04 ms: 1.01x slower                                                          |
| sqlglot_normalize          | 118 ms                                                       | 120 ms: 1.01x slower                                                           |
| logging_silent             | 97.7 ns                                                      | 98.9 ns: 1.01x slower                                                          |
| unpickle_pure_python       | 214 us                                                       | 218 us: 1.02x slower                                                           |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                           |
| json                       | 5.22 ms                                                      | 5.34 ms: 1.02x slower                                                          |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                          |
| html5lib                   | 71.9 ms                                                      | 74.0 ms: 1.03x slower                                                          |
| regex_v8                   | 26.2 ms                                                      | 27.1 ms: 1.03x slower                                                          |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.2 ms: 1.03x slower                                                          |
| json_loads                 | 24.0 us                                                      | 24.9 us: 1.04x slower                                                          |
| regex_effbot               | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                                          |
| django_template            | 38.9 ms                                                      | 40.5 ms: 1.04x slower                                                          |
| tomli_loads                | 2.41 sec                                                     | 2.51 sec: 1.04x slower                                                         |
| regex_dna                  | 244 ms                                                       | 255 ms: 1.05x slower                                                           |
| docutils                   | 2.81 sec                                                     | 2.96 sec: 1.05x slower                                                         |
| nbody                      | 88.0 ms                                                      | 92.6 ms: 1.05x slower                                                          |
| gc_traversal               | 4.11 ms                                                      | 4.46 ms: 1.08x slower                                                          |
| go                         | 160 ms                                                       | 177 ms: 1.10x slower                                                           |
| create_gc_cycles           | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                   |

Benchmark hidden because not significant (7): xml_etree_iterparse, sympy_expand, pprint_safe_repr, comprehensions, fannkuch, typing_runtime_protocols, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x