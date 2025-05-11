# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-aarch64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.030x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                                  |
| html5lib       | 65.1 ms                                                               | 62.0 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                                    |
| async_tree_none            | 624 ms                                                                | 387 ms: 1.61x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 463 ms: 1.60x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 887 ms: 1.59x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 900 ms: 1.56x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 651 ms: 1.40x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 655 ms: 1.35x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.3 ms: 1.07x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 122 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                   |
| regex_compile  | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| regex_dna      | 254 ms                                                                | 240 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.08x faster                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                  |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.06x faster                                                    |
| xml_etree_generate  | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| xml_etree_process   | 79.0 ms                                                               | 79.6 ms: 1.01x slower                                                   |
| pickle_dict         | 37.3 us                                                               | 39.0 us: 1.05x slower                                                   |
| pickle_list         | 5.25 us                                                               | 5.68 us: 1.08x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 395 us: 1.08x slower                                                    |
| unpickle_list       | 6.17 us                                                               | 6.80 us: 1.10x slower                                                   |
| pickle              | 13.4 us                                                               | 15.7 us: 1.17x slower                                                   |
| json_loads          | 30.7 us                                                               | 36.4 us: 1.19x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (2): unpickle, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.66 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 38.7 ms: 1.05x faster                                                   |
| mako            | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.67 sec: 2.04x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                                    |
| async_tree_none            | 624 ms                                                                | 387 ms: 1.61x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 463 ms: 1.60x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 887 ms: 1.59x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 900 ms: 1.56x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 651 ms: 1.40x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 655 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 335 us: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.1 us: 1.30x faster                                                   |
| go                         | 157 ms                                                                | 129 ms: 1.22x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                   |
| comprehensions             | 25.4 us                                                               | 21.2 us: 1.20x faster                                                   |
| generators                 | 43.5 ms                                                               | 36.9 ms: 1.18x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 54.0 ms: 1.15x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.57 us: 1.15x faster                                                   |
| pylint                     | 355 ms                                                                | 315 ms: 1.13x faster                                                    |
| regex_compile              | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.10x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.78 ms: 1.09x faster                                                   |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.7 ms: 1.08x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.1 ms: 1.08x faster                                                   |
| pyflate                    | 559 ms                                                                | 523 ms: 1.07x faster                                                    |
| async_generators           | 491 ms                                                                | 460 ms: 1.07x faster                                                    |
| float                      | 92.1 ms                                                               | 86.3 ms: 1.07x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                  |
| asyncio_tcp                | 566 ms                                                                | 534 ms: 1.06x faster                                                    |
| regex_dna                  | 254 ms                                                                | 240 ms: 1.06x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.06x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.6 ms: 1.05x faster                                                   |
| django_template            | 40.7 ms                                                               | 38.7 ms: 1.05x faster                                                   |
| html5lib                   | 65.1 ms                                                               | 62.0 ms: 1.05x faster                                                   |
| pprint_safe_repr           | 916 ms                                                                | 891 ms: 1.03x faster                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.84 sec: 1.03x faster                                                  |
| scimark_lu                 | 146 ms                                                                | 142 ms: 1.02x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 85.1 ms: 1.02x faster                                                   |
| docutils                   | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                                  |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.75 us: 1.01x faster                                                   |
| xml_etree_process          | 79.0 ms                                                               | 79.6 ms: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                    |
| sympy_expand               | 454 ms                                                                | 465 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.66 ms: 1.04x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 30.2 ms: 1.04x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 39.0 us: 1.05x slower                                                   |
| scimark_fft                | 418 ms                                                                | 445 ms: 1.06x slower                                                    |
| fannkuch                   | 443 ms                                                                | 474 ms: 1.07x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.68 us: 1.08x slower                                                   |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 395 us: 1.08x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 198 us: 1.10x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.80 us: 1.10x slower                                                   |
| json                       | 5.54 ms                                                               | 6.11 ms: 1.10x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.91 ms: 1.12x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.70 ms: 1.14x slower                                                   |
| nbody                      | 105 ms                                                                | 122 ms: 1.16x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.7 us: 1.17x slower                                                   |
| json_loads                 | 30.7 us                                                               | 36.4 us: 1.19x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                   |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.97 ms: 1.59x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.70 ms: 1.93x slower                                                   |
| logging_silent             | 127 ns                                                                | 605 ns: 4.77x slower                                                    |
| coverage                   | 87.3 ms                                                               | 545 ms: 6.24x slower                                                    |
| thrift                     | 937 us                                                                | 194 ms: 206.68x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 4.01 sec: 568.65x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                            |

Benchmark hidden because not significant (18): sympy_str, scimark_sor, chaos, asyncio_tcp_ssl, 2to3, richards_super, spectral_norm, logging_simple, logging_format, regex_v8, pycparser, genshi_text, nqueens, richards, unpickle, genshi_xml, hexiom, unpickle_pure_python
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.030x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x