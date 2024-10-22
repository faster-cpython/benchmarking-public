# Results vs. 3.13.0

- fork: mdboom
- ref: initialize_locals
- machine: linux-x86_64
- commit hash: 1021191
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 284 ms: 1.03x faster                                                     |
| docutils       | 2.81 sec                                                     | 2.93 sec: 1.04x slower                                                   |
| html5lib       | 71.9 ms                                                      | 71.2 ms: 1.01x faster                                                    |
| tornado_http   | 120 ms                                                       | 117 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                        | 1.00x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                     |
| async_tree_none            | 372 ms                                                       | 323 ms: 1.15x faster                                                     |
| async_tree_memoization     | 452 ms                                                       | 402 ms: 1.13x faster                                                     |
| async_tree_none_tg         | 340 ms                                                       | 311 ms: 1.09x faster                                                     |
| async_tree_io              | 847 ms                                                       | 806 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 551 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                     |
| async_tree_io_tg           | 819 ms                                                       | 792 ms: 1.03x faster                                                     |
| asyncio_tcp                | 380 ms                                                       | 369 ms: 1.03x faster                                                     |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                    |
| asyncio_websockets         | 382 ms                                                       | 387 ms: 1.01x slower                                                     |
| async_generators           | 359 ms                                                       | 371 ms: 1.03x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                             |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.4 ms: 1.04x faster                                                    |
| nbody          | 88.0 ms                                                      | 84.8 ms: 1.04x faster                                                    |
| pidigits       | 253 ms                                                       | 253 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                        | 1.03x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 235 ms: 1.04x faster                                                     |
| regex_compile  | 144 ms                                                       | 142 ms: 1.02x faster                                                     |
| regex_v8       | 26.2 ms                                                      | 26.9 ms: 1.03x slower                                                    |
| regex_effbot   | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                        | 1.00x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_process    | 60.9 ms                                                      | 59.5 ms: 1.02x faster                                                    |
| xml_etree_generate   | 85.3 ms                                                      | 85.7 ms: 1.00x slower                                                    |
| xml_etree_iterparse  | 100 ms                                                       | 101 ms: 1.01x slower                                                     |
| unpickle_pure_python | 214 us                                                       | 219 us: 1.02x slower                                                     |
| json_loads           | 24.0 us                                                      | 24.9 us: 1.04x slower                                                    |
| tomli_loads          | 2.41 sec                                                     | 2.58 sec: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                    |
| python_startup_no_site | 8.94 ms                                                      | 9.09 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 53.6 ms: 1.07x faster                                                    |
| genshi_text     | 26.6 ms                                                      | 24.9 ms: 1.07x faster                                                    |
| django_template | 38.9 ms                                                      | 41.2 ms: 1.06x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 287 us: 1.38x faster                                                     |
| deepcopy_memo              | 39.5 us                                                      | 29.9 us: 1.32x faster                                                    |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                                    |
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                     |
| go                         | 160 ms                                                       | 137 ms: 1.17x faster                                                     |
| async_tree_none            | 372 ms                                                       | 323 ms: 1.15x faster                                                     |
| generators                 | 33.5 ms                                                      | 29.1 ms: 1.15x faster                                                    |
| async_tree_memoization     | 452 ms                                                       | 402 ms: 1.13x faster                                                     |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                    |
| async_tree_none_tg         | 340 ms                                                       | 311 ms: 1.09x faster                                                     |
| genshi_xml                 | 57.3 ms                                                      | 53.6 ms: 1.07x faster                                                    |
| genshi_text                | 26.6 ms                                                      | 24.9 ms: 1.07x faster                                                    |
| richards_super             | 59.8 ms                                                      | 56.5 ms: 1.06x faster                                                    |
| scimark_sor                | 126 ms                                                       | 119 ms: 1.06x faster                                                     |
| richards                   | 52.7 ms                                                      | 50.0 ms: 1.05x faster                                                    |
| async_tree_io              | 847 ms                                                       | 806 ms: 1.05x faster                                                     |
| pyflate                    | 492 ms                                                       | 469 ms: 1.05x faster                                                     |
| float                      | 81.9 ms                                                      | 78.4 ms: 1.04x faster                                                    |
| logging_format             | 7.07 us                                                      | 6.78 us: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 551 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                     |
| bench_thread_pool          | 901 us                                                       | 866 us: 1.04x faster                                                     |
| fannkuch                   | 365 ms                                                       | 351 ms: 1.04x faster                                                     |
| bpe_tokeniser              | 5.10 sec                                                     | 4.91 sec: 1.04x faster                                                   |
| regex_dna                  | 244 ms                                                       | 235 ms: 1.04x faster                                                     |
| nbody                      | 88.0 ms                                                      | 84.8 ms: 1.04x faster                                                    |
| async_tree_io_tg           | 819 ms                                                       | 792 ms: 1.03x faster                                                     |
| asyncio_tcp                | 380 ms                                                       | 369 ms: 1.03x faster                                                     |
| tornado_http               | 120 ms                                                       | 117 ms: 1.03x faster                                                     |
| 2to3                       | 291 ms                                                       | 284 ms: 1.03x faster                                                     |
| telco                      | 8.58 ms                                                      | 8.37 ms: 1.03x faster                                                    |
| scimark_lu                 | 97.8 ms                                                      | 95.6 ms: 1.02x faster                                                    |
| xml_etree_process          | 60.9 ms                                                      | 59.5 ms: 1.02x faster                                                    |
| hexiom                     | 6.33 ms                                                      | 6.20 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 812 ms                                                       | 795 ms: 1.02x faster                                                     |
| logging_simple             | 6.40 us                                                      | 6.27 us: 1.02x faster                                                    |
| regex_compile              | 144 ms                                                       | 142 ms: 1.02x faster                                                     |
| raytrace                   | 289 ms                                                       | 285 ms: 1.02x faster                                                     |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                   |
| coverage                   | 81.1 ms                                                      | 80.1 ms: 1.01x faster                                                    |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                     |
| html5lib                   | 71.9 ms                                                      | 71.2 ms: 1.01x faster                                                    |
| spectral_norm              | 97.4 ms                                                      | 96.5 ms: 1.01x faster                                                    |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                    |
| sympy_integrate            | 23.3 ms                                                      | 23.2 ms: 1.01x faster                                                    |
| thrift                     | 877 us                                                       | 872 us: 1.01x faster                                                     |
| scimark_fft                | 314 ms                                                       | 313 ms: 1.00x faster                                                     |
| sympy_str                  | 296 ms                                                       | 295 ms: 1.00x faster                                                     |
| pidigits                   | 253 ms                                                       | 253 ms: 1.00x slower                                                     |
| sympy_expand               | 505 ms                                                       | 506 ms: 1.00x slower                                                     |
| mdp                        | 2.52 sec                                                     | 2.53 sec: 1.00x slower                                                   |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.30 ms: 1.00x slower                                                    |
| xml_etree_generate         | 85.3 ms                                                      | 85.7 ms: 1.00x slower                                                    |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                    |
| asyncio_websockets         | 382 ms                                                       | 387 ms: 1.01x slower                                                     |
| xml_etree_iterparse        | 100 ms                                                       | 101 ms: 1.01x slower                                                     |
| json                       | 5.22 ms                                                      | 5.30 ms: 1.01x slower                                                    |
| crypto_pyaes               | 72.8 ms                                                      | 73.9 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.94 ms                                                      | 9.09 ms: 1.02x slower                                                    |
| sqlglot_normalize          | 118 ms                                                       | 120 ms: 1.02x slower                                                     |
| comprehensions             | 17.3 us                                                      | 17.6 us: 1.02x slower                                                    |
| nqueens                    | 88.2 ms                                                      | 89.9 ms: 1.02x slower                                                    |
| unpickle_pure_python       | 214 us                                                       | 219 us: 1.02x slower                                                     |
| sqlglot_transpile          | 1.78 ms                                                      | 1.83 ms: 1.03x slower                                                    |
| scimark_monte_carlo        | 64.9 ms                                                      | 66.7 ms: 1.03x slower                                                    |
| regex_v8                   | 26.2 ms                                                      | 26.9 ms: 1.03x slower                                                    |
| async_generators           | 359 ms                                                       | 371 ms: 1.03x slower                                                     |
| json_loads                 | 24.0 us                                                      | 24.9 us: 1.04x slower                                                    |
| logging_silent             | 97.7 ns                                                      | 101 ns: 1.04x slower                                                     |
| regex_effbot               | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                      | 1.44 ms: 1.04x slower                                                    |
| docutils                   | 2.81 sec                                                     | 2.93 sec: 1.04x slower                                                   |
| django_template            | 38.9 ms                                                      | 41.2 ms: 1.06x slower                                                    |
| tomli_loads                | 2.41 sec                                                     | 2.58 sec: 1.07x slower                                                   |
| gc_traversal               | 4.11 ms                                                      | 4.47 ms: 1.09x slower                                                    |
| create_gc_cycles           | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                             |

Benchmark hidden because not significant (13): bench_mp_pool, mako, xml_etree_parse, sympy_sum, pycparser, asyncio_tcp_ssl, pickle_pure_python, json_dumps, sqlglot_optimize, chaos, deltablue, typing_runtime_protocols, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x