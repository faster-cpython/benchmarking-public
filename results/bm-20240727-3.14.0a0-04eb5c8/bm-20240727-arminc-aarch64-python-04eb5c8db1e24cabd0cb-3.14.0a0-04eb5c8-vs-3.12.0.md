# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-aarch64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.03x faster
- HPT reliability: 90.02%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 304 ms: 1.01x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.11 sec: 1.04x slower                                                  |
| html5lib       | 65.1 ms                                                               | 66.4 ms: 1.02x slower                                                   |
| tornado_http   | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 444 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 413 ms: 1.40x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 563 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 543 ms: 1.36x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.13 sec: 1.25x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 730 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 712 ms: 1.24x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.13 sec: 1.24x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 109 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 145 ms: 1.04x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 251 us: 1.03x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                                  |
| pickle_pure_python   | 365 us                                                                | 360 us: 1.02x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 80.2 ms: 1.02x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.8 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.89 ms: 1.06x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                                   |
| django_template | 40.7 ms                                                               | 41.6 ms: 1.02x slower                                                   |
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 444 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 413 ms: 1.40x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 563 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 543 ms: 1.36x faster                                                    |
| deepcopy                   | 446 us                                                                | 335 us: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.2 us: 1.30x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.13 sec: 1.25x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 730 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 712 ms: 1.24x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.13 sec: 1.24x faster                                                  |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.24x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.3 ms: 1.23x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.43 us: 1.20x faster                                                   |
| raytrace                   | 353 ms                                                                | 296 ms: 1.19x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.3 ms: 1.15x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.97 us: 1.10x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.67 us: 1.09x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.84 ms: 1.07x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                    |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.07x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 81.9 ms: 1.06x faster                                                   |
| chaos                      | 71.4 ms                                                               | 67.5 ms: 1.06x faster                                                   |
| tornado_http               | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 145 ms: 1.04x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.0 ms: 1.04x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 251 us: 1.03x faster                                                    |
| dask                       | 376 ms                                                                | 364 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                  |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.02x faster                                                  |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.02x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                                  |
| pickle_pure_python         | 365 us                                                                | 360 us: 1.02x faster                                                    |
| 2to3                       | 308 ms                                                                | 304 ms: 1.01x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.7 ms: 1.01x faster                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.15 ms: 1.01x slower                                                   |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.02x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 80.2 ms: 1.02x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 62.4 ms: 1.02x slower                                                   |
| logging_silent             | 127 ns                                                                | 129 ns: 1.02x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                                   |
| sympy_expand               | 454 ms                                                                | 463 ms: 1.02x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 66.4 ms: 1.02x slower                                                   |
| django_template            | 40.7 ms                                                               | 41.6 ms: 1.02x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.15 ms: 1.02x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 580 ms: 1.03x slower                                                    |
| richards                   | 50.9 ms                                                               | 52.3 ms: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.24 sec: 1.03x slower                                                  |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.37 ms: 1.03x slower                                                   |
| go                         | 157 ms                                                                | 162 ms: 1.03x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.95 sec: 1.03x slower                                                  |
| json                       | 5.54 ms                                                               | 5.74 ms: 1.04x slower                                                   |
| pyflate                    | 559 ms                                                                | 580 ms: 1.04x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 952 ms: 1.04x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.11 sec: 1.04x slower                                                  |
| thrift                     | 937 us                                                                | 977 us: 1.04x slower                                                    |
| nbody                      | 105 ms                                                                | 109 ms: 1.04x slower                                                    |
| scimark_fft                | 418 ms                                                                | 438 ms: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.89 ms: 1.06x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.8 us: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                    |
| fannkuch                   | 443 ms                                                                | 476 ms: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.82 ms: 1.10x slower                                                   |
| coverage                   | 87.3 ms                                                               | 97.4 ms: 1.12x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.95 ms: 1.17x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.33 ms: 1.21x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (11): sqlglot_transpile, float, xml_etree_generate, asyncio_websockets, nqueens, richards_super, async_generators, pylint, regex_dna, genshi_xml, sqlglot_normalize
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: bpe_tokeniser

# HPT report

- Reliability score: 90.02% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x