# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.078x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 375 ms: 1.22x slower                                             |
| docutils       | 2.98 sec                                                              | 3.67 sec: 1.23x slower                                           |
| html5lib       | 65.1 ms                                                               | 71.1 ms: 1.09x slower                                            |
| tornado_http   | 136 ms                                                                | 146 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                                 | 1.15x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 455 ms: 1.37x faster                                             |
| async_tree_none_tg         | 577 ms                                                                | 422 ms: 1.37x faster                                             |
| async_tree_memoization_tg  | 740 ms                                                                | 544 ms: 1.36x faster                                             |
| async_tree_memoization     | 777 ms                                                                | 582 ms: 1.33x faster                                             |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 718 ms: 1.23x faster                                             |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 757 ms: 1.21x faster                                             |
| async_tree_io_tg           | 1.40 sec                                                              | 1.19 sec: 1.18x faster                                           |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                           |
| Geometric mean             | (ref)                                                                 | 1.28x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 236 ms: 1.01x slower                                             |
| float          | 92.1 ms                                                               | 93.8 ms: 1.02x slower                                            |
| nbody          | 105 ms                                                                | 110 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                             |
| regex_effbot   | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                            |
| regex_v8       | 28.3 ms                                                               | 31.5 ms: 1.11x slower                                            |
| regex_compile  | 137 ms                                                                | 176 ms: 1.29x slower                                             |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                             |
| pickle_list          | 5.25 us                                                               | 5.21 us: 1.01x faster                                            |
| json_loads           | 30.7 us                                                               | 31.2 us: 1.02x slower                                            |
| xml_etree_process    | 79.0 ms                                                               | 80.5 ms: 1.02x slower                                            |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                           |
| pickle_dict          | 37.3 us                                                               | 38.2 us: 1.02x slower                                            |
| unpickle_pure_python | 260 us                                                                | 267 us: 1.03x slower                                             |
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                            |
| unpickle             | 18.5 us                                                               | 19.2 us: 1.04x slower                                            |
| pickle_pure_python   | 365 us                                                                | 388 us: 1.06x slower                                             |
| unpickle_list        | 6.17 us                                                               | 6.60 us: 1.07x slower                                            |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                            |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                     |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.76 ms: 1.05x slower                                            |
| python_startup         | 11.4 ms                                                               | 14.7 ms: 1.30x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 12.9 ms: 1.00x slower                                            |
| genshi_text     | 27.4 ms                                                               | 35.0 ms: 1.28x slower                                            |
| django_template | 40.7 ms                                                               | 52.3 ms: 1.29x slower                                            |
| genshi_xml      | 60.6 ms                                                               | 85.1 ms: 1.40x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 455 ms: 1.37x faster                                             |
| async_tree_none_tg         | 577 ms                                                                | 422 ms: 1.37x faster                                             |
| async_tree_memoization_tg  | 740 ms                                                                | 544 ms: 1.36x faster                                             |
| async_tree_memoization     | 777 ms                                                                | 582 ms: 1.33x faster                                             |
| deepcopy_memo              | 49.6 us                                                               | 37.7 us: 1.32x faster                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 718 ms: 1.23x faster                                             |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 757 ms: 1.21x faster                                             |
| async_tree_io_tg           | 1.40 sec                                                              | 1.19 sec: 1.18x faster                                           |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                           |
| pathlib                    | 24.5 ms                                                               | 21.6 ms: 1.14x faster                                            |
| deepcopy                   | 446 us                                                                | 397 us: 1.12x faster                                             |
| deepcopy_reduce            | 4.10 us                                                               | 3.83 us: 1.07x faster                                            |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                             |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                             |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                            |
| comprehensions             | 25.4 us                                                               | 24.9 us: 1.02x faster                                            |
| raytrace                   | 353 ms                                                                | 347 ms: 1.02x faster                                             |
| logging_format             | 8.34 us                                                               | 8.22 us: 1.01x faster                                            |
| pickle_list                | 5.25 us                                                               | 5.21 us: 1.01x faster                                            |
| mako                       | 12.9 ms                                                               | 12.9 ms: 1.00x slower                                            |
| asyncio_websockets         | 658 ms                                                                | 663 ms: 1.01x slower                                             |
| pidigits                   | 233 ms                                                                | 236 ms: 1.01x slower                                             |
| scimark_sor                | 150 ms                                                                | 152 ms: 1.02x slower                                             |
| sqlite_synth               | 3.77 us                                                               | 3.83 us: 1.02x slower                                            |
| json_loads                 | 30.7 us                                                               | 31.2 us: 1.02x slower                                            |
| float                      | 92.1 ms                                                               | 93.8 ms: 1.02x slower                                            |
| xml_etree_process          | 79.0 ms                                                               | 80.5 ms: 1.02x slower                                            |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                           |
| pickle_dict                | 37.3 us                                                               | 38.2 us: 1.02x slower                                            |
| crypto_pyaes               | 86.6 ms                                                               | 88.5 ms: 1.02x slower                                            |
| thrift                     | 937 us                                                                | 958 us: 1.02x slower                                             |
| scimark_lu                 | 146 ms                                                                | 149 ms: 1.02x slower                                             |
| mdp                        | 3.41 sec                                                              | 3.49 sec: 1.02x slower                                           |
| unpickle_pure_python       | 260 us                                                                | 267 us: 1.03x slower                                             |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                            |
| async_generators           | 491 ms                                                                | 510 ms: 1.04x slower                                             |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.28 sec: 1.04x slower                                           |
| unpickle                   | 18.5 us                                                               | 19.2 us: 1.04x slower                                            |
| python_startup_no_site     | 8.37 ms                                                               | 8.76 ms: 1.05x slower                                            |
| nbody                      | 105 ms                                                                | 110 ms: 1.05x slower                                             |
| regex_effbot               | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                            |
| scimark_fft                | 418 ms                                                                | 443 ms: 1.06x slower                                             |
| pickle_pure_python         | 365 us                                                                | 388 us: 1.06x slower                                             |
| logging_silent             | 127 ns                                                                | 135 ns: 1.07x slower                                             |
| scimark_monte_carlo        | 85.1 ms                                                               | 90.9 ms: 1.07x slower                                            |
| unpickle_list              | 6.17 us                                                               | 6.60 us: 1.07x slower                                            |
| bench_thread_pool          | 1.31 ms                                                               | 1.40 ms: 1.07x slower                                            |
| tornado_http               | 136 ms                                                                | 146 ms: 1.08x slower                                             |
| deltablue                  | 4.12 ms                                                               | 4.47 ms: 1.08x slower                                            |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                            |
| html5lib                   | 65.1 ms                                                               | 71.1 ms: 1.09x slower                                            |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.80 ms: 1.10x slower                                            |
| asyncio_tcp                | 566 ms                                                                | 623 ms: 1.10x slower                                             |
| pyflate                    | 559 ms                                                                | 621 ms: 1.11x slower                                             |
| regex_v8                   | 28.3 ms                                                               | 31.5 ms: 1.11x slower                                            |
| meteor_contest             | 112 ms                                                                | 125 ms: 1.11x slower                                             |
| telco                      | 8.51 ms                                                               | 9.53 ms: 1.12x slower                                            |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                             |
| sqlglot_parse              | 1.46 ms                                                               | 1.69 ms: 1.15x slower                                            |
| spectral_norm              | 131 ms                                                                | 152 ms: 1.16x slower                                             |
| fannkuch                   | 443 ms                                                                | 519 ms: 1.17x slower                                             |
| pycparser                  | 1.26 sec                                                              | 1.48 sec: 1.18x slower                                           |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                             |
| go                         | 157 ms                                                                | 189 ms: 1.20x slower                                             |
| sqlglot_transpile          | 1.83 ms                                                               | 2.20 ms: 1.20x slower                                            |
| chaos                      | 71.4 ms                                                               | 86.0 ms: 1.21x slower                                            |
| 2to3                       | 308 ms                                                                | 375 ms: 1.22x slower                                             |
| nqueens                    | 99.2 ms                                                               | 121 ms: 1.22x slower                                             |
| sqlglot_normalize          | 126 ms                                                                | 154 ms: 1.23x slower                                             |
| docutils                   | 2.98 sec                                                              | 3.67 sec: 1.23x slower                                           |
| dulwich_log                | 62.0 ms                                                               | 77.3 ms: 1.25x slower                                            |
| sympy_str                  | 280 ms                                                                | 355 ms: 1.27x slower                                             |
| genshi_text                | 27.4 ms                                                               | 35.0 ms: 1.28x slower                                            |
| django_template            | 40.7 ms                                                               | 52.3 ms: 1.29x slower                                            |
| regex_compile              | 137 ms                                                                | 176 ms: 1.29x slower                                             |
| sqlglot_optimize           | 61.3 ms                                                               | 79.2 ms: 1.29x slower                                            |
| python_startup             | 11.4 ms                                                               | 14.7 ms: 1.30x slower                                            |
| richards_super             | 58.5 ms                                                               | 76.3 ms: 1.31x slower                                            |
| sympy_expand               | 454 ms                                                                | 593 ms: 1.31x slower                                             |
| pprint_safe_repr           | 916 ms                                                                | 1.22 sec: 1.33x slower                                           |
| sympy_integrate            | 21.6 ms                                                               | 28.9 ms: 1.34x slower                                            |
| richards                   | 50.9 ms                                                               | 68.8 ms: 1.35x slower                                            |
| sympy_sum                  | 154 ms                                                                | 210 ms: 1.36x slower                                             |
| pylint                     | 355 ms                                                                | 483 ms: 1.36x slower                                             |
| generators                 | 43.5 ms                                                               | 59.3 ms: 1.36x slower                                            |
| pprint_pformat             | 1.88 sec                                                              | 2.60 sec: 1.38x slower                                           |
| gc_traversal               | 4.40 ms                                                               | 6.17 ms: 1.40x slower                                            |
| genshi_xml                 | 60.6 ms                                                               | 85.1 ms: 1.40x slower                                            |
| hexiom                     | 6.98 ms                                                               | 10.4 ms: 1.49x slower                                            |
| create_gc_cycles           | 1.92 ms                                                               | 3.58 ms: 1.87x slower                                            |
| bench_mp_pool              | 7.05 ms                                                               | 3.29 sec: 465.90x slower                                         |
| Geometric mean             | (ref)                                                                 | 1.16x slower                                                     |

Benchmark hidden because not significant (4): logging_simple, json, xml_etree_generate, xml_etree_iterparse
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93.json: bpe_tokeniser, sphinx, unpack_sequence

- Geometric mean (including insignificant results): 1.078x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.11x