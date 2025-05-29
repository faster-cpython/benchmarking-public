# Results vs. 3.12.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-aarch64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.028x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 301 ms: 1.02x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                  |
| html5lib       | 65.1 ms                                                               | 60.6 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 454 ms: 1.71x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 453 ms: 1.63x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 866 ms: 1.63x faster                                                    |
| async_tree_none            | 624 ms                                                                | 384 ms: 1.62x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 364 ms: 1.58x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 894 ms: 1.57x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 721 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 715 ms: 1.24x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.0 ms: 1.06x faster                                                   |
| nbody          | 105 ms                                                                | 128 ms: 1.23x slower                                                    |
| pidigits       | 233 ms                                                                | 292 ms: 1.26x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 120 ms: 1.14x faster                                                    |
| regex_dna      | 254 ms                                                                | 246 ms: 1.03x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.50 ms: 1.03x faster                                                   |
| regex_v8       | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle            | 18.5 us                                                               | 17.1 us: 1.08x faster                                                   |
| tomli_loads         | 2.59 sec                                                              | 2.41 sec: 1.08x faster                                                  |
| unpickle_list       | 6.17 us                                                               | 5.79 us: 1.07x faster                                                   |
| xml_etree_process   | 79.0 ms                                                               | 75.9 ms: 1.04x faster                                                   |
| xml_etree_iterparse | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| pickle_list         | 5.25 us                                                               | 5.38 us: 1.03x slower                                                   |
| xml_etree_parse     | 195 ms                                                                | 204 ms: 1.05x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 400 us: 1.09x slower                                                    |
| json_loads          | 30.7 us                                                               | 34.2 us: 1.11x slower                                                   |
| pickle              | 13.4 us                                                               | 15.1 us: 1.12x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_generate, unpickle_pure_python, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.83 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.3 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.19x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 38.9 ms: 1.05x faster                                                   |
| mako            | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.64 sec: 2.08x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 454 ms: 1.71x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 453 ms: 1.63x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 866 ms: 1.63x faster                                                    |
| async_tree_none            | 624 ms                                                                | 384 ms: 1.62x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 364 ms: 1.58x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 894 ms: 1.57x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 35.7 us: 1.39x faster                                                   |
| deepcopy                   | 446 us                                                                | 321 us: 1.39x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 721 ms: 1.27x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.3 us: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 715 ms: 1.24x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.5 ms: 1.23x faster                                                   |
| go                         | 157 ms                                                                | 130 ms: 1.21x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.42 us: 1.20x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 52.3 ms: 1.18x faster                                                   |
| async_generators           | 491 ms                                                                | 429 ms: 1.14x faster                                                    |
| regex_compile              | 137 ms                                                                | 120 ms: 1.14x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                   |
| pylint                     | 355 ms                                                                | 321 ms: 1.10x faster                                                    |
| raytrace                   | 353 ms                                                                | 320 ms: 1.10x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.09x faster                                                    |
| chaos                      | 71.4 ms                                                               | 65.5 ms: 1.09x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 134 ms: 1.09x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.0 ms: 1.08x faster                                                   |
| unpickle                   | 18.5 us                                                               | 17.1 us: 1.08x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 78.8 ms: 1.08x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.41 sec: 1.08x faster                                                  |
| pyflate                    | 559 ms                                                                | 519 ms: 1.08x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 60.6 ms: 1.07x faster                                                   |
| spectral_norm              | 131 ms                                                                | 122 ms: 1.07x faster                                                    |
| unpickle_list              | 6.17 us                                                               | 5.79 us: 1.07x faster                                                   |
| float                      | 92.1 ms                                                               | 87.0 ms: 1.06x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.92 ms: 1.05x faster                                                   |
| django_template            | 40.7 ms                                                               | 38.9 ms: 1.05x faster                                                   |
| scimark_sor                | 150 ms                                                                | 143 ms: 1.05x faster                                                    |
| scimark_fft                | 418 ms                                                                | 400 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 75.9 ms: 1.04x faster                                                   |
| richards_super             | 58.5 ms                                                               | 56.4 ms: 1.04x faster                                                   |
| asyncio_tcp                | 566 ms                                                                | 546 ms: 1.04x faster                                                    |
| regex_dna                  | 254 ms                                                                | 246 ms: 1.03x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.50 ms: 1.03x faster                                                   |
| 2to3                       | 308 ms                                                                | 301 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| logging_format             | 8.34 us                                                               | 8.22 us: 1.02x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 85.4 ms: 1.01x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.01x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.58 us: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 927 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.90 sec: 1.01x slower                                                  |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.38 us: 1.03x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 102 ms: 1.03x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 204 ms: 1.05x slower                                                    |
| meteor_contest             | 112 ms                                                                | 118 ms: 1.05x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.83 ms: 1.05x slower                                                   |
| json                       | 5.54 ms                                                               | 5.89 ms: 1.06x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.67 ms: 1.08x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 195 us: 1.08x slower                                                    |
| fannkuch                   | 443 ms                                                                | 482 ms: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 400 us: 1.09x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.44 ms: 1.11x slower                                                   |
| json_loads                 | 30.7 us                                                               | 34.2 us: 1.11x slower                                                   |
| pickle                     | 13.4 us                                                               | 15.1 us: 1.12x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                   |
| nbody                      | 105 ms                                                                | 128 ms: 1.23x slower                                                    |
| pidigits                   | 233 ms                                                                | 292 ms: 1.26x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.3 ms: 1.35x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.70 ms: 1.52x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.81 ms: 1.99x slower                                                   |
| logging_silent             | 127 ns                                                                | 647 ns: 5.10x slower                                                    |
| coverage                   | 87.3 ms                                                               | 535 ms: 6.13x slower                                                    |
| thrift                     | 937 us                                                                | 193 ms: 206.05x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 3.27 sec: 463.20x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (11): xml_etree_generate, unpickle_pure_python, richards, genshi_xml, pycparser, pickle_dict, genshi_text, sympy_expand, sqlite_synth, bench_thread_pool, hexiom
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.028x slower

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.12x