# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc1
- machine: linux-x86_64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.00x faster
- HPT reliability: 83.69%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 289 ms: 1.01x faster                                               |
| chameleon      | 7.42 ms                                                      | 7.33 ms: 1.01x faster                                              |
| docutils       | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                             |
| html5lib       | 71.9 ms                                                      | 72.8 ms: 1.01x slower                                              |
| tornado_http   | 120 ms                                                       | 118 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                        | 1.01x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg | 461 ms                                                       | 440 ms: 1.05x faster                                               |
| coroutines                | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                              |
| async_tree_none           | 372 ms                                                       | 368 ms: 1.01x faster                                               |
| asyncio_tcp               | 380 ms                                                       | 376 ms: 1.01x faster                                               |
| asyncio_tcp_ssl           | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                             |
| asyncio_websockets        | 382 ms                                                       | 390 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed   | 600 ms                                                       | 612 ms: 1.02x slower                                               |
| async_tree_memoization    | 452 ms                                                       | 466 ms: 1.03x slower                                               |
| async_generators          | 359 ms                                                       | 370 ms: 1.03x slower                                               |
| async_tree_io             | 847 ms                                                       | 895 ms: 1.06x slower                                               |
| async_tree_io_tg          | 819 ms                                                       | 911 ms: 1.11x slower                                               |
| Geometric mean            | (ref)                                                        | 1.02x slower                                                       |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 80.3 ms: 1.02x faster                                              |
| pidigits       | 253 ms                                                       | 254 ms: 1.01x slower                                               |
| nbody          | 88.0 ms                                                      | 92.0 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                        | 1.01x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                               |
| regex_effbot   | 3.37 ms                                                      | 3.39 ms: 1.01x slower                                              |
| regex_v8       | 26.2 ms                                                      | 26.4 ms: 1.01x slower                                              |
| regex_dna      | 244 ms                                                       | 245 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                        | 1.00x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.19 sec: 1.10x faster                                             |
| xml_etree_parse      | 145 ms                                                       | 141 ms: 1.02x faster                                               |
| unpickle_pure_python | 214 us                                                       | 213 us: 1.01x faster                                               |
| json_loads           | 24.0 us                                                      | 24.1 us: 1.00x slower                                              |
| xml_etree_generate   | 85.3 ms                                                      | 86.2 ms: 1.01x slower                                              |
| json_dumps           | 11.0 ms                                                      | 11.2 ms: 1.02x slower                                              |
| xml_etree_iterparse  | 100 ms                                                       | 103 ms: 1.03x slower                                               |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                       |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.98 ms: 1.00x slower                                              |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 53.4 ms: 1.07x faster                                              |
| genshi_text     | 26.6 ms                                                      | 25.5 ms: 1.04x faster                                              |
| django_template | 38.9 ms                                                      | 39.3 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                       |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| mypy2                     | 1.05 sec                                                     | 769 ms: 1.36x faster                                               |
| tomli_loads               | 2.41 sec                                                     | 2.19 sec: 1.10x faster                                             |
| raytrace                  | 289 ms                                                       | 265 ms: 1.09x faster                                               |
| genshi_xml                | 57.3 ms                                                      | 53.4 ms: 1.07x faster                                              |
| async_tree_memoization_tg | 461 ms                                                       | 440 ms: 1.05x faster                                               |
| pyflate                   | 492 ms                                                       | 469 ms: 1.05x faster                                               |
| genshi_text               | 26.6 ms                                                      | 25.5 ms: 1.04x faster                                              |
| richards_super            | 59.8 ms                                                      | 57.4 ms: 1.04x faster                                              |
| richards                  | 52.7 ms                                                      | 50.9 ms: 1.04x faster                                              |
| deepcopy                  | 397 us                                                       | 385 us: 1.03x faster                                               |
| deepcopy_memo             | 39.5 us                                                      | 38.3 us: 1.03x faster                                              |
| chaos                     | 61.7 ms                                                      | 60.1 ms: 1.03x faster                                              |
| xml_etree_parse           | 145 ms                                                       | 141 ms: 1.02x faster                                               |
| fannkuch                  | 365 ms                                                       | 356 ms: 1.02x faster                                               |
| deltablue                 | 3.41 ms                                                      | 3.34 ms: 1.02x faster                                              |
| float                     | 81.9 ms                                                      | 80.3 ms: 1.02x faster                                              |
| dulwich_log               | 65.5 ms                                                      | 64.2 ms: 1.02x faster                                              |
| scimark_fft               | 314 ms                                                       | 308 ms: 1.02x faster                                               |
| go                        | 160 ms                                                       | 158 ms: 1.02x faster                                               |
| telco                     | 8.58 ms                                                      | 8.43 ms: 1.02x faster                                              |
| coverage                  | 81.1 ms                                                      | 79.8 ms: 1.02x faster                                              |
| tornado_http              | 120 ms                                                       | 118 ms: 1.02x faster                                               |
| pathlib                   | 17.4 ms                                                      | 17.2 ms: 1.01x faster                                              |
| coroutines                | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                              |
| mdp                       | 2.52 sec                                                     | 2.49 sec: 1.01x faster                                             |
| chameleon                 | 7.42 ms                                                      | 7.33 ms: 1.01x faster                                              |
| deepcopy_reduce           | 3.54 us                                                      | 3.50 us: 1.01x faster                                              |
| logging_format            | 7.07 us                                                      | 6.99 us: 1.01x faster                                              |
| async_tree_none           | 372 ms                                                       | 368 ms: 1.01x faster                                               |
| asyncio_tcp               | 380 ms                                                       | 376 ms: 1.01x faster                                               |
| regex_compile             | 144 ms                                                       | 143 ms: 1.01x faster                                               |
| 2to3                      | 291 ms                                                       | 289 ms: 1.01x faster                                               |
| unpickle_pure_python      | 214 us                                                       | 213 us: 1.01x faster                                               |
| asyncio_tcp_ssl           | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                             |
| spectral_norm             | 97.4 ms                                                      | 97.6 ms: 1.00x slower                                              |
| python_startup_no_site    | 8.94 ms                                                      | 8.98 ms: 1.00x slower                                              |
| json_loads                | 24.0 us                                                      | 24.1 us: 1.00x slower                                              |
| meteor_contest            | 128 ms                                                       | 129 ms: 1.00x slower                                               |
| crypto_pyaes              | 72.8 ms                                                      | 73.1 ms: 1.00x slower                                              |
| sqlglot_transpile         | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                              |
| regex_effbot              | 3.37 ms                                                      | 3.39 ms: 1.01x slower                                              |
| sympy_integrate           | 23.3 ms                                                      | 23.5 ms: 1.01x slower                                              |
| pidigits                  | 253 ms                                                       | 254 ms: 1.01x slower                                               |
| sympy_str                 | 296 ms                                                       | 298 ms: 1.01x slower                                               |
| regex_v8                  | 26.2 ms                                                      | 26.4 ms: 1.01x slower                                              |
| regex_dna                 | 244 ms                                                       | 245 ms: 1.01x slower                                               |
| sympy_expand              | 505 ms                                                       | 508 ms: 1.01x slower                                               |
| hexiom                    | 6.33 ms                                                      | 6.40 ms: 1.01x slower                                              |
| xml_etree_generate        | 85.3 ms                                                      | 86.2 ms: 1.01x slower                                              |
| logging_simple            | 6.40 us                                                      | 6.46 us: 1.01x slower                                              |
| generators                | 33.5 ms                                                      | 33.9 ms: 1.01x slower                                              |
| html5lib                  | 71.9 ms                                                      | 72.8 ms: 1.01x slower                                              |
| scimark_lu                | 97.8 ms                                                      | 99.0 ms: 1.01x slower                                              |
| scimark_sor               | 126 ms                                                       | 127 ms: 1.01x slower                                               |
| django_template           | 38.9 ms                                                      | 39.3 ms: 1.01x slower                                              |
| thrift                    | 877 us                                                       | 888 us: 1.01x slower                                               |
| sympy_sum                 | 154 ms                                                       | 156 ms: 1.01x slower                                               |
| asyncio_websockets        | 382 ms                                                       | 390 ms: 1.02x slower                                               |
| sqlglot_parse             | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed   | 600 ms                                                       | 612 ms: 1.02x slower                                               |
| scimark_sparse_mat_mult   | 4.29 ms                                                      | 4.38 ms: 1.02x slower                                              |
| pprint_pformat            | 1.65 sec                                                     | 1.69 sec: 1.02x slower                                             |
| pprint_safe_repr          | 812 ms                                                       | 831 ms: 1.02x slower                                               |
| json_dumps                | 11.0 ms                                                      | 11.2 ms: 1.02x slower                                              |
| nqueens                   | 88.2 ms                                                      | 90.4 ms: 1.02x slower                                              |
| sqlglot_normalize         | 118 ms                                                       | 121 ms: 1.03x slower                                               |
| xml_etree_iterparse       | 100 ms                                                       | 103 ms: 1.03x slower                                               |
| async_tree_memoization    | 452 ms                                                       | 466 ms: 1.03x slower                                               |
| async_generators          | 359 ms                                                       | 370 ms: 1.03x slower                                               |
| scimark_monte_carlo       | 64.9 ms                                                      | 67.0 ms: 1.03x slower                                              |
| nbody                     | 88.0 ms                                                      | 92.0 ms: 1.05x slower                                              |
| dask                      | 379 ms                                                       | 398 ms: 1.05x slower                                               |
| async_tree_io             | 847 ms                                                       | 895 ms: 1.06x slower                                               |
| docutils                  | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                             |
| gc_traversal              | 4.11 ms                                                      | 4.45 ms: 1.08x slower                                              |
| async_tree_io_tg          | 819 ms                                                       | 911 ms: 1.11x slower                                               |
| create_gc_cycles          | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                              |
| Geometric mean            | (ref)                                                        | 1.00x faster                                                       |

Benchmark hidden because not significant (16): json, pickle_pure_python, comprehensions, typing_runtime_protocols, bpe_tokeniser, python_startup, sqlglot_optimize, pycparser, xml_etree_process, logging_silent, mako, bench_thread_pool, async_tree_cpu_io_mixed_tg, bench_mp_pool, pylint, async_tree_none_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 83.69% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x