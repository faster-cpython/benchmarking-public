# Results vs. base

- fork: python
- ref: ec12559ebafca01ded22
- machine: linux-x86_64
- commit hash: ec12559
- commit date: 2025-06-03
- overall geometric mean: 1.387x faster
- HPT reliability: 95.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250603-3.15.0a0-ec12559/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json | results/bm-20250603-3.15.0a0-ec12559-JIT/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                                                          | 260 ms: 1.02x slower                                                                                                |
| docutils       | 2.58 sec                                                                                                        | 2.64 sec: 1.02x slower                                                                                              |
| Geometric mean | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250603-3.15.0a0-ec12559/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json | results/bm-20250603-3.15.0a0-ec12559-JIT/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 318 ms                                                                                                          | 311 ms: 1.02x faster                                                                                                |
| coroutines                 | 26.0 ms                                                                                                         | 25.5 ms: 1.02x faster                                                                                               |
| async_tree_none_tg         | 252 ms                                                                                                          | 250 ms: 1.01x faster                                                                                                |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                                                          | 497 ms: 1.02x slower                                                                                                |
| async_tree_cpu_io_mixed    | 494 ms                                                                                                          | 506 ms: 1.02x slower                                                                                                |
| async_generators           | 416 ms                                                                                                          | 430 ms: 1.03x slower                                                                                                |
| Geometric mean             | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_io, asyncio_websockets, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250603-3.15.0a0-ec12559/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json | results/bm-20250603-3.15.0a0-ec12559-JIT/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 71.5 ms                                                                                                         | 64.5 ms: 1.11x faster                                                                                               |
| nbody          | 98.1 ms                                                                                                         | 91.8 ms: 1.07x faster                                                                                               |
| pidigits       | 187 ms                                                                                                          | 191 ms: 1.02x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.05x faster                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250603-3.15.0a0-ec12559/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json | results/bm-20250603-3.15.0a0-ec12559-JIT/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 23.2 ms                                                                                                         | 22.1 ms: 1.05x faster                                                                                               |
| regex_effbot   | 3.22 ms                                                                                                         | 3.24 ms: 1.01x slower                                                                                               |
| regex_dna      | 194 ms                                                                                                          | 197 ms: 1.02x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250603-3.15.0a0-ec12559/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json | results/bm-20250603-3.15.0a0-ec12559-JIT/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 220 us                                                                                                          | 200 us: 1.10x faster                                                                                                |
| xml_etree_process    | 60.0 ms                                                                                                         | 55.8 ms: 1.08x faster                                                                                               |
| xml_etree_generate   | 85.9 ms                                                                                                         | 80.1 ms: 1.07x faster                                                                                               |
| tomli_loads          | 2.01 sec                                                                                                        | 1.89 sec: 1.06x faster                                                                                              |
| xml_etree_iterparse  | 99.4 ms                                                                                                         | 97.4 ms: 1.02x faster                                                                                               |
| xml_etree_parse      | 142 ms                                                                                                          | 140 ms: 1.02x faster                                                                                                |
| json_dumps           | 10.9 ms                                                                                                         | 11.0 ms: 1.01x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.04x faster                                                                                                        |

Benchmark hidden because not significant (2): json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250603-3.15.0a0-ec12559/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json | results/bm-20250603-3.15.0a0-ec12559-JIT/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                                                                         | 12.2 ms: 1.00x slower                                                                                               |
| python_startup_no_site | 6.95 ms                                                                                                         | 6.98 ms: 1.00x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250603-3.15.0a0-ec12559/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json | results/bm-20250603-3.15.0a0-ec12559-JIT/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako           | 11.3 ms                                                                                                         | 10.8 ms: 1.05x faster                                                                                               |
| genshi_text    | 21.4 ms                                                                                                         | 21.3 ms: 1.01x faster                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.02x faster                                                                                                        |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250603-3.15.0a0-ec12559/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json | results/bm-20250603-3.15.0a0-ec12559-JIT/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| pprint_pformat             | 1.66 sec                                                                                                        | 1.45 us: 1141163.77x faster                                                                                         |
| pprint_safe_repr           | 812 ms                                                                                                          | 829 ns: 979692.37x faster                                                                                           |
| richards                   | 43.4 ms                                                                                                         | 33.4 ms: 1.30x faster                                                                                               |
| richards_super             | 49.6 ms                                                                                                         | 39.4 ms: 1.26x faster                                                                                               |
| deltablue                  | 3.52 ms                                                                                                         | 3.06 ms: 1.15x faster                                                                                               |
| scimark_fft                | 380 ms                                                                                                          | 332 ms: 1.14x faster                                                                                                |
| float                      | 71.5 ms                                                                                                         | 64.5 ms: 1.11x faster                                                                                               |
| unpickle_pure_python       | 220 us                                                                                                          | 200 us: 1.10x faster                                                                                                |
| spectral_norm              | 109 ms                                                                                                          | 100 ms: 1.09x faster                                                                                                |
| xml_etree_process          | 60.0 ms                                                                                                         | 55.8 ms: 1.08x faster                                                                                               |
| xml_etree_generate         | 85.9 ms                                                                                                         | 80.1 ms: 1.07x faster                                                                                               |
| nbody                      | 98.1 ms                                                                                                         | 91.8 ms: 1.07x faster                                                                                               |
| tomli_loads                | 2.01 sec                                                                                                        | 1.89 sec: 1.06x faster                                                                                              |
| shortest_path              | 523 ms                                                                                                          | 494 ms: 1.06x faster                                                                                                |
| connected_components       | 479 ms                                                                                                          | 453 ms: 1.06x faster                                                                                                |
| regex_v8                   | 23.2 ms                                                                                                         | 22.1 ms: 1.05x faster                                                                                               |
| mako                       | 11.3 ms                                                                                                         | 10.8 ms: 1.05x faster                                                                                               |
| pyflate                    | 432 ms                                                                                                          | 413 ms: 1.04x faster                                                                                                |
| bpe_tokeniser              | 4.53 sec                                                                                                        | 4.37 sec: 1.04x faster                                                                                              |
| scimark_sparse_mat_mult    | 5.12 ms                                                                                                         | 4.96 ms: 1.03x faster                                                                                               |
| deepcopy_reduce            | 2.73 us                                                                                                         | 2.65 us: 1.03x faster                                                                                               |
| sqlite_synth               | 2.87 us                                                                                                         | 2.80 us: 1.03x faster                                                                                               |
| async_tree_memoization_tg  | 318 ms                                                                                                          | 311 ms: 1.02x faster                                                                                                |
| scimark_lu                 | 118 ms                                                                                                          | 116 ms: 1.02x faster                                                                                                |
| xml_etree_iterparse        | 99.4 ms                                                                                                         | 97.4 ms: 1.02x faster                                                                                               |
| xml_etree_parse            | 142 ms                                                                                                          | 140 ms: 1.02x faster                                                                                                |
| generators                 | 30.5 ms                                                                                                         | 30.0 ms: 1.02x faster                                                                                               |
| gc_traversal               | 5.00 ms                                                                                                         | 4.91 ms: 1.02x faster                                                                                               |
| coroutines                 | 26.0 ms                                                                                                         | 25.5 ms: 1.02x faster                                                                                               |
| deepcopy                   | 257 us                                                                                                          | 253 us: 1.02x faster                                                                                                |
| pathlib                    | 17.2 ms                                                                                                         | 16.9 ms: 1.01x faster                                                                                               |
| scimark_monte_carlo        | 67.9 ms                                                                                                         | 66.9 ms: 1.01x faster                                                                                               |
| logging_simple             | 6.17 us                                                                                                         | 6.09 us: 1.01x faster                                                                                               |
| coverage                   | 426 ms                                                                                                          | 422 ms: 1.01x faster                                                                                                |
| json                       | 5.15 ms                                                                                                         | 5.10 ms: 1.01x faster                                                                                               |
| logging_silent             | 475 ns                                                                                                          | 471 ns: 1.01x faster                                                                                                |
| async_tree_none_tg         | 252 ms                                                                                                          | 250 ms: 1.01x faster                                                                                                |
| logging_format             | 6.81 us                                                                                                         | 6.74 us: 1.01x faster                                                                                               |
| genshi_text                | 21.4 ms                                                                                                         | 21.3 ms: 1.01x faster                                                                                               |
| sqlglot_v2_optimize        | 52.2 ms                                                                                                         | 52.1 ms: 1.00x faster                                                                                               |
| python_startup             | 12.2 ms                                                                                                         | 12.2 ms: 1.00x slower                                                                                               |
| sqlglot_v2_normalize       | 105 ms                                                                                                          | 106 ms: 1.00x slower                                                                                                |
| python_startup_no_site     | 6.95 ms                                                                                                         | 6.98 ms: 1.00x slower                                                                                               |
| regex_effbot               | 3.22 ms                                                                                                         | 3.24 ms: 1.01x slower                                                                                               |
| deepcopy_memo              | 29.3 us                                                                                                         | 29.6 us: 1.01x slower                                                                                               |
| fannkuch                   | 417 ms                                                                                                          | 421 ms: 1.01x slower                                                                                                |
| crypto_pyaes               | 75.5 ms                                                                                                         | 76.3 ms: 1.01x slower                                                                                               |
| sqlglot_v2_transpile       | 1.57 ms                                                                                                         | 1.58 ms: 1.01x slower                                                                                               |
| meteor_contest             | 105 ms                                                                                                          | 106 ms: 1.01x slower                                                                                                |
| sympy_str                  | 267 ms                                                                                                          | 271 ms: 1.01x slower                                                                                                |
| json_dumps                 | 10.9 ms                                                                                                         | 11.0 ms: 1.01x slower                                                                                               |
| chaos                      | 61.0 ms                                                                                                         | 61.9 ms: 1.01x slower                                                                                               |
| many_optionals             | 958 us                                                                                                          | 973 us: 1.02x slower                                                                                                |
| sympy_integrate            | 19.0 ms                                                                                                         | 19.4 ms: 1.02x slower                                                                                               |
| nqueens                    | 81.6 ms                                                                                                         | 83.2 ms: 1.02x slower                                                                                               |
| regex_dna                  | 194 ms                                                                                                          | 197 ms: 1.02x slower                                                                                                |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                                                          | 497 ms: 1.02x slower                                                                                                |
| dulwich_log                | 59.7 ms                                                                                                         | 60.9 ms: 1.02x slower                                                                                               |
| pidigits                   | 187 ms                                                                                                          | 191 ms: 1.02x slower                                                                                                |
| docutils                   | 2.58 sec                                                                                                        | 2.64 sec: 1.02x slower                                                                                              |
| typing_runtime_protocols   | 166 us                                                                                                          | 170 us: 1.02x slower                                                                                                |
| 2to3                       | 255 ms                                                                                                          | 260 ms: 1.02x slower                                                                                                |
| async_tree_cpu_io_mixed    | 494 ms                                                                                                          | 506 ms: 1.02x slower                                                                                                |
| sympy_expand               | 452 ms                                                                                                          | 463 ms: 1.03x slower                                                                                                |
| async_generators           | 416 ms                                                                                                          | 430 ms: 1.03x slower                                                                                                |
| comprehensions             | 16.0 us                                                                                                         | 17.0 us: 1.06x slower                                                                                               |
| hexiom                     | 6.04 ms                                                                                                         | 6.48 ms: 1.07x slower                                                                                               |
| go                         | 112 ms                                                                                                          | 123 ms: 1.10x slower                                                                                                |
| Geometric mean             | (ref)                                                                                                           | 1.38x faster                                                                                                        |

Benchmark hidden because not significant (23): pycparser, telco, genshi_xml, async_tree_memoization, html5lib, async_tree_io, json_loads, django_template, subparsers, scimark_sor, create_gc_cycles, mdp, thrift, sympy_sum, asyncio_websockets, sqlglot_v2_parse, async_tree_none, pickle_pure_python, k_core, raytrace, sphinx, async_tree_io_tg, pylint
Ignored benchmarks (1) of results/bm-20250603-3.15.0a0-ec12559/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json: regex_compile

- Geometric mean (including insignificant results): 1.387x faster

# HPT report

- Reliability score: 95.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x