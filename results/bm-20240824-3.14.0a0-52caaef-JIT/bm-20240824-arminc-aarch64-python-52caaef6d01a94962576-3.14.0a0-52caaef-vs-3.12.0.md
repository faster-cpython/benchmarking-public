# Results vs. 3.12.0

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.08x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 379 ms: 1.23x slower                                                    |
| docutils       | 2.98 sec                                                              | 4.10 sec: 1.37x slower                                                  |
| html5lib       | 65.1 ms                                                               | 72.5 ms: 1.11x slower                                                   |
| tornado_http   | 136 ms                                                                | 149 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.20x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 457 ms: 1.37x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 425 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 574 ms: 1.35x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 553 ms: 1.34x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 714 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 742 ms: 1.23x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.16 sec: 1.21x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.18x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.4 ms: 1.04x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| regex_compile  | 137 ms                                                                | 190 ms: 1.38x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 147 ms: 1.02x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.02x slower                                                  |
| unpickle_pure_python | 260 us                                                                | 266 us: 1.02x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 382 us: 1.05x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.85 ms: 1.06x slower                                                   |
| python_startup         | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.4 ms: 1.25x slower                                                   |
| django_template | 40.7 ms                                                               | 51.1 ms: 1.26x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 82.0 ms: 1.35x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 457 ms: 1.37x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 425 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 574 ms: 1.35x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 553 ms: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.3 us: 1.33x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 714 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 742 ms: 1.23x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.16 sec: 1.21x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.18x faster                                                  |
| deepcopy                   | 446 us                                                                | 396 us: 1.12x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.78 us: 1.08x faster                                                   |
| float                      | 92.1 ms                                                               | 88.4 ms: 1.04x faster                                                   |
| comprehensions             | 25.4 us                                                               | 24.6 us: 1.03x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 147 ms: 1.02x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.47 us: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 662 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.32 ms: 1.01x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.02x slower                                                  |
| mdp                        | 3.41 sec                                                              | 3.48 sec: 1.02x slower                                                  |
| thrift                     | 937 us                                                                | 955 us: 1.02x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 266 us: 1.02x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 149 ms: 1.02x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 89.0 ms: 1.03x slower                                                   |
| scimark_sor                | 150 ms                                                                | 154 ms: 1.03x slower                                                    |
| async_generators           | 491 ms                                                                | 511 ms: 1.04x slower                                                    |
| json                       | 5.54 ms                                                               | 5.78 ms: 1.04x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 382 us: 1.05x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.29 sec: 1.05x slower                                                  |
| deltablue                  | 4.12 ms                                                               | 4.34 ms: 1.05x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.85 ms: 1.06x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 7.56 ms: 1.07x slower                                                   |
| logging_silent             | 127 ns                                                                | 136 ns: 1.07x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 92.1 ms: 1.08x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.76 ms: 1.09x slower                                                   |
| nbody                      | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| scimark_fft                | 418 ms                                                                | 459 ms: 1.10x slower                                                    |
| tornado_http               | 136 ms                                                                | 149 ms: 1.10x slower                                                    |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.10x slower                                                    |
| pyflate                    | 559 ms                                                                | 622 ms: 1.11x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 72.5 ms: 1.11x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.93 ms: 1.12x slower                                                   |
| spectral_norm              | 131 ms                                                                | 147 ms: 1.12x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 638 ms: 1.13x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.8 ms: 1.13x slower                                                   |
| fannkuch                   | 443 ms                                                                | 502 ms: 1.13x slower                                                    |
| python_startup             | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 209 us: 1.16x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.19 ms: 1.20x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.76 ms: 1.20x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 152 ms: 1.21x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.33 ms: 1.21x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.53 sec: 1.22x slower                                                  |
| 2to3                       | 308 ms                                                                | 379 ms: 1.23x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 124 ms: 1.25x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.7 ms: 1.25x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 34.4 ms: 1.25x slower                                                   |
| django_template            | 40.7 ms                                                               | 51.1 ms: 1.26x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 77.7 ms: 1.27x slower                                                   |
| chaos                      | 71.4 ms                                                               | 90.9 ms: 1.27x slower                                                   |
| sympy_str                  | 280 ms                                                                | 361 ms: 1.29x slower                                                    |
| richards_super             | 58.5 ms                                                               | 77.3 ms: 1.32x slower                                                   |
| generators                 | 43.5 ms                                                               | 57.6 ms: 1.32x slower                                                   |
| richards                   | 50.9 ms                                                               | 67.5 ms: 1.33x slower                                                   |
| sympy_expand               | 454 ms                                                                | 603 ms: 1.33x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 29.0 ms: 1.34x slower                                                   |
| pylint                     | 355 ms                                                                | 480 ms: 1.35x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 82.0 ms: 1.35x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 211 ms: 1.36x slower                                                    |
| docutils                   | 2.98 sec                                                              | 4.10 sec: 1.37x slower                                                  |
| regex_compile              | 137 ms                                                                | 190 ms: 1.38x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.28 sec: 1.40x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.65 sec: 1.41x slower                                                  |
| go                         | 157 ms                                                                | 226 ms: 1.44x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.2 ms: 1.47x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.08x slower                                                            |

Benchmark hidden because not significant (4): logging_format, raytrace, regex_dna, xml_etree_process
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240824-3.14.0a0-52caaef-JIT/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json: bpe_tokeniser

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.01x