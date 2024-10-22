# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.04x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 296 ms: 1.04x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                  |
| html5lib       | 65.1 ms                                                               | 63.2 ms: 1.03x faster                                                   |
| tornado_http   | 136 ms                                                                | 127 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 423 ms: 1.47x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 558 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 418 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 551 ms: 1.34x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 727 ms: 1.26x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 724 ms: 1.22x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 108 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.89 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 190 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 147 ms: 1.02x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 358 us: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| json_loads           | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.77 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 59.6 ms: 1.02x faster                                                   |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| django_template | 40.7 ms                                                               | 42.4 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 423 ms: 1.47x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 558 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 418 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 551 ms: 1.34x faster                                                    |
| deepcopy                   | 446 us                                                                | 333 us: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.9 us: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 727 ms: 1.26x faster                                                    |
| generators                 | 43.5 ms                                                               | 34.7 ms: 1.25x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.3 us: 1.25x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 724 ms: 1.22x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.47 us: 1.18x faster                                                   |
| raytrace                   | 353 ms                                                                | 300 ms: 1.18x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.2 ms: 1.16x faster                                                   |
| go                         | 157 ms                                                                | 136 ms: 1.15x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 140 ms: 1.10x faster                                                    |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 133 ms: 1.10x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.64 us: 1.09x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.02 us: 1.09x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.84 ms: 1.07x faster                                                   |
| tornado_http               | 136 ms                                                                | 127 ms: 1.07x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.4 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                   |
| sympy_str                  | 280 ms                                                                | 265 ms: 1.06x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.06x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 82.1 ms: 1.05x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.40 ms: 1.05x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.7 ms: 1.05x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.3 ms: 1.04x faster                                                   |
| 2to3                       | 308 ms                                                                | 296 ms: 1.04x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 63.2 ms: 1.03x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.32 sec: 1.03x faster                                                  |
| xml_etree_parse            | 195 ms                                                                | 190 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| async_generators           | 491 ms                                                                | 479 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 147 ms: 1.02x faster                                                    |
| pickle_pure_python         | 365 us                                                                | 358 us: 1.02x faster                                                    |
| nqueens                    | 99.2 ms                                                               | 97.4 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 6.94 ms: 1.02x faster                                                   |
| genshi_xml                 | 60.6 ms                                                               | 59.6 ms: 1.02x faster                                                   |
| meteor_contest             | 112 ms                                                                | 110 ms: 1.01x faster                                                    |
| pprint_safe_repr           | 916 ms                                                                | 907 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.87 sec: 1.01x faster                                                  |
| hexiom                     | 6.98 ms                                                               | 7.02 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                  |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| thrift                     | 937 us                                                                | 947 us: 1.01x slower                                                    |
| sympy_expand               | 454 ms                                                                | 458 ms: 1.01x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| richards_super             | 58.5 ms                                                               | 59.7 ms: 1.02x slower                                                   |
| pyflate                    | 559 ms                                                                | 575 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.39 ms: 1.03x slower                                                   |
| nbody                      | 105 ms                                                                | 108 ms: 1.03x slower                                                    |
| json                       | 5.54 ms                                                               | 5.73 ms: 1.03x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| logging_silent             | 127 ns                                                                | 131 ns: 1.04x slower                                                    |
| fannkuch                   | 443 ms                                                                | 460 ms: 1.04x slower                                                    |
| scimark_sor                | 150 ms                                                                | 156 ms: 1.04x slower                                                    |
| django_template            | 40.7 ms                                                               | 42.4 ms: 1.04x slower                                                   |
| richards                   | 50.9 ms                                                               | 53.3 ms: 1.05x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.77 ms: 1.05x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.89 ms: 1.06x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 192 us: 1.06x slower                                                    |
| scimark_fft                | 418 ms                                                                | 446 ms: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| coverage                   | 87.3 ms                                                               | 97.8 ms: 1.12x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.99 ms: 1.14x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.81 ms: 1.15x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.29 ms: 1.19x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                            |

Benchmark hidden because not significant (9): xml_etree_generate, regex_dna, genshi_text, float, asyncio_tcp, pylint, asyncio_websockets, sqlglot_optimize, xml_etree_process
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: bpe_tokeniser

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x