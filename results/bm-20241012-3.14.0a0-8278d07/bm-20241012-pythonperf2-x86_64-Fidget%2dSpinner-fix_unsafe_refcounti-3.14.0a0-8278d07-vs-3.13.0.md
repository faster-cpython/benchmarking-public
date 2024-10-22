# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-x86_64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 280 ms: 1.04x faster                                                                  |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                                |
| html5lib       | 71.9 ms                                                      | 70.1 ms: 1.03x faster                                                                 |
| tornado_http   | 120 ms                                                       | 116 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 393 ms: 1.17x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 321 ms: 1.16x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 803 ms: 1.05x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 783 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 550 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                                  |
| asyncio_tcp                | 380 ms                                                       | 371 ms: 1.02x faster                                                                  |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                                |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                                  |
| async_generators           | 359 ms                                                       | 371 ms: 1.03x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                          |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 80.6 ms: 1.02x faster                                                                 |
| nbody          | 88.0 ms                                                      | 89.8 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 24.9 ms: 1.05x faster                                                                 |
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                                  |
| regex_dna      | 244 ms                                                       | 242 ms: 1.01x faster                                                                  |
| regex_effbot   | 3.37 ms                                                      | 3.46 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|---------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_dict         | 32.1 us                                                      | 30.4 us: 1.05x faster                                                                 |
| xml_etree_process   | 60.9 ms                                                      | 59.9 ms: 1.02x faster                                                                 |
| pickle_pure_python  | 318 us                                                       | 317 us: 1.01x faster                                                                  |
| xml_etree_generate  | 85.3 ms                                                      | 84.9 ms: 1.01x faster                                                                 |
| pickle              | 10.5 us                                                      | 10.6 us: 1.00x slower                                                                 |
| xml_etree_iterparse | 100 ms                                                       | 101 ms: 1.01x slower                                                                  |
| unpickle_list       | 4.62 us                                                      | 4.69 us: 1.01x slower                                                                 |
| unpickle            | 15.1 us                                                      | 15.7 us: 1.04x slower                                                                 |
| tomli_loads         | 2.41 sec                                                     | 2.50 sec: 1.04x slower                                                                |
| json_loads          | 24.0 us                                                      | 24.9 us: 1.04x slower                                                                 |
| json_dumps          | 11.0 ms                                                      | 12.1 ms: 1.10x slower                                                                 |
| Geometric mean      | (ref)                                                        | 1.01x slower                                                                          |

Benchmark hidden because not significant (3): pickle_list, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.96 ms: 1.00x slower                                                                 |
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 24.6 ms: 1.08x faster                                                                 |
| genshi_xml      | 57.3 ms                                                      | 53.1 ms: 1.08x faster                                                                 |
| mako            | 10.4 ms                                                      | 10.8 ms: 1.03x slower                                                                 |
| django_template | 38.9 ms                                                      | 42.7 ms: 1.10x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 287 us: 1.38x faster                                                                  |
| deepcopy_memo              | 39.5 us                                                      | 29.6 us: 1.33x faster                                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 2.96 us: 1.19x faster                                                                 |
| async_tree_memoization_tg  | 461 ms                                                       | 393 ms: 1.17x faster                                                                  |
| go                         | 160 ms                                                       | 137 ms: 1.17x faster                                                                  |
| scimark_sor                | 126 ms                                                       | 108 ms: 1.16x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 321 ms: 1.16x faster                                                                  |
| unpack_sequence            | 56.8 ns                                                      | 49.1 ns: 1.16x faster                                                                 |
| generators                 | 33.5 ms                                                      | 29.3 ms: 1.14x faster                                                                 |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                                                  |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.11x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                       | 309 ms: 1.10x faster                                                                  |
| telco                      | 8.58 ms                                                      | 7.88 ms: 1.09x faster                                                                 |
| genshi_text                | 26.6 ms                                                      | 24.6 ms: 1.08x faster                                                                 |
| raytrace                   | 289 ms                                                       | 267 ms: 1.08x faster                                                                  |
| genshi_xml                 | 57.3 ms                                                      | 53.1 ms: 1.08x faster                                                                 |
| richards                   | 52.7 ms                                                      | 49.3 ms: 1.07x faster                                                                 |
| richards_super             | 59.8 ms                                                      | 56.2 ms: 1.06x faster                                                                 |
| bpe_tokeniser              | 5.10 sec                                                     | 4.80 sec: 1.06x faster                                                                |
| scimark_fft                | 314 ms                                                       | 298 ms: 1.06x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 803 ms: 1.05x faster                                                                  |
| pickle_dict                | 32.1 us                                                      | 30.4 us: 1.05x faster                                                                 |
| regex_v8                   | 26.2 ms                                                      | 24.9 ms: 1.05x faster                                                                 |
| async_tree_io_tg           | 819 ms                                                       | 783 ms: 1.05x faster                                                                  |
| meteor_contest             | 128 ms                                                       | 123 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 550 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                                  |
| 2to3                       | 291 ms                                                       | 280 ms: 1.04x faster                                                                  |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.13 ms: 1.04x faster                                                                 |
| scimark_lu                 | 97.8 ms                                                      | 94.3 ms: 1.04x faster                                                                 |
| pycparser                  | 1.26 sec                                                     | 1.21 sec: 1.04x faster                                                                |
| pprint_safe_repr           | 812 ms                                                       | 784 ms: 1.03x faster                                                                  |
| fannkuch                   | 365 ms                                                       | 353 ms: 1.03x faster                                                                  |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                                  |
| tornado_http               | 120 ms                                                       | 116 ms: 1.03x faster                                                                  |
| coverage                   | 81.1 ms                                                      | 78.9 ms: 1.03x faster                                                                 |
| html5lib                   | 71.9 ms                                                      | 70.1 ms: 1.03x faster                                                                 |
| asyncio_tcp                | 380 ms                                                       | 371 ms: 1.02x faster                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.02x faster                                                                |
| mdp                        | 2.52 sec                                                     | 2.47 sec: 1.02x faster                                                                |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                                  |
| sympy_str                  | 296 ms                                                       | 290 ms: 1.02x faster                                                                  |
| sympy_expand               | 505 ms                                                       | 495 ms: 1.02x faster                                                                  |
| pyflate                    | 492 ms                                                       | 484 ms: 1.02x faster                                                                  |
| sqlite_synth               | 2.79 us                                                      | 2.74 us: 1.02x faster                                                                 |
| float                      | 81.9 ms                                                      | 80.6 ms: 1.02x faster                                                                 |
| xml_etree_process          | 60.9 ms                                                      | 59.9 ms: 1.02x faster                                                                 |
| hexiom                     | 6.33 ms                                                      | 6.26 ms: 1.01x faster                                                                 |
| spectral_norm              | 97.4 ms                                                      | 96.5 ms: 1.01x faster                                                                 |
| regex_dna                  | 244 ms                                                       | 242 ms: 1.01x faster                                                                  |
| comprehensions             | 17.3 us                                                      | 17.1 us: 1.01x faster                                                                 |
| pickle_pure_python         | 318 us                                                       | 317 us: 1.01x faster                                                                  |
| xml_etree_generate         | 85.3 ms                                                      | 84.9 ms: 1.01x faster                                                                 |
| deltablue                  | 3.41 ms                                                      | 3.39 ms: 1.00x faster                                                                 |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                                |
| python_startup_no_site     | 8.94 ms                                                      | 8.96 ms: 1.00x slower                                                                 |
| sympy_integrate            | 23.3 ms                                                      | 23.4 ms: 1.00x slower                                                                 |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.00x slower                                                                 |
| crypto_pyaes               | 72.8 ms                                                      | 73.1 ms: 1.00x slower                                                                 |
| logging_silent             | 97.7 ns                                                      | 98.2 ns: 1.01x slower                                                                 |
| dulwich_log                | 65.5 ms                                                      | 65.9 ms: 1.01x slower                                                                 |
| typing_runtime_protocols   | 174 us                                                       | 175 us: 1.01x slower                                                                  |
| sqlglot_normalize          | 118 ms                                                       | 119 ms: 1.01x slower                                                                  |
| xml_etree_iterparse        | 100 ms                                                       | 101 ms: 1.01x slower                                                                  |
| unpickle_list              | 4.62 us                                                      | 4.69 us: 1.01x slower                                                                 |
| logging_simple             | 6.40 us                                                      | 6.52 us: 1.02x slower                                                                 |
| nqueens                    | 88.2 ms                                                      | 90.0 ms: 1.02x slower                                                                 |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                                  |
| nbody                      | 88.0 ms                                                      | 89.8 ms: 1.02x slower                                                                 |
| scimark_monte_carlo        | 64.9 ms                                                      | 66.4 ms: 1.02x slower                                                                 |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                                 |
| regex_effbot               | 3.37 ms                                                      | 3.46 ms: 1.03x slower                                                                 |
| chaos                      | 61.7 ms                                                      | 63.5 ms: 1.03x slower                                                                 |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                                |
| async_generators           | 359 ms                                                       | 371 ms: 1.03x slower                                                                  |
| json                       | 5.22 ms                                                      | 5.39 ms: 1.03x slower                                                                 |
| mako                       | 10.4 ms                                                      | 10.8 ms: 1.03x slower                                                                 |
| unpickle                   | 15.1 us                                                      | 15.7 us: 1.04x slower                                                                 |
| tomli_loads                | 2.41 sec                                                     | 2.50 sec: 1.04x slower                                                                |
| json_loads                 | 24.0 us                                                      | 24.9 us: 1.04x slower                                                                 |
| django_template            | 38.9 ms                                                      | 42.7 ms: 1.10x slower                                                                 |
| json_dumps                 | 11.0 ms                                                      | 12.1 ms: 1.10x slower                                                                 |
| gc_traversal               | 4.11 ms                                                      | 4.74 ms: 1.15x slower                                                                 |
| create_gc_cycles           | 1.76 ms                                                      | 2.06 ms: 1.17x slower                                                                 |
| bench_mp_pool              | 4.65 ms                                                      | 2.45 sec: 527.39x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                          |

Benchmark hidden because not significant (11): bench_thread_pool, coroutines, pickle_list, sqlglot_optimize, pylint, pidigits, thrift, xml_etree_parse, logging_format, unpickle_pure_python, sqlglot_transpile
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x