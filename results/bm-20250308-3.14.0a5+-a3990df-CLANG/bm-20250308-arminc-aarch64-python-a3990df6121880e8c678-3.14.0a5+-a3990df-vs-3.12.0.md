# Results vs. 3.12.0

- fork: python
- ref: a3990df6121880e8c678
- machine: linux-aarch64
- commit hash: a3990df
- commit date: 2025-03-08
- overall geometric mean: 1.095x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 284 ms: 1.09x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.87 sec: 1.04x faster                                                   |
| html5lib       | 65.1 ms                                                               | 57.3 ms: 1.14x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 453 ms: 1.71x faster                                                     |
| async_tree_none            | 624 ms                                                                | 364 ms: 1.71x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 847 ms: 1.66x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 861 ms: 1.64x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 454 ms: 1.63x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 357 ms: 1.61x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 712 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 703 ms: 1.26x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.55x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 84.4 ms: 1.09x faster                                                    |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                     |
| pidigits       | 233 ms                                                                | 296 ms: 1.27x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 121 ms: 1.13x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.21 ms: 1.10x faster                                                    |
| regex_dna      | 254 ms                                                                | 245 ms: 1.04x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 32.3 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.29 sec: 1.13x faster                                                   |
| xml_etree_generate  | 112 ms                                                                | 100 ms: 1.12x faster                                                     |
| unpickle            | 18.5 us                                                               | 16.5 us: 1.12x faster                                                    |
| xml_etree_process   | 79.0 ms                                                               | 72.1 ms: 1.10x faster                                                    |
| unpickle_list       | 6.17 us                                                               | 5.75 us: 1.07x faster                                                    |
| pickle_dict         | 37.3 us                                                               | 36.0 us: 1.04x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 149 ms: 1.01x faster                                                     |
| pickle_list         | 5.25 us                                                               | 5.35 us: 1.02x slower                                                    |
| xml_etree_parse     | 195 ms                                                                | 207 ms: 1.06x slower                                                     |
| json_loads          | 30.7 us                                                               | 32.9 us: 1.07x slower                                                    |
| pickle              | 13.4 us                                                               | 15.0 us: 1.12x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (2): unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 37.2 ms: 1.09x faster                                                    |
| genshi_xml      | 60.6 ms                                                               | 57.2 ms: 1.06x faster                                                    |
| genshi_text     | 27.4 ms                                                               | 26.3 ms: 1.04x faster                                                    |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.04x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 453 ms: 1.71x faster                                                     |
| async_tree_none            | 624 ms                                                                | 364 ms: 1.71x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 847 ms: 1.66x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 861 ms: 1.64x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 454 ms: 1.63x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 357 ms: 1.61x faster                                                     |
| deepcopy                   | 446 us                                                                | 292 us: 1.52x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 34.6 us: 1.44x faster                                                    |
| comprehensions             | 25.4 us                                                               | 18.8 us: 1.35x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 712 ms: 1.28x faster                                                     |
| spectral_norm              | 131 ms                                                                | 102 ms: 1.28x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.26 us: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 703 ms: 1.26x faster                                                     |
| async_generators           | 491 ms                                                                | 395 ms: 1.24x faster                                                     |
| generators                 | 43.5 ms                                                               | 35.4 ms: 1.23x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 50.5 ms: 1.23x faster                                                    |
| go                         | 157 ms                                                                | 131 ms: 1.20x faster                                                     |
| pylint                     | 355 ms                                                                | 299 ms: 1.19x faster                                                     |
| raytrace                   | 353 ms                                                                | 302 ms: 1.17x faster                                                     |
| logging_simple             | 7.63 us                                                               | 6.58 us: 1.16x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.3 ms: 1.15x faster                                                    |
| scimark_fft                | 418 ms                                                                | 363 ms: 1.15x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.26 us: 1.15x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 14.7 ms: 1.14x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 57.3 ms: 1.14x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.29 sec: 1.13x faster                                                   |
| regex_compile              | 137 ms                                                                | 121 ms: 1.13x faster                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 75.2 ms: 1.13x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 140 ms: 1.13x faster                                                     |
| xml_etree_generate         | 112 ms                                                                | 100 ms: 1.12x faster                                                     |
| unpickle                   | 18.5 us                                                               | 16.5 us: 1.12x faster                                                    |
| chaos                      | 71.4 ms                                                               | 63.9 ms: 1.12x faster                                                    |
| logging_silent             | 127 ns                                                                | 114 ns: 1.11x faster                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 1.64 ms: 1.11x faster                                                    |
| scimark_sor                | 150 ms                                                                | 135 ms: 1.11x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 139 ms: 1.11x faster                                                     |
| pyflate                    | 559 ms                                                                | 506 ms: 1.11x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.21 ms: 1.10x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 132 ms: 1.10x faster                                                     |
| sympy_integrate            | 21.6 ms                                                               | 19.7 ms: 1.10x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 72.1 ms: 1.10x faster                                                    |
| sympy_str                  | 280 ms                                                                | 255 ms: 1.10x faster                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.34 ms: 1.09x faster                                                    |
| django_template            | 40.7 ms                                                               | 37.2 ms: 1.09x faster                                                    |
| float                      | 92.1 ms                                                               | 84.4 ms: 1.09x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.78 ms: 1.09x faster                                                    |
| 2to3                       | 308 ms                                                                | 284 ms: 1.09x faster                                                     |
| richards_super             | 58.5 ms                                                               | 53.9 ms: 1.09x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.16 sec: 1.08x faster                                                   |
| unpickle_list              | 6.17 us                                                               | 5.75 us: 1.07x faster                                                    |
| sqlglot_normalize          | 126 ms                                                                | 118 ms: 1.07x faster                                                     |
| richards                   | 50.9 ms                                                               | 48.0 ms: 1.06x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 27.4 ms: 1.06x faster                                                    |
| genshi_xml                 | 60.6 ms                                                               | 57.2 ms: 1.06x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 542 ms: 1.04x faster                                                     |
| genshi_text                | 27.4 ms                                                               | 26.3 ms: 1.04x faster                                                    |
| docutils                   | 2.98 sec                                                              | 2.87 sec: 1.04x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.21 sec: 1.04x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 83.5 ms: 1.04x faster                                                    |
| pickle_dict                | 37.3 us                                                               | 36.0 us: 1.04x faster                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 5.98 ms: 1.04x faster                                                    |
| typing_runtime_protocols   | 181 us                                                                | 174 us: 1.04x faster                                                     |
| regex_dna                  | 254 ms                                                                | 245 ms: 1.04x faster                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 59.4 ms: 1.03x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.27 ms: 1.03x faster                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.84 sec: 1.02x faster                                                   |
| sympy_expand               | 454 ms                                                                | 444 ms: 1.02x faster                                                     |
| pprint_safe_repr           | 916 ms                                                                | 903 ms: 1.01x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                                     |
| hexiom                     | 6.98 ms                                                               | 6.90 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.17 sec: 1.01x faster                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.74 us: 1.01x faster                                                    |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.35 us: 1.02x slower                                                    |
| json                       | 5.54 ms                                                               | 5.69 ms: 1.03x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                    |
| coverage                   | 87.3 ms                                                               | 91.3 ms: 1.05x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 207 ms: 1.06x slower                                                     |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                     |
| fannkuch                   | 443 ms                                                                | 475 ms: 1.07x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.9 us: 1.07x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.24 ms: 1.09x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.0 us: 1.12x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.3 ms: 1.14x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                    |
| pidigits                   | 233 ms                                                                | 296 ms: 1.27x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.62 ms: 1.51x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.61 ms: 1.88x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 5.87 sec: 831.64x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (5): nqueens, thrift, unpickle_pure_python, asyncio_websockets, pickle_pure_python
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.095x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.08x