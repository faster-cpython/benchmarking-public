# Results vs. 3.12.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-aarch64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 361 ms: 1.17x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.55 sec: 1.19x slower                                                  |
| html5lib       | 65.1 ms                                                               | 69.9 ms: 1.07x slower                                                   |
| tornado_http   | 136 ms                                                                | 142 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 414 ms: 1.39x faster                                                    |
| async_tree_none            | 624 ms                                                                | 451 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 542 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 590 ms: 1.32x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 739 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 720 ms: 1.23x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.6 ms: 1.02x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 259 ms: 1.02x slower                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.94 ms: 1.07x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| regex_compile  | 137 ms                                                                | 178 ms: 1.29x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 110 ms: 1.01x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| unpickle_pure_python | 260 us                                                                | 274 us: 1.05x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.07x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 415 us: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.94 ms: 1.07x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| django_template | 40.7 ms                                                               | 50.9 ms: 1.25x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.4 ms: 1.25x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 80.5 ms: 1.33x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 414 ms: 1.39x faster                                                    |
| async_tree_none            | 624 ms                                                                | 451 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 542 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 590 ms: 1.32x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| deepcopy_memo              | 49.6 us                                                               | 38.0 us: 1.31x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 739 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 720 ms: 1.23x faster                                                    |
| deepcopy                   | 446 us                                                                | 372 us: 1.20x faster                                                    |
| generators                 | 43.5 ms                                                               | 38.6 ms: 1.13x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.0 ms: 1.12x faster                                                   |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                    |
| comprehensions             | 25.4 us                                                               | 23.4 us: 1.08x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.17 us: 1.06x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.93 us: 1.05x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.03 us: 1.02x faster                                                   |
| float                      | 92.1 ms                                                               | 90.6 ms: 1.02x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 110 ms: 1.01x faster                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.02x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.47 sec: 1.02x slower                                                  |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| regex_dna                  | 254 ms                                                                | 259 ms: 1.02x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| async_generators           | 491 ms                                                                | 505 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.04x slower                                                  |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.04x slower                                                    |
| dask                       | 376 ms                                                                | 391 ms: 1.04x slower                                                    |
| thrift                     | 937 us                                                                | 974 us: 1.04x slower                                                    |
| richards_super             | 58.5 ms                                                               | 61.4 ms: 1.05x slower                                                   |
| tornado_http               | 136 ms                                                                | 142 ms: 1.05x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 274 us: 1.05x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.9 ms: 1.06x slower                                                   |
| fannkuch                   | 443 ms                                                                | 470 ms: 1.06x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.94 ms: 1.07x slower                                                   |
| richards                   | 50.9 ms                                                               | 54.3 ms: 1.07x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.94 ms: 1.07x slower                                                   |
| json                       | 5.54 ms                                                               | 5.92 ms: 1.07x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| logging_silent             | 127 ns                                                                | 136 ns: 1.07x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.07x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 69.9 ms: 1.07x slower                                                   |
| pyflate                    | 559 ms                                                                | 603 ms: 1.08x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.45 ms: 1.08x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                  |
| sqlglot_parse              | 1.46 ms                                                               | 1.59 ms: 1.09x slower                                                   |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.76 ms: 1.09x slower                                                   |
| spectral_norm              | 131 ms                                                                | 144 ms: 1.10x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 625 ms: 1.10x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.02 ms: 1.11x slower                                                   |
| scimark_fft                | 418 ms                                                                | 463 ms: 1.11x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 69.1 ms: 1.13x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 415 us: 1.14x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.02 ms: 1.14x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 144 ms: 1.14x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 71.1 ms: 1.15x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                   |
| go                         | 157 ms                                                                | 181 ms: 1.15x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 209 us: 1.16x slower                                                    |
| sympy_str                  | 280 ms                                                                | 324 ms: 1.16x slower                                                    |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                    |
| pylint                     | 355 ms                                                                | 413 ms: 1.16x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 8.27 ms: 1.17x slower                                                   |
| 2to3                       | 308 ms                                                                | 361 ms: 1.17x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 118 ms: 1.19x slower                                                    |
| scimark_sor                | 150 ms                                                                | 178 ms: 1.19x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.55 sec: 1.19x slower                                                  |
| sympy_expand               | 454 ms                                                                | 541 ms: 1.19x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 185 ms: 1.20x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 26.2 ms: 1.21x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.4 ms: 1.23x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.13 sec: 1.23x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.34 sec: 1.24x slower                                                  |
| create_gc_cycles           | 1.92 ms                                                               | 2.39 ms: 1.25x slower                                                   |
| django_template            | 40.7 ms                                                               | 50.9 ms: 1.25x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 34.4 ms: 1.25x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 183 ms: 1.26x slower                                                    |
| chaos                      | 71.4 ms                                                               | 90.9 ms: 1.27x slower                                                   |
| regex_compile              | 137 ms                                                                | 178 ms: 1.29x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.03 ms: 1.29x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 80.5 ms: 1.33x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (5): coroutines, xml_etree_iterparse, xml_etree_process, asyncio_websockets, crypto_pyaes
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.01x