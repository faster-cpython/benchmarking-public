# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.042x faster
- HPT reliability: 99.27%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 295 ms: 1.04x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.04 sec: 1.02x slower                                                  |
| tornado_http   | 136 ms                                                                | 128 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 426 ms: 1.46x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 553 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 417 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 548 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 726 ms: 1.26x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 725 ms: 1.22x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 93.4 ms: 1.01x slower                                                   |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 358 us: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| json_loads           | 30.7 us                                                               | 32.4 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 42.5 ms: 1.04x slower                                                   |
| mako            | 12.9 ms                                                               | 13.5 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 426 ms: 1.46x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 553 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 417 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 548 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.9 us: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 726 ms: 1.26x faster                                                    |
| generators                 | 43.5 ms                                                               | 34.7 ms: 1.25x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.23x faster                                                  |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 725 ms: 1.22x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.50 us: 1.17x faster                                                   |
| raytrace                   | 353 ms                                                                | 304 ms: 1.16x faster                                                    |
| go                         | 157 ms                                                                | 137 ms: 1.15x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.4 ms: 1.15x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 140 ms: 1.11x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.64 us: 1.09x faster                                                   |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.02 us: 1.09x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 135 ms: 1.08x faster                                                    |
| sympy_str                  | 280 ms                                                                | 261 ms: 1.07x faster                                                    |
| tornado_http               | 136 ms                                                                | 128 ms: 1.06x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 81.9 ms: 1.06x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.91 ms: 1.05x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.39 ms: 1.05x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.7 ms: 1.05x faster                                                   |
| 2to3                       | 308 ms                                                                | 295 ms: 1.04x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.6 ms: 1.04x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.6 ms: 1.04x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.21 sec: 1.04x faster                                                  |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.31 sec: 1.03x faster                                                  |
| xml_etree_iterparse        | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| async_generators           | 491 ms                                                                | 480 ms: 1.02x faster                                                    |
| pickle_pure_python         | 365 us                                                                | 358 us: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.85 sec: 1.01x faster                                                  |
| pprint_safe_repr           | 916 ms                                                                | 904 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                  |
| float                      | 92.1 ms                                                               | 93.4 ms: 1.01x slower                                                   |
| richards_super             | 58.5 ms                                                               | 59.4 ms: 1.02x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.04 sec: 1.02x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 7.10 ms: 1.02x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| json                       | 5.54 ms                                                               | 5.68 ms: 1.03x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.39 ms: 1.03x slower                                                   |
| pyflate                    | 559 ms                                                                | 581 ms: 1.04x slower                                                    |
| richards                   | 50.9 ms                                                               | 53.0 ms: 1.04x slower                                                   |
| django_template            | 40.7 ms                                                               | 42.5 ms: 1.04x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.5 ms: 1.05x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                                   |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.05x slower                                                    |
| scimark_fft                | 418 ms                                                                | 441 ms: 1.05x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 190 us: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.06x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                   |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                    |
| fannkuch                   | 443 ms                                                                | 475 ms: 1.07x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.85 ms: 1.10x slower                                                   |
| coverage                   | 87.3 ms                                                               | 98.1 ms: 1.12x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.97 ms: 1.17x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.29 ms: 1.20x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                            |

Benchmark hidden because not significant (18): xml_etree_parse, genshi_xml, thrift, asyncio_tcp, regex_dna, asyncio_websockets, html5lib, sqlglot_optimize, genshi_text, nqueens, sympy_expand, bench_mp_pool, pidigits, xml_etree_generate, pylint, meteor_contest, xml_etree_process, sqlglot_normalize
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: bpe_tokeniser

- Geometric mean (including insignificant results): 1.042x faster
# HPT report

- Reliability score: 99.27% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x