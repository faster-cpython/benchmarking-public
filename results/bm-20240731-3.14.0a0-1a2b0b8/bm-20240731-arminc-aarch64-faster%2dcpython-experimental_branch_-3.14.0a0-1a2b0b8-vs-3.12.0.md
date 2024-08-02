# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-aarch64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.03x faster
- HPT reliability: 90.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 303 ms: 1.02x faster                                                              |
| docutils       | 2.98 sec                                                              | 3.20 sec: 1.07x slower                                                            |
| html5lib       | 65.1 ms                                                               | 68.6 ms: 1.05x slower                                                             |
| tornado_http   | 136 ms                                                                | 128 ms: 1.06x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 436 ms: 1.43x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 404 ms: 1.43x faster                                                              |
| async_tree_memoization     | 777 ms                                                                | 557 ms: 1.39x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 533 ms: 1.39x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 1.12 sec: 1.26x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 726 ms: 1.26x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 1.12 sec: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 713 ms: 1.24x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.33x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                              |
| float          | 92.1 ms                                                               | 93.7 ms: 1.02x slower                                                             |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                              |
| regex_dna      | 254 ms                                                                | 253 ms: 1.01x faster                                                              |
| regex_effbot   | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                             |
| regex_v8       | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                                              |
| unpickle_pure_python | 260 us                                                                | 250 us: 1.04x faster                                                              |
| tomli_loads          | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                            |
| json_loads           | 30.7 us                                                               | 32.6 us: 1.06x slower                                                             |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_iterparse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.91 ms: 1.07x slower                                                             |
| python_startup         | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.11x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 61.6 ms: 1.02x slower                                                             |
| genshi_text     | 27.4 ms                                                               | 27.9 ms: 1.02x slower                                                             |
| django_template | 40.7 ms                                                               | 42.3 ms: 1.04x slower                                                             |
| mako            | 12.9 ms                                                               | 13.5 ms: 1.05x slower                                                             |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 436 ms: 1.43x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 404 ms: 1.43x faster                                                              |
| async_tree_memoization     | 777 ms                                                                | 557 ms: 1.39x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 533 ms: 1.39x faster                                                              |
| deepcopy                   | 446 us                                                                | 329 us: 1.35x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 38.3 us: 1.29x faster                                                             |
| async_tree_io              | 1.41 sec                                                              | 1.12 sec: 1.26x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 726 ms: 1.26x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 1.12 sec: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 713 ms: 1.24x faster                                                              |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                                             |
| generators                 | 43.5 ms                                                               | 35.4 ms: 1.23x faster                                                             |
| raytrace                   | 353 ms                                                                | 296 ms: 1.19x faster                                                              |
| deepcopy_reduce            | 4.10 us                                                               | 3.45 us: 1.19x faster                                                             |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                                             |
| logging_simple             | 7.63 us                                                               | 7.01 us: 1.09x faster                                                             |
| logging_format             | 8.34 us                                                               | 7.70 us: 1.08x faster                                                             |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                              |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.06x faster                                                             |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.06x faster                                                              |
| tornado_http               | 136 ms                                                                | 128 ms: 1.06x faster                                                              |
| deltablue                  | 4.12 ms                                                               | 3.89 ms: 1.06x faster                                                             |
| chaos                      | 71.4 ms                                                               | 67.6 ms: 1.06x faster                                                             |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.05x faster                                                             |
| crypto_pyaes               | 86.6 ms                                                               | 82.3 ms: 1.05x faster                                                             |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.05x faster                                                              |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                                              |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                              |
| unpickle_pure_python       | 260 us                                                                | 250 us: 1.04x faster                                                              |
| dask                       | 376 ms                                                                | 363 ms: 1.04x faster                                                              |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                            |
| sqlglot_parse              | 1.46 ms                                                               | 1.42 ms: 1.03x faster                                                             |
| mdp                        | 3.41 sec                                                              | 3.34 sec: 1.02x faster                                                            |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.4 ms: 1.02x faster                                                             |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                             |
| sympy_integrate            | 21.6 ms                                                               | 21.2 ms: 1.02x faster                                                             |
| 2to3                       | 308 ms                                                                | 303 ms: 1.02x faster                                                              |
| tomli_loads                | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                            |
| async_generators           | 491 ms                                                                | 486 ms: 1.01x faster                                                              |
| regex_dna                  | 254 ms                                                                | 253 ms: 1.01x faster                                                              |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                              |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                                            |
| richards_super             | 58.5 ms                                                               | 59.2 ms: 1.01x slower                                                             |
| sqlglot_normalize          | 126 ms                                                                | 128 ms: 1.02x slower                                                              |
| go                         | 157 ms                                                                | 160 ms: 1.02x slower                                                              |
| genshi_xml                 | 60.6 ms                                                               | 61.6 ms: 1.02x slower                                                             |
| genshi_text                | 27.4 ms                                                               | 27.9 ms: 1.02x slower                                                             |
| float                      | 92.1 ms                                                               | 93.7 ms: 1.02x slower                                                             |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.02x slower                                                              |
| sympy_expand               | 454 ms                                                                | 463 ms: 1.02x slower                                                              |
| logging_silent             | 127 ns                                                                | 130 ns: 1.02x slower                                                              |
| sqlglot_optimize           | 61.3 ms                                                               | 62.6 ms: 1.02x slower                                                             |
| pprint_pformat             | 1.88 sec                                                              | 1.93 sec: 1.02x slower                                                            |
| hexiom                     | 6.98 ms                                                               | 7.18 ms: 1.03x slower                                                             |
| pprint_safe_repr           | 916 ms                                                                | 942 ms: 1.03x slower                                                              |
| json                       | 5.54 ms                                                               | 5.70 ms: 1.03x slower                                                             |
| thrift                     | 937 us                                                                | 965 us: 1.03x slower                                                              |
| pyflate                    | 559 ms                                                                | 580 ms: 1.04x slower                                                              |
| richards                   | 50.9 ms                                                               | 52.9 ms: 1.04x slower                                                             |
| django_template            | 40.7 ms                                                               | 42.3 ms: 1.04x slower                                                             |
| mako                       | 12.9 ms                                                               | 13.5 ms: 1.05x slower                                                             |
| fannkuch                   | 443 ms                                                                | 465 ms: 1.05x slower                                                              |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.50 ms: 1.05x slower                                                             |
| html5lib                   | 65.1 ms                                                               | 68.6 ms: 1.05x slower                                                             |
| regex_effbot               | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                             |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                                              |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.91 ms: 1.07x slower                                                             |
| scimark_fft                | 418 ms                                                                | 448 ms: 1.07x slower                                                              |
| docutils                   | 2.98 sec                                                              | 3.20 sec: 1.07x slower                                                            |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                              |
| regex_v8                   | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                             |
| scimark_sor                | 150 ms                                                                | 162 ms: 1.08x slower                                                              |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                             |
| typing_runtime_protocols   | 181 us                                                                | 199 us: 1.10x slower                                                              |
| gc_traversal               | 4.40 ms                                                               | 4.95 ms: 1.13x slower                                                             |
| coverage                   | 87.3 ms                                                               | 99.3 ms: 1.14x slower                                                             |
| telco                      | 8.51 ms                                                               | 9.77 ms: 1.15x slower                                                             |
| python_startup             | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 2.36 ms: 1.23x slower                                                             |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                                      |

Benchmark hidden because not significant (9): pickle_pure_python, xml_etree_iterparse, bench_mp_pool, asyncio_websockets, asyncio_tcp, nqueens, xml_etree_process, xml_etree_generate, pylint
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240731-3.14.0a0-1a2b0b8/bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json: bpe_tokeniser

# HPT report

- Reliability score: 90.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x