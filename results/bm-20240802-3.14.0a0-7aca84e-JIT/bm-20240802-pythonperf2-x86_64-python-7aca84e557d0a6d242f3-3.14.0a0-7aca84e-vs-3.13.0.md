# Results vs. 3.13.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-x86_64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.01x faster
- HPT reliability: 64.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 308 ms: 1.06x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.14 sec: 1.12x slower                                                      |
| html5lib       | 71.9 ms                                                      | 71.1 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 388 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 322 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 306 ms: 1.11x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 413 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 563 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 540 ms: 1.06x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 771 ms: 1.06x faster                                                        |
| async_tree_io              | 847 ms                                                       | 828 ms: 1.02x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                                        |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                       |
| async_generators           | 359 ms                                                       | 386 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 76.2 ms: 1.07x faster                                                       |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.48 ms: 1.03x slower                                                       |
| regex_v8       | 26.2 ms                                                      | 27.1 ms: 1.03x slower                                                       |
| regex_dna      | 244 ms                                                       | 261 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.10 sec: 1.14x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 56.5 ms: 1.08x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 80.3 ms: 1.06x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 139 ms: 1.04x faster                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 97.2 ms: 1.03x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                       |
| unpickle_pure_python | 214 us                                                       | 211 us: 1.02x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 314 us: 1.01x faster                                                        |
| json_loads           | 24.0 us                                                      | 25.4 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.10 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.12 ms: 1.14x faster                                                       |
| genshi_text     | 26.6 ms                                                      | 28.2 ms: 1.06x slower                                                       |
| django_template | 38.9 ms                                                      | 41.5 ms: 1.07x slower                                                       |
| genshi_xml      | 57.3 ms                                                      | 62.0 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 29.1 us: 1.36x faster                                                       |
| deepcopy                   | 397 us                                                       | 311 us: 1.28x faster                                                        |
| scimark_sor                | 126 ms                                                       | 104 ms: 1.21x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 81.4 ms: 1.20x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 388 ms: 1.19x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.04 us: 1.17x faster                                                       |
| async_tree_none            | 372 ms                                                       | 322 ms: 1.15x faster                                                        |
| tomli_loads                | 2.41 sec                                                     | 2.10 sec: 1.14x faster                                                      |
| mako                       | 10.4 ms                                                      | 9.12 ms: 1.14x faster                                                       |
| richards                   | 52.7 ms                                                      | 46.6 ms: 1.13x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 306 ms: 1.11x faster                                                        |
| richards_super             | 59.8 ms                                                      | 54.1 ms: 1.10x faster                                                       |
| scimark_fft                | 314 ms                                                       | 285 ms: 1.10x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 413 ms: 1.09x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 56.5 ms: 1.08x faster                                                       |
| float                      | 81.9 ms                                                      | 76.2 ms: 1.07x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 16.3 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 563 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 540 ms: 1.06x faster                                                        |
| xml_etree_generate         | 85.3 ms                                                      | 80.3 ms: 1.06x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 771 ms: 1.06x faster                                                        |
| pyflate                    | 492 ms                                                       | 463 ms: 1.06x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.09 ms: 1.06x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.82 sec: 1.06x faster                                                      |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| xml_etree_parse            | 145 ms                                                       | 139 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.11 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 97.2 ms: 1.03x faster                                                       |
| coverage                   | 81.1 ms                                                      | 78.8 ms: 1.03x faster                                                       |
| fannkuch                   | 365 ms                                                       | 355 ms: 1.03x faster                                                        |
| crypto_pyaes               | 72.8 ms                                                      | 71.0 ms: 1.02x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                       |
| async_tree_io              | 847 ms                                                       | 828 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 214 us                                                       | 211 us: 1.02x faster                                                        |
| logging_simple             | 6.40 us                                                      | 6.29 us: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 314 us: 1.01x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 71.1 ms: 1.01x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                                        |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                        |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.10 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                        |
| mdp                        | 2.52 sec                                                     | 2.59 sec: 1.03x slower                                                      |
| logging_silent             | 97.7 ns                                                      | 100 ns: 1.03x slower                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 4.79 ms: 1.03x slower                                                       |
| thrift                     | 877 us                                                       | 902 us: 1.03x slower                                                        |
| sympy_expand               | 505 ms                                                       | 521 ms: 1.03x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.48 ms: 1.03x slower                                                       |
| regex_v8                   | 26.2 ms                                                      | 27.1 ms: 1.03x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.84 ms: 1.04x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                       |
| json                       | 5.22 ms                                                      | 5.42 ms: 1.04x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.5 ms: 1.04x slower                                                       |
| dask                       | 379 ms                                                       | 395 ms: 1.04x slower                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 62.2 ms: 1.04x slower                                                       |
| comprehensions             | 17.3 us                                                      | 18.0 us: 1.04x slower                                                       |
| sympy_str                  | 296 ms                                                       | 310 ms: 1.05x slower                                                        |
| go                         | 160 ms                                                       | 168 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 183 us: 1.05x slower                                                        |
| gc_traversal               | 4.11 ms                                                      | 4.34 ms: 1.06x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.4 us: 1.06x slower                                                       |
| genshi_text                | 26.6 ms                                                      | 28.2 ms: 1.06x slower                                                       |
| 2to3                       | 291 ms                                                       | 308 ms: 1.06x slower                                                        |
| django_template            | 38.9 ms                                                      | 41.5 ms: 1.07x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 6.77 ms: 1.07x slower                                                       |
| chaos                      | 61.7 ms                                                      | 66.0 ms: 1.07x slower                                                       |
| regex_dna                  | 244 ms                                                       | 261 ms: 1.07x slower                                                        |
| async_generators           | 359 ms                                                       | 386 ms: 1.07x slower                                                        |
| sqlglot_normalize          | 118 ms                                                       | 128 ms: 1.08x slower                                                        |
| genshi_xml                 | 57.3 ms                                                      | 62.0 ms: 1.08x slower                                                       |
| generators                 | 33.5 ms                                                      | 36.2 ms: 1.08x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 167 ms: 1.08x slower                                                        |
| create_gc_cycles           | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                                       |
| deltablue                  | 3.41 ms                                                      | 3.74 ms: 1.10x slower                                                       |
| sympy_integrate            | 23.3 ms                                                      | 25.9 ms: 1.11x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.14 sec: 1.12x slower                                                      |
| pylint                     | 346 ms                                                       | 387 ms: 1.12x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 99.3 ms: 1.13x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (10): pycparser, logging_format, scimark_lu, raytrace, pprint_safe_repr, asyncio_tcp_ssl, pprint_pformat, tornado_http, nbody, bench_thread_pool
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 64.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x