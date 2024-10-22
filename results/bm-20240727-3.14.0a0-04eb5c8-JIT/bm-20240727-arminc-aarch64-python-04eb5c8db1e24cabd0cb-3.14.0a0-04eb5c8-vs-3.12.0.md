# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-aarch64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.05x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 359 ms: 1.16x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.61 sec: 1.21x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.0 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 434 ms: 1.44x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 413 ms: 1.40x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 570 ms: 1.36x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 546 ms: 1.36x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.10 sec: 1.28x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 700 ms: 1.26x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 738 ms: 1.24x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.9 ms: 1.01x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 249 ms: 1.02x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.2 ms: 1.06x slower                                                   |
| regex_compile  | 137 ms                                                                | 180 ms: 1.31x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 82.0 ms: 1.04x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 272 us: 1.05x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 396 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.92 ms: 1.07x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 12.8 ms: 1.01x faster                                                   |
| django_template | 40.7 ms                                                               | 50.7 ms: 1.25x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 35.0 ms: 1.28x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 82.9 ms: 1.37x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 434 ms: 1.44x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 413 ms: 1.40x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 570 ms: 1.36x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 546 ms: 1.36x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.7 us: 1.28x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.10 sec: 1.28x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 700 ms: 1.26x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 738 ms: 1.24x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.6 ms: 1.22x faster                                                   |
| deepcopy                   | 446 us                                                                | 380 us: 1.17x faster                                                    |
| comprehensions             | 25.4 us                                                               | 23.5 us: 1.08x faster                                                   |
| raytrace                   | 353 ms                                                                | 329 ms: 1.07x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.0 ms: 1.07x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.24 us: 1.05x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.96 us: 1.05x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.2 ms: 1.03x faster                                                   |
| regex_dna                  | 254 ms                                                                | 249 ms: 1.02x faster                                                    |
| float                      | 92.1 ms                                                               | 90.9 ms: 1.01x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.30 ms: 1.01x faster                                                   |
| mako                       | 12.9 ms                                                               | 12.8 ms: 1.01x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.44 sec: 1.01x slower                                                  |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 88.4 ms: 1.02x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.23 sec: 1.02x slower                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 4.20 us: 1.02x slower                                                   |
| async_generators           | 491 ms                                                                | 505 ms: 1.03x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 87.7 ms: 1.03x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 82.0 ms: 1.04x slower                                                   |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.04x slower                                                    |
| dask                       | 376 ms                                                                | 392 ms: 1.04x slower                                                    |
| thrift                     | 937 us                                                                | 981 us: 1.05x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 272 us: 1.05x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.32 ms: 1.05x slower                                                   |
| richards_super             | 58.5 ms                                                               | 61.4 ms: 1.05x slower                                                   |
| richards                   | 50.9 ms                                                               | 53.8 ms: 1.06x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                                   |
| json                       | 5.54 ms                                                               | 5.86 ms: 1.06x slower                                                   |
| pyflate                    | 559 ms                                                                | 593 ms: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.2 ms: 1.06x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.92 ms: 1.07x slower                                                   |
| logging_silent             | 127 ns                                                                | 135 ns: 1.07x slower                                                    |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| fannkuch                   | 443 ms                                                                | 479 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 396 us: 1.08x slower                                                    |
| scimark_fft                | 418 ms                                                                | 456 ms: 1.09x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.60 ms: 1.09x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 617 ms: 1.09x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.0 ms: 1.09x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.77 ms: 1.09x slower                                                   |
| spectral_norm              | 131 ms                                                                | 144 ms: 1.10x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.03 ms: 1.11x slower                                                   |
| coverage                   | 87.3 ms                                                               | 97.9 ms: 1.12x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.41 sec: 1.12x slower                                                  |
| go                         | 157 ms                                                                | 180 ms: 1.14x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.04 ms: 1.15x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 145 ms: 1.16x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 209 us: 1.16x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 71.2 ms: 1.16x slower                                                   |
| 2to3                       | 308 ms                                                                | 359 ms: 1.16x slower                                                    |
| scimark_sor                | 150 ms                                                                | 176 ms: 1.18x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 8.38 ms: 1.19x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 119 ms: 1.19x slower                                                    |
| pylint                     | 355 ms                                                                | 428 ms: 1.21x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.61 sec: 1.21x slower                                                  |
| telco                      | 8.51 ms                                                               | 10.3 ms: 1.21x slower                                                   |
| sympy_str                  | 280 ms                                                                | 339 ms: 1.21x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.33 ms: 1.22x slower                                                   |
| chaos                      | 71.4 ms                                                               | 87.5 ms: 1.23x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 181 ms: 1.24x slower                                                    |
| django_template            | 40.7 ms                                                               | 50.7 ms: 1.25x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 27.1 ms: 1.25x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.15 sec: 1.25x slower                                                  |
| sympy_expand               | 454 ms                                                                | 571 ms: 1.26x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.38 sec: 1.27x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 35.0 ms: 1.28x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 199 ms: 1.28x slower                                                    |
| regex_compile              | 137 ms                                                                | 180 ms: 1.31x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.16 ms: 1.31x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 82.9 ms: 1.37x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_generate, asyncio_websockets, tornado_http
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: bpe_tokeniser

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x