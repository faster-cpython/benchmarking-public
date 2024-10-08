# Results vs. 3.12.0

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: linux-aarch64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.03x faster
- HPT reliability: 94.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 303 ms: 1.02x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| html5lib       | 65.1 ms                                                               | 68.0 ms: 1.05x slower                                                   |
| tornado_http   | 136 ms                                                                | 130 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 446 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 413 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 536 ms: 1.38x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 574 ms: 1.35x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.12 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 732 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 718 ms: 1.23x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.14 sec: 1.23x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                    |
| regex_dna      | 254 ms                                                                | 251 ms: 1.01x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 251 us: 1.03x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 147 ms: 1.03x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                  |
| json_loads           | 30.7 us                                                               | 33.5 us: 1.09x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.87 ms: 1.06x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 41.8 ms: 1.03x slower                                                   |
| mako            | 12.9 ms                                                               | 13.5 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 446 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 413 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 536 ms: 1.38x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 574 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 332 us: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.7 us: 1.28x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.12 sec: 1.26x faster                                                  |
| generators                 | 43.5 ms                                                               | 34.9 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 732 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 718 ms: 1.23x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.14 sec: 1.23x faster                                                  |
| raytrace                   | 353 ms                                                                | 300 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.50 us: 1.17x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.6 ms: 1.13x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.83 ms: 1.07x faster                                                   |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.84 us: 1.06x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.18 us: 1.06x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 82.0 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.05x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.05x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 59.1 ms: 1.05x faster                                                   |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| tornado_http               | 136 ms                                                                | 130 ms: 1.05x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.5 ms: 1.04x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.5 ms: 1.04x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 251 us: 1.03x faster                                                    |
| dask                       | 376 ms                                                                | 364 ms: 1.03x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.2 ms: 1.03x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 147 ms: 1.03x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.02x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                  |
| 2to3                       | 308 ms                                                                | 303 ms: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                                  |
| regex_dna                  | 254 ms                                                                | 251 ms: 1.01x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                  |
| meteor_contest             | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| hexiom                     | 6.98 ms                                                               | 6.99 ms: 1.00x slower                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                                  |
| sympy_expand               | 454 ms                                                                | 457 ms: 1.01x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 61.9 ms: 1.01x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 572 ms: 1.01x slower                                                    |
| richards_super             | 58.5 ms                                                               | 59.2 ms: 1.01x slower                                                   |
| go                         | 157 ms                                                                | 160 ms: 1.02x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.91 sec: 1.02x slower                                                  |
| logging_silent             | 127 ns                                                                | 129 ns: 1.02x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 128 ms: 1.02x slower                                                    |
| thrift                     | 937 us                                                                | 961 us: 1.03x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 940 ms: 1.03x slower                                                    |
| pyflate                    | 559 ms                                                                | 574 ms: 1.03x slower                                                    |
| richards                   | 50.9 ms                                                               | 52.3 ms: 1.03x slower                                                   |
| django_template            | 40.7 ms                                                               | 41.8 ms: 1.03x slower                                                   |
| fannkuch                   | 443 ms                                                                | 458 ms: 1.03x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.43 ms: 1.04x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.5 ms: 1.04x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 68.0 ms: 1.05x slower                                                   |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                   |
| scimark_fft                | 418 ms                                                                | 441 ms: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.06x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.87 ms: 1.06x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.08x slower                                                    |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.5 us: 1.09x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.99 ms: 1.14x slower                                                   |
| coverage                   | 87.3 ms                                                               | 99.4 ms: 1.14x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.93 ms: 1.17x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.33 ms: 1.22x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (11): pylint, pickle_pure_python, float, xml_etree_generate, asyncio_websockets, bench_mp_pool, nqueens, genshi_xml, genshi_text, async_generators, xml_etree_process
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: bpe_tokeniser

# HPT report

- Reliability score: 94.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x