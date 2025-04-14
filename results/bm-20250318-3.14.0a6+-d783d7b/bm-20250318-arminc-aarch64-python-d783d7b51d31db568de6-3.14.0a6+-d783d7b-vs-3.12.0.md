# Results vs. 3.12.0

- fork: python
- ref: d783d7b51d31db568de6
- machine: linux-aarch64
- commit hash: d783d7b
- commit date: 2025-03-18
- overall geometric mean: 1.042x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 297 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                             |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 468 ms: 1.66x faster                                                     |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.62x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 890 ms: 1.58x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 368 ms: 1.57x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 915 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 650 ms: 1.36x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.4 ms: 1.05x faster                                                    |
| nbody          | 105 ms                                                                | 128 ms: 1.23x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.98 ms: 1.17x faster                                                    |
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                     |
| regex_dna      | 254 ms                                                                | 244 ms: 1.04x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 28.1 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 176 ms: 1.11x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 141 ms: 1.07x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.48 sec: 1.05x faster                                                   |
| unpickle_pure_python | 260 us                                                                | 269 us: 1.03x slower                                                     |
| xml_etree_process    | 79.0 ms                                                               | 82.2 ms: 1.04x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 398 us: 1.09x slower                                                     |
| json_loads           | 30.7 us                                                               | 34.6 us: 1.13x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.2 ms: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.21x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 27.0 ms: 1.02x faster                                                    |
| mako           | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 468 ms: 1.66x faster                                                     |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.62x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 890 ms: 1.58x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 368 ms: 1.57x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 915 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 650 ms: 1.36x faster                                                     |
| deepcopy                   | 446 us                                                                | 331 us: 1.34x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 38.2 us: 1.30x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.7 ms: 1.22x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 51.9 ms: 1.20x faster                                                    |
| comprehensions             | 25.4 us                                                               | 21.6 us: 1.18x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.98 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.53 us: 1.16x faster                                                    |
| go                         | 157 ms                                                                | 140 ms: 1.13x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 176 ms: 1.11x faster                                                     |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.5 ms: 1.09x faster                                                    |
| raytrace                   | 353 ms                                                                | 323 ms: 1.09x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.07 us: 1.08x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 147 ms: 1.07x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                     |
| async_generators           | 491 ms                                                                | 461 ms: 1.06x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.84 us: 1.06x faster                                                    |
| pylint                     | 355 ms                                                                | 334 ms: 1.06x faster                                                     |
| float                      | 92.1 ms                                                               | 87.4 ms: 1.05x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.9 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.48 sec: 1.05x faster                                                   |
| regex_dna                  | 254 ms                                                                | 244 ms: 1.04x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.97 ms: 1.04x faster                                                    |
| 2to3                       | 308 ms                                                                | 297 ms: 1.04x faster                                                     |
| mdp                        | 3.41 sec                                                              | 3.31 sec: 1.03x faster                                                   |
| pyflate                    | 559 ms                                                                | 548 ms: 1.02x faster                                                     |
| genshi_text                | 27.4 ms                                                               | 27.0 ms: 1.02x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 28.1 ms: 1.01x faster                                                    |
| scimark_sor                | 150 ms                                                                | 149 ms: 1.01x faster                                                     |
| coroutines                 | 29.0 ms                                                               | 29.1 ms: 1.00x slower                                                    |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                     |
| scimark_fft                | 418 ms                                                                | 424 ms: 1.01x slower                                                     |
| thrift                     | 937 us                                                                | 949 us: 1.01x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                     |
| richards                   | 50.9 ms                                                               | 51.8 ms: 1.02x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.34 ms: 1.02x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 149 ms: 1.03x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.87 us: 1.03x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 269 us: 1.03x slower                                                     |
| sympy_expand               | 454 ms                                                                | 470 ms: 1.04x slower                                                     |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 82.2 ms: 1.04x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 104 ms: 1.04x slower                                                     |
| json                       | 5.54 ms                                                               | 5.79 ms: 1.04x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 959 ms: 1.05x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.97 sec: 1.05x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.33 ms: 1.05x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.59 ms: 1.06x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 398 us: 1.09x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 199 us: 1.10x slower                                                     |
| json_loads                 | 30.7 us                                                               | 34.6 us: 1.13x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.7 ms: 1.13x slower                                                    |
| fannkuch                   | 443 ms                                                                | 508 ms: 1.15x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.2 ms: 1.15x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.89 ms: 1.16x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.21x slower                                                    |
| nbody                      | 105 ms                                                                | 128 ms: 1.23x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.56 ms: 1.49x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.68 ms: 1.92x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.47 sec: 350.32x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (13): spectral_norm, html5lib, docutils, django_template, sympy_integrate, crypto_pyaes, genshi_xml, pycparser, chaos, pidigits, richards_super, scimark_monte_carlo, xml_etree_generate
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250318-3.14.0a6+-d783d7b/bm-20250318-arminc-aarch64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x