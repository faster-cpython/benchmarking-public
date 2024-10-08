# Results vs. 3.12.0

- fork: python
- ref: d27a53fc02a87e76066f
- machine: linux-aarch64
- commit hash: d27a53f
- commit date: 2024-07-30
- overall geometric mean: 1.04x faster
- HPT reliability: 97.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 299 ms: 1.03x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.14 sec: 1.05x slower                                                  |
| html5lib       | 65.1 ms                                                               | 66.9 ms: 1.03x slower                                                   |
| tornado_http   | 136 ms                                                                | 126 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 405 ms: 1.42x faster                                                    |
| async_tree_none            | 624 ms                                                                | 442 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 532 ms: 1.39x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 560 ms: 1.39x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.08 sec: 1.30x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.12 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 728 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 711 ms: 1.24x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.33x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 107 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 30.2 ms: 1.06x slower                                                   |
| regex_effbot   | 4.64 ms                                                               | 4.94 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.05x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 251 us: 1.03x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.53 sec: 1.03x faster                                                  |
| xml_etree_iterparse  | 150 ms                                                                | 147 ms: 1.03x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 357 us: 1.02x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 80.6 ms: 1.02x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.4 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.85 ms: 1.06x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 59.7 ms: 1.01x faster                                                   |
| django_template | 40.7 ms                                                               | 41.4 ms: 1.02x slower                                                   |
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 405 ms: 1.42x faster                                                    |
| async_tree_none            | 624 ms                                                                | 442 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 532 ms: 1.39x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 560 ms: 1.39x faster                                                    |
| deepcopy                   | 446 us                                                                | 332 us: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.0 us: 1.31x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.08 sec: 1.30x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.12 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 728 ms: 1.25x faster                                                    |
| generators                 | 43.5 ms                                                               | 34.9 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 711 ms: 1.24x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.24x faster                                                   |
| raytrace                   | 353 ms                                                                | 294 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.45 us: 1.19x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.58 us: 1.10x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.97 us: 1.10x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.80 ms: 1.08x faster                                                   |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                    |
| tornado_http               | 136 ms                                                                | 126 ms: 1.08x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.71 ms: 1.07x faster                                                   |
| chaos                      | 71.4 ms                                                               | 67.2 ms: 1.06x faster                                                   |
| sympy_str                  | 280 ms                                                                | 266 ms: 1.05x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.05x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 82.5 ms: 1.05x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.05x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.40 ms: 1.04x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.1 ms: 1.04x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.21 sec: 1.04x faster                                                  |
| unpickle_pure_python       | 260 us                                                                | 251 us: 1.03x faster                                                    |
| 2to3                       | 308 ms                                                                | 299 ms: 1.03x faster                                                    |
| dask                       | 376 ms                                                                | 366 ms: 1.03x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.53 sec: 1.03x faster                                                  |
| xml_etree_iterparse        | 150 ms                                                                | 147 ms: 1.03x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.03x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.02x faster                                                  |
| pickle_pure_python         | 365 us                                                                | 357 us: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                   |
| genshi_xml                 | 60.6 ms                                                               | 59.7 ms: 1.01x faster                                                   |
| async_generators           | 491 ms                                                                | 485 ms: 1.01x faster                                                    |
| thrift                     | 937 us                                                                | 943 us: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 62.2 ms: 1.01x slower                                                   |
| go                         | 157 ms                                                                | 160 ms: 1.02x slower                                                    |
| django_template            | 40.7 ms                                                               | 41.4 ms: 1.02x slower                                                   |
| sympy_expand               | 454 ms                                                                | 462 ms: 1.02x slower                                                    |
| json                       | 5.54 ms                                                               | 5.64 ms: 1.02x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.11 ms: 1.02x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 80.6 ms: 1.02x slower                                                   |
| richards                   | 50.9 ms                                                               | 52.0 ms: 1.02x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                   |
| logging_silent             | 127 ns                                                                | 130 ns: 1.03x slower                                                    |
| nbody                      | 105 ms                                                                | 107 ms: 1.03x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 66.9 ms: 1.03x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.94 sec: 1.03x slower                                                  |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.41 ms: 1.03x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 949 ms: 1.04x slower                                                    |
| pyflate                    | 559 ms                                                                | 582 ms: 1.04x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                    |
| scimark_fft                | 418 ms                                                                | 439 ms: 1.05x slower                                                    |
| fannkuch                   | 443 ms                                                                | 466 ms: 1.05x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.14 sec: 1.05x slower                                                  |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.06x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.85 ms: 1.06x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.2 ms: 1.06x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.94 ms: 1.06x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.07x slower                                                    |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.85 ms: 1.10x slower                                                   |
| coverage                   | 87.3 ms                                                               | 98.8 ms: 1.13x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.0 ms: 1.18x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.31 ms: 1.21x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                            |

Benchmark hidden because not significant (13): pylint, nqueens, float, bench_mp_pool, asyncio_tcp, xml_etree_generate, meteor_contest, asyncio_tcp_ssl, asyncio_websockets, richards_super, sqlglot_normalize, genshi_text, regex_dna
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240730-3.14.0a0-d27a53f/bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f.json: bpe_tokeniser

# HPT report

- Reliability score: 97.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x