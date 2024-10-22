# Results vs. 3.12.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-aarch64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.07x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 386 ms: 1.25x slower                                                    |
| docutils       | 2.98 sec                                                              | 4.04 sec: 1.35x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.9 ms: 1.10x slower                                                   |
| tornado_http   | 136 ms                                                                | 140 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 435 ms: 1.43x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 412 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 542 ms: 1.37x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 580 ms: 1.34x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.10 sec: 1.28x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 705 ms: 1.25x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 751 ms: 1.22x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.3 ms: 1.04x faster                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 246 ms: 1.03x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.81 ms: 1.04x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.2 ms: 1.07x slower                                                   |
| regex_compile  | 137 ms                                                                | 188 ms: 1.37x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 79.7 ms: 1.01x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 268 us: 1.03x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 391 us: 1.07x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.81 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| django_template | 40.7 ms                                                               | 50.8 ms: 1.25x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.3 ms: 1.25x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 82.0 ms: 1.35x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 435 ms: 1.43x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 412 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 542 ms: 1.37x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 36.8 us: 1.35x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 580 ms: 1.34x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.10 sec: 1.28x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 705 ms: 1.25x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 751 ms: 1.22x faster                                                    |
| deepcopy                   | 446 us                                                                | 397 us: 1.12x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.0 ms: 1.12x faster                                                   |
| raytrace                   | 353 ms                                                                | 328 ms: 1.08x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.81 us: 1.07x faster                                                   |
| comprehensions             | 25.4 us                                                               | 24.2 us: 1.05x faster                                                   |
| float                      | 92.1 ms                                                               | 88.3 ms: 1.04x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 246 ms: 1.03x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.44 us: 1.03x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.16 us: 1.02x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                                  |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.32 ms: 1.01x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 79.7 ms: 1.01x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 147 ms: 1.01x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.47 sec: 1.02x slower                                                  |
| crypto_pyaes               | 86.6 ms                                                               | 88.2 ms: 1.02x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.24 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.71 ms: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                  |
| unpickle_pure_python       | 260 us                                                                | 268 us: 1.03x slower                                                    |
| tornado_http               | 136 ms                                                                | 140 ms: 1.04x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.81 ms: 1.04x slower                                                   |
| async_generators           | 491 ms                                                                | 511 ms: 1.04x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.81 ms: 1.05x slower                                                   |
| logging_silent             | 127 ns                                                                | 134 ns: 1.06x slower                                                    |
| thrift                     | 937 us                                                                | 992 us: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.2 ms: 1.07x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 90.8 ms: 1.07x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 7.56 ms: 1.07x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 391 us: 1.07x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 614 ms: 1.08x slower                                                    |
| scimark_fft                | 418 ms                                                                | 454 ms: 1.09x slower                                                    |
| meteor_contest             | 112 ms                                                                | 122 ms: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.80 ms: 1.10x slower                                                   |
| nbody                      | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.9 ms: 1.10x slower                                                   |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.11x slower                                                    |
| coverage                   | 87.3 ms                                                               | 97.7 ms: 1.12x slower                                                   |
| fannkuch                   | 443 ms                                                                | 502 ms: 1.13x slower                                                    |
| pyflate                    | 559 ms                                                                | 643 ms: 1.15x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.69 ms: 1.15x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.08 ms: 1.16x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 210 us: 1.16x slower                                                    |
| go                         | 157 ms                                                                | 186 ms: 1.18x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.49 sec: 1.19x slower                                                  |
| telco                      | 8.51 ms                                                               | 10.2 ms: 1.20x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 150 ms: 1.20x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.32 ms: 1.21x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.22 ms: 1.22x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 123 ms: 1.24x slower                                                    |
| chaos                      | 71.4 ms                                                               | 88.9 ms: 1.25x slower                                                   |
| django_template            | 40.7 ms                                                               | 50.8 ms: 1.25x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 34.3 ms: 1.25x slower                                                   |
| 2to3                       | 308 ms                                                                | 386 ms: 1.25x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 78.4 ms: 1.28x slower                                                   |
| richards_super             | 58.5 ms                                                               | 75.0 ms: 1.28x slower                                                   |
| generators                 | 43.5 ms                                                               | 57.2 ms: 1.32x slower                                                   |
| sympy_str                  | 280 ms                                                                | 370 ms: 1.32x slower                                                    |
| sympy_expand               | 454 ms                                                                | 604 ms: 1.33x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 28.9 ms: 1.34x slower                                                   |
| richards                   | 50.9 ms                                                               | 68.4 ms: 1.34x slower                                                   |
| pylint                     | 355 ms                                                                | 477 ms: 1.34x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 82.0 ms: 1.35x slower                                                   |
| docutils                   | 2.98 sec                                                              | 4.04 sec: 1.35x slower                                                  |
| regex_compile              | 137 ms                                                                | 188 ms: 1.37x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 218 ms: 1.41x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.0 ms: 1.43x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.35 sec: 1.47x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.79 sec: 1.48x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, coroutines, scimark_sor, asyncio_websockets, xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: bpe_tokeniser

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.02x