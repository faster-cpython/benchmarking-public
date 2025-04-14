# Results vs. base

- fork: brandtbucher
- ref: remove_optimizer_api
- machine: linux-x86_64
- commit hash: 085e172
- commit date: 2025-01-21
- overall geometric mean: 1.002x slower
- HPT reliability: 63.41%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                                       |
| html5lib       | 61.7 ms                                                                | 60.8 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 585 ms                                                                 | 591 ms: 1.01x slower                                                         |
| async_generators           | 384 ms                                                                 | 388 ms: 1.01x slower                                                         |
| async_tree_none_tg         | 248 ms                                                                 | 251 ms: 1.01x slower                                                         |
| async_tree_memoization_tg  | 305 ms                                                                 | 310 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed    | 480 ms                                                                 | 491 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 461 ms                                                                 | 473 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (5): asyncio_websockets, coroutines, async_tree_none, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 95.1 ms                                                                | 92.9 ms: 1.02x faster                                                        |
| pidigits       | 187 ms                                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                                | 25.0 ms: 1.04x faster                                                        |
| regex_dna      | 211 ms                                                                 | 208 ms: 1.01x faster                                                         |
| regex_compile  | 127 ms                                                                 | 128 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse | 98.1 ms                                                                | 97.2 ms: 1.01x faster                                                        |
| json_dumps          | 12.0 ms                                                                | 11.9 ms: 1.01x faster                                                        |
| xml_etree_generate  | 84.4 ms                                                                | 83.8 ms: 1.01x faster                                                        |
| xml_etree_process   | 61.7 ms                                                                | 61.4 ms: 1.00x faster                                                        |
| json_loads          | 28.8 us                                                                | 29.0 us: 1.01x slower                                                        |
| pickle_pure_python  | 328 us                                                                 | 331 us: 1.01x slower                                                         |
| xml_etree_parse     | 138 ms                                                                 | 140 ms: 1.01x slower                                                         |
| tomli_loads         | 1.96 sec                                                               | 1.99 sec: 1.01x slower                                                       |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                        |
| python_startup_no_site | 7.04 ms                                                                | 7.08 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 32.4 ms                                                                | 31.8 ms: 1.02x faster                                                        |
| genshi_text     | 21.8 ms                                                                | 22.2 ms: 1.01x slower                                                        |
| mako            | 11.0 ms                                                                | 11.3 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| logging_silent             | 107 ns                                                                 | 100.0 ns: 1.07x faster                                                       |
| regex_v8                   | 26.0 ms                                                                | 25.0 ms: 1.04x faster                                                        |
| nbody                      | 95.1 ms                                                                | 92.9 ms: 1.02x faster                                                        |
| scimark_lu                 | 117 ms                                                                 | 115 ms: 1.02x faster                                                         |
| django_template            | 32.4 ms                                                                | 31.8 ms: 1.02x faster                                                        |
| html5lib                   | 61.7 ms                                                                | 60.8 ms: 1.02x faster                                                        |
| nqueens                    | 79.9 ms                                                                | 78.7 ms: 1.02x faster                                                        |
| coverage                   | 91.1 ms                                                                | 89.8 ms: 1.01x faster                                                        |
| regex_dna                  | 211 ms                                                                 | 208 ms: 1.01x faster                                                         |
| comprehensions             | 17.0 us                                                                | 16.8 us: 1.01x faster                                                        |
| meteor_contest             | 108 ms                                                                 | 106 ms: 1.01x faster                                                         |
| pprint_pformat             | 1.49 sec                                                               | 1.47 sec: 1.01x faster                                                       |
| richards                   | 44.2 ms                                                                | 43.8 ms: 1.01x faster                                                        |
| logging_format             | 6.31 us                                                                | 6.25 us: 1.01x faster                                                        |
| xml_etree_iterparse        | 98.1 ms                                                                | 97.2 ms: 1.01x faster                                                        |
| scimark_sor                | 120 ms                                                                 | 119 ms: 1.01x faster                                                         |
| logging_simple             | 5.70 us                                                                | 5.65 us: 1.01x faster                                                        |
| json_dumps                 | 12.0 ms                                                                | 11.9 ms: 1.01x faster                                                        |
| dulwich_log                | 65.0 ms                                                                | 64.5 ms: 1.01x faster                                                        |
| deltablue                  | 3.19 ms                                                                | 3.16 ms: 1.01x faster                                                        |
| xml_etree_generate         | 84.4 ms                                                                | 83.8 ms: 1.01x faster                                                        |
| json                       | 5.21 ms                                                                | 5.18 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.01x faster                                                         |
| xml_etree_process          | 61.7 ms                                                                | 61.4 ms: 1.00x faster                                                        |
| pprint_safe_repr           | 730 ms                                                                 | 727 ms: 1.00x faster                                                         |
| go                         | 116 ms                                                                 | 116 ms: 1.00x faster                                                         |
| sqlglot_transpile          | 1.56 ms                                                                | 1.56 ms: 1.00x faster                                                        |
| docutils                   | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                                       |
| sqlalchemy_declarative     | 131 ms                                                                 | 131 ms: 1.00x faster                                                         |
| sqlglot_parse              | 1.26 ms                                                                | 1.25 ms: 1.00x faster                                                        |
| raytrace                   | 272 ms                                                                 | 272 ms: 1.00x faster                                                         |
| regex_compile              | 127 ms                                                                 | 128 ms: 1.00x slower                                                         |
| python_startup             | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                        |
| sqlglot_optimize           | 52.9 ms                                                                | 53.0 ms: 1.00x slower                                                        |
| sqlglot_normalize          | 105 ms                                                                 | 105 ms: 1.00x slower                                                         |
| create_gc_cycles           | 2.44 ms                                                                | 2.45 ms: 1.00x slower                                                        |
| mdp                        | 2.48 sec                                                               | 2.49 sec: 1.00x slower                                                       |
| many_optionals             | 945 us                                                                 | 950 us: 1.00x slower                                                         |
| json_loads                 | 28.8 us                                                                | 29.0 us: 1.01x slower                                                        |
| python_startup_no_site     | 7.04 ms                                                                | 7.08 ms: 1.01x slower                                                        |
| pyflate                    | 463 ms                                                                 | 466 ms: 1.01x slower                                                         |
| bpe_tokeniser              | 4.49 sec                                                               | 4.52 sec: 1.01x slower                                                       |
| pickle_pure_python         | 328 us                                                                 | 331 us: 1.01x slower                                                         |
| deepcopy                   | 255 us                                                                 | 257 us: 1.01x slower                                                         |
| async_tree_io_tg           | 585 ms                                                                 | 591 ms: 1.01x slower                                                         |
| thrift                     | 776 us                                                                 | 784 us: 1.01x slower                                                         |
| async_generators           | 384 ms                                                                 | 388 ms: 1.01x slower                                                         |
| xml_etree_parse            | 138 ms                                                                 | 140 ms: 1.01x slower                                                         |
| async_tree_none_tg         | 248 ms                                                                 | 251 ms: 1.01x slower                                                         |
| hexiom                     | 6.15 ms                                                                | 6.23 ms: 1.01x slower                                                        |
| tomli_loads                | 1.96 sec                                                               | 1.99 sec: 1.01x slower                                                       |
| genshi_text                | 21.8 ms                                                                | 22.2 ms: 1.01x slower                                                        |
| deepcopy_reduce            | 2.61 us                                                                | 2.65 us: 1.02x slower                                                        |
| async_tree_memoization_tg  | 305 ms                                                                 | 310 ms: 1.02x slower                                                         |
| crypto_pyaes               | 71.8 ms                                                                | 73.0 ms: 1.02x slower                                                        |
| deepcopy_memo              | 30.7 us                                                                | 31.2 us: 1.02x slower                                                        |
| chaos                      | 58.2 ms                                                                | 59.4 ms: 1.02x slower                                                        |
| pathlib                    | 15.9 ms                                                                | 16.2 ms: 1.02x slower                                                        |
| subparsers                 | 20.4 ms                                                                | 20.9 ms: 1.02x slower                                                        |
| spectral_norm              | 100 ms                                                                 | 102 ms: 1.02x slower                                                         |
| scimark_sparse_mat_mult    | 4.52 ms                                                                | 4.61 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed    | 480 ms                                                                 | 491 ms: 1.02x slower                                                         |
| fannkuch                   | 398 ms                                                                 | 407 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 461 ms                                                                 | 473 ms: 1.03x slower                                                         |
| scimark_monte_carlo        | 66.4 ms                                                                | 68.3 ms: 1.03x slower                                                        |
| mako                       | 11.0 ms                                                                | 11.3 ms: 1.03x slower                                                        |
| gc_traversal               | 4.61 ms                                                                | 4.77 ms: 1.04x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (29): k_core, unpickle_pure_python, sympy_str, telco, connected_components, sympy_sum, scimark_fft, sphinx, generators, richards_super, pylint, sympy_expand, asyncio_websockets, sympy_integrate, bench_thread_pool, typing_runtime_protocols, sqlalchemy_imperative, sqlite_synth, coroutines, 2to3, bench_mp_pool, pycparser, async_tree_none, shortest_path, regex_effbot, genshi_xml, async_tree_memoization, async_tree_io, float

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 63.41% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x