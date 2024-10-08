# Results vs. 3.13.0b2

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-x86_64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 255 ms: 1.08x faster                                                 |
| docutils       | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                               |
| html5lib       | 67.2 ms                                                    | 63.0 ms: 1.07x faster                                                |
| tornado_http   | 94.6 ms                                                    | 90.4 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                      | 1.06x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 313 ms: 1.21x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 391 ms: 1.18x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 559 ms: 1.09x faster                                                 |
| async_tree_io              | 939 ms                                                     | 861 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 546 ms: 1.08x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 871 ms: 1.08x faster                                                 |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                 |
| float          | 78.9 ms                                                    | 77.7 ms: 1.02x faster                                                |
| nbody          | 88.3 ms                                                    | 89.4 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                      | 1.01x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 130 ms: 1.06x faster                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.53 ms: 1.04x faster                                                |
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                                 |
| regex_v8       | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                      | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.7 us: 1.08x faster                                                |
| xml_etree_parse      | 162 ms                                                     | 154 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.04x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                                |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 85.6 ms: 1.02x faster                                                |
| tomli_loads          | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                               |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.01x faster                                                 |
| pickle_list          | 5.11 us                                                    | 5.06 us: 1.01x faster                                                |
| pickle_dict          | 34.8 us                                                    | 34.9 us: 1.00x slower                                                |
| unpickle_list        | 5.34 us                                                    | 5.44 us: 1.02x slower                                                |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                         |

Benchmark hidden because not significant (2): pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                |
| python_startup_no_site | 7.11 ms                                                    | 6.97 ms: 1.02x faster                                                |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text    | 23.7 ms                                                    | 23.1 ms: 1.03x faster                                                |
| mako           | 11.2 ms                                                    | 11.2 ms: 1.01x faster                                                |
| genshi_xml     | 51.6 ms                                                    | 52.2 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                      | 1.01x faster                                                         |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 261 us: 1.41x faster                                                 |
| deepcopy_memo              | 39.7 us                                                    | 30.8 us: 1.29x faster                                                |
| deepcopy_reduce            | 3.35 us                                                    | 2.67 us: 1.26x faster                                                |
| go                         | 145 ms                                                     | 117 ms: 1.23x faster                                                 |
| async_tree_none            | 378 ms                                                     | 313 ms: 1.21x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 391 ms: 1.18x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                                 |
| richards                   | 50.9 ms                                                    | 46.0 ms: 1.11x faster                                                |
| richards_super             | 57.4 ms                                                    | 51.9 ms: 1.10x faster                                                |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 559 ms: 1.09x faster                                                 |
| async_tree_io              | 939 ms                                                     | 861 ms: 1.09x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                |
| gc_traversal               | 3.98 ms                                                    | 3.66 ms: 1.09x faster                                                |
| json_loads                 | 28.9 us                                                    | 26.7 us: 1.08x faster                                                |
| mdp                        | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                               |
| crypto_pyaes               | 77.5 ms                                                    | 71.8 ms: 1.08x faster                                                |
| json                       | 5.31 ms                                                    | 4.92 ms: 1.08x faster                                                |
| coverage                   | 93.1 ms                                                    | 86.5 ms: 1.08x faster                                                |
| 2to3                       | 274 ms                                                     | 255 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 546 ms: 1.08x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 871 ms: 1.08x faster                                                 |
| asyncio_tcp                | 508 ms                                                     | 475 ms: 1.07x faster                                                 |
| thrift                     | 823 us                                                     | 770 us: 1.07x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 63.0 ms: 1.07x faster                                                |
| docutils                   | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                               |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.06x faster                                                 |
| generators                 | 29.6 ms                                                    | 27.9 ms: 1.06x faster                                                |
| create_gc_cycles           | 1.82 ms                                                    | 1.71 ms: 1.06x faster                                                |
| sympy_sum                  | 156 ms                                                     | 147 ms: 1.06x faster                                                 |
| scimark_fft                | 392 ms                                                     | 371 ms: 1.06x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.98 ms: 1.06x faster                                                |
| bench_thread_pool          | 834 us                                                     | 789 us: 1.06x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 718 ms: 1.06x faster                                                 |
| regex_compile              | 137 ms                                                     | 130 ms: 1.06x faster                                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.05x faster                                               |
| xml_etree_parse            | 162 ms                                                     | 154 ms: 1.05x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 90.4 ms: 1.05x faster                                                |
| sqlite_synth               | 2.99 us                                                    | 2.85 us: 1.05x faster                                                |
| sympy_integrate            | 20.5 ms                                                    | 19.6 ms: 1.05x faster                                                |
| sympy_str                  | 282 ms                                                     | 270 ms: 1.05x faster                                                 |
| logging_silent             | 105 ns                                                     | 100 ns: 1.04x faster                                                 |
| chaos                      | 61.3 ms                                                    | 58.9 ms: 1.04x faster                                                |
| dulwich_log                | 67.2 ms                                                    | 64.5 ms: 1.04x faster                                                |
| regex_effbot               | 3.67 ms                                                    | 3.53 ms: 1.04x faster                                                |
| bpe_tokeniser              | 5.02 sec                                                   | 4.84 sec: 1.04x faster                                               |
| async_generators           | 442 ms                                                     | 427 ms: 1.04x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.04x faster                                                 |
| spectral_norm              | 116 ms                                                     | 112 ms: 1.03x faster                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 53.7 ms: 1.03x faster                                                |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                                |
| xml_etree_process          | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                                |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                |
| raytrace                   | 267 ms                                                     | 259 ms: 1.03x faster                                                 |
| sympy_expand               | 473 ms                                                     | 460 ms: 1.03x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                               |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                |
| nqueens                    | 81.4 ms                                                    | 79.3 ms: 1.03x faster                                                |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.03x faster                                                |
| genshi_text                | 23.7 ms                                                    | 23.1 ms: 1.03x faster                                                |
| typing_runtime_protocols   | 165 us                                                     | 161 us: 1.02x faster                                                 |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                 |
| pyflate                    | 484 ms                                                     | 474 ms: 1.02x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 85.6 ms: 1.02x faster                                                |
| tomli_loads                | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                               |
| regex_dna                  | 221 ms                                                     | 217 ms: 1.02x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.8 ms: 1.02x faster                                                |
| deltablue                  | 3.25 ms                                                    | 3.19 ms: 1.02x faster                                                |
| python_startup_no_site     | 7.11 ms                                                    | 6.97 ms: 1.02x faster                                                |
| pycparser                  | 1.16 sec                                                   | 1.14 sec: 1.02x faster                                               |
| float                      | 78.9 ms                                                    | 77.7 ms: 1.02x faster                                                |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.01x faster                                                 |
| sqlglot_normalize          | 110 ms                                                     | 109 ms: 1.01x faster                                                 |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                                |
| logging_format             | 6.47 us                                                    | 6.38 us: 1.01x faster                                                |
| pickle_pure_python         | 305 us                                                     | 301 us: 1.01x faster                                                 |
| regex_v8                   | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                |
| hexiom                     | 6.30 ms                                                    | 6.22 ms: 1.01x faster                                                |
| pickle_list                | 5.11 us                                                    | 5.06 us: 1.01x faster                                                |
| mako                       | 11.2 ms                                                    | 11.2 ms: 1.01x faster                                                |
| scimark_sor                | 127 ms                                                     | 127 ms: 1.01x faster                                                 |
| pickle_dict                | 34.8 us                                                    | 34.9 us: 1.00x slower                                                |
| fannkuch                   | 402 ms                                                     | 403 ms: 1.00x slower                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                |
| genshi_xml                 | 51.6 ms                                                    | 52.2 ms: 1.01x slower                                                |
| nbody                      | 88.3 ms                                                    | 89.4 ms: 1.01x slower                                                |
| coroutines                 | 23.2 ms                                                    | 23.6 ms: 1.02x slower                                                |
| unpickle_list              | 5.34 us                                                    | 5.44 us: 1.02x slower                                                |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                         |

Benchmark hidden because not significant (6): pickle, logging_simple, django_template, telco, pylint, unpickle
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.00x