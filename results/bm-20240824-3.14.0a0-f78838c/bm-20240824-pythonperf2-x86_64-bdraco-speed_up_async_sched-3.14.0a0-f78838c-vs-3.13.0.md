# Results vs. 3.13.0

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-x86_64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 281 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                      |
| html5lib       | 71.9 ms                                                      | 73.1 ms: 1.02x slower                                                       |
| tornado_http   | 120 ms                                                       | 117 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 379 ms: 1.22x faster                                                        |
| async_tree_none            | 372 ms                                                       | 318 ms: 1.17x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 404 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 558 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 775 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 550 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 366 ms: 1.04x faster                                                        |
| async_tree_io              | 847 ms                                                       | 827 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.59 sec: 1.00x slower                                                      |
| asyncio_websockets         | 382 ms                                                       | 388 ms: 1.02x slower                                                        |
| async_generators           | 359 ms                                                       | 368 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.9 ms: 1.04x faster                                                       |
| pidigits       | 253 ms                                                       | 252 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 234 ms: 1.04x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 25.3 ms: 1.04x faster                                                       |
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 144 ms: 1.01x faster                                                        |
| unpickle_pure_python | 214 us                                                       | 216 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 102 ms: 1.02x slower                                                        |
| xml_etree_generate   | 85.3 ms                                                      | 87.4 ms: 1.02x slower                                                       |
| json_loads           | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.56 sec: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text    | 26.6 ms                                                      | 24.9 ms: 1.07x faster                                                       |
| genshi_xml     | 57.3 ms                                                      | 54.3 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 285 us: 1.39x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.0 us: 1.36x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 379 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.93 us: 1.21x faster                                                       |
| async_tree_none            | 372 ms                                                       | 318 ms: 1.17x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.8 ms: 1.16x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 404 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                       |
| raytrace                   | 289 ms                                                       | 267 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 558 ms: 1.07x faster                                                        |
| richards_super             | 59.8 ms                                                      | 56.0 ms: 1.07x faster                                                       |
| scimark_sor                | 126 ms                                                       | 118 ms: 1.07x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 24.9 ms: 1.07x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 775 ms: 1.06x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 54.3 ms: 1.06x faster                                                       |
| bench_thread_pool          | 901 us                                                       | 859 us: 1.05x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.18 ms: 1.05x faster                                                       |
| richards                   | 52.7 ms                                                      | 50.3 ms: 1.05x faster                                                       |
| scimark_fft                | 314 ms                                                       | 300 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 550 ms: 1.04x faster                                                        |
| regex_dna                  | 244 ms                                                       | 234 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 366 ms: 1.04x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.91 sec: 1.04x faster                                                      |
| float                      | 81.9 ms                                                      | 78.9 ms: 1.04x faster                                                       |
| pyflate                    | 492 ms                                                       | 474 ms: 1.04x faster                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 4.48 ms: 1.04x faster                                                       |
| regex_v8                   | 26.2 ms                                                      | 25.3 ms: 1.04x faster                                                       |
| thrift                     | 877 us                                                       | 846 us: 1.04x faster                                                        |
| fannkuch                   | 365 ms                                                       | 352 ms: 1.04x faster                                                        |
| 2to3                       | 291 ms                                                       | 281 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| tornado_http               | 120 ms                                                       | 117 ms: 1.03x faster                                                        |
| async_tree_io              | 847 ms                                                       | 827 ms: 1.02x faster                                                        |
| mdp                        | 2.52 sec                                                     | 2.48 sec: 1.02x faster                                                      |
| sympy_str                  | 296 ms                                                       | 290 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| hexiom                     | 6.33 ms                                                      | 6.23 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 23.0 ms: 1.01x faster                                                       |
| typing_runtime_protocols   | 174 us                                                       | 172 us: 1.01x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 59.0 ms: 1.01x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| sympy_expand               | 505 ms                                                       | 499 ms: 1.01x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 96.8 ms: 1.01x faster                                                       |
| chaos                      | 61.7 ms                                                      | 61.1 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| xml_etree_parse            | 145 ms                                                       | 144 ms: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.8 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 807 ms: 1.01x faster                                                        |
| pidigits                   | 253 ms                                                       | 252 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.59 sec: 1.00x slower                                                      |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 119 ms: 1.01x slower                                                        |
| deltablue                  | 3.41 ms                                                      | 3.44 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 216 us: 1.01x slower                                                        |
| pycparser                  | 1.26 sec                                                     | 1.27 sec: 1.01x slower                                                      |
| python_startup_no_site     | 8.94 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.34 ms: 1.01x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 388 ms: 1.02x slower                                                        |
| html5lib                   | 71.9 ms                                                      | 73.1 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 102 ms: 1.02x slower                                                        |
| logging_silent             | 97.7 ns                                                      | 99.3 ns: 1.02x slower                                                       |
| logging_format             | 7.07 us                                                      | 7.19 us: 1.02x slower                                                       |
| logging_simple             | 6.40 us                                                      | 6.52 us: 1.02x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 90.0 ms: 1.02x slower                                                       |
| coverage                   | 81.1 ms                                                      | 83.1 ms: 1.02x slower                                                       |
| async_generators           | 359 ms                                                       | 368 ms: 1.02x slower                                                        |
| xml_etree_generate         | 85.3 ms                                                      | 87.4 ms: 1.02x slower                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 74.6 ms: 1.03x slower                                                       |
| json                       | 5.22 ms                                                      | 5.40 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.03x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                      |
| tomli_loads                | 2.41 sec                                                     | 2.56 sec: 1.06x slower                                                      |
| gc_traversal               | 4.11 ms                                                      | 4.48 ms: 1.09x slower                                                       |
| go                         | 160 ms                                                       | 181 ms: 1.13x slower                                                        |
| create_gc_cycles           | 1.76 ms                                                      | 2.02 ms: 1.15x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (8): pickle_pure_python, xml_etree_process, nbody, mako, scimark_monte_carlo, comprehensions, django_template, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x