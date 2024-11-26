# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.040x faster
- HPT reliability: 98.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 294 ms: 1.05x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                  |
| html5lib       | 65.1 ms                                                               | 63.7 ms: 1.02x faster                                                   |
| tornado_http   | 136 ms                                                                | 126 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 437 ms: 1.43x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 419 ms: 1.38x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 568 ms: 1.37x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 553 ms: 1.34x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 739 ms: 1.24x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 732 ms: 1.21x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 92.6 ms: 1.01x slower                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 109 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.94 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 253 us: 1.03x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 359 us: 1.02x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                  |
| json_loads           | 30.7 us                                                               | 32.7 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.80 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.16x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 59.5 ms: 1.02x faster                                                   |
| genshi_text     | 27.4 ms                                                               | 27.1 ms: 1.01x faster                                                   |
| django_template | 40.7 ms                                                               | 41.7 ms: 1.03x slower                                                   |
| mako            | 12.9 ms                                                               | 13.5 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 437 ms: 1.43x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 419 ms: 1.38x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 568 ms: 1.37x faster                                                    |
| deepcopy                   | 446 us                                                                | 329 us: 1.35x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 553 ms: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.4 us: 1.29x faster                                                   |
| generators                 | 43.5 ms                                                               | 34.6 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 739 ms: 1.24x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 732 ms: 1.21x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.48 us: 1.18x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 20.9 ms: 1.17x faster                                                   |
| raytrace                   | 353 ms                                                                | 303 ms: 1.17x faster                                                    |
| go                         | 157 ms                                                                | 136 ms: 1.16x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.00 us: 1.09x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.69 us: 1.09x faster                                                   |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 135 ms: 1.08x faster                                                    |
| tornado_http               | 136 ms                                                                | 126 ms: 1.07x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.07x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.88 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                   |
| sympy_str                  | 280 ms                                                                | 265 ms: 1.06x faster                                                    |
| 2to3                       | 308 ms                                                                | 294 ms: 1.05x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 83.0 ms: 1.04x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.6 ms: 1.04x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.2 ms: 1.03x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 253 us: 1.03x faster                                                    |
| async_generators           | 491 ms                                                                | 479 ms: 1.03x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.3 ms: 1.02x faster                                                   |
| html5lib                   | 65.1 ms                                                               | 63.7 ms: 1.02x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                  |
| genshi_xml                 | 60.6 ms                                                               | 59.5 ms: 1.02x faster                                                   |
| pickle_pure_python         | 365 us                                                                | 359 us: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                                  |
| genshi_text                | 27.4 ms                                                               | 27.1 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 916 ms                                                                | 905 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.87 sec: 1.01x faster                                                  |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| thrift                     | 937 us                                                                | 939 us: 1.00x slower                                                    |
| float                      | 92.1 ms                                                               | 92.6 ms: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                  |
| richards_super             | 58.5 ms                                                               | 59.2 ms: 1.01x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 62.1 ms: 1.01x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                  |
| sympy_expand               | 454 ms                                                                | 461 ms: 1.02x slower                                                    |
| django_template            | 40.7 ms                                                               | 41.7 ms: 1.03x slower                                                   |
| meteor_contest             | 112 ms                                                                | 115 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.39 ms: 1.03x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.22 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.73 ms: 1.04x slower                                                   |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                    |
| pyflate                    | 559 ms                                                                | 582 ms: 1.04x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.5 ms: 1.04x slower                                                   |
| nbody                      | 105 ms                                                                | 109 ms: 1.04x slower                                                    |
| richards                   | 50.9 ms                                                               | 53.2 ms: 1.05x slower                                                   |
| fannkuch                   | 443 ms                                                                | 465 ms: 1.05x slower                                                    |
| scimark_fft                | 418 ms                                                                | 440 ms: 1.05x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.80 ms: 1.05x slower                                                   |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.94 ms: 1.06x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.07x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                   |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.09x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.99 ms: 1.13x slower                                                   |
| coverage                   | 87.3 ms                                                               | 99.4 ms: 1.14x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.16x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.18x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.30 ms: 1.20x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (8): nqueens, regex_dna, sqlglot_normalize, bench_mp_pool, asyncio_websockets, asyncio_tcp, pylint, xml_etree_process
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: bpe_tokeniser

- Geometric mean (including insignificant results): 1.040x faster
# HPT report

- Reliability score: 98.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x