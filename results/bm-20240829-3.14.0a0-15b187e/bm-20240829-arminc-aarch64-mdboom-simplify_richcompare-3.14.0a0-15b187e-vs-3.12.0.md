# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.04x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 292 ms: 1.05x faster                                                    |
| html5lib       | 65.1 ms                                                               | 63.5 ms: 1.02x faster                                                   |
| tornado_http   | 136 ms                                                                | 124 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 423 ms: 1.47x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 412 ms: 1.40x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 556 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 545 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 724 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 721 ms: 1.23x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.22x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.16 sec: 1.21x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 92.9 ms: 1.01x slower                                                   |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| regex_dna      | 254 ms                                                                | 246 ms: 1.03x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.85 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 254 us: 1.02x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 358 us: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| json_loads           | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 60.0 ms: 1.01x faster                                                   |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| django_template | 40.7 ms                                                               | 42.5 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 423 ms: 1.47x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 412 ms: 1.40x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 556 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 545 ms: 1.36x faster                                                    |
| deepcopy                   | 446 us                                                                | 337 us: 1.32x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.0 us: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 724 ms: 1.26x faster                                                    |
| generators                 | 43.5 ms                                                               | 34.6 ms: 1.26x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 721 ms: 1.23x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.22x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.16 sec: 1.21x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.49 us: 1.18x faster                                                   |
| raytrace                   | 353 ms                                                                | 303 ms: 1.16x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.1 ms: 1.16x faster                                                   |
| go                         | 157 ms                                                                | 140 ms: 1.12x faster                                                    |
| tornado_http               | 136 ms                                                                | 124 ms: 1.09x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.01 us: 1.09x faster                                                   |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.74 us: 1.08x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.71 ms: 1.07x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.07x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.88 ms: 1.06x faster                                                   |
| sympy_str                  | 280 ms                                                                | 263 ms: 1.06x faster                                                    |
| 2to3                       | 308 ms                                                                | 292 ms: 1.05x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 538 ms: 1.05x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 82.6 ms: 1.05x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.40 ms: 1.05x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.5 ms: 1.04x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.8 ms: 1.04x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 246 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| xml_etree_iterparse        | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 63.5 ms: 1.02x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 254 us: 1.02x faster                                                    |
| async_generators           | 491 ms                                                                | 479 ms: 1.02x faster                                                    |
| pickle_pure_python         | 365 us                                                                | 358 us: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.37 sec: 1.01x faster                                                  |
| thrift                     | 937 us                                                                | 926 us: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.16 sec: 1.01x faster                                                  |
| genshi_xml                 | 60.6 ms                                                               | 60.0 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 916 ms                                                                | 910 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.87 sec: 1.01x faster                                                  |
| pyflate                    | 559 ms                                                                | 562 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| sympy_expand               | 454 ms                                                                | 457 ms: 1.01x slower                                                    |
| float                      | 92.1 ms                                                               | 92.9 ms: 1.01x slower                                                   |
| richards_super             | 58.5 ms                                                               | 59.2 ms: 1.01x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 7.15 ms: 1.01x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 62.3 ms: 1.02x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 7.21 ms: 1.03x slower                                                   |
| richards                   | 50.9 ms                                                               | 52.7 ms: 1.03x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.42 ms: 1.04x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| json                       | 5.54 ms                                                               | 5.77 ms: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                                   |
| django_template            | 40.7 ms                                                               | 42.5 ms: 1.04x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.85 ms: 1.05x slower                                                   |
| fannkuch                   | 443 ms                                                                | 464 ms: 1.05x slower                                                    |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.06x slower                                                    |
| scimark_fft                | 418 ms                                                                | 445 ms: 1.06x slower                                                    |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 196 us: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| coverage                   | 87.3 ms                                                               | 98.5 ms: 1.13x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.97 ms: 1.13x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.94 ms: 1.17x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.29 ms: 1.19x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                            |

Benchmark hidden because not significant (10): docutils, coroutines, xml_etree_process, genshi_text, meteor_contest, pylint, nqueens, asyncio_websockets, xml_etree_generate, sqlglot_normalize
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240829-3.14.0a0-15b187e/bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json: bpe_tokeniser

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x