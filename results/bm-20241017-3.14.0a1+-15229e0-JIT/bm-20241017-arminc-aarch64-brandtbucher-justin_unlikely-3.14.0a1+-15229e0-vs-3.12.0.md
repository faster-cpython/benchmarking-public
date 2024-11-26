# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-aarch64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.086x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 385 ms: 1.25x slower                                                      |
| docutils       | 2.98 sec                                                              | 3.62 sec: 1.21x slower                                                    |
| html5lib       | 65.1 ms                                                               | 71.1 ms: 1.09x slower                                                     |
| tornado_http   | 136 ms                                                                | 146 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 539 ms: 1.37x faster                                                      |
| async_tree_none            | 624 ms                                                                | 458 ms: 1.36x faster                                                      |
| async_tree_memoization     | 777 ms                                                                | 603 ms: 1.29x faster                                                      |
| async_tree_none_tg         | 577 ms                                                                | 448 ms: 1.29x faster                                                      |
| async_tree_io              | 1.41 sec                                                              | 1.16 sec: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 755 ms: 1.21x faster                                                      |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 742 ms: 1.19x faster                                                      |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.13x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.25x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                      |
| float          | 92.1 ms                                                               | 97.2 ms: 1.06x slower                                                     |
| nbody          | 105 ms                                                                | 119 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 245 ms: 1.04x faster                                                      |
| regex_effbot   | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 31.4 ms: 1.11x slower                                                     |
| regex_compile  | 137 ms                                                                | 183 ms: 1.33x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 185 ms: 1.05x faster                                                      |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                                     |
| xml_etree_process    | 79.0 ms                                                               | 80.6 ms: 1.02x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 266 us: 1.02x slower                                                      |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                     |
| unpickle             | 18.5 us                                                               | 19.0 us: 1.03x slower                                                     |
| json_loads           | 30.7 us                                                               | 31.7 us: 1.03x slower                                                     |
| unpickle_list        | 6.17 us                                                               | 6.50 us: 1.05x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 387 us: 1.06x slower                                                      |
| json_dumps           | 12.3 ms                                                               | 14.3 ms: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                              |

Benchmark hidden because not significant (3): pickle_list, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                                     |
| python_startup         | 11.4 ms                                                               | 14.6 ms: 1.29x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                     |
| genshi_text     | 27.4 ms                                                               | 34.2 ms: 1.25x slower                                                     |
| django_template | 40.7 ms                                                               | 50.9 ms: 1.25x slower                                                     |
| genshi_xml      | 60.6 ms                                                               | 84.6 ms: 1.40x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 539 ms: 1.37x faster                                                      |
| async_tree_none            | 624 ms                                                                | 458 ms: 1.36x faster                                                      |
| async_tree_memoization     | 777 ms                                                                | 603 ms: 1.29x faster                                                      |
| async_tree_none_tg         | 577 ms                                                                | 448 ms: 1.29x faster                                                      |
| deepcopy_memo              | 49.6 us                                                               | 39.3 us: 1.26x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.16 sec: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 755 ms: 1.21x faster                                                      |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 742 ms: 1.19x faster                                                      |
| deepcopy                   | 446 us                                                                | 379 us: 1.17x faster                                                      |
| pathlib                    | 24.5 ms                                                               | 21.5 ms: 1.14x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.13x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 185 ms: 1.05x faster                                                      |
| regex_dna                  | 254 ms                                                                | 245 ms: 1.04x faster                                                      |
| logging_format             | 8.34 us                                                               | 8.06 us: 1.04x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.41 us: 1.03x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.99 us: 1.03x faster                                                     |
| comprehensions             | 25.4 us                                                               | 24.9 us: 1.02x faster                                                     |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.01x faster                                                     |
| asyncio_websockets         | 658 ms                                                                | 662 ms: 1.01x slower                                                      |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                      |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 148 ms: 1.02x slower                                                      |
| xml_etree_process          | 79.0 ms                                                               | 80.6 ms: 1.02x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.49 sec: 1.02x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 266 us: 1.02x slower                                                      |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                     |
| unpickle                   | 18.5 us                                                               | 19.0 us: 1.03x slower                                                     |
| json_loads                 | 30.7 us                                                               | 31.7 us: 1.03x slower                                                     |
| json                       | 5.54 ms                                                               | 5.74 ms: 1.04x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.91 us: 1.04x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                                     |
| thrift                     | 937 us                                                                | 979 us: 1.05x slower                                                      |
| async_generators           | 491 ms                                                                | 513 ms: 1.05x slower                                                      |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.29 sec: 1.05x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 90.7 ms: 1.05x slower                                                     |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                      |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.50 us: 1.05x slower                                                     |
| float                      | 92.1 ms                                                               | 97.2 ms: 1.06x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 387 us: 1.06x slower                                                      |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                                      |
| scimark_monte_carlo        | 85.1 ms                                                               | 90.7 ms: 1.07x slower                                                     |
| tornado_http               | 136 ms                                                                | 146 ms: 1.08x slower                                                      |
| html5lib                   | 65.1 ms                                                               | 71.1 ms: 1.09x slower                                                     |
| scimark_fft                | 418 ms                                                                | 463 ms: 1.11x slower                                                      |
| regex_v8                   | 28.3 ms                                                               | 31.4 ms: 1.11x slower                                                     |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.11x slower                                                      |
| deltablue                  | 4.12 ms                                                               | 4.63 ms: 1.12x slower                                                     |
| asyncio_tcp                | 566 ms                                                                | 639 ms: 1.13x slower                                                      |
| coverage                   | 87.3 ms                                                               | 98.8 ms: 1.13x slower                                                     |
| nbody                      | 105 ms                                                                | 119 ms: 1.14x slower                                                      |
| fannkuch                   | 443 ms                                                                | 508 ms: 1.14x slower                                                      |
| pyflate                    | 559 ms                                                                | 643 ms: 1.15x slower                                                      |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.16 ms: 1.16x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.89 ms: 1.16x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.3 ms: 1.16x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.71 ms: 1.17x slower                                                     |
| go                         | 157 ms                                                                | 185 ms: 1.18x slower                                                      |
| spectral_norm              | 131 ms                                                                | 155 ms: 1.18x slower                                                      |
| pycparser                  | 1.26 sec                                                              | 1.52 sec: 1.21x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 218 us: 1.21x slower                                                      |
| docutils                   | 2.98 sec                                                              | 3.62 sec: 1.21x slower                                                    |
| chaos                      | 71.4 ms                                                               | 87.2 ms: 1.22x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 2.24 ms: 1.22x slower                                                     |
| richards_super             | 58.5 ms                                                               | 71.7 ms: 1.23x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 123 ms: 1.24x slower                                                      |
| sqlglot_normalize          | 126 ms                                                                | 156 ms: 1.24x slower                                                      |
| genshi_text                | 27.4 ms                                                               | 34.2 ms: 1.25x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 77.4 ms: 1.25x slower                                                     |
| 2to3                       | 308 ms                                                                | 385 ms: 1.25x slower                                                      |
| django_template            | 40.7 ms                                                               | 50.9 ms: 1.25x slower                                                     |
| richards                   | 50.9 ms                                                               | 63.8 ms: 1.25x slower                                                     |
| python_startup             | 11.4 ms                                                               | 14.6 ms: 1.29x slower                                                     |
| sympy_str                  | 280 ms                                                                | 363 ms: 1.30x slower                                                      |
| sympy_expand               | 454 ms                                                                | 592 ms: 1.30x slower                                                      |
| regex_compile              | 137 ms                                                                | 183 ms: 1.33x slower                                                      |
| sqlglot_optimize           | 61.3 ms                                                               | 82.9 ms: 1.35x slower                                                     |
| generators                 | 43.5 ms                                                               | 58.9 ms: 1.35x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 29.3 ms: 1.35x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.24 sec: 1.36x slower                                                    |
| pylint                     | 355 ms                                                                | 493 ms: 1.39x slower                                                      |
| pprint_pformat             | 1.88 sec                                                              | 2.61 sec: 1.39x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 84.6 ms: 1.40x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 216 ms: 1.40x slower                                                      |
| gc_traversal               | 4.40 ms                                                               | 6.23 ms: 1.42x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 10.2 ms: 1.47x slower                                                     |
| create_gc_cycles           | 1.92 ms                                                               | 3.68 ms: 1.92x slower                                                     |
| bench_mp_pool              | 7.05 ms                                                               | 1.92 sec: 272.66x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.16x slower                                                              |

Benchmark hidden because not significant (4): pickle_list, raytrace, xml_etree_generate, xml_etree_iterparse
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: bpe_tokeniser, sphinx, unpack_sequence

- Geometric mean (including insignificant results): 1.086x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x