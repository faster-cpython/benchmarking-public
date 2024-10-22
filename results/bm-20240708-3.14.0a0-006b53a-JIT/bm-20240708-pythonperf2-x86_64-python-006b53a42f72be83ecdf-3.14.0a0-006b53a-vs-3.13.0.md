# Results vs. 3.13.0

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: linux-x86_64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.01x faster
- HPT reliability: 60.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 306 ms: 1.05x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.11 sec: 1.11x slower                                                      |
| html5lib       | 71.9 ms                                                      | 71.4 ms: 1.01x faster                                                       |
| tornado_http   | 120 ms                                                       | 121 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 381 ms: 1.21x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 302 ms: 1.13x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 405 ms: 1.12x faster                                                        |
| async_tree_none            | 372 ms                                                       | 336 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 536 ms: 1.07x faster                                                        |
| async_tree_io              | 847 ms                                                       | 810 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 788 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 577 ms: 1.04x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.03x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 375 ms: 1.01x faster                                                        |
| asyncio_websockets         | 382 ms                                                       | 394 ms: 1.03x slower                                                        |
| async_generators           | 359 ms                                                       | 385 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 75.7 ms: 1.08x faster                                                       |
| nbody          | 88.0 ms                                                      | 83.1 ms: 1.06x faster                                                       |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.05x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 26.8 ms: 1.02x slower                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.46 ms: 1.03x slower                                                       |
| regex_dna      | 244 ms                                                       | 256 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.11 sec: 1.14x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 58.5 ms: 1.04x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 82.1 ms: 1.04x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 99.0 ms: 1.01x faster                                                       |
| unpickle_pure_python | 214 us                                                       | 217 us: 1.01x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (2): pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.08 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.21 ms: 1.13x faster                                                       |
| genshi_text     | 26.6 ms                                                      | 28.5 ms: 1.07x slower                                                       |
| django_template | 38.9 ms                                                      | 42.1 ms: 1.08x slower                                                       |
| genshi_xml      | 57.3 ms                                                      | 63.8 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 28.0 us: 1.41x faster                                                       |
| deepcopy                   | 397 us                                                       | 310 us: 1.28x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 381 ms: 1.21x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 82.9 ms: 1.17x faster                                                       |
| richards                   | 52.7 ms                                                      | 44.9 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 3.05 us: 1.16x faster                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.11 sec: 1.14x faster                                                      |
| mako                       | 10.4 ms                                                      | 9.21 ms: 1.13x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 302 ms: 1.13x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 405 ms: 1.12x faster                                                        |
| richards_super             | 59.8 ms                                                      | 53.6 ms: 1.12x faster                                                       |
| pyflate                    | 492 ms                                                       | 443 ms: 1.11x faster                                                        |
| async_tree_none            | 372 ms                                                       | 336 ms: 1.11x faster                                                        |
| float                      | 81.9 ms                                                      | 75.7 ms: 1.08x faster                                                       |
| scimark_fft                | 314 ms                                                       | 291 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 536 ms: 1.07x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 16.3 ms: 1.07x faster                                                       |
| telco                      | 8.58 ms                                                      | 8.07 ms: 1.06x faster                                                       |
| nbody                      | 88.0 ms                                                      | 83.1 ms: 1.06x faster                                                       |
| regex_compile              | 144 ms                                                       | 138 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 810 ms: 1.05x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 58.5 ms: 1.04x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 82.1 ms: 1.04x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 788 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 577 ms: 1.04x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.21 sec: 1.04x faster                                                      |
| coverage                   | 81.1 ms                                                      | 78.8 ms: 1.03x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 70.7 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.17 ms: 1.03x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.03x faster                                                       |
| fannkuch                   | 365 ms                                                       | 358 ms: 1.02x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 375 ms: 1.01x faster                                                        |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| raytrace                   | 289 ms                                                       | 286 ms: 1.01x faster                                                        |
| xml_etree_iterparse        | 100 ms                                                       | 99.0 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 805 ms: 1.01x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 71.4 ms: 1.01x faster                                                       |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 64.8 ms: 1.00x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 5.11 sec: 1.00x slower                                                      |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.01x slower                                                        |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| mdp                        | 2.52 sec                                                     | 2.55 sec: 1.01x slower                                                      |
| unpickle_pure_python       | 214 us                                                       | 217 us: 1.01x slower                                                        |
| tornado_http               | 120 ms                                                       | 121 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 9.08 ms: 1.02x slower                                                       |
| bench_thread_pool          | 901 us                                                       | 921 us: 1.02x slower                                                        |
| scimark_sor                | 126 ms                                                       | 128 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.02x slower                                                       |
| regex_v8                   | 26.2 ms                                                      | 26.8 ms: 1.02x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 67.2 ms: 1.03x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.46 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 394 ms: 1.03x slower                                                        |
| logging_silent             | 97.7 ns                                                      | 101 ns: 1.03x slower                                                        |
| generators                 | 33.5 ms                                                      | 34.7 ms: 1.04x slower                                                       |
| sympy_expand               | 505 ms                                                       | 526 ms: 1.04x slower                                                        |
| json                       | 5.22 ms                                                      | 5.46 ms: 1.05x slower                                                       |
| thrift                     | 877 us                                                       | 918 us: 1.05x slower                                                        |
| gc_traversal               | 4.11 ms                                                      | 4.31 ms: 1.05x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 6.64 ms: 1.05x slower                                                       |
| regex_dna                  | 244 ms                                                       | 256 ms: 1.05x slower                                                        |
| 2to3                       | 291 ms                                                       | 306 ms: 1.05x slower                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 4.91 ms: 1.06x slower                                                       |
| sympy_str                  | 296 ms                                                       | 312 ms: 1.06x slower                                                        |
| dask                       | 379 ms                                                       | 400 ms: 1.06x slower                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 63.0 ms: 1.06x slower                                                       |
| comprehensions             | 17.3 us                                                      | 18.2 us: 1.06x slower                                                       |
| typing_runtime_protocols   | 174 us                                                       | 184 us: 1.06x slower                                                        |
| chaos                      | 61.7 ms                                                      | 65.6 ms: 1.06x slower                                                       |
| genshi_text                | 26.6 ms                                                      | 28.5 ms: 1.07x slower                                                       |
| async_generators           | 359 ms                                                       | 385 ms: 1.07x slower                                                        |
| pylint                     | 346 ms                                                       | 371 ms: 1.07x slower                                                        |
| sqlglot_normalize          | 118 ms                                                       | 128 ms: 1.08x slower                                                        |
| django_template            | 38.9 ms                                                      | 42.1 ms: 1.08x slower                                                       |
| deltablue                  | 3.41 ms                                                      | 3.70 ms: 1.08x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 168 ms: 1.09x slower                                                        |
| create_gc_cycles           | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 96.5 ms: 1.09x slower                                                       |
| sympy_integrate            | 23.3 ms                                                      | 25.6 ms: 1.10x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.11 sec: 1.11x slower                                                      |
| genshi_xml                 | 57.3 ms                                                      | 63.8 ms: 1.11x slower                                                       |
| scimark_lu                 | 97.8 ms                                                      | 112 ms: 1.15x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (7): pickle_pure_python, logging_simple, pprint_pformat, asyncio_tcp_ssl, logging_format, go, json_dumps
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 60.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x