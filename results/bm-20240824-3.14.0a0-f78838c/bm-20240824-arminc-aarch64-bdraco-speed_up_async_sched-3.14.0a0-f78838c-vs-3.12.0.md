# Results vs. 3.12.0

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-aarch64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.03x faster
- HPT reliability: 91.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 293 ms: 1.05x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| tornado_http   | 136 ms                                                                | 126 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 426 ms: 1.47x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 541 ms: 1.37x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 423 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 575 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 733 ms: 1.24x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.14 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 732 ms: 1.21x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.1 ms: 1.01x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 110 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.85 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 31.2 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 365 us                                                                | 355 us: 1.03x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 253 us: 1.03x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 191 ms: 1.02x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| json_dumps           | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.81 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.8 ms: 1.01x slower                                                   |
| django_template | 40.7 ms                                                               | 42.1 ms: 1.04x slower                                                   |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 426 ms: 1.47x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 541 ms: 1.37x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 423 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 575 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 338 us: 1.32x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.9 us: 1.31x faster                                                   |
| generators                 | 43.5 ms                                                               | 34.8 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 733 ms: 1.24x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.14 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 732 ms: 1.21x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                                  |
| raytrace                   | 353 ms                                                                | 302 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.53 us: 1.16x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.2 ms: 1.16x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                    |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 135 ms: 1.08x faster                                                    |
| tornado_http               | 136 ms                                                                | 126 ms: 1.07x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.79 us: 1.07x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.13 us: 1.07x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.06x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.89 ms: 1.06x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 81.7 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.05x faster                                                   |
| 2to3                       | 308 ms                                                                | 293 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                                    |
| chaos                      | 71.4 ms                                                               | 68.6 ms: 1.04x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.9 ms: 1.04x faster                                                   |
| pickle_pure_python         | 365 us                                                                | 355 us: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| unpickle_pure_python       | 260 us                                                                | 253 us: 1.03x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 191 ms: 1.02x faster                                                    |
| thrift                     | 937 us                                                                | 918 us: 1.02x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.36 sec: 1.01x faster                                                  |
| float                      | 92.1 ms                                                               | 91.1 ms: 1.01x faster                                                   |
| asyncio_websockets         | 658 ms                                                                | 661 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 924 ms: 1.01x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 27.8 ms: 1.01x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.91 sec: 1.02x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 7.11 ms: 1.02x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| sympy_expand               | 454 ms                                                                | 463 ms: 1.02x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 62.9 ms: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.24 sec: 1.03x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 582 ms: 1.03x slower                                                    |
| richards_super             | 58.5 ms                                                               | 60.2 ms: 1.03x slower                                                   |
| django_template            | 40.7 ms                                                               | 42.1 ms: 1.04x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.44 ms: 1.04x slower                                                   |
| fannkuch                   | 443 ms                                                                | 462 ms: 1.04x slower                                                    |
| json                       | 5.54 ms                                                               | 5.79 ms: 1.04x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.85 ms: 1.05x slower                                                   |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                    |
| nbody                      | 105 ms                                                                | 110 ms: 1.05x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.81 ms: 1.05x slower                                                   |
| richards                   | 50.9 ms                                                               | 53.9 ms: 1.06x slower                                                   |
| pyflate                    | 559 ms                                                                | 593 ms: 1.06x slower                                                    |
| scimark_fft                | 418 ms                                                                | 444 ms: 1.06x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 195 us: 1.08x slower                                                    |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.2 ms: 1.10x slower                                                   |
| coverage                   | 87.3 ms                                                               | 98.3 ms: 1.13x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.96 ms: 1.13x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.0 ms: 1.18x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.29 ms: 1.20x slower                                                   |
| go                         | 157 ms                                                                | 191 ms: 1.22x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (11): sqlglot_parse, coroutines, nqueens, html5lib, genshi_xml, xml_etree_generate, meteor_contest, async_generators, pylint, bench_mp_pool, xml_etree_process
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240824-3.14.0a0-f78838c/bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json: bpe_tokeniser

# HPT report

- Reliability score: 91.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x