# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-aarch64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.01x faster
- HPT reliability: 91.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| chameleon      | 8.81 ms                                                               | 9.16 ms: 1.04x slower                                                   |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| tornado_http   | 136 ms                                                                | 130 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 490 ms: 1.27x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 600 ms: 1.23x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 467 ms: 1.23x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 647 ms: 1.20x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 756 ms: 1.17x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 784 ms: 1.16x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.11x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.19x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 105 ms                                                                | 113 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 129 ms: 1.06x faster                                                    |
| regex_dna      | 254 ms                                                                | 250 ms: 1.02x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 190 ms: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.53 sec: 1.02x faster                                                  |
| pickle_pure_python   | 365 us                                                                | 361 us: 1.01x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| pickle               | 13.4 us                                                               | 13.6 us: 1.02x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 81.2 ms: 1.03x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.2 us: 1.05x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.59 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (3): pickle_list, pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 11.4 ms                                                               | 12.6 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.9 ms: 1.02x slower                                                   |
| django_template | 40.7 ms                                                               | 41.6 ms: 1.02x slower                                                   |
| mako            | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 490 ms: 1.27x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.25x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 600 ms: 1.23x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 467 ms: 1.23x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 647 ms: 1.20x faster                                                    |
| raytrace                   | 353 ms                                                                | 297 ms: 1.19x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 756 ms: 1.17x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 784 ms: 1.16x faster                                                    |
| generators                 | 43.5 ms                                                               | 37.6 ms: 1.16x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.4 ms: 1.15x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.11x faster                                                  |
| logging_simple             | 7.63 us                                                               | 7.11 us: 1.07x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.78 us: 1.07x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                    |
| regex_compile              | 137 ms                                                                | 129 ms: 1.06x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 137 ms: 1.06x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.90 ms: 1.06x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 82.0 ms: 1.06x faster                                                   |
| chaos                      | 71.4 ms                                                               | 67.9 ms: 1.05x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.1 ms: 1.05x faster                                                   |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 59.4 ms: 1.04x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.40 ms: 1.04x faster                                                   |
| tornado_http               | 136 ms                                                                | 130 ms: 1.04x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.27 ms: 1.03x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.32 sec: 1.03x faster                                                  |
| xml_etree_parse            | 195 ms                                                                | 190 ms: 1.02x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.53 sec: 1.02x faster                                                  |
| dask                       | 376 ms                                                                | 368 ms: 1.02x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.02 us: 1.02x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 21.3 ms: 1.02x faster                                                   |
| regex_dna                  | 254 ms                                                                | 250 ms: 1.02x faster                                                    |
| async_generators           | 491 ms                                                                | 483 ms: 1.02x faster                                                    |
| nqueens                    | 99.2 ms                                                               | 98.0 ms: 1.01x faster                                                   |
| pickle_pure_python         | 365 us                                                                | 361 us: 1.01x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 50.1 us: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 1.91 sec: 1.01x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 7.07 ms: 1.01x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 62.1 ms: 1.01x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 666 ms: 1.01x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 930 ms: 1.02x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 128 ms: 1.02x slower                                                    |
| sympy_expand               | 454 ms                                                                | 461 ms: 1.02x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.02x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 27.9 ms: 1.02x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.84 us: 1.02x slower                                                   |
| go                         | 157 ms                                                                | 160 ms: 1.02x slower                                                    |
| django_template            | 40.7 ms                                                               | 41.6 ms: 1.02x slower                                                   |
| json                       | 5.54 ms                                                               | 5.68 ms: 1.02x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 81.2 ms: 1.03x slower                                                   |
| thrift                     | 937 us                                                                | 967 us: 1.03x slower                                                    |
| richards_super             | 58.5 ms                                                               | 60.4 ms: 1.03x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| fannkuch                   | 443 ms                                                                | 460 ms: 1.04x slower                                                    |
| chameleon                  | 8.81 ms                                                               | 9.16 ms: 1.04x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.2 us: 1.05x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                   |
| richards                   | 50.9 ms                                                               | 53.7 ms: 1.05x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| logging_silent             | 127 ns                                                                | 134 ns: 1.06x slower                                                    |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| scimark_fft                | 418 ms                                                                | 446 ms: 1.07x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.59 us: 1.07x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.65 ms: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| nbody                      | 105 ms                                                                | 113 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 200 us: 1.11x slower                                                    |
| python_startup             | 11.4 ms                                                               | 12.6 ms: 1.11x slower                                                   |
| coverage                   | 87.3 ms                                                               | 97.9 ms: 1.12x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.85 ms: 1.16x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.22 ms: 1.19x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.39 ms: 1.24x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (16): pylint, 2to3, bench_mp_pool, pyflate, pickle_list, float, coroutines, pickle_dict, deepcopy, genshi_xml, meteor_contest, python_startup_no_site, pidigits, asyncio_tcp, html5lib, xml_etree_iterparse
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging

# HPT report

- Reliability score: 91.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x