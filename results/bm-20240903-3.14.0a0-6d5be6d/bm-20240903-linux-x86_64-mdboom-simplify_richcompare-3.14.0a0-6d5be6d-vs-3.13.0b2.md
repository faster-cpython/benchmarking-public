# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 257 ms: 1.07x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.67 sec: 1.06x faster                                                |
| html5lib       | 67.2 ms                                                    | 61.8 ms: 1.09x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 90.8 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                      | 1.06x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 390 ms: 1.19x faster                                                  |
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 401 ms: 1.11x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 896 ms: 1.04x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 85.8 ms: 1.03x faster                                                 |
| pidigits       | 191 ms                                                     | 187 ms: 1.03x faster                                                  |
| float          | 78.9 ms                                                    | 77.8 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 130 ms: 1.05x faster                                                  |
| regex_dna      | 221 ms                                                     | 225 ms: 1.02x slower                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.76 ms: 1.03x slower                                                 |
| regex_v8       | 25.1 ms                                                    | 26.8 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 154 ms: 1.05x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 58.8 ms: 1.04x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 2.05 sec: 1.04x faster                                                |
| xml_etree_generate   | 87.4 ms                                                    | 84.9 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.03x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 33.5 ms: 1.04x faster                                                 |
| genshi_text     | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                                 |
| mako            | 11.2 ms                                                    | 11.2 ms: 1.00x faster                                                 |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 264 us: 1.39x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.8 us: 1.33x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.75 us: 1.22x faster                                                 |
| go                         | 145 ms                                                     | 119 ms: 1.21x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 390 ms: 1.19x faster                                                  |
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                  |
| richards_super             | 57.4 ms                                                    | 51.7 ms: 1.11x faster                                                 |
| richards                   | 50.9 ms                                                    | 46.0 ms: 1.11x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 401 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.77 ms: 1.10x faster                                                 |
| coverage                   | 93.1 ms                                                    | 84.9 ms: 1.10x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 61.8 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.57 sec: 1.08x faster                                                |
| scimark_fft                | 392 ms                                                     | 363 ms: 1.08x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 72.4 ms: 1.07x faster                                                 |
| 2to3                       | 274 ms                                                     | 257 ms: 1.07x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                 |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.07x faster                                                  |
| generators                 | 29.6 ms                                                    | 27.8 ms: 1.07x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 714 ms: 1.06x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                |
| bench_thread_pool          | 834 us                                                     | 787 us: 1.06x faster                                                  |
| docutils                   | 2.83 sec                                                   | 2.67 sec: 1.06x faster                                                |
| thrift                     | 823 us                                                     | 778 us: 1.06x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 482 ms: 1.06x faster                                                  |
| regex_compile              | 137 ms                                                     | 130 ms: 1.05x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.78 ms: 1.05x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 154 ms: 1.05x faster                                                  |
| sympy_integrate            | 20.5 ms                                                    | 19.5 ms: 1.05x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.79 sec: 1.05x faster                                                |
| logging_format             | 6.47 us                                                    | 6.17 us: 1.05x faster                                                 |
| sympy_str                  | 282 ms                                                     | 270 ms: 1.05x faster                                                  |
| sympy_sum                  | 156 ms                                                     | 149 ms: 1.05x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.05x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 896 ms: 1.04x faster                                                  |
| chaos                      | 61.3 ms                                                    | 58.7 ms: 1.04x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 90.8 ms: 1.04x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 58.8 ms: 1.04x faster                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 53.4 ms: 1.04x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.52 us: 1.04x faster                                                 |
| django_template            | 34.8 ms                                                    | 33.5 ms: 1.04x faster                                                 |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 2.05 sec: 1.04x faster                                                |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                                 |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.03x faster                                                  |
| sympy_expand               | 473 ms                                                     | 459 ms: 1.03x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 84.9 ms: 1.03x faster                                                 |
| nbody                      | 88.3 ms                                                    | 85.8 ms: 1.03x faster                                                 |
| genshi_text                | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                |
| async_generators           | 442 ms                                                     | 431 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.03x faster                                                  |
| pidigits                   | 191 ms                                                     | 187 ms: 1.03x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                 |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                 |
| logging_silent             | 105 ns                                                     | 102 ns: 1.02x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| hexiom                     | 6.30 ms                                                    | 6.19 ms: 1.02x faster                                                 |
| deltablue                  | 3.25 ms                                                    | 3.20 ms: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                  |
| float                      | 78.9 ms                                                    | 77.8 ms: 1.01x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.2 ms: 1.01x faster                                                 |
| pyflate                    | 484 ms                                                     | 478 ms: 1.01x faster                                                  |
| nqueens                    | 81.4 ms                                                    | 80.4 ms: 1.01x faster                                                 |
| telco                      | 8.41 ms                                                    | 8.31 ms: 1.01x faster                                                 |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                  |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| raytrace                   | 267 ms                                                     | 264 ms: 1.01x faster                                                  |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                 |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                 |
| json                       | 5.31 ms                                                    | 5.27 ms: 1.01x faster                                                 |
| mako                       | 11.2 ms                                                    | 11.2 ms: 1.00x faster                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| fannkuch                   | 402 ms                                                     | 407 ms: 1.01x slower                                                  |
| regex_dna                  | 221 ms                                                     | 225 ms: 1.02x slower                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.76 ms: 1.03x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.20 sec: 1.03x slower                                                |
| regex_v8                   | 25.1 ms                                                    | 26.8 ms: 1.07x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (4): async_tree_io, genshi_xml, typing_runtime_protocols, pylint
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x