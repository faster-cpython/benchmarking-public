# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 257 ms: 1.07x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                                |
| html5lib       | 67.2 ms                                                    | 63.5 ms: 1.06x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 90.7 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                      | 1.06x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 394 ms: 1.18x faster                                                  |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 405 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 313 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 549 ms: 1.07x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 908 ms: 1.03x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| nbody          | 88.3 ms                                                    | 86.0 ms: 1.03x faster                                                 |
| float          | 78.9 ms                                                    | 77.5 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 131 ms: 1.05x faster                                                  |
| regex_dna      | 221 ms                                                     | 222 ms: 1.01x slower                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                 |
| regex_v8       | 25.1 ms                                                    | 26.1 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 155 ms: 1.04x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 210 us: 1.04x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 59.4 ms: 1.03x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 86.0 ms: 1.02x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.01x faster                                                  |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.01x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                |
| json_loads           | 28.9 us                                                    | 28.7 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.1 ms: 1.02x faster                                                 |
| django_template | 34.8 ms                                                    | 34.0 ms: 1.02x faster                                                 |
| genshi_xml      | 51.6 ms                                                    | 50.9 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 30.3 us: 1.31x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                                 |
| go                         | 145 ms                                                     | 119 ms: 1.22x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 394 ms: 1.18x faster                                                  |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                  |
| richards                   | 50.9 ms                                                    | 45.7 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.74 ms: 1.11x faster                                                 |
| richards_super             | 57.4 ms                                                    | 51.8 ms: 1.11x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 405 ms: 1.10x faster                                                  |
| scimark_fft                | 392 ms                                                     | 360 ms: 1.09x faster                                                  |
| coverage                   | 93.1 ms                                                    | 85.7 ms: 1.09x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 313 ms: 1.07x faster                                                  |
| spectral_norm              | 116 ms                                                     | 108 ms: 1.07x faster                                                  |
| generators                 | 29.6 ms                                                    | 27.7 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 549 ms: 1.07x faster                                                  |
| thrift                     | 823 us                                                     | 771 us: 1.07x faster                                                  |
| 2to3                       | 274 ms                                                     | 257 ms: 1.07x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.72 ms: 1.07x faster                                                 |
| docutils                   | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                                |
| asyncio_tcp                | 508 ms                                                     | 479 ms: 1.06x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 787 us: 1.06x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 63.5 ms: 1.06x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 717 ms: 1.06x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                |
| scimark_lu                 | 122 ms                                                     | 115 ms: 1.06x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.64 sec: 1.05x faster                                                |
| crypto_pyaes               | 77.5 ms                                                    | 73.6 ms: 1.05x faster                                                 |
| sympy_sum                  | 156 ms                                                     | 148 ms: 1.05x faster                                                  |
| sympy_str                  | 282 ms                                                     | 270 ms: 1.05x faster                                                  |
| sympy_integrate            | 20.5 ms                                                    | 19.6 ms: 1.05x faster                                                 |
| regex_compile              | 137 ms                                                     | 131 ms: 1.05x faster                                                  |
| chaos                      | 61.3 ms                                                    | 58.7 ms: 1.05x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 90.7 ms: 1.04x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.51 us: 1.04x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 155 ms: 1.04x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 210 us: 1.04x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.86 sec: 1.03x faster                                                |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                 |
| logging_silent             | 105 ns                                                     | 101 ns: 1.03x faster                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 53.8 ms: 1.03x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 908 ms: 1.03x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 59.4 ms: 1.03x faster                                                 |
| pyflate                    | 484 ms                                                     | 471 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| nbody                      | 88.3 ms                                                    | 86.0 ms: 1.03x faster                                                 |
| sympy_expand               | 473 ms                                                     | 461 ms: 1.03x faster                                                  |
| genshi_text                | 23.7 ms                                                    | 23.1 ms: 1.02x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                 |
| django_template            | 34.8 ms                                                    | 34.0 ms: 1.02x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| typing_runtime_protocols   | 165 us                                                     | 161 us: 1.02x faster                                                  |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                  |
| float                      | 78.9 ms                                                    | 77.5 ms: 1.02x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 86.0 ms: 1.02x faster                                                 |
| genshi_xml                 | 51.6 ms                                                    | 50.9 ms: 1.01x faster                                                 |
| deltablue                  | 3.25 ms                                                    | 3.21 ms: 1.01x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 106 ms: 1.01x faster                                                  |
| pickle_pure_python         | 305 us                                                     | 301 us: 1.01x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                                  |
| raytrace                   | 267 ms                                                     | 263 ms: 1.01x faster                                                  |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                  |
| sqlglot_normalize          | 110 ms                                                     | 109 ms: 1.01x faster                                                  |
| telco                      | 8.41 ms                                                    | 8.34 ms: 1.01x faster                                                 |
| tomli_loads                | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                |
| nqueens                    | 81.4 ms                                                    | 80.7 ms: 1.01x faster                                                 |
| json_loads                 | 28.9 us                                                    | 28.7 us: 1.01x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.7 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                                 |
| fannkuch                   | 402 ms                                                     | 403 ms: 1.00x slower                                                  |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| regex_dna                  | 221 ms                                                     | 222 ms: 1.01x slower                                                  |
| async_generators           | 442 ms                                                     | 445 ms: 1.01x slower                                                  |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                |
| regex_effbot               | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                 |
| regex_v8                   | 25.1 ms                                                    | 26.1 ms: 1.04x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (5): async_tree_io, hexiom, mako, json, pylint
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x