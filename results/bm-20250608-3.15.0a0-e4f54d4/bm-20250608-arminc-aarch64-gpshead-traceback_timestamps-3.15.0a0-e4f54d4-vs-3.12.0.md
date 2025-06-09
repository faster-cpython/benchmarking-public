# Results vs. 3.12.0

- fork: gpshead
- ref: traceback_timestamps
- machine: linux-aarch64
- commit hash: e4f54d4
- commit date: 2025-06-08
- overall geometric mean: 1.030x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 298 ms: 1.03x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 457 ms: 1.70x faster                                                     |
| async_tree_none            | 624 ms                                                                | 383 ms: 1.63x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 870 ms: 1.62x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 461 ms: 1.61x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 905 ms: 1.55x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 374 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 650 ms: 1.40x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 648 ms: 1.36x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.55x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.5 ms: 1.07x faster                                                    |
| pidigits       | 233 ms                                                                | 240 ms: 1.03x slower                                                     |
| nbody          | 105 ms                                                                | 124 ms: 1.19x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                    |
| regex_compile  | 137 ms                                                                | 122 ms: 1.12x faster                                                     |
| regex_dna      | 254 ms                                                                | 232 ms: 1.09x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 27.6 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.49 sec: 1.04x faster                                                   |
| xml_etree_process   | 79.0 ms                                                               | 80.8 ms: 1.02x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 381 us: 1.04x slower                                                     |
| json_loads          | 30.7 us                                                               | 32.4 us: 1.06x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                    |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 62.5 ms: 1.03x slower                                                    |
| mako           | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 457 ms: 1.70x faster                                                     |
| async_tree_none            | 624 ms                                                                | 383 ms: 1.63x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 870 ms: 1.62x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 461 ms: 1.61x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 905 ms: 1.55x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 374 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 650 ms: 1.40x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 648 ms: 1.36x faster                                                     |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 37.5 us: 1.32x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.2 us: 1.26x faster                                                    |
| go                         | 157 ms                                                                | 130 ms: 1.21x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.3 ms: 1.20x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 52.1 ms: 1.19x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.48 us: 1.18x faster                                                    |
| pylint                     | 355 ms                                                                | 315 ms: 1.13x faster                                                     |
| regex_compile              | 137 ms                                                                | 122 ms: 1.12x faster                                                     |
| regex_dna                  | 254 ms                                                                | 232 ms: 1.09x faster                                                     |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.08x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 79.2 ms: 1.07x faster                                                    |
| float                      | 92.1 ms                                                               | 86.5 ms: 1.07x faster                                                    |
| async_generators           | 491 ms                                                                | 462 ms: 1.06x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.91 ms: 1.05x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| sympy_integrate            | 21.6 ms                                                               | 20.7 ms: 1.05x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.49 sec: 1.04x faster                                                   |
| 2to3                       | 308 ms                                                                | 298 ms: 1.03x faster                                                     |
| regex_v8                   | 28.3 ms                                                               | 27.6 ms: 1.03x faster                                                    |
| spectral_norm              | 131 ms                                                                | 128 ms: 1.02x faster                                                     |
| docutils                   | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                   |
| hexiom                     | 6.98 ms                                                               | 6.88 ms: 1.01x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.68 us: 1.01x slower                                                    |
| logging_format             | 8.34 us                                                               | 8.46 us: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                     |
| coroutines                 | 29.0 ms                                                               | 29.4 ms: 1.01x slower                                                    |
| richards                   | 50.9 ms                                                               | 52.1 ms: 1.02x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 80.8 ms: 1.02x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.86 us: 1.02x slower                                                    |
| json                       | 5.54 ms                                                               | 5.70 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                    |
| scimark_fft                | 418 ms                                                                | 431 ms: 1.03x slower                                                     |
| pidigits                   | 233 ms                                                                | 240 ms: 1.03x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 62.5 ms: 1.03x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 381 us: 1.04x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.06x slower                                                    |
| fannkuch                   | 443 ms                                                                | 469 ms: 1.06x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.72 ms: 1.09x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 999 ms: 1.09x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 2.06 sec: 1.09x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.37 ms: 1.10x slower                                                    |
| nbody                      | 105 ms                                                                | 124 ms: 1.19x slower                                                     |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.90 ms: 1.57x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.82 ms: 1.99x slower                                                    |
| logging_silent             | 127 ns                                                                | 612 ns: 4.83x slower                                                     |
| coverage                   | 87.3 ms                                                               | 561 ms: 6.42x slower                                                     |
| thrift                     | 937 us                                                                | 192 ms: 205.09x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (16): html5lib, scimark_sor, crypto_pyaes, sympy_str, django_template, chaos, pyflate, pycparser, xml_etree_generate, nqueens, scimark_lu, genshi_text, meteor_contest, sympy_expand, unpickle_pure_python, richards_super
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250608-3.15.0a0-e4f54d4/bm-20250608-arminc-aarch64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.030x slower

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x