# Results vs. base

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: linux-aarch64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.008x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250301-3.14.0a5+-c9932a9/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json | results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| html5lib       | 64.2 ms                                                                                                             | 60.4 ms: 1.06x faster                                                                                                     |
| sphinx         | 1.18 sec                                                                                                            | 1.14 sec: 1.03x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250301-3.14.0a5+-c9932a9/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json | results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_generators           | 451 ms                                                                                                              | 417 ms: 1.08x faster                                                                                                      |
| async_tree_io_tg           | 922 ms                                                                                                              | 883 ms: 1.04x faster                                                                                                      |
| async_tree_none            | 380 ms                                                                                                              | 371 ms: 1.03x faster                                                                                                      |
| async_tree_cpu_io_mixed_tg | 668 ms                                                                                                              | 727 ms: 1.09x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 677 ms                                                                                                              | 749 ms: 1.11x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.00x faster                                                                                                              |

Benchmark hidden because not significant (8): coroutines, async_tree_memoization_tg, async_tree_memoization, async_tree_io, asyncio_tcp_ssl, async_tree_none_tg, asyncio_websockets, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250301-3.14.0a5+-c9932a9/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json | results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 241 ms                                                                                                              | 293 ms: 1.22x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.07x slower                                                                                                              |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250301-3.14.0a5+-c9932a9/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json | results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                                                                             | 4.32 ms: 1.08x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (3): regex_compile, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250301-3.14.0a5+-c9932a9/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json | results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json |
|---------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list       | 6.43 us                                                                                                             | 5.89 us: 1.09x faster                                                                                                     |
| pickle_list         | 6.00 us                                                                                                             | 5.56 us: 1.08x faster                                                                                                     |
| xml_etree_process   | 82.2 ms                                                                                                             | 76.3 ms: 1.08x faster                                                                                                     |
| pickle              | 16.0 us                                                                                                             | 15.0 us: 1.06x faster                                                                                                     |
| json_loads          | 35.6 us                                                                                                             | 33.6 us: 1.06x faster                                                                                                     |
| pickle_dict         | 39.4 us                                                                                                             | 37.2 us: 1.06x faster                                                                                                     |
| tomli_loads         | 2.56 sec                                                                                                            | 2.45 sec: 1.05x faster                                                                                                    |
| xml_etree_iterparse | 144 ms                                                                                                              | 154 ms: 1.07x slower                                                                                                      |
| xml_etree_parse     | 188 ms                                                                                                              | 212 ms: 1.13x slower                                                                                                      |
| Geometric mean      | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (5): xml_etree_generate, unpickle, unpickle_pure_python, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250301-3.14.0a5+-c9932a9/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json | results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| django_template | 40.2 ms                                                                                                             | 37.7 ms: 1.07x faster                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.04x faster                                                                                                              |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | results/bm-20250301-3.14.0a5+-c9932a9/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json | results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| logging_silent             | 136 ns                                                                                                              | 119 ns: 1.14x faster                                                                                                      |
| sympy_integrate            | 22.6 ms                                                                                                             | 20.3 ms: 1.11x faster                                                                                                     |
| comprehensions             | 21.6 us                                                                                                             | 19.7 us: 1.10x faster                                                                                                     |
| richards                   | 53.7 ms                                                                                                             | 48.9 ms: 1.10x faster                                                                                                     |
| deepcopy                   | 343 us                                                                                                              | 313 us: 1.10x faster                                                                                                      |
| scimark_sor                | 155 ms                                                                                                              | 142 ms: 1.09x faster                                                                                                      |
| unpickle_list              | 6.43 us                                                                                                             | 5.89 us: 1.09x faster                                                                                                     |
| scimark_fft                | 423 ms                                                                                                              | 388 ms: 1.09x faster                                                                                                      |
| deepcopy_memo              | 40.3 us                                                                                                             | 37.0 us: 1.09x faster                                                                                                     |
| async_generators           | 451 ms                                                                                                              | 417 ms: 1.08x faster                                                                                                      |
| spectral_norm              | 121 ms                                                                                                              | 112 ms: 1.08x faster                                                                                                      |
| pickle_list                | 6.00 us                                                                                                             | 5.56 us: 1.08x faster                                                                                                     |
| xml_etree_process          | 82.2 ms                                                                                                             | 76.3 ms: 1.08x faster                                                                                                     |
| scimark_sparse_mat_mult    | 6.50 ms                                                                                                             | 6.07 ms: 1.07x faster                                                                                                     |
| logging_simple             | 7.37 us                                                                                                             | 6.90 us: 1.07x faster                                                                                                     |
| django_template            | 40.2 ms                                                                                                             | 37.7 ms: 1.07x faster                                                                                                     |
| deepcopy_reduce            | 3.57 us                                                                                                             | 3.35 us: 1.07x faster                                                                                                     |
| pickle                     | 16.0 us                                                                                                             | 15.0 us: 1.06x faster                                                                                                     |
| html5lib                   | 64.2 ms                                                                                                             | 60.4 ms: 1.06x faster                                                                                                     |
| json_loads                 | 35.6 us                                                                                                             | 33.6 us: 1.06x faster                                                                                                     |
| pickle_dict                | 39.4 us                                                                                                             | 37.2 us: 1.06x faster                                                                                                     |
| sqlglot_transpile          | 1.80 ms                                                                                                             | 1.70 ms: 1.06x faster                                                                                                     |
| go                         | 142 ms                                                                                                              | 135 ms: 1.05x faster                                                                                                      |
| tomli_loads                | 2.56 sec                                                                                                            | 2.45 sec: 1.05x faster                                                                                                    |
| async_tree_io_tg           | 922 ms                                                                                                              | 883 ms: 1.04x faster                                                                                                      |
| mdp                        | 3.38 sec                                                                                                            | 3.24 sec: 1.04x faster                                                                                                    |
| pyflate                    | 556 ms                                                                                                              | 537 ms: 1.03x faster                                                                                                      |
| pathlib                    | 22.1 ms                                                                                                             | 21.3 ms: 1.03x faster                                                                                                     |
| sphinx                     | 1.18 sec                                                                                                            | 1.14 sec: 1.03x faster                                                                                                    |
| async_tree_none            | 380 ms                                                                                                              | 371 ms: 1.03x faster                                                                                                      |
| bpe_tokeniser              | 5.59 sec                                                                                                            | 5.46 sec: 1.02x faster                                                                                                    |
| xml_etree_iterparse        | 144 ms                                                                                                              | 154 ms: 1.07x slower                                                                                                      |
| regex_effbot               | 3.99 ms                                                                                                             | 4.32 ms: 1.08x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 668 ms                                                                                                              | 727 ms: 1.09x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 677 ms                                                                                                              | 749 ms: 1.11x slower                                                                                                      |
| unpack_sequence            | 63.4 ns                                                                                                             | 70.4 ns: 1.11x slower                                                                                                     |
| xml_etree_parse            | 188 ms                                                                                                              | 212 ms: 1.13x slower                                                                                                      |
| pidigits                   | 241 ms                                                                                                              | 293 ms: 1.22x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (66): bench_mp_pool, thrift, xml_etree_generate, scimark_monte_carlo, typing_runtime_protocols, nqueens, coverage, sympy_sum, telco, genshi_text, bench_thread_pool, coroutines, unpickle, genshi_xml, scimark_lu, nbody, regex_compile, logging_format, raytrace, sqlglot_normalize, sqlalchemy_declarative, unpickle_pure_python, sqlglot_parse, pylint, pprint_safe_repr, sympy_str, async_tree_memoization_tg, json, async_tree_memoization, pprint_pformat, chaos, sqlglot_optimize, pycparser, sympy_expand, hexiom, dulwich_log, async_tree_io, regex_dna, richards_super, pickle_pure_python, k_core, sqlalchemy_imperative, gc_traversal, asyncio_tcp_ssl, sqlite_synth, async_tree_none_tg, crypto_pyaes, docutils, many_optionals, 2to3, json_dumps, mako, python_startup, python_startup_no_site, connected_components, asyncio_websockets, deltablue, fannkuch, shortest_path, create_gc_cycles, regex_v8, generators, float, asyncio_tcp, subparsers, meteor_contest

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x