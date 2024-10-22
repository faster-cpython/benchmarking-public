# Results vs. 3.12.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-aarch64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.03x faster
- HPT reliability: 97.40%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 295 ms: 1.05x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.03 sec: 1.01x slower                                                  |
| tornado_http   | 136 ms                                                                | 124 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 419 ms: 1.49x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 553 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 549 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 723 ms: 1.26x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 718 ms: 1.23x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 93.3 ms: 1.01x slower                                                   |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| regex_dna      | 254 ms                                                                | 252 ms: 1.01x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 256 us: 1.02x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 361 us: 1.01x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| pickle_list          | 5.25 us                                                               | 5.26 us: 1.00x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 79.3 ms: 1.00x slower                                                   |
| pickle               | 13.4 us                                                               | 13.6 us: 1.01x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| pickle_dict          | 37.3 us                                                               | 38.3 us: 1.02x slower                                                   |
| json_loads           | 30.7 us                                                               | 31.7 us: 1.03x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.54 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.2 ms: 1.01x faster                                                   |
| django_template | 40.7 ms                                                               | 41.9 ms: 1.03x slower                                                   |
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 419 ms: 1.49x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 553 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 549 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 333 us: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.0 us: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 723 ms: 1.26x faster                                                    |
| generators                 | 43.5 ms                                                               | 34.7 ms: 1.25x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.23x faster                                                  |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 718 ms: 1.23x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.50 us: 1.17x faster                                                   |
| raytrace                   | 353 ms                                                                | 302 ms: 1.17x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.2 ms: 1.16x faster                                                   |
| go                         | 157 ms                                                                | 138 ms: 1.14x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 139 ms: 1.11x faster                                                    |
| tornado_http               | 136 ms                                                                | 124 ms: 1.10x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.65 us: 1.09x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.02 us: 1.09x faster                                                   |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 81.4 ms: 1.06x faster                                                   |
| sympy_str                  | 280 ms                                                                | 263 ms: 1.06x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.06x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.39 ms: 1.05x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.74 ms: 1.05x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.6 ms: 1.05x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.93 ms: 1.05x faster                                                   |
| 2to3                       | 308 ms                                                                | 295 ms: 1.05x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 59.4 ms: 1.04x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.9 ms: 1.04x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| mdp                        | 3.41 sec                                                              | 3.31 sec: 1.03x faster                                                  |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.6 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.02x faster                                                   |
| async_generators           | 491 ms                                                                | 483 ms: 1.02x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 256 us: 1.02x faster                                                    |
| pickle_pure_python         | 365 us                                                                | 361 us: 1.01x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 27.2 ms: 1.01x faster                                                   |
| regex_dna                  | 254 ms                                                                | 252 ms: 1.01x faster                                                    |
| pickle_list                | 5.25 us                                                               | 5.26 us: 1.00x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 79.3 ms: 1.00x slower                                                   |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| richards_super             | 58.5 ms                                                               | 59.1 ms: 1.01x slower                                                   |
| sympy_expand               | 454 ms                                                                | 459 ms: 1.01x slower                                                    |
| float                      | 92.1 ms                                                               | 93.3 ms: 1.01x slower                                                   |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.01x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.03 sec: 1.01x slower                                                  |
| nqueens                    | 99.2 ms                                                               | 101 ms: 1.02x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 62.5 ms: 1.02x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.11 ms: 1.02x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| pickle_dict                | 37.3 us                                                               | 38.3 us: 1.02x slower                                                   |
| django_template            | 40.7 ms                                                               | 41.9 ms: 1.03x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.89 us: 1.03x slower                                                   |
| json_loads                 | 30.7 us                                                               | 31.7 us: 1.03x slower                                                   |
| richards                   | 50.9 ms                                                               | 52.7 ms: 1.04x slower                                                   |
| fannkuch                   | 443 ms                                                                | 459 ms: 1.04x slower                                                    |
| pyflate                    | 559 ms                                                                | 580 ms: 1.04x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                                   |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.53 ms: 1.05x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| scimark_fft                | 418 ms                                                                | 444 ms: 1.06x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.54 us: 1.06x slower                                                   |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                   |
| coverage                   | 87.3 ms                                                               | 99.2 ms: 1.14x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.09 ms: 1.16x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.28 ms: 1.19x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.3 ms: 1.21x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (13): asyncio_tcp, thrift, pprint_safe_repr, asyncio_tcp_ssl, json, pprint_pformat, xml_etree_generate, asyncio_websockets, html5lib, bench_mp_pool, pylint, genshi_xml, sqlglot_normalize
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 97.40% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x