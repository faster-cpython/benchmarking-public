# Results vs. 3.12.0

- fork: python
- ref: c8db0e817e7e0db50153
- machine: linux-aarch64
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.040x faster
- HPT reliability: 94.63%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 295 ms: 1.04x faster                                                    |
| tornado_http   | 136 ms                                                                | 124 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 418 ms: 1.49x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 413 ms: 1.39x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 558 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 549 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 726 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 716 ms: 1.23x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 94.6 ms: 1.03x slower                                                   |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| regex_dna      | 254 ms                                                                | 262 ms: 1.03x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                   |
| regex_effbot   | 4.64 ms                                                               | 5.03 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 254 us: 1.02x faster                                                    |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                                   |
| pickle_list          | 5.25 us                                                               | 5.32 us: 1.01x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 370 us: 1.01x slower                                                    |
| pickle               | 13.4 us                                                               | 13.6 us: 1.02x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| json_loads           | 30.7 us                                                               | 31.3 us: 1.02x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.4 us: 1.05x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.59 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.64 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 28.1 ms: 1.02x slower                                                   |
| mako            | 12.9 ms                                                               | 13.5 ms: 1.05x slower                                                   |
| django_template | 40.7 ms                                                               | 42.6 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 418 ms: 1.49x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 413 ms: 1.39x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 558 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 549 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 333 us: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.6 us: 1.32x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 726 ms: 1.26x faster                                                    |
| generators                 | 43.5 ms                                                               | 34.9 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 716 ms: 1.23x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.23x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.52 us: 1.16x faster                                                   |
| raytrace                   | 353 ms                                                                | 304 ms: 1.16x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.3 ms: 1.15x faster                                                   |
| go                         | 157 ms                                                                | 139 ms: 1.13x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.10x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 133 ms: 1.09x faster                                                    |
| tornado_http               | 136 ms                                                                | 124 ms: 1.09x faster                                                    |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.70 us: 1.08x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.05 us: 1.08x faster                                                   |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 58.8 ms: 1.05x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.74 ms: 1.05x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 82.5 ms: 1.05x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.93 ms: 1.05x faster                                                   |
| 2to3                       | 308 ms                                                                | 295 ms: 1.04x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.0 ms: 1.04x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.31 sec: 1.03x faster                                                  |
| async_generators           | 491 ms                                                                | 477 ms: 1.03x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 254 us: 1.02x faster                                                    |
| chaos                      | 71.4 ms                                                               | 69.7 ms: 1.02x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                  |
| asyncio_tcp                | 566 ms                                                                | 558 ms: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.01x faster                                                   |
| nqueens                    | 99.2 ms                                                               | 99.8 ms: 1.01x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.89 sec: 1.01x slower                                                  |
| sympy_expand               | 454 ms                                                                | 457 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                  |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.32 us: 1.01x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 370 us: 1.01x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.02x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.83 us: 1.02x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| json_loads                 | 30.7 us                                                               | 31.3 us: 1.02x slower                                                   |
| richards_super             | 58.5 ms                                                               | 59.7 ms: 1.02x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 28.1 ms: 1.02x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.14 ms: 1.02x slower                                                   |
| float                      | 92.1 ms                                                               | 94.6 ms: 1.03x slower                                                   |
| logging_silent             | 127 ns                                                                | 130 ns: 1.03x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.64 ms: 1.03x slower                                                   |
| regex_dna                  | 254 ms                                                                | 262 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.41 ms: 1.03x slower                                                   |
| richards                   | 50.9 ms                                                               | 52.7 ms: 1.04x slower                                                   |
| scimark_fft                | 418 ms                                                                | 434 ms: 1.04x slower                                                    |
| fannkuch                   | 443 ms                                                                | 463 ms: 1.04x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.5 ms: 1.05x slower                                                   |
| django_template            | 40.7 ms                                                               | 42.6 ms: 1.05x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.4 us: 1.05x slower                                                   |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.59 us: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.08x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 5.03 ms: 1.08x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.47 ms: 1.11x slower                                                   |
| coverage                   | 87.3 ms                                                               | 98.9 ms: 1.13x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.16 ms: 1.17x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.26 ms: 1.18x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 5.71 sec: 809.26x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (15): thrift, bench_thread_pool, pyflate, xml_etree_iterparse, pprint_safe_repr, html5lib, xml_etree_generate, genshi_xml, json, docutils, asyncio_websockets, meteor_contest, pylint, xml_etree_process, sqlglot_optimize
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.040x faster
# HPT report

- Reliability score: 94.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x