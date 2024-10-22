# Results vs. 3.12.0

- fork: python
- ref: d27a53fc02a87e76066f
- machine: linux-aarch64
- commit hash: d27a53f
- commit date: 2024-07-30
- overall geometric mean: 1.04x faster
- HPT reliability: 97.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 302 ms: 1.02x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.16 sec: 1.06x slower                                                  |
| html5lib       | 65.1 ms                                                               | 67.8 ms: 1.04x slower                                                   |
| tornado_http   | 136 ms                                                                | 124 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 438 ms: 1.42x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 406 ms: 1.42x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 555 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 538 ms: 1.38x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.09 sec: 1.29x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 727 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 706 ms: 1.25x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.12 sec: 1.25x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.33x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 109 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| regex_dna      | 254 ms                                                                | 255 ms: 1.00x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                                   |
| regex_effbot   | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 185 ms: 1.05x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 251 us: 1.04x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.52 sec: 1.03x faster                                                  |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| json_loads           | 30.7 us                                                               | 33.2 us: 1.08x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.80 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 42.0 ms: 1.03x slower                                                   |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 438 ms: 1.42x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 406 ms: 1.42x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 555 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 538 ms: 1.38x faster                                                    |
| deepcopy                   | 446 us                                                                | 328 us: 1.36x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.6 us: 1.32x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.09 sec: 1.29x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 727 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 706 ms: 1.25x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.12 sec: 1.25x faster                                                  |
| generators                 | 43.5 ms                                                               | 34.8 ms: 1.25x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.23x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.34 us: 1.23x faster                                                   |
| raytrace                   | 353 ms                                                                | 294 ms: 1.20x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                                   |
| tornado_http               | 136 ms                                                                | 124 ms: 1.09x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.04 us: 1.08x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.80 ms: 1.08x faster                                                   |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.75 us: 1.08x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.06x faster                                                   |
| chaos                      | 71.4 ms                                                               | 67.0 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.4 ms: 1.06x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.39 ms: 1.06x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 82.1 ms: 1.06x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 185 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 251 us: 1.04x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.1 ms: 1.03x faster                                                   |
| dask                       | 376 ms                                                                | 365 ms: 1.03x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.52 sec: 1.03x faster                                                  |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.02x faster                                                  |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| 2to3                       | 308 ms                                                                | 302 ms: 1.02x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 558 ms: 1.02x faster                                                    |
| async_generators           | 491 ms                                                                | 484 ms: 1.01x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| regex_dna                  | 254 ms                                                                | 255 ms: 1.00x slower                                                    |
| pyflate                    | 559 ms                                                                | 562 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| sympy_expand               | 454 ms                                                                | 457 ms: 1.01x slower                                                    |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.01x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 62.3 ms: 1.02x slower                                                   |
| logging_silent             | 127 ns                                                                | 129 ns: 1.02x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.10 ms: 1.02x slower                                                   |
| go                         | 157 ms                                                                | 160 ms: 1.02x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.94 sec: 1.03x slower                                                  |
| django_template            | 40.7 ms                                                               | 42.0 ms: 1.03x slower                                                   |
| richards                   | 50.9 ms                                                               | 52.7 ms: 1.03x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 948 ms: 1.04x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| fannkuch                   | 443 ms                                                                | 460 ms: 1.04x slower                                                    |
| json                       | 5.54 ms                                                               | 5.76 ms: 1.04x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.44 ms: 1.04x slower                                                   |
| thrift                     | 937 us                                                                | 974 us: 1.04x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 67.8 ms: 1.04x slower                                                   |
| nbody                      | 105 ms                                                                | 109 ms: 1.04x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.80 ms: 1.05x slower                                                   |
| scimark_fft                | 418 ms                                                                | 441 ms: 1.05x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.16 sec: 1.06x slower                                                  |
| regex_effbot               | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                   |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.2 us: 1.08x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 196 us: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.10x slower                                                   |
| coverage                   | 87.3 ms                                                               | 98.2 ms: 1.13x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.06 ms: 1.15x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.84 ms: 1.16x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.34 ms: 1.22x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                            |

Benchmark hidden because not significant (12): bench_mp_pool, float, asyncio_websockets, pickle_pure_python, xml_etree_process, genshi_text, asyncio_tcp_ssl, richards_super, nqueens, genshi_xml, pylint, sqlglot_normalize
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240730-3.14.0a0-d27a53f/bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f.json: bpe_tokeniser

# HPT report

- Reliability score: 97.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.94x