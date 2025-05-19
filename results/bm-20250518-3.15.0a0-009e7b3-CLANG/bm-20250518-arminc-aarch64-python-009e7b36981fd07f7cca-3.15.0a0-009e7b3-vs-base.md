# Results vs. base

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-aarch64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.004x slower
- HPT reliability: 87.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 299 ms                                                                                                            | 301 ms: 1.01x slower                                                                                                    |
| docutils       | 2.94 sec                                                                                                          | 3.01 sec: 1.02x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.00x faster                                                                                                            |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_generators           | 449 ms                                                                                                            | 429 ms: 1.05x faster                                                                                                    |
| coroutines                 | 29.5 ms                                                                                                           | 28.6 ms: 1.03x faster                                                                                                   |
| async_tree_memoization_tg  | 467 ms                                                                                                            | 453 ms: 1.03x faster                                                                                                    |
| async_tree_none_tg         | 373 ms                                                                                                            | 364 ms: 1.02x faster                                                                                                    |
| async_tree_none            | 392 ms                                                                                                            | 384 ms: 1.02x faster                                                                                                    |
| async_tree_memoization     | 461 ms                                                                                                            | 454 ms: 1.02x faster                                                                                                    |
| async_tree_io_tg           | 903 ms                                                                                                            | 894 ms: 1.01x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 654 ms                                                                                                            | 715 ms: 1.09x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 649 ms                                                                                                            | 721 ms: 1.11x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.00x slower                                                                                                            |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_io, asyncio_tcp_ssl, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| nbody          | 122 ms                                                                                                            | 128 ms: 1.05x slower                                                                                                    |
| pidigits       | 238 ms                                                                                                            | 292 ms: 1.23x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.09x slower                                                                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 231 ms                                                                                                            | 246 ms: 1.06x slower                                                                                                    |
| regex_v8       | 28.2 ms                                                                                                           | 32.5 ms: 1.15x slower                                                                                                   |
| regex_effbot   | 3.82 ms                                                                                                           | 4.50 ms: 1.18x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                             | 1.09x slower                                                                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|---------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| unpickle_list       | 6.45 us                                                                                                           | 5.79 us: 1.11x faster                                                                                                   |
| unpickle            | 18.2 us                                                                                                           | 17.1 us: 1.07x faster                                                                                                   |
| xml_etree_generate  | 114 ms                                                                                                            | 108 ms: 1.06x faster                                                                                                    |
| pickle_dict         | 39.4 us                                                                                                           | 37.1 us: 1.06x faster                                                                                                   |
| json_loads          | 36.0 us                                                                                                           | 34.2 us: 1.05x faster                                                                                                   |
| xml_etree_process   | 79.3 ms                                                                                                           | 75.9 ms: 1.04x faster                                                                                                   |
| pickle_list         | 5.58 us                                                                                                           | 5.38 us: 1.04x faster                                                                                                   |
| tomli_loads         | 2.44 sec                                                                                                          | 2.41 sec: 1.02x faster                                                                                                  |
| pickle              | 15.2 us                                                                                                           | 15.1 us: 1.01x faster                                                                                                   |
| xml_etree_iterparse | 141 ms                                                                                                            | 148 ms: 1.05x slower                                                                                                    |
| xml_etree_parse     | 178 ms                                                                                                            | 204 ms: 1.15x slower                                                                                                    |
| Geometric mean      | (ref)                                                                                                             | 1.02x faster                                                                                                            |

Benchmark hidden because not significant (3): unpickle_pure_python, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.1 ms                                                                                                           | 15.3 ms: 1.02x slower                                                                                                   |
| python_startup_no_site | 8.62 ms                                                                                                           | 8.83 ms: 1.02x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.02x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| mako           | 13.9 ms                                                                                                           | 14.3 ms: 1.02x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (3): django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 4.22 sec                                                                                                          | 3.27 sec: 1.29x faster                                                                                                  |
| unpickle_list              | 6.45 us                                                                                                           | 5.79 us: 1.11x faster                                                                                                   |
| scimark_lu                 | 148 ms                                                                                                            | 134 ms: 1.10x faster                                                                                                    |
| scimark_fft                | 439 ms                                                                                                            | 400 ms: 1.10x faster                                                                                                    |
| chaos                      | 70.3 ms                                                                                                           | 65.5 ms: 1.07x faster                                                                                                   |
| unpickle                   | 18.2 us                                                                                                           | 17.1 us: 1.07x faster                                                                                                   |
| deepcopy_memo              | 38.0 us                                                                                                           | 35.7 us: 1.06x faster                                                                                                   |
| xml_etree_generate         | 114 ms                                                                                                            | 108 ms: 1.06x faster                                                                                                    |
| spectral_norm              | 130 ms                                                                                                            | 122 ms: 1.06x faster                                                                                                    |
| pickle_dict                | 39.4 us                                                                                                           | 37.1 us: 1.06x faster                                                                                                   |
| bpe_tokeniser              | 5.56 sec                                                                                                          | 5.24 sec: 1.06x faster                                                                                                  |
| generators                 | 37.5 ms                                                                                                           | 35.5 ms: 1.06x faster                                                                                                   |
| json_loads                 | 36.0 us                                                                                                           | 34.2 us: 1.05x faster                                                                                                   |
| scimark_monte_carlo        | 82.9 ms                                                                                                           | 78.8 ms: 1.05x faster                                                                                                   |
| async_generators           | 449 ms                                                                                                            | 429 ms: 1.05x faster                                                                                                    |
| scimark_sparse_mat_mult    | 6.99 ms                                                                                                           | 6.67 ms: 1.05x faster                                                                                                   |
| dulwich_log                | 54.7 ms                                                                                                           | 52.3 ms: 1.05x faster                                                                                                   |
| xml_etree_process          | 79.3 ms                                                                                                           | 75.9 ms: 1.04x faster                                                                                                   |
| pathlib                    | 22.8 ms                                                                                                           | 21.9 ms: 1.04x faster                                                                                                   |
| json                       | 6.11 ms                                                                                                           | 5.89 ms: 1.04x faster                                                                                                   |
| pickle_list                | 5.58 us                                                                                                           | 5.38 us: 1.04x faster                                                                                                   |
| coroutines                 | 29.5 ms                                                                                                           | 28.6 ms: 1.03x faster                                                                                                   |
| async_tree_memoization_tg  | 467 ms                                                                                                            | 453 ms: 1.03x faster                                                                                                    |
| coverage                   | 548 ms                                                                                                            | 535 ms: 1.02x faster                                                                                                    |
| async_tree_none_tg         | 373 ms                                                                                                            | 364 ms: 1.02x faster                                                                                                    |
| async_tree_none            | 392 ms                                                                                                            | 384 ms: 1.02x faster                                                                                                    |
| sqlglot_v2_transpile       | 1.74 ms                                                                                                           | 1.71 ms: 1.02x faster                                                                                                   |
| async_tree_memoization     | 461 ms                                                                                                            | 454 ms: 1.02x faster                                                                                                    |
| tomli_loads                | 2.44 sec                                                                                                          | 2.41 sec: 1.02x faster                                                                                                  |
| async_tree_io_tg           | 903 ms                                                                                                            | 894 ms: 1.01x faster                                                                                                    |
| pickle                     | 15.2 us                                                                                                           | 15.1 us: 1.01x faster                                                                                                   |
| logging_format             | 8.27 us                                                                                                           | 8.22 us: 1.01x faster                                                                                                   |
| 2to3                       | 299 ms                                                                                                            | 301 ms: 1.01x slower                                                                                                    |
| python_startup             | 15.1 ms                                                                                                           | 15.3 ms: 1.02x slower                                                                                                   |
| mako                       | 13.9 ms                                                                                                           | 14.3 ms: 1.02x slower                                                                                                   |
| docutils                   | 2.94 sec                                                                                                          | 3.01 sec: 1.02x slower                                                                                                  |
| pprint_safe_repr           | 905 ms                                                                                                            | 927 ms: 1.02x slower                                                                                                    |
| python_startup_no_site     | 8.62 ms                                                                                                           | 8.83 ms: 1.02x slower                                                                                                   |
| pprint_pformat             | 1.85 sec                                                                                                          | 1.90 sec: 1.03x slower                                                                                                  |
| meteor_contest             | 114 ms                                                                                                            | 118 ms: 1.03x slower                                                                                                    |
| fannkuch                   | 466 ms                                                                                                            | 482 ms: 1.03x slower                                                                                                    |
| pylint                     | 307 ms                                                                                                            | 321 ms: 1.05x slower                                                                                                    |
| xml_etree_iterparse        | 141 ms                                                                                                            | 148 ms: 1.05x slower                                                                                                    |
| nbody                      | 122 ms                                                                                                            | 128 ms: 1.05x slower                                                                                                    |
| regex_dna                  | 231 ms                                                                                                            | 246 ms: 1.06x slower                                                                                                    |
| logging_silent             | 604 ns                                                                                                            | 647 ns: 1.07x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 654 ms                                                                                                            | 715 ms: 1.09x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 649 ms                                                                                                            | 721 ms: 1.11x slower                                                                                                    |
| xml_etree_parse            | 178 ms                                                                                                            | 204 ms: 1.15x slower                                                                                                    |
| regex_v8                   | 28.2 ms                                                                                                           | 32.5 ms: 1.15x slower                                                                                                   |
| regex_effbot               | 3.82 ms                                                                                                           | 4.50 ms: 1.18x slower                                                                                                   |
| pidigits                   | 238 ms                                                                                                            | 292 ms: 1.23x slower                                                                                                    |
| unpack_sequence            | 50.8 ns                                                                                                           | 71.7 ns: 1.41x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.00x faster                                                                                                            |

Benchmark hidden because not significant (49): deepcopy_reduce, typing_runtime_protocols, comprehensions, html5lib, sympy_sum, deepcopy, unpickle_pure_python, sympy_expand, sqlglot_v2_parse, richards_super, scimark_sor, sqlite_synth, thrift, json_dumps, gc_traversal, django_template, sqlglot_v2_optimize, regex_compile, pycparser, sympy_integrate, telco, richards, pyflate, subparsers, k_core, crypto_pyaes, genshi_xml, raytrace, sphinx, sympy_str, go, mdp, asyncio_websockets, async_tree_io, many_optionals, logging_simple, asyncio_tcp_ssl, hexiom, bench_thread_pool, shortest_path, nqueens, connected_components, float, sqlglot_v2_normalize, create_gc_cycles, asyncio_tcp, genshi_text, pickle_pure_python, deltablue

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 87.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x