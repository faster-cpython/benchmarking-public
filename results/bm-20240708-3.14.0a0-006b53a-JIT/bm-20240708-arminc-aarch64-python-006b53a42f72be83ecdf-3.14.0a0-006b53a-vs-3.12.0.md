# Results vs. 3.12.0

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: linux-aarch64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.05x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 359 ms: 1.17x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.52 sec: 1.18x slower                                                  |
| html5lib       | 65.1 ms                                                               | 69.6 ms: 1.07x slower                                                   |
| tornado_http   | 136 ms                                                                | 139 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 412 ms: 1.40x faster                                                    |
| async_tree_none            | 624 ms                                                                | 447 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 541 ms: 1.37x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 581 ms: 1.34x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.06 sec: 1.33x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.27x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 712 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 735 ms: 1.24x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.1 ms: 1.03x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 248 ms: 1.02x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                   |
| regex_compile  | 137 ms                                                                | 180 ms: 1.31x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                  |
| unpickle_pure_python | 260 us                                                                | 274 us: 1.05x slower                                                    |
| json_loads           | 30.7 us                                                               | 33.3 us: 1.09x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 412 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.83 ms: 1.06x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| django_template | 40.7 ms                                                               | 50.2 ms: 1.23x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.3 ms: 1.25x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 79.6 ms: 1.31x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 412 ms: 1.40x faster                                                    |
| async_tree_none            | 624 ms                                                                | 447 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 541 ms: 1.37x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 581 ms: 1.34x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.06 sec: 1.33x faster                                                  |
| deepcopy_memo              | 49.6 us                                                               | 38.1 us: 1.30x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.27x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 712 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 735 ms: 1.24x faster                                                    |
| deepcopy                   | 446 us                                                                | 374 us: 1.19x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                                   |
| generators                 | 43.5 ms                                                               | 38.6 ms: 1.13x faster                                                   |
| comprehensions             | 25.4 us                                                               | 23.3 us: 1.09x faster                                                   |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.22 us: 1.06x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.98 us: 1.05x faster                                                   |
| float                      | 92.1 ms                                                               | 89.1 ms: 1.03x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 248 ms: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.44 sec: 1.01x slower                                                  |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 87.5 ms: 1.01x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 29.4 ms: 1.01x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                  |
| async_generators           | 491 ms                                                                | 499 ms: 1.02x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| thrift                     | 937 us                                                                | 958 us: 1.02x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.34 ms: 1.02x slower                                                   |
| tornado_http               | 136 ms                                                                | 139 ms: 1.03x slower                                                    |
| dask                       | 376 ms                                                                | 388 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.03x slower                                                  |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.04x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.2 ms: 1.05x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 274 us: 1.05x slower                                                    |
| richards_super             | 58.5 ms                                                               | 61.6 ms: 1.05x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.83 ms: 1.06x slower                                                   |
| json                       | 5.54 ms                                                               | 5.87 ms: 1.06x slower                                                   |
| richards                   | 50.9 ms                                                               | 54.3 ms: 1.07x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 69.6 ms: 1.07x slower                                                   |
| pyflate                    | 559 ms                                                                | 599 ms: 1.07x slower                                                    |
| logging_silent             | 127 ns                                                                | 136 ns: 1.07x slower                                                    |
| fannkuch                   | 443 ms                                                                | 477 ms: 1.08x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.35 sec: 1.08x slower                                                  |
| regex_v8                   | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.47 ms: 1.08x slower                                                   |
| json_loads                 | 30.7 us                                                               | 33.3 us: 1.09x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.59 ms: 1.09x slower                                                   |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| spectral_norm              | 131 ms                                                                | 144 ms: 1.10x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.01 ms: 1.10x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 624 ms: 1.10x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.89 ms: 1.11x slower                                                   |
| scimark_fft                | 418 ms                                                                | 467 ms: 1.12x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 412 us: 1.13x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 142 ms: 1.13x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.00 ms: 1.14x slower                                                   |
| go                         | 157 ms                                                                | 180 ms: 1.14x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 70.2 ms: 1.14x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 208 us: 1.15x slower                                                    |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 71.9 ms: 1.16x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 8.21 ms: 1.16x slower                                                   |
| 2to3                       | 308 ms                                                                | 359 ms: 1.17x slower                                                    |
| pylint                     | 355 ms                                                                | 416 ms: 1.17x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.52 sec: 1.18x slower                                                  |
| sympy_str                  | 280 ms                                                                | 332 ms: 1.19x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 118 ms: 1.19x slower                                                    |
| scimark_sor                | 150 ms                                                                | 179 ms: 1.20x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.32 ms: 1.21x slower                                                   |
| sympy_expand               | 454 ms                                                                | 550 ms: 1.21x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 26.6 ms: 1.23x slower                                                   |
| django_template            | 40.7 ms                                                               | 50.2 ms: 1.23x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.6 ms: 1.24x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 192 ms: 1.25x slower                                                    |
| chaos                      | 71.4 ms                                                               | 89.3 ms: 1.25x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.15 sec: 1.25x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 34.3 ms: 1.25x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 183 ms: 1.26x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.38 sec: 1.26x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 9.01 ms: 1.29x slower                                                   |
| regex_compile              | 137 ms                                                                | 180 ms: 1.31x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 79.6 ms: 1.31x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, deepcopy_reduce, xml_etree_process, asyncio_websockets, xml_etree_iterparse
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: bpe_tokeniser

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x