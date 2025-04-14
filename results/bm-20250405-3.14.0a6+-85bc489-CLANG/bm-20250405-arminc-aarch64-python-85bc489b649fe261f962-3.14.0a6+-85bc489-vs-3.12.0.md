# Results vs. 3.12.0

- fork: python
- ref: 85bc489b649fe261f962
- machine: linux-aarch64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.082x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 288 ms: 1.07x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.91 sec: 1.02x faster                                                   |
| html5lib       | 65.1 ms                                                               | 58.3 ms: 1.12x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 446 ms: 1.74x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 445 ms: 1.66x faster                                                     |
| async_tree_none            | 624 ms                                                                | 375 ms: 1.66x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 862 ms: 1.64x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 860 ms: 1.63x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 362 ms: 1.59x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 715 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 698 ms: 1.27x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.55x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 84.2 ms: 1.09x faster                                                    |
| nbody          | 105 ms                                                                | 130 ms: 1.24x slower                                                     |
| pidigits       | 233 ms                                                                | 290 ms: 1.25x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 121 ms: 1.13x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.30 ms: 1.08x faster                                                    |
| regex_dna      | 254 ms                                                                | 245 ms: 1.04x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle           | 18.5 us                                                               | 16.6 us: 1.11x faster                                                    |
| tomli_loads        | 2.59 sec                                                              | 2.33 sec: 1.11x faster                                                   |
| unpickle_list      | 6.17 us                                                               | 5.60 us: 1.10x faster                                                    |
| xml_etree_generate | 112 ms                                                                | 105 ms: 1.07x faster                                                     |
| pickle_dict        | 37.3 us                                                               | 35.4 us: 1.06x faster                                                    |
| xml_etree_process  | 79.0 ms                                                               | 75.9 ms: 1.04x faster                                                    |
| pickle_pure_python | 365 us                                                                | 370 us: 1.01x slower                                                     |
| pickle_list        | 5.25 us                                                               | 5.48 us: 1.04x slower                                                    |
| xml_etree_parse    | 195 ms                                                                | 205 ms: 1.05x slower                                                     |
| json_loads         | 30.7 us                                                               | 33.9 us: 1.11x slower                                                    |
| pickle             | 13.4 us                                                               | 14.9 us: 1.11x slower                                                    |
| json_dumps         | 12.3 ms                                                               | 13.8 ms: 1.12x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.21x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 25.6 ms: 1.07x faster                                                    |
| django_template | 40.7 ms                                                               | 38.0 ms: 1.07x faster                                                    |
| mako            | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.61 sec: 2.11x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 446 ms: 1.74x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 445 ms: 1.66x faster                                                     |
| async_tree_none            | 624 ms                                                                | 375 ms: 1.66x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 862 ms: 1.64x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 860 ms: 1.63x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 362 ms: 1.59x faster                                                     |
| deepcopy                   | 446 us                                                                | 299 us: 1.49x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 35.9 us: 1.38x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.20 us: 1.28x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 715 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 698 ms: 1.27x faster                                                     |
| comprehensions             | 25.4 us                                                               | 20.1 us: 1.27x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 50.1 ms: 1.24x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.9 ms: 1.21x faster                                                    |
| go                         | 157 ms                                                                | 131 ms: 1.20x faster                                                     |
| async_generators           | 491 ms                                                                | 409 ms: 1.20x faster                                                     |
| pylint                     | 355 ms                                                                | 300 ms: 1.18x faster                                                     |
| logging_simple             | 7.63 us                                                               | 6.62 us: 1.15x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.3 ms: 1.15x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.27 us: 1.15x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 135 ms: 1.14x faster                                                     |
| logging_silent             | 127 ns                                                                | 111 ns: 1.14x faster                                                     |
| regex_compile              | 137 ms                                                                | 121 ms: 1.13x faster                                                     |
| raytrace                   | 353 ms                                                                | 315 ms: 1.12x faster                                                     |
| html5lib                   | 65.1 ms                                                               | 58.3 ms: 1.12x faster                                                    |
| unpickle                   | 18.5 us                                                               | 16.6 us: 1.11x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.33 sec: 1.11x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 19.5 ms: 1.11x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.73 ms: 1.10x faster                                                    |
| unpickle_list              | 6.17 us                                                               | 5.60 us: 1.10x faster                                                    |
| spectral_norm              | 131 ms                                                                | 119 ms: 1.10x faster                                                     |
| float                      | 92.1 ms                                                               | 84.2 ms: 1.09x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 78.4 ms: 1.09x faster                                                    |
| chaos                      | 71.4 ms                                                               | 65.9 ms: 1.08x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.30 ms: 1.08x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 135 ms: 1.08x faster                                                     |
| scimark_sor                | 150 ms                                                                | 139 ms: 1.07x faster                                                     |
| genshi_text                | 27.4 ms                                                               | 25.6 ms: 1.07x faster                                                    |
| sympy_str                  | 280 ms                                                                | 261 ms: 1.07x faster                                                     |
| django_template            | 40.7 ms                                                               | 38.0 ms: 1.07x faster                                                    |
| 2to3                       | 308 ms                                                                | 288 ms: 1.07x faster                                                     |
| xml_etree_generate         | 112 ms                                                                | 105 ms: 1.07x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 148 ms: 1.07x faster                                                     |
| pyflate                    | 559 ms                                                                | 526 ms: 1.06x faster                                                     |
| richards                   | 50.9 ms                                                               | 48.1 ms: 1.06x faster                                                    |
| pickle_dict                | 37.3 us                                                               | 35.4 us: 1.06x faster                                                    |
| scimark_fft                | 418 ms                                                                | 400 ms: 1.05x faster                                                     |
| richards_super             | 58.5 ms                                                               | 56.0 ms: 1.04x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 543 ms: 1.04x faster                                                     |
| xml_etree_process          | 79.0 ms                                                               | 75.9 ms: 1.04x faster                                                    |
| regex_dna                  | 254 ms                                                                | 245 ms: 1.04x faster                                                     |
| docutils                   | 2.98 sec                                                              | 2.91 sec: 1.02x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.86 sec: 1.01x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 85.8 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.17 sec: 1.01x faster                                                   |
| pickle_pure_python         | 365 us                                                                | 370 us: 1.01x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.84 us: 1.02x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 187 us: 1.04x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.48 us: 1.04x slower                                                    |
| telco                      | 8.51 ms                                                               | 8.88 ms: 1.04x slower                                                    |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.05x slower                                                     |
| xml_etree_parse            | 195 ms                                                                | 205 ms: 1.05x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.59 ms: 1.06x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                    |
| coverage                   | 87.3 ms                                                               | 94.4 ms: 1.08x slower                                                    |
| json                       | 5.54 ms                                                               | 6.00 ms: 1.08x slower                                                    |
| fannkuch                   | 443 ms                                                                | 490 ms: 1.10x slower                                                     |
| json_loads                 | 30.7 us                                                               | 33.9 us: 1.11x slower                                                    |
| pickle                     | 13.4 us                                                               | 14.9 us: 1.11x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.8 ms: 1.12x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.21x slower                                                    |
| nbody                      | 105 ms                                                                | 130 ms: 1.24x slower                                                     |
| pidigits                   | 233 ms                                                                | 290 ms: 1.25x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.42x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.58 ms: 1.50x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.76 ms: 1.96x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.87 sec: 406.84x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (10): genshi_xml, coroutines, unpickle_pure_python, pprint_safe_repr, xml_etree_iterparse, sympy_expand, sqlalchemy_imperative, bench_thread_pool, hexiom, nqueens
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.082x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.09x