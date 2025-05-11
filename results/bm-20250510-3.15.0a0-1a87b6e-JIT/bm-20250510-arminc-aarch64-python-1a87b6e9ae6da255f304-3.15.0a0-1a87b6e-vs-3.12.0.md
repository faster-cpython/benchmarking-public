# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-aarch64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.054x slower
- HPT reliability: 94.55%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 313 ms: 1.01x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                                  |
| html5lib       | 65.1 ms                                                               | 61.0 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 483 ms: 1.61x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 915 ms: 1.54x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 483 ms: 1.53x faster                                                    |
| async_tree_none            | 624 ms                                                                | 412 ms: 1.51x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 945 ms: 1.49x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 389 ms: 1.48x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 677 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 676 ms: 1.31x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.47x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 84.4 ms: 1.09x faster                                                   |
| nbody          | 105 ms                                                                | 119 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.83 ms: 1.21x faster                                                   |
| regex_compile  | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| regex_dna      | 254 ms                                                                | 232 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.37 sec: 1.10x faster                                                  |
| xml_etree_parse     | 195 ms                                                                | 185 ms: 1.05x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.04x faster                                                    |
| xml_etree_generate  | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| pickle_dict         | 37.3 us                                                               | 38.8 us: 1.04x slower                                                   |
| unpickle_list       | 6.17 us                                                               | 6.43 us: 1.04x slower                                                   |
| pickle_list         | 5.25 us                                                               | 5.65 us: 1.08x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 394 us: 1.08x slower                                                    |
| json_loads          | 30.7 us                                                               | 35.3 us: 1.15x slower                                                   |
| pickle              | 13.4 us                                                               | 15.5 us: 1.15x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 14.3 ms: 1.17x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_process, unpickle, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.65 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 62.8 ms: 1.04x slower                                                   |
| mako           | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 483 ms: 1.61x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 915 ms: 1.54x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 483 ms: 1.53x faster                                                    |
| async_tree_none            | 624 ms                                                                | 412 ms: 1.51x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 945 ms: 1.49x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 389 ms: 1.48x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 677 ms: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.5 us: 1.32x faster                                                   |
| deepcopy                   | 446 us                                                                | 338 us: 1.32x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 676 ms: 1.31x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.83 ms: 1.21x faster                                                   |
| generators                 | 43.5 ms                                                               | 37.3 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.56 us: 1.15x faster                                                   |
| richards_super             | 58.5 ms                                                               | 51.9 ms: 1.13x faster                                                   |
| regex_compile              | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| pylint                     | 355 ms                                                                | 320 ms: 1.11x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.37 sec: 1.10x faster                                                  |
| regex_dna                  | 254 ms                                                                | 232 ms: 1.09x faster                                                    |
| float                      | 92.1 ms                                                               | 84.4 ms: 1.09x faster                                                   |
| richards                   | 50.9 ms                                                               | 46.9 ms: 1.09x faster                                                   |
| comprehensions             | 25.4 us                                                               | 23.6 us: 1.08x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 57.7 ms: 1.07x faster                                                   |
| raytrace                   | 353 ms                                                                | 330 ms: 1.07x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.85 ms: 1.07x faster                                                   |
| html5lib                   | 65.1 ms                                                               | 61.0 ms: 1.07x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 23.0 ms: 1.07x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 185 ms: 1.05x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.04x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 544 ms: 1.04x faster                                                    |
| async_generators           | 491 ms                                                                | 473 ms: 1.04x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 84.7 ms: 1.00x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.41 us: 1.01x slower                                                   |
| logging_simple             | 7.63 us                                                               | 7.74 us: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.22 sec: 1.01x slower                                                  |
| pyflate                    | 559 ms                                                                | 567 ms: 1.01x slower                                                    |
| 2to3                       | 308 ms                                                                | 313 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.65 ms: 1.03x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                                  |
| genshi_xml                 | 60.6 ms                                                               | 62.8 ms: 1.04x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 30.1 ms: 1.04x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 38.8 us: 1.04x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.43 us: 1.04x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                   |
| go                         | 157 ms                                                                | 167 ms: 1.06x slower                                                    |
| sympy_expand               | 454 ms                                                                | 483 ms: 1.07x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.65 us: 1.08x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.18 ms: 1.08x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 394 us: 1.08x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                  |
| crypto_pyaes               | 86.6 ms                                                               | 93.7 ms: 1.08x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 108 ms: 1.09x slower                                                    |
| meteor_contest             | 112 ms                                                                | 125 ms: 1.12x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.82 ms: 1.12x slower                                                   |
| json                       | 5.54 ms                                                               | 6.22 ms: 1.12x slower                                                   |
| fannkuch                   | 443 ms                                                                | 499 ms: 1.12x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.03 ms: 1.14x slower                                                   |
| nbody                      | 105 ms                                                                | 119 ms: 1.14x slower                                                    |
| json_loads                 | 30.7 us                                                               | 35.3 us: 1.15x slower                                                   |
| pickle                     | 13.4 us                                                               | 15.5 us: 1.15x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.3 ms: 1.17x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 214 us: 1.19x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.14 sec: 1.25x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.37 sec: 1.26x slower                                                  |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.75 ms: 1.54x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.71 ms: 1.93x slower                                                   |
| logging_silent             | 127 ns                                                                | 629 ns: 4.96x slower                                                    |
| coverage                   | 87.3 ms                                                               | 545 ms: 6.24x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.40 sec: 197.90x slower                                                |
| thrift                     | 937 us                                                                | 194 ms: 206.58x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.14x slower                                                            |

Benchmark hidden because not significant (16): sympy_sum, sympy_integrate, scimark_sor, sympy_str, chaos, genshi_text, django_template, xml_etree_process, unpickle, unpickle_pure_python, scimark_lu, scimark_fft, pidigits, regex_v8, spectral_norm, sqlite_synth
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.054x slower

# HPT report

- Reliability score: 94.55% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x