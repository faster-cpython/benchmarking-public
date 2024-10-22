# Results vs. 3.13.0

- fork: faster-cpython
- ref: binary_subscr_getite
- machine: linux-x86_64
- commit hash: 71920f1
- commit date: 2024-07-30
- overall geometric mean: 1.01x faster
- HPT reliability: 86.27%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 273 ms: 1.03x slower                                                            |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                          |
| html5lib       | 64.5 ms                                                | 65.7 ms: 1.02x slower                                                           |
| tornado_http   | 91.5 ms                                                | 92.2 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                            |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 417 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 527 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                          |
| asyncio_tcp                | 488 ms                                                 | 505 ms: 1.03x slower                                                            |
| async_generators           | 433 ms                                                 | 450 ms: 1.04x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 868 ms: 1.05x slower                                                            |
| async_tree_io              | 843 ms                                                 | 913 ms: 1.08x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.8 ms: 1.11x faster                                                           |
| nbody          | 85.7 ms                                                | 79.5 ms: 1.08x faster                                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.69 ms: 1.05x faster                                                           |
| regex_v8       | 25.3 ms                                                | 25.4 ms: 1.00x slower                                                           |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                                            |
| regex_compile  | 131 ms                                                 | 133 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.10x faster                                                          |
| xml_etree_generate   | 87.0 ms                                                | 79.7 ms: 1.09x faster                                                           |
| xml_etree_process    | 60.4 ms                                                | 56.6 ms: 1.07x faster                                                           |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.06x faster                                                            |
| xml_etree_iterparse  | 102 ms                                                 | 99.5 ms: 1.03x faster                                                           |
| pickle_pure_python   | 300 us                                                 | 294 us: 1.02x faster                                                            |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                            |
| json_loads           | 27.0 us                                                | 28.1 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.16 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.93 ms: 1.12x faster                                                           |
| django_template | 34.4 ms                                                | 35.6 ms: 1.03x slower                                                           |
| genshi_xml      | 50.3 ms                                                | 53.9 ms: 1.07x slower                                                           |
| genshi_text     | 22.9 ms                                                | 24.7 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-71920f1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.4 us: 1.34x faster                                                           |
| deepcopy                   | 352 us                                                 | 279 us: 1.26x faster                                                            |
| scimark_fft                | 369 ms                                                 | 303 ms: 1.22x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.19 ms: 1.20x faster                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                            |
| richards                   | 48.1 ms                                                | 41.2 ms: 1.17x faster                                                           |
| deepcopy_reduce            | 3.17 us                                                | 2.73 us: 1.16x faster                                                           |
| richards_super             | 54.4 ms                                                | 47.1 ms: 1.15x faster                                                           |
| mako                       | 11.1 ms                                                | 9.93 ms: 1.12x faster                                                           |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                            |
| float                      | 78.5 ms                                                | 70.8 ms: 1.11x faster                                                           |
| crypto_pyaes               | 73.0 ms                                                | 65.8 ms: 1.11x faster                                                           |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.10x faster                                                          |
| xml_etree_generate         | 87.0 ms                                                | 79.7 ms: 1.09x faster                                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 60.9 ms: 1.09x faster                                                           |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                            |
| nbody                      | 85.7 ms                                                | 79.5 ms: 1.08x faster                                                           |
| scimark_sor                | 122 ms                                                 | 114 ms: 1.07x faster                                                            |
| xml_etree_process          | 60.4 ms                                                | 56.6 ms: 1.07x faster                                                           |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                            |
| scimark_lu                 | 115 ms                                                 | 108 ms: 1.07x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 417 ms: 1.06x faster                                                            |
| telco                      | 8.45 ms                                                | 7.96 ms: 1.06x faster                                                           |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                           |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.06x faster                                                            |
| regex_effbot               | 3.88 ms                                                | 3.69 ms: 1.05x faster                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.04x faster                                                          |
| logging_format             | 6.25 us                                                | 6.00 us: 1.04x faster                                                           |
| logging_simple             | 5.66 us                                                | 5.45 us: 1.04x faster                                                           |
| gc_traversal               | 3.81 ms                                                | 3.67 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 527 ms: 1.03x faster                                                            |
| fannkuch                   | 381 ms                                                 | 370 ms: 1.03x faster                                                            |
| pprint_safe_repr           | 744 ms                                                 | 725 ms: 1.03x faster                                                            |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| xml_etree_iterparse        | 102 ms                                                 | 99.5 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                                            |
| pyflate                    | 460 ms                                                 | 449 ms: 1.02x faster                                                            |
| pprint_pformat             | 1.51 sec                                               | 1.48 sec: 1.02x faster                                                          |
| pickle_pure_python         | 300 us                                                 | 294 us: 1.02x faster                                                            |
| json                       | 5.20 ms                                                | 5.12 ms: 1.01x faster                                                           |
| mdp                        | 2.74 sec                                               | 2.71 sec: 1.01x faster                                                          |
| pycparser                  | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                          |
| chaos                      | 58.4 ms                                                | 57.8 ms: 1.01x faster                                                           |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                           |
| regex_v8                   | 25.3 ms                                                | 25.4 ms: 1.00x slower                                                           |
| bench_thread_pool          | 815 us                                                 | 819 us: 1.01x slower                                                            |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.01x slower                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                          |
| tornado_http               | 91.5 ms                                                | 92.2 ms: 1.01x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                           |
| regex_compile              | 131 ms                                                 | 133 ms: 1.02x slower                                                            |
| thrift                     | 796 us                                                 | 811 us: 1.02x slower                                                            |
| html5lib                   | 64.5 ms                                                | 65.7 ms: 1.02x slower                                                           |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                                            |
| python_startup_no_site     | 6.99 ms                                                | 7.16 ms: 1.02x slower                                                           |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                           |
| go                         | 142 ms                                                 | 146 ms: 1.03x slower                                                            |
| 2to3                       | 265 ms                                                 | 273 ms: 1.03x slower                                                            |
| sqlglot_optimize           | 53.9 ms                                                | 55.7 ms: 1.03x slower                                                           |
| asyncio_tcp                | 488 ms                                                 | 505 ms: 1.03x slower                                                            |
| django_template            | 34.4 ms                                                | 35.6 ms: 1.03x slower                                                           |
| async_generators           | 433 ms                                                 | 450 ms: 1.04x slower                                                            |
| json_loads                 | 27.0 us                                                | 28.1 us: 1.04x slower                                                           |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 868 ms: 1.05x slower                                                            |
| nqueens                    | 80.6 ms                                                | 85.8 ms: 1.06x slower                                                           |
| typing_runtime_protocols   | 159 us                                                 | 170 us: 1.07x slower                                                            |
| genshi_xml                 | 50.3 ms                                                | 53.9 ms: 1.07x slower                                                           |
| genshi_text                | 22.9 ms                                                | 24.7 ms: 1.08x slower                                                           |
| dask                       | 338 ms                                                 | 365 ms: 1.08x slower                                                            |
| async_tree_io              | 843 ms                                                 | 913 ms: 1.08x slower                                                            |
| coverage                   | 83.7 ms                                                | 90.9 ms: 1.09x slower                                                           |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                           |
| hexiom                     | 6.13 ms                                                | 6.70 ms: 1.09x slower                                                           |
| sympy_str                  | 274 ms                                                 | 299 ms: 1.09x slower                                                            |
| sympy_expand               | 462 ms                                                 | 507 ms: 1.10x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                          |
| pylint                     | 313 ms                                                 | 354 ms: 1.13x slower                                                            |
| deltablue                  | 3.15 ms                                                | 3.57 ms: 1.13x slower                                                           |
| sympy_integrate            | 19.9 ms                                                | 22.5 ms: 1.13x slower                                                           |
| sympy_sum                  | 150 ms                                                 | 170 ms: 1.14x slower                                                            |
| generators                 | 28.8 ms                                                | 32.9 ms: 1.14x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (5): coroutines, json_dumps, bench_mp_pool, comprehensions, asyncio_websockets
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 86.27% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x