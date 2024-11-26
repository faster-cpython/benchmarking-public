# Results vs. 3.12.0

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: linux-aarch64
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.041x faster
- HPT reliability: 99.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 295 ms: 1.05x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.02 sec: 1.01x slower                                                  |
| tornado_http   | 136 ms                                                                | 127 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 425 ms: 1.47x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 560 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 422 ms: 1.37x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 553 ms: 1.34x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 725 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 729 ms: 1.21x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.21x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 110 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 185 ms: 1.05x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 254 us: 1.02x faster                                                    |
| pickle_list          | 5.25 us                                                               | 5.23 us: 1.00x faster                                                   |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                  |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| json_loads           | 30.7 us                                                               | 31.7 us: 1.03x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.38 us: 1.03x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.4 us: 1.05x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.58 ms: 1.02x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.08x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 41.4 ms: 1.02x slower                                                   |
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 425 ms: 1.47x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 560 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 422 ms: 1.37x faster                                                    |
| deepcopy                   | 446 us                                                                | 331 us: 1.35x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 553 ms: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.6 us: 1.32x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 725 ms: 1.26x faster                                                    |
| generators                 | 43.5 ms                                                               | 34.7 ms: 1.25x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.3 us: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 729 ms: 1.21x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.21x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 20.9 ms: 1.17x faster                                                   |
| raytrace                   | 353 ms                                                                | 302 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.54 us: 1.16x faster                                                   |
| go                         | 157 ms                                                                | 138 ms: 1.14x faster                                                    |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.69 us: 1.08x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.06 us: 1.08x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 57.7 ms: 1.08x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.07x faster                                                   |
| tornado_http               | 136 ms                                                                | 127 ms: 1.06x faster                                                    |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 81.8 ms: 1.06x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.89 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 185 ms: 1.05x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.6 ms: 1.05x faster                                                   |
| 2to3                       | 308 ms                                                                | 295 ms: 1.05x faster                                                    |
| chaos                      | 71.4 ms                                                               | 68.7 ms: 1.04x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.21 sec: 1.04x faster                                                  |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.1 ms: 1.04x faster                                                   |
| asyncio_tcp                | 566 ms                                                                | 551 ms: 1.03x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 254 us: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.4 ms: 1.02x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.34 sec: 1.02x faster                                                  |
| thrift                     | 937 us                                                                | 924 us: 1.01x faster                                                    |
| pprint_safe_repr           | 916 ms                                                                | 911 ms: 1.01x faster                                                    |
| pickle_list                | 5.25 us                                                               | 5.23 us: 1.00x faster                                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 663 ms: 1.01x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 100 ms: 1.01x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.02 sec: 1.01x slower                                                  |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                  |
| django_template            | 40.7 ms                                                               | 41.4 ms: 1.02x slower                                                   |
| sympy_expand               | 454 ms                                                                | 462 ms: 1.02x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.10 ms: 1.02x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 62.5 ms: 1.02x slower                                                   |
| richards_super             | 58.5 ms                                                               | 59.6 ms: 1.02x slower                                                   |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.58 ms: 1.02x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| json_loads                 | 30.7 us                                                               | 31.7 us: 1.03x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.38 us: 1.03x slower                                                   |
| fannkuch                   | 443 ms                                                                | 459 ms: 1.04x slower                                                    |
| richards                   | 50.9 ms                                                               | 52.9 ms: 1.04x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.93 us: 1.04x slower                                                   |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.49 ms: 1.05x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.4 us: 1.05x slower                                                   |
| nbody                      | 105 ms                                                                | 110 ms: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 192 us: 1.07x slower                                                    |
| spectral_norm              | 131 ms                                                                | 143 ms: 1.09x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| coverage                   | 87.3 ms                                                               | 97.7 ms: 1.12x slower                                                   |
| scimark_fft                | 418 ms                                                                | 471 ms: 1.13x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.12 ms: 1.16x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.28 ms: 1.19x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.2 ms: 1.20x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (15): genshi_text, async_generators, bench_mp_pool, pyflate, float, pprint_pformat, xml_etree_process, json, meteor_contest, genshi_xml, xml_etree_generate, sqlglot_normalize, pickle_pure_python, html5lib, pylint
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240911-3.14.0a0-5436d8b/bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.041x faster
# HPT report

- Reliability score: 99.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x