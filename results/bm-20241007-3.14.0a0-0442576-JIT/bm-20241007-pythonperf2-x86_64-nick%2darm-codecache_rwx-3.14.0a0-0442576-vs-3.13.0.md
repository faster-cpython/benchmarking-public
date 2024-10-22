# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.07x slower
- HPT reliability: 76.23%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 315 ms: 1.08x slower                                                     |
| docutils       | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                                   |
| html5lib       | 71.9 ms                                                      | 73.1 ms: 1.02x slower                                                    |
| tornado_http   | 120 ms                                                       | 123 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                        | 1.06x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                     |
| async_tree_none            | 372 ms                                                       | 329 ms: 1.13x faster                                                     |
| async_tree_memoization     | 452 ms                                                       | 407 ms: 1.11x faster                                                     |
| async_tree_none_tg         | 340 ms                                                       | 312 ms: 1.09x faster                                                     |
| async_tree_io              | 847 ms                                                       | 805 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 547 ms: 1.05x faster                                                     |
| async_tree_io_tg           | 819 ms                                                       | 782 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 580 ms: 1.03x faster                                                     |
| asyncio_tcp                | 380 ms                                                       | 371 ms: 1.02x faster                                                     |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                                   |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                     |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                    |
| async_generators           | 359 ms                                                       | 382 ms: 1.06x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 75.3 ms: 1.09x faster                                                    |
| nbody          | 88.0 ms                                                      | 83.3 ms: 1.06x faster                                                    |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                        | 1.05x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 24.8 ms: 1.06x faster                                                    |
| regex_dna      | 244 ms                                                       | 236 ms: 1.03x faster                                                     |
| regex_compile  | 144 ms                                                       | 150 ms: 1.04x slower                                                     |
| regex_effbot   | 3.37 ms                                                      | 3.60 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.20 sec: 1.10x faster                                                   |
| xml_etree_generate   | 85.3 ms                                                      | 78.8 ms: 1.08x faster                                                    |
| xml_etree_process    | 60.9 ms                                                      | 56.4 ms: 1.08x faster                                                    |
| pickle_dict          | 32.1 us                                                      | 29.8 us: 1.08x faster                                                    |
| pickle_list          | 4.59 us                                                      | 4.30 us: 1.07x faster                                                    |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                                    |
| unpickle             | 15.1 us                                                      | 14.8 us: 1.02x faster                                                    |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                    |
| json_loads           | 24.0 us                                                      | 23.8 us: 1.01x faster                                                    |
| unpickle_list        | 4.62 us                                                      | 4.71 us: 1.02x slower                                                    |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                     |
| unpickle_pure_python | 214 us                                                       | 219 us: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.97 ms: 1.00x slower                                                    |
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.15 ms: 1.14x faster                                                    |
| genshi_text     | 26.6 ms                                                      | 29.8 ms: 1.12x slower                                                    |
| genshi_xml      | 57.3 ms                                                      | 66.2 ms: 1.16x slower                                                    |
| django_template | 38.9 ms                                                      | 46.0 ms: 1.18x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.08x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 27.3 us: 1.45x faster                                                    |
| deepcopy                   | 397 us                                                       | 300 us: 1.32x faster                                                     |
| deepcopy_reduce            | 3.54 us                                                      | 2.95 us: 1.20x faster                                                    |
| scimark_sor                | 126 ms                                                       | 105 ms: 1.19x faster                                                     |
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                     |
| spectral_norm              | 97.4 ms                                                      | 82.8 ms: 1.18x faster                                                    |
| mako                       | 10.4 ms                                                      | 9.15 ms: 1.14x faster                                                    |
| async_tree_none            | 372 ms                                                       | 329 ms: 1.13x faster                                                     |
| telco                      | 8.58 ms                                                      | 7.63 ms: 1.13x faster                                                    |
| scimark_fft                | 314 ms                                                       | 280 ms: 1.12x faster                                                     |
| richards                   | 52.7 ms                                                      | 47.3 ms: 1.11x faster                                                    |
| async_tree_memoization     | 452 ms                                                       | 407 ms: 1.11x faster                                                     |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                    |
| tomli_loads                | 2.41 sec                                                     | 2.20 sec: 1.10x faster                                                   |
| async_tree_none_tg         | 340 ms                                                       | 312 ms: 1.09x faster                                                     |
| float                      | 81.9 ms                                                      | 75.3 ms: 1.09x faster                                                    |
| xml_etree_generate         | 85.3 ms                                                      | 78.8 ms: 1.08x faster                                                    |
| pyflate                    | 492 ms                                                       | 456 ms: 1.08x faster                                                     |
| xml_etree_process          | 60.9 ms                                                      | 56.4 ms: 1.08x faster                                                    |
| richards_super             | 59.8 ms                                                      | 55.4 ms: 1.08x faster                                                    |
| pickle_dict                | 32.1 us                                                      | 29.8 us: 1.08x faster                                                    |
| bpe_tokeniser              | 5.10 sec                                                     | 4.75 sec: 1.07x faster                                                   |
| pickle_list                | 4.59 us                                                      | 4.30 us: 1.07x faster                                                    |
| pprint_safe_repr           | 812 ms                                                       | 762 ms: 1.06x faster                                                     |
| deltablue                  | 3.41 ms                                                      | 3.23 ms: 1.06x faster                                                    |
| nbody                      | 88.0 ms                                                      | 83.3 ms: 1.06x faster                                                    |
| regex_v8                   | 26.2 ms                                                      | 24.8 ms: 1.06x faster                                                    |
| fannkuch                   | 365 ms                                                       | 346 ms: 1.06x faster                                                     |
| async_tree_io              | 847 ms                                                       | 805 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 547 ms: 1.05x faster                                                     |
| async_tree_io_tg           | 819 ms                                                       | 782 ms: 1.05x faster                                                     |
| crypto_pyaes               | 72.8 ms                                                      | 70.0 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 580 ms: 1.03x faster                                                     |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.15 ms: 1.03x faster                                                    |
| regex_dna                  | 244 ms                                                       | 236 ms: 1.03x faster                                                     |
| pprint_pformat             | 1.65 sec                                                     | 1.60 sec: 1.03x faster                                                   |
| asyncio_tcp                | 380 ms                                                       | 371 ms: 1.02x faster                                                     |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                                    |
| sqlite_synth               | 2.79 us                                                      | 2.73 us: 1.02x faster                                                    |
| unpickle                   | 15.1 us                                                      | 14.8 us: 1.02x faster                                                    |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                    |
| scimark_lu                 | 97.8 ms                                                      | 96.0 ms: 1.02x faster                                                    |
| go                         | 160 ms                                                       | 158 ms: 1.01x faster                                                     |
| dulwich_log                | 65.5 ms                                                      | 64.8 ms: 1.01x faster                                                    |
| json_loads                 | 24.0 us                                                      | 23.8 us: 1.01x faster                                                    |
| json                       | 5.22 ms                                                      | 5.19 ms: 1.01x faster                                                    |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                                     |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                                   |
| python_startup_no_site     | 8.94 ms                                                      | 8.97 ms: 1.00x slower                                                    |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                    |
| logging_silent             | 97.7 ns                                                      | 98.1 ns: 1.00x slower                                                    |
| typing_runtime_protocols   | 174 us                                                       | 176 us: 1.01x slower                                                     |
| html5lib                   | 71.9 ms                                                      | 73.1 ms: 1.02x slower                                                    |
| unpickle_list              | 4.62 us                                                      | 4.71 us: 1.02x slower                                                    |
| coverage                   | 81.1 ms                                                      | 82.6 ms: 1.02x slower                                                    |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                     |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                     |
| unpickle_pure_python       | 214 us                                                       | 219 us: 1.02x slower                                                     |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                    |
| tornado_http               | 120 ms                                                       | 123 ms: 1.02x slower                                                     |
| mdp                        | 2.52 sec                                                     | 2.60 sec: 1.03x slower                                                   |
| logging_format             | 7.07 us                                                      | 7.28 us: 1.03x slower                                                    |
| logging_simple             | 6.40 us                                                      | 6.63 us: 1.04x slower                                                    |
| regex_compile              | 144 ms                                                       | 150 ms: 1.04x slower                                                     |
| thrift                     | 877 us                                                       | 913 us: 1.04x slower                                                     |
| pycparser                  | 1.26 sec                                                     | 1.31 sec: 1.04x slower                                                   |
| meteor_contest             | 128 ms                                                       | 134 ms: 1.05x slower                                                     |
| gc_traversal               | 4.11 ms                                                      | 4.31 ms: 1.05x slower                                                    |
| bench_thread_pool          | 901 us                                                       | 946 us: 1.05x slower                                                     |
| sympy_expand               | 505 ms                                                       | 534 ms: 1.06x slower                                                     |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.8 ms: 1.06x slower                                                    |
| async_generators           | 359 ms                                                       | 382 ms: 1.06x slower                                                     |
| regex_effbot               | 3.37 ms                                                      | 3.60 ms: 1.07x slower                                                    |
| sympy_str                  | 296 ms                                                       | 318 ms: 1.08x slower                                                     |
| create_gc_cycles           | 1.76 ms                                                      | 1.90 ms: 1.08x slower                                                    |
| 2to3                       | 291 ms                                                       | 315 ms: 1.08x slower                                                     |
| comprehensions             | 17.3 us                                                      | 18.7 us: 1.08x slower                                                    |
| sqlglot_transpile          | 1.78 ms                                                      | 1.94 ms: 1.09x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                      | 1.51 ms: 1.10x slower                                                    |
| chaos                      | 61.7 ms                                                      | 68.0 ms: 1.10x slower                                                    |
| generators                 | 33.5 ms                                                      | 37.3 ms: 1.11x slower                                                    |
| raytrace                   | 289 ms                                                       | 323 ms: 1.12x slower                                                     |
| sympy_sum                  | 154 ms                                                       | 172 ms: 1.12x slower                                                     |
| hexiom                     | 6.33 ms                                                      | 7.09 ms: 1.12x slower                                                    |
| genshi_text                | 26.6 ms                                                      | 29.8 ms: 1.12x slower                                                    |
| docutils                   | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                                   |
| sqlglot_normalize          | 118 ms                                                       | 136 ms: 1.15x slower                                                     |
| genshi_xml                 | 57.3 ms                                                      | 66.2 ms: 1.16x slower                                                    |
| sympy_integrate            | 23.3 ms                                                      | 27.0 ms: 1.16x slower                                                    |
| nqueens                    | 88.2 ms                                                      | 102 ms: 1.16x slower                                                     |
| sqlglot_optimize           | 59.7 ms                                                      | 69.6 ms: 1.17x slower                                                    |
| pylint                     | 346 ms                                                       | 407 ms: 1.17x slower                                                     |
| django_template            | 38.9 ms                                                      | 46.0 ms: 1.18x slower                                                    |
| unpack_sequence            | 56.8 ns                                                      | 94.8 ns: 1.67x slower                                                    |
| bench_mp_pool              | 4.65 ms                                                      | 3.26 sec: 699.78x slower                                                 |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 76.23% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x