# Results vs. 3.12.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-aarch64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.055x slower
- HPT reliability: 95.12%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 314 ms: 1.02x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| html5lib       | 65.1 ms                                                               | 61.0 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 489 ms: 1.59x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 908 ms: 1.55x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 479 ms: 1.55x faster                                                    |
| async_tree_none            | 624 ms                                                                | 411 ms: 1.52x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 928 ms: 1.51x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 386 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 675 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 667 ms: 1.33x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.48x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 84.8 ms: 1.09x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 118 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                   |
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| regex_dna      | 254 ms                                                                | 238 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.35 sec: 1.10x faster                                                  |
| xml_etree_parse     | 195 ms                                                                | 182 ms: 1.07x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                    |
| xml_etree_process   | 79.0 ms                                                               | 77.8 ms: 1.02x faster                                                   |
| pickle_dict         | 37.3 us                                                               | 39.0 us: 1.04x slower                                                   |
| pickle_list         | 5.25 us                                                               | 5.58 us: 1.06x slower                                                   |
| unpickle_list       | 6.17 us                                                               | 6.67 us: 1.08x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 396 us: 1.09x slower                                                    |
| json_loads          | 30.7 us                                                               | 35.3 us: 1.15x slower                                                   |
| pickle              | 13.4 us                                                               | 15.6 us: 1.16x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (3): unpickle_pure_python, xml_etree_generate, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.3 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.19x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 63.0 ms: 1.04x slower                                                   |
| mako           | 12.9 ms                                                               | 13.5 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 489 ms: 1.59x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 908 ms: 1.55x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 479 ms: 1.55x faster                                                    |
| async_tree_none            | 624 ms                                                                | 411 ms: 1.52x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 928 ms: 1.51x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 386 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 675 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 333 us: 1.34x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 667 ms: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.5 us: 1.32x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                   |
| generators                 | 43.5 ms                                                               | 36.8 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.52 us: 1.16x faster                                                   |
| richards_super             | 58.5 ms                                                               | 51.9 ms: 1.13x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.35 sec: 1.10x faster                                                  |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| float                      | 92.1 ms                                                               | 84.8 ms: 1.09x faster                                                   |
| richards                   | 50.9 ms                                                               | 47.2 ms: 1.08x faster                                                   |
| comprehensions             | 25.4 us                                                               | 23.6 us: 1.07x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.85 ms: 1.07x faster                                                   |
| regex_dna                  | 254 ms                                                                | 238 ms: 1.07x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 61.0 ms: 1.07x faster                                                   |
| pylint                     | 355 ms                                                                | 335 ms: 1.06x faster                                                    |
| raytrace                   | 353 ms                                                                | 334 ms: 1.06x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.3 ms: 1.05x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 269 ms: 1.04x faster                                                    |
| pyflate                    | 559 ms                                                                | 548 ms: 1.02x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 555 ms: 1.02x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 77.8 ms: 1.02x faster                                                   |
| spectral_norm              | 131 ms                                                                | 131 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| 2to3                       | 308 ms                                                                | 314 ms: 1.02x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                    |
| scimark_fft                | 418 ms                                                                | 430 ms: 1.03x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 29.9 ms: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| genshi_xml                 | 60.6 ms                                                               | 63.0 ms: 1.04x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.5 ms: 1.04x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 39.0 us: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                                   |
| sympy_expand               | 454 ms                                                                | 479 ms: 1.06x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 105 ms: 1.06x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.58 us: 1.06x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.40 ms: 1.07x slower                                                   |
| go                         | 157 ms                                                                | 168 ms: 1.07x slower                                                    |
| meteor_contest             | 112 ms                                                                | 120 ms: 1.07x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.67 us: 1.08x slower                                                   |
| json                       | 5.54 ms                                                               | 6.00 ms: 1.08x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 396 us: 1.09x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 94.4 ms: 1.09x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.39 sec: 1.10x slower                                                  |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.85 ms: 1.11x slower                                                   |
| fannkuch                   | 443 ms                                                                | 492 ms: 1.11x slower                                                    |
| nbody                      | 105 ms                                                                | 118 ms: 1.12x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.60 ms: 1.13x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.90 ms: 1.13x slower                                                   |
| json_loads                 | 30.7 us                                                               | 35.3 us: 1.15x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 209 us: 1.16x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.6 us: 1.16x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.14 sec: 1.24x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.35 sec: 1.25x slower                                                  |
| python_startup             | 11.4 ms                                                               | 15.3 ms: 1.34x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.85 ms: 1.56x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.76 ms: 1.96x slower                                                   |
| logging_silent             | 127 ns                                                                | 626 ns: 4.94x slower                                                    |
| coverage                   | 87.3 ms                                                               | 548 ms: 6.27x slower                                                    |
| thrift                     | 937 us                                                                | 194 ms: 206.74x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 3.94 sec: 558.96x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.16x slower                                                            |

Benchmark hidden because not significant (17): dulwich_log, django_template, sympy_integrate, sympy_sum, scimark_sor, async_generators, chaos, unpickle_pure_python, xml_etree_generate, regex_v8, logging_simple, sqlite_synth, logging_format, scimark_lu, genshi_text, unpickle, scimark_monte_carlo
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250518-3.15.0a0-009e7b3-JIT/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.055x slower

# HPT report

- Reliability score: 95.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x