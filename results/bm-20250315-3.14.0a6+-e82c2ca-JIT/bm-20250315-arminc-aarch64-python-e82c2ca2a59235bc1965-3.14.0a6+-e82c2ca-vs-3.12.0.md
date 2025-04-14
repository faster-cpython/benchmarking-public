# Results vs. 3.12.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.010x faster
- HPT reliability: 81.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.14 sec: 1.05x slower                                                   |
| html5lib       | 65.1 ms                                                               | 63.3 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 480 ms: 1.62x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 887 ms: 1.59x faster                                                     |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 475 ms: 1.56x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 375 ms: 1.54x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 929 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 669 ms: 1.36x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 652 ms: 1.35x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.2 ms: 1.08x faster                                                    |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                     |
| nbody          | 105 ms                                                                | 132 ms: 1.26x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                    |
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                     |
| regex_dna      | 254 ms                                                                | 239 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 178 ms: 1.10x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| xml_etree_process    | 79.0 ms                                                               | 77.9 ms: 1.01x faster                                                    |
| unpickle_list        | 6.17 us                                                               | 6.33 us: 1.03x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 39.3 us: 1.05x slower                                                    |
| pickle_list          | 5.25 us                                                               | 5.77 us: 1.10x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 404 us: 1.11x slower                                                     |
| json_loads           | 30.7 us                                                               | 34.1 us: 1.11x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 292 us: 1.12x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 13.8 ms: 1.12x slower                                                    |
| pickle               | 13.4 us                                                               | 16.1 us: 1.20x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (2): unpickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.6 ms: 1.03x faster                                                    |
| genshi_text     | 27.4 ms                                                               | 26.9 ms: 1.02x faster                                                    |
| genshi_xml      | 60.6 ms                                                               | 62.2 ms: 1.03x slower                                                    |
| mako            | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 480 ms: 1.62x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 887 ms: 1.59x faster                                                     |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 475 ms: 1.56x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 375 ms: 1.54x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 929 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 669 ms: 1.36x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 652 ms: 1.35x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 37.4 us: 1.33x faster                                                    |
| deepcopy                   | 446 us                                                                | 338 us: 1.32x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.51 us: 1.17x faster                                                    |
| generators                 | 43.5 ms                                                               | 37.3 ms: 1.17x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 55.8 ms: 1.11x faster                                                    |
| pylint                     | 355 ms                                                                | 322 ms: 1.10x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.10x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.05 us: 1.08x faster                                                    |
| float                      | 92.1 ms                                                               | 85.2 ms: 1.08x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.73 us: 1.08x faster                                                    |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.9 ms: 1.07x faster                                                    |
| regex_dna                  | 254 ms                                                                | 239 ms: 1.06x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                   |
| raytrace                   | 353 ms                                                                | 334 ms: 1.06x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| asyncio_tcp                | 566 ms                                                                | 545 ms: 1.04x faster                                                     |
| richards_super             | 58.5 ms                                                               | 56.5 ms: 1.03x faster                                                    |
| async_generators           | 491 ms                                                                | 474 ms: 1.03x faster                                                     |
| mdp                        | 3.41 sec                                                              | 3.31 sec: 1.03x faster                                                   |
| sqlalchemy_imperative      | 16.7 ms                                                               | 16.2 ms: 1.03x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 63.3 ms: 1.03x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.6 ms: 1.03x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 26.9 ms: 1.02x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 77.9 ms: 1.01x faster                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.75 us: 1.01x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 21.7 ms: 1.00x slower                                                    |
| thrift                     | 937 us                                                                | 942 us: 1.01x slower                                                     |
| comprehensions             | 25.4 us                                                               | 25.6 us: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 62.2 ms: 1.03x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.33 us: 1.03x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 88.4 ms: 1.04x slower                                                    |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 39.3 us: 1.05x slower                                                    |
| scimark_fft                | 418 ms                                                                | 440 ms: 1.05x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.38 ms: 1.05x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.14 sec: 1.05x slower                                                   |
| pyflate                    | 559 ms                                                                | 592 ms: 1.06x slower                                                     |
| json                       | 5.54 ms                                                               | 5.89 ms: 1.06x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 155 ms: 1.07x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 108 ms: 1.08x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.77 us: 1.10x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 404 us: 1.11x slower                                                     |
| json_loads                 | 30.7 us                                                               | 34.1 us: 1.11x slower                                                    |
| sympy_expand               | 454 ms                                                                | 505 ms: 1.11x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.40 sec: 1.12x slower                                                   |
| coverage                   | 87.3 ms                                                               | 98.1 ms: 1.12x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 292 us: 1.12x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 13.8 ms: 1.12x slower                                                    |
| meteor_contest             | 112 ms                                                                | 126 ms: 1.13x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.08 ms: 1.14x slower                                                    |
| go                         | 157 ms                                                                | 181 ms: 1.15x slower                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 101 ms: 1.16x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.91 ms: 1.17x slower                                                    |
| fannkuch                   | 443 ms                                                                | 529 ms: 1.19x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 216 us: 1.20x slower                                                     |
| pickle                     | 13.4 us                                                               | 16.1 us: 1.20x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 8.58 ms: 1.23x slower                                                    |
| nbody                      | 105 ms                                                                | 132 ms: 1.26x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.24 sec: 1.36x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.56 sec: 1.36x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.81 ms: 1.55x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.60 ms: 1.87x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.36 sec: 193.33x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (14): sqlalchemy_declarative, unpickle, xml_etree_generate, asyncio_tcp_ssl, richards, sympy_sum, chaos, scimark_sor, deltablue, 2to3, sympy_str, regex_v8, coroutines, spectral_norm
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 81.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x