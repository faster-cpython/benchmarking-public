# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a1
- machine: linux-aarch64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.085x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 382 ms: 1.24x slower                                         |
| docutils       | 2.98 sec                                                              | 3.61 sec: 1.21x slower                                       |
| html5lib       | 65.1 ms                                                               | 71.8 ms: 1.10x slower                                        |
| tornado_http   | 136 ms                                                                | 147 ms: 1.09x slower                                         |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 542 ms: 1.37x faster                                         |
| async_tree_none            | 624 ms                                                                | 463 ms: 1.35x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 605 ms: 1.28x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 451 ms: 1.28x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 759 ms: 1.20x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 742 ms: 1.19x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.19x faster                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.12x faster                                       |
| Geometric mean             | (ref)                                                                 | 1.25x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                         |
| float          | 92.1 ms                                                               | 97.2 ms: 1.06x slower                                        |
| nbody          | 105 ms                                                                | 116 ms: 1.11x slower                                         |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 244 ms: 1.04x faster                                         |
| regex_effbot   | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                        |
| regex_v8       | 28.3 ms                                                               | 31.6 ms: 1.11x slower                                        |
| regex_compile  | 137 ms                                                                | 179 ms: 1.30x slower                                         |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 186 ms: 1.05x faster                                         |
| pickle_list          | 5.25 us                                                               | 5.12 us: 1.03x faster                                        |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                         |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                        |
| xml_etree_process    | 79.0 ms                                                               | 80.4 ms: 1.02x slower                                        |
| tomli_loads          | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                       |
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                        |
| unpickle_pure_python | 260 us                                                                | 268 us: 1.03x slower                                         |
| unpickle             | 18.5 us                                                               | 19.0 us: 1.03x slower                                        |
| json_loads           | 30.7 us                                                               | 31.7 us: 1.03x slower                                        |
| unpickle_list        | 6.17 us                                                               | 6.52 us: 1.06x slower                                        |
| pickle_pure_python   | 365 us                                                                | 389 us: 1.06x slower                                         |
| json_dumps           | 12.3 ms                                                               | 14.4 ms: 1.17x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                        |
| python_startup         | 11.4 ms                                                               | 14.7 ms: 1.29x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                        |
| genshi_text     | 27.4 ms                                                               | 34.2 ms: 1.25x slower                                        |
| django_template | 40.7 ms                                                               | 52.4 ms: 1.29x slower                                        |
| genshi_xml      | 60.6 ms                                                               | 84.1 ms: 1.39x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 542 ms: 1.37x faster                                         |
| async_tree_none            | 624 ms                                                                | 463 ms: 1.35x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 605 ms: 1.28x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 451 ms: 1.28x faster                                         |
| deepcopy_memo              | 49.6 us                                                               | 39.2 us: 1.26x faster                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 759 ms: 1.20x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 742 ms: 1.19x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.19x faster                                       |
| deepcopy                   | 446 us                                                                | 377 us: 1.18x faster                                         |
| pathlib                    | 24.5 ms                                                               | 21.6 ms: 1.14x faster                                        |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.12x faster                                       |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                         |
| regex_dna                  | 254 ms                                                                | 244 ms: 1.04x faster                                         |
| logging_format             | 8.34 us                                                               | 8.08 us: 1.03x faster                                        |
| deepcopy_reduce            | 4.10 us                                                               | 3.98 us: 1.03x faster                                        |
| comprehensions             | 25.4 us                                                               | 24.7 us: 1.03x faster                                        |
| pickle_list                | 5.25 us                                                               | 5.12 us: 1.03x faster                                        |
| logging_simple             | 7.63 us                                                               | 7.45 us: 1.02x faster                                        |
| raytrace                   | 353 ms                                                                | 349 ms: 1.01x faster                                         |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                         |
| asyncio_websockets         | 658 ms                                                                | 664 ms: 1.01x slower                                         |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                         |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                        |
| xml_etree_process          | 79.0 ms                                                               | 80.4 ms: 1.02x slower                                        |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                       |
| thrift                     | 937 us                                                                | 956 us: 1.02x slower                                         |
| json                       | 5.54 ms                                                               | 5.67 ms: 1.02x slower                                        |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                        |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                        |
| scimark_sor                | 150 ms                                                                | 154 ms: 1.03x slower                                         |
| mdp                        | 3.41 sec                                                              | 3.51 sec: 1.03x slower                                       |
| unpickle_pure_python       | 260 us                                                                | 268 us: 1.03x slower                                         |
| unpickle                   | 18.5 us                                                               | 19.0 us: 1.03x slower                                        |
| sqlite_synth               | 3.77 us                                                               | 3.89 us: 1.03x slower                                        |
| json_loads                 | 30.7 us                                                               | 31.7 us: 1.03x slower                                        |
| async_generators           | 491 ms                                                                | 507 ms: 1.03x slower                                         |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.04x slower                                         |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.27 sec: 1.04x slower                                       |
| crypto_pyaes               | 86.6 ms                                                               | 90.8 ms: 1.05x slower                                        |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                        |
| python_startup_no_site     | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                        |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.5 ms: 1.05x slower                                        |
| logging_silent             | 127 ns                                                                | 134 ns: 1.05x slower                                         |
| float                      | 92.1 ms                                                               | 97.2 ms: 1.06x slower                                        |
| unpickle_list              | 6.17 us                                                               | 6.52 us: 1.06x slower                                        |
| regex_effbot               | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                        |
| pickle_pure_python         | 365 us                                                                | 389 us: 1.06x slower                                         |
| scimark_fft                | 418 ms                                                                | 454 ms: 1.09x slower                                         |
| tornado_http               | 136 ms                                                                | 147 ms: 1.09x slower                                         |
| meteor_contest             | 112 ms                                                                | 123 ms: 1.10x slower                                         |
| pyflate                    | 559 ms                                                                | 615 ms: 1.10x slower                                         |
| html5lib                   | 65.1 ms                                                               | 71.8 ms: 1.10x slower                                        |
| deltablue                  | 4.12 ms                                                               | 4.55 ms: 1.10x slower                                        |
| nbody                      | 105 ms                                                                | 116 ms: 1.11x slower                                         |
| asyncio_tcp                | 566 ms                                                                | 630 ms: 1.11x slower                                         |
| regex_v8                   | 28.3 ms                                                               | 31.6 ms: 1.11x slower                                        |
| fannkuch                   | 443 ms                                                                | 503 ms: 1.13x slower                                         |
| telco                      | 8.51 ms                                                               | 9.74 ms: 1.15x slower                                        |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.16 ms: 1.16x slower                                        |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                         |
| sqlglot_parse              | 1.46 ms                                                               | 1.70 ms: 1.16x slower                                        |
| go                         | 157 ms                                                                | 184 ms: 1.17x slower                                         |
| json_dumps                 | 12.3 ms                                                               | 14.4 ms: 1.17x slower                                        |
| spectral_norm              | 131 ms                                                                | 155 ms: 1.18x slower                                         |
| chaos                      | 71.4 ms                                                               | 85.0 ms: 1.19x slower                                        |
| sqlglot_transpile          | 1.83 ms                                                               | 2.20 ms: 1.20x slower                                        |
| typing_runtime_protocols   | 181 us                                                                | 218 us: 1.21x slower                                         |
| docutils                   | 2.98 sec                                                              | 3.61 sec: 1.21x slower                                       |
| pycparser                  | 1.26 sec                                                              | 1.52 sec: 1.21x slower                                       |
| richards_super             | 58.5 ms                                                               | 71.4 ms: 1.22x slower                                        |
| 2to3                       | 308 ms                                                                | 382 ms: 1.24x slower                                         |
| genshi_text                | 27.4 ms                                                               | 34.2 ms: 1.25x slower                                        |
| sqlglot_normalize          | 126 ms                                                                | 157 ms: 1.25x slower                                         |
| dulwich_log                | 62.0 ms                                                               | 77.6 ms: 1.25x slower                                        |
| nqueens                    | 99.2 ms                                                               | 125 ms: 1.26x slower                                         |
| richards                   | 50.9 ms                                                               | 64.2 ms: 1.26x slower                                        |
| sympy_str                  | 280 ms                                                                | 357 ms: 1.28x slower                                         |
| django_template            | 40.7 ms                                                               | 52.4 ms: 1.29x slower                                        |
| python_startup             | 11.4 ms                                                               | 14.7 ms: 1.29x slower                                        |
| regex_compile              | 137 ms                                                                | 179 ms: 1.30x slower                                         |
| sympy_expand               | 454 ms                                                                | 594 ms: 1.31x slower                                         |
| pprint_safe_repr           | 916 ms                                                                | 1.21 sec: 1.32x slower                                       |
| sqlglot_optimize           | 61.3 ms                                                               | 82.2 ms: 1.34x slower                                        |
| pprint_pformat             | 1.88 sec                                                              | 2.55 sec: 1.35x slower                                       |
| generators                 | 43.5 ms                                                               | 59.0 ms: 1.36x slower                                        |
| sympy_integrate            | 21.6 ms                                                               | 29.4 ms: 1.36x slower                                        |
| genshi_xml                 | 60.6 ms                                                               | 84.1 ms: 1.39x slower                                        |
| sympy_sum                  | 154 ms                                                                | 215 ms: 1.39x slower                                         |
| pylint                     | 355 ms                                                                | 494 ms: 1.39x slower                                         |
| gc_traversal               | 4.40 ms                                                               | 6.22 ms: 1.42x slower                                        |
| hexiom                     | 6.98 ms                                                               | 10.3 ms: 1.48x slower                                        |
| create_gc_cycles           | 1.92 ms                                                               | 3.67 ms: 1.91x slower                                        |
| bench_mp_pool              | 7.05 ms                                                               | 1.45 sec: 205.63x slower                                     |
| Geometric mean             | (ref)                                                                 | 1.15x slower                                                 |

Benchmark hidden because not significant (2): coroutines, xml_etree_iterparse
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: bpe_tokeniser, sphinx, unpack_sequence

- Geometric mean (including insignificant results): 1.085x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x