# Results vs. 3.12.0

- fork: python
- ref: 42b2c9d78da7ebd6bd59
- machine: linux-aarch64
- commit hash: 42b2c9d
- commit date: 2024-06-25
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 358 ms: 1.16x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.53 sec: 1.18x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.8 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 410 ms: 1.41x faster                                                    |
| async_tree_none            | 624 ms                                                                | 448 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 547 ms: 1.35x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 586 ms: 1.32x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 748 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 729 ms: 1.21x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.0 ms: 1.03x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 262 ms: 1.03x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 30.2 ms: 1.06x slower                                                   |
| regex_effbot   | 4.64 ms                                                               | 4.97 ms: 1.07x slower                                                   |
| regex_compile  | 137 ms                                                                | 173 ms: 1.26x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| pickle_list          | 5.25 us                                                               | 5.29 us: 1.01x slower                                                   |
| pickle_dict          | 37.3 us                                                               | 37.7 us: 1.01x slower                                                   |
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.67 sec: 1.03x slower                                                  |
| unpickle_pure_python | 260 us                                                                | 277 us: 1.07x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 393 us: 1.08x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.65 us: 1.08x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.9 us: 1.08x slower                                                   |
| json_loads           | 30.7 us                                                               | 33.3 us: 1.08x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 11.1 ms: 1.33x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.6 ms: 1.37x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.35x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                   |
| django_template | 40.7 ms                                                               | 50.2 ms: 1.24x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.9 ms: 1.27x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 82.5 ms: 1.36x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.22x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 410 ms: 1.41x faster                                                    |
| async_tree_none            | 624 ms                                                                | 448 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 547 ms: 1.35x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 586 ms: 1.32x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.26x faster                                                  |
| deepcopy_memo              | 49.6 us                                                               | 39.7 us: 1.25x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 748 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 729 ms: 1.21x faster                                                    |
| deepcopy                   | 446 us                                                                | 377 us: 1.18x faster                                                    |
| generators                 | 43.5 ms                                                               | 38.8 ms: 1.12x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.1 ms: 1.11x faster                                                   |
| comprehensions             | 25.4 us                                                               | 23.3 us: 1.09x faster                                                   |
| raytrace                   | 353 ms                                                                | 324 ms: 1.09x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.22 us: 1.06x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.92 us: 1.05x faster                                                   |
| float                      | 92.1 ms                                                               | 89.0 ms: 1.03x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 662 ms: 1.01x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.29 us: 1.01x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 37.7 us: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.32 ms: 1.01x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.49 sec: 1.02x slower                                                  |
| sqlite_synth               | 3.77 us                                                               | 3.85 us: 1.02x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 29.7 ms: 1.02x slower                                                   |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.67 sec: 1.03x slower                                                  |
| regex_dna                  | 254 ms                                                                | 262 ms: 1.03x slower                                                    |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.03x slower                                                    |
| dask                       | 376 ms                                                                | 390 ms: 1.04x slower                                                    |
| thrift                     | 937 us                                                                | 970 us: 1.04x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.27 sec: 1.04x slower                                                  |
| async_generators           | 491 ms                                                                | 517 ms: 1.05x slower                                                    |
| json                       | 5.54 ms                                                               | 5.87 ms: 1.06x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.2 ms: 1.06x slower                                                   |
| fannkuch                   | 443 ms                                                                | 472 ms: 1.06x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 277 us: 1.07x slower                                                    |
| richards_super             | 58.5 ms                                                               | 62.3 ms: 1.07x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.97 ms: 1.07x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.57 ms: 1.08x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 393 us: 1.08x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.65 us: 1.08x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.44 ms: 1.08x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.9 us: 1.08x slower                                                   |
| richards                   | 50.9 ms                                                               | 55.1 ms: 1.08x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                  |
| json_loads                 | 30.7 us                                                               | 33.3 us: 1.08x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.00 ms: 1.09x slower                                                   |
| pyflate                    | 559 ms                                                                | 613 ms: 1.10x slower                                                    |
| logging_silent             | 127 ns                                                                | 139 ns: 1.10x slower                                                    |
| nbody                      | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| scimark_fft                | 418 ms                                                                | 460 ms: 1.10x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 622 ms: 1.10x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.8 ms: 1.10x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.87 ms: 1.11x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 7.93 ms: 1.12x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 70.0 ms: 1.13x slower                                                   |
| go                         | 157 ms                                                                | 178 ms: 1.14x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 143 ms: 1.14x slower                                                    |
| sympy_str                  | 280 ms                                                                | 319 ms: 1.14x slower                                                    |
| spectral_norm              | 131 ms                                                                | 149 ms: 1.14x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 69.9 ms: 1.14x slower                                                   |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 179 ms: 1.16x slower                                                    |
| 2to3                       | 308 ms                                                                | 358 ms: 1.16x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.11 ms: 1.16x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 212 us: 1.17x slower                                                    |
| scimark_sor                | 150 ms                                                                | 176 ms: 1.18x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 117 ms: 1.18x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.53 sec: 1.18x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 25.6 ms: 1.18x slower                                                   |
| pylint                     | 355 ms                                                                | 424 ms: 1.19x slower                                                    |
| sympy_expand               | 454 ms                                                                | 542 ms: 1.20x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.12 sec: 1.22x slower                                                  |
| chaos                      | 71.4 ms                                                               | 87.6 ms: 1.23x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.31 sec: 1.23x slower                                                  |
| django_template            | 40.7 ms                                                               | 50.2 ms: 1.24x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.5 ms: 1.24x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.39 ms: 1.24x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 182 ms: 1.25x slower                                                    |
| regex_compile              | 137 ms                                                                | 173 ms: 1.26x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 34.9 ms: 1.27x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 8.91 ms: 1.28x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 11.1 ms: 1.33x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 82.5 ms: 1.36x slower                                                   |
| python_startup             | 11.4 ms                                                               | 15.6 ms: 1.37x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (7): xml_etree_parse, crypto_pyaes, xml_etree_generate, scimark_monte_carlo, deepcopy_reduce, xml_etree_process, tornado_http
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240625-3.14.0a0-42b2c9d-JIT/bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.01x