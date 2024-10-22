# Results vs. 3.12.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-aarch64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.04x slower
- HPT reliability: 99.15%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 296 ms: 1.04x faster                                             |
| docutils       | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                           |
| html5lib       | 65.1 ms                                                               | 63.1 ms: 1.03x faster                                            |
| tornado_http   | 136 ms                                                                | 126 ms: 1.08x faster                                             |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 429 ms: 1.45x faster                                             |
| async_tree_memoization     | 777 ms                                                                | 553 ms: 1.40x faster                                             |
| async_tree_none_tg         | 577 ms                                                                | 421 ms: 1.37x faster                                             |
| async_tree_memoization_tg  | 740 ms                                                                | 550 ms: 1.35x faster                                             |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 714 ms: 1.28x faster                                             |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 705 ms: 1.25x faster                                             |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.20x faster                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                           |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                             |
| float          | 92.1 ms                                                               | 94.4 ms: 1.03x slower                                            |
| nbody          | 105 ms                                                                | 110 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 125 ms: 1.09x faster                                             |
| regex_effbot   | 4.64 ms                                                               | 4.99 ms: 1.08x slower                                            |
| regex_v8       | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                            |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 255 us: 1.02x faster                                             |
| xml_etree_parse      | 195 ms                                                                | 193 ms: 1.01x faster                                             |
| json_loads           | 30.7 us                                                               | 31.1 us: 1.01x slower                                            |
| pickle_dict          | 37.3 us                                                               | 38.1 us: 1.02x slower                                            |
| tomli_loads          | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                           |
| pickle               | 13.4 us                                                               | 13.9 us: 1.03x slower                                            |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.06x slower                                            |
| unpickle_list        | 6.17 us                                                               | 6.64 us: 1.08x slower                                            |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                            |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                     |

Benchmark hidden because not significant (5): pickle_list, pickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                            |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                            |
| django_template | 40.7 ms                                                               | 42.1 ms: 1.04x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                     |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 429 ms: 1.45x faster                                             |
| async_tree_memoization     | 777 ms                                                                | 553 ms: 1.40x faster                                             |
| async_tree_none_tg         | 577 ms                                                                | 421 ms: 1.37x faster                                             |
| deepcopy                   | 446 us                                                                | 331 us: 1.35x faster                                             |
| async_tree_memoization_tg  | 740 ms                                                                | 550 ms: 1.35x faster                                             |
| deepcopy_memo              | 49.6 us                                                               | 37.9 us: 1.31x faster                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 714 ms: 1.28x faster                                             |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 705 ms: 1.25x faster                                             |
| comprehensions             | 25.4 us                                                               | 20.5 us: 1.24x faster                                            |
| generators                 | 43.5 ms                                                               | 35.2 ms: 1.24x faster                                            |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.20x faster                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                           |
| deepcopy_reduce            | 4.10 us                                                               | 3.45 us: 1.19x faster                                            |
| raytrace                   | 353 ms                                                                | 304 ms: 1.16x faster                                             |
| pathlib                    | 24.5 ms                                                               | 21.5 ms: 1.14x faster                                            |
| go                         | 157 ms                                                                | 138 ms: 1.14x faster                                             |
| scimark_lu                 | 146 ms                                                                | 132 ms: 1.11x faster                                             |
| sympy_sum                  | 154 ms                                                                | 140 ms: 1.10x faster                                             |
| regex_compile              | 137 ms                                                                | 125 ms: 1.09x faster                                             |
| tornado_http               | 136 ms                                                                | 126 ms: 1.08x faster                                             |
| logging_simple             | 7.63 us                                                               | 7.11 us: 1.07x faster                                            |
| logging_format             | 8.34 us                                                               | 7.81 us: 1.07x faster                                            |
| dulwich_log                | 62.0 ms                                                               | 58.6 ms: 1.06x faster                                            |
| crypto_pyaes               | 86.6 ms                                                               | 82.0 ms: 1.06x faster                                            |
| sympy_str                  | 280 ms                                                                | 265 ms: 1.05x faster                                             |
| deltablue                  | 4.12 ms                                                               | 3.93 ms: 1.05x faster                                            |
| sqlglot_transpile          | 1.83 ms                                                               | 1.74 ms: 1.05x faster                                            |
| 2to3                       | 308 ms                                                                | 296 ms: 1.04x faster                                             |
| async_generators           | 491 ms                                                                | 475 ms: 1.03x faster                                             |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.4 ms: 1.03x faster                                            |
| html5lib                   | 65.1 ms                                                               | 63.1 ms: 1.03x faster                                            |
| bench_thread_pool          | 1.31 ms                                                               | 1.27 ms: 1.03x faster                                            |
| sqlglot_parse              | 1.46 ms                                                               | 1.43 ms: 1.03x faster                                            |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.02x faster                                            |
| chaos                      | 71.4 ms                                                               | 69.7 ms: 1.02x faster                                            |
| mdp                        | 3.41 sec                                                              | 3.34 sec: 1.02x faster                                           |
| unpickle_pure_python       | 260 us                                                                | 255 us: 1.02x faster                                             |
| pprint_safe_repr           | 916 ms                                                                | 904 ms: 1.01x faster                                             |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.01x faster                                           |
| pprint_pformat             | 1.88 sec                                                              | 1.86 sec: 1.01x faster                                           |
| xml_etree_parse            | 195 ms                                                                | 193 ms: 1.01x faster                                             |
| meteor_contest             | 112 ms                                                                | 111 ms: 1.01x faster                                             |
| nqueens                    | 99.2 ms                                                               | 98.5 ms: 1.01x faster                                            |
| json                       | 5.54 ms                                                               | 5.50 ms: 1.01x faster                                            |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                             |
| hexiom                     | 6.98 ms                                                               | 7.03 ms: 1.01x slower                                            |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                             |
| docutils                   | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                           |
| sqlglot_optimize           | 61.3 ms                                                               | 62.0 ms: 1.01x slower                                            |
| sympy_expand               | 454 ms                                                                | 459 ms: 1.01x slower                                             |
| json_loads                 | 30.7 us                                                               | 31.1 us: 1.01x slower                                            |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.22 sec: 1.02x slower                                           |
| sqlite_synth               | 3.77 us                                                               | 3.83 us: 1.02x slower                                            |
| scimark_fft                | 418 ms                                                                | 426 ms: 1.02x slower                                             |
| richards_super             | 58.5 ms                                                               | 59.6 ms: 1.02x slower                                            |
| pickle_dict                | 37.3 us                                                               | 38.1 us: 1.02x slower                                            |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                           |
| float                      | 92.1 ms                                                               | 94.4 ms: 1.03x slower                                            |
| thrift                     | 937 us                                                                | 962 us: 1.03x slower                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.39 ms: 1.03x slower                                            |
| pickle                     | 13.4 us                                                               | 13.9 us: 1.03x slower                                            |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                            |
| richards                   | 50.9 ms                                                               | 52.7 ms: 1.04x slower                                            |
| django_template            | 40.7 ms                                                               | 42.1 ms: 1.04x slower                                            |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                            |
| pyflate                    | 559 ms                                                                | 583 ms: 1.04x slower                                             |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                             |
| nbody                      | 105 ms                                                                | 110 ms: 1.05x slower                                             |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.06x slower                                            |
| fannkuch                   | 443 ms                                                                | 471 ms: 1.06x slower                                             |
| regex_effbot               | 4.64 ms                                                               | 4.99 ms: 1.08x slower                                            |
| unpickle_list              | 6.17 us                                                               | 6.64 us: 1.08x slower                                            |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.08x slower                                             |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                            |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                             |
| regex_v8                   | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                            |
| telco                      | 8.51 ms                                                               | 9.25 ms: 1.09x slower                                            |
| coverage                   | 87.3 ms                                                               | 99.0 ms: 1.13x slower                                            |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                            |
| gc_traversal               | 4.40 ms                                                               | 5.07 ms: 1.15x slower                                            |
| create_gc_cycles           | 1.92 ms                                                               | 2.35 ms: 1.23x slower                                            |
| bench_mp_pool              | 7.05 ms                                                               | 5.20 sec: 737.60x slower                                         |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                     |

Benchmark hidden because not significant (12): asyncio_tcp, coroutines, genshi_text, genshi_xml, pickle_list, regex_dna, pylint, asyncio_websockets, pickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_process
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 99.15% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x