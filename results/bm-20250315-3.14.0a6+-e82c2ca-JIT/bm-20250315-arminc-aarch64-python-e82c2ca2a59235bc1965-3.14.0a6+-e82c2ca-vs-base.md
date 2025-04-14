# Results vs. base

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.028x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 296 ms                                                                                                              | 309 ms: 1.04x slower                                                                                                    |
| docutils       | 2.99 sec                                                                                                            | 3.14 sec: 1.05x slower                                                                                                  |
| html5lib       | 64.3 ms                                                                                                             | 63.3 ms: 1.02x faster                                                                                                   |
| sphinx         | 1.14 sec                                                                                                            | 1.18 sec: 1.03x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.03x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|--------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg | 371 ms                                                                                                              | 375 ms: 1.01x slower                                                                                                    |
| async_tree_io_tg   | 911 ms                                                                                                              | 929 ms: 1.02x slower                                                                                                    |
| async_generators   | 451 ms                                                                                                              | 474 ms: 1.05x slower                                                                                                    |
| Geometric mean     | (ref)                                                                                                               | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (10): coroutines, asyncio_tcp_ssl, async_tree_io, asyncio_tcp, async_tree_cpu_io_mixed_tg, async_tree_memoization, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 87.7 ms                                                                                                             | 85.2 ms: 1.03x faster                                                                                                   |
| Geometric mean | (ref)                                                                                                               | 1.00x slower                                                                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 243 ms                                                                                                              | 239 ms: 1.02x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_process    | 80.2 ms                                                                                                             | 77.9 ms: 1.03x faster                                                                                                   |
| tomli_loads          | 2.50 sec                                                                                                            | 2.45 sec: 1.02x faster                                                                                                  |
| unpickle_list        | 6.39 us                                                                                                             | 6.33 us: 1.01x faster                                                                                                   |
| xml_etree_iterparse  | 141 ms                                                                                                              | 143 ms: 1.01x slower                                                                                                    |
| pickle_list          | 5.55 us                                                                                                             | 5.77 us: 1.04x slower                                                                                                   |
| pickle_pure_python   | 388 us                                                                                                              | 404 us: 1.04x slower                                                                                                    |
| unpickle_pure_python | 269 us                                                                                                              | 292 us: 1.09x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                               | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (7): xml_etree_generate, xml_etree_parse, json_loads, json_dumps, pickle_dict, pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup | 16.1 ms                                                                                                             | 16.1 ms: 1.00x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                               | 1.00x slower                                                                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| django_template | 40.5 ms                                                                                                             | 39.6 ms: 1.02x faster                                                                                                   |
| genshi_text     | 26.7 ms                                                                                                             | 26.9 ms: 1.01x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.00x faster                                                                                                            |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 2.92 sec                                                                                                            | 1.36 sec: 2.14x faster                                                                                                  |
| richards                 | 53.2 ms                                                                                                             | 50.8 ms: 1.05x faster                                                                                                   |
| richards_super           | 58.9 ms                                                                                                             | 56.5 ms: 1.04x faster                                                                                                   |
| xml_etree_process        | 80.2 ms                                                                                                             | 77.9 ms: 1.03x faster                                                                                                   |
| float                    | 87.7 ms                                                                                                             | 85.2 ms: 1.03x faster                                                                                                   |
| django_template          | 40.5 ms                                                                                                             | 39.6 ms: 1.02x faster                                                                                                   |
| coverage                 | 100 ms                                                                                                              | 98.1 ms: 1.02x faster                                                                                                   |
| tomli_loads              | 2.50 sec                                                                                                            | 2.45 sec: 1.02x faster                                                                                                  |
| sqlite_synth             | 3.82 us                                                                                                             | 3.75 us: 1.02x faster                                                                                                   |
| regex_dna                | 243 ms                                                                                                              | 239 ms: 1.02x faster                                                                                                    |
| html5lib                 | 64.3 ms                                                                                                             | 63.3 ms: 1.02x faster                                                                                                   |
| deepcopy_memo            | 37.9 us                                                                                                             | 37.4 us: 1.01x faster                                                                                                   |
| unpickle_list            | 6.39 us                                                                                                             | 6.33 us: 1.01x faster                                                                                                   |
| thrift                   | 949 us                                                                                                              | 942 us: 1.01x faster                                                                                                    |
| python_startup           | 16.1 ms                                                                                                             | 16.1 ms: 1.00x slower                                                                                                   |
| json                     | 5.85 ms                                                                                                             | 5.89 ms: 1.01x slower                                                                                                   |
| connected_components     | 560 ms                                                                                                              | 565 ms: 1.01x slower                                                                                                    |
| genshi_text              | 26.7 ms                                                                                                             | 26.9 ms: 1.01x slower                                                                                                   |
| async_tree_none_tg       | 371 ms                                                                                                              | 375 ms: 1.01x slower                                                                                                    |
| xml_etree_iterparse      | 141 ms                                                                                                              | 143 ms: 1.01x slower                                                                                                    |
| logging_simple           | 6.95 us                                                                                                             | 7.05 us: 1.02x slower                                                                                                   |
| logging_format           | 7.60 us                                                                                                             | 7.73 us: 1.02x slower                                                                                                   |
| async_tree_io_tg         | 911 ms                                                                                                              | 929 ms: 1.02x slower                                                                                                    |
| shortest_path            | 577 ms                                                                                                              | 591 ms: 1.02x slower                                                                                                    |
| k_core                   | 2.81 sec                                                                                                            | 2.87 sec: 1.02x slower                                                                                                  |
| gc_traversal             | 6.64 ms                                                                                                             | 6.81 ms: 1.03x slower                                                                                                   |
| sympy_integrate          | 21.2 ms                                                                                                             | 21.7 ms: 1.03x slower                                                                                                   |
| sqlglot_v2_normalize     | 127 ms                                                                                                              | 131 ms: 1.03x slower                                                                                                    |
| sphinx                   | 1.14 sec                                                                                                            | 1.18 sec: 1.03x slower                                                                                                  |
| raytrace                 | 322 ms                                                                                                              | 334 ms: 1.04x slower                                                                                                    |
| bench_thread_pool        | 1.33 ms                                                                                                             | 1.38 ms: 1.04x slower                                                                                                   |
| pickle_list              | 5.55 us                                                                                                             | 5.77 us: 1.04x slower                                                                                                   |
| pyflate                  | 569 ms                                                                                                              | 592 ms: 1.04x slower                                                                                                    |
| pickle_pure_python       | 388 us                                                                                                              | 404 us: 1.04x slower                                                                                                    |
| 2to3                     | 296 ms                                                                                                              | 309 ms: 1.04x slower                                                                                                    |
| telco                    | 9.49 ms                                                                                                             | 9.91 ms: 1.05x slower                                                                                                   |
| deltablue                | 3.95 ms                                                                                                             | 4.13 ms: 1.05x slower                                                                                                   |
| scimark_monte_carlo      | 84.5 ms                                                                                                             | 88.4 ms: 1.05x slower                                                                                                   |
| many_optionals           | 833 us                                                                                                              | 872 us: 1.05x slower                                                                                                    |
| docutils                 | 2.99 sec                                                                                                            | 3.14 sec: 1.05x slower                                                                                                  |
| async_generators         | 451 ms                                                                                                              | 474 ms: 1.05x slower                                                                                                    |
| fannkuch                 | 502 ms                                                                                                              | 529 ms: 1.05x slower                                                                                                    |
| sqlalchemy_declarative   | 145 ms                                                                                                              | 154 ms: 1.07x slower                                                                                                    |
| sympy_expand             | 472 ms                                                                                                              | 505 ms: 1.07x slower                                                                                                    |
| sqlglot_v2_transpile     | 1.79 ms                                                                                                             | 1.92 ms: 1.07x slower                                                                                                   |
| sympy_sum                | 144 ms                                                                                                              | 154 ms: 1.07x slower                                                                                                    |
| scimark_sparse_mat_mult  | 6.54 ms                                                                                                             | 7.08 ms: 1.08x slower                                                                                                   |
| dulwich_log              | 51.4 ms                                                                                                             | 55.8 ms: 1.08x slower                                                                                                   |
| typing_runtime_protocols | 199 us                                                                                                              | 216 us: 1.09x slower                                                                                                    |
| unpickle_pure_python     | 269 us                                                                                                              | 292 us: 1.09x slower                                                                                                    |
| spectral_norm            | 122 ms                                                                                                              | 135 ms: 1.10x slower                                                                                                    |
| pycparser                | 1.27 sec                                                                                                            | 1.40 sec: 1.11x slower                                                                                                  |
| sqlglot_v2_parse         | 1.45 ms                                                                                                             | 1.62 ms: 1.12x slower                                                                                                   |
| hexiom                   | 7.52 ms                                                                                                             | 8.58 ms: 1.14x slower                                                                                                   |
| crypto_pyaes             | 87.0 ms                                                                                                             | 101 ms: 1.16x slower                                                                                                    |
| comprehensions           | 21.3 us                                                                                                             | 25.6 us: 1.20x slower                                                                                                   |
| go                       | 144 ms                                                                                                              | 181 ms: 1.26x slower                                                                                                    |
| pprint_safe_repr         | 948 ms                                                                                                              | 1.24 sec: 1.31x slower                                                                                                  |
| pprint_pformat           | 1.92 sec                                                                                                            | 2.56 sec: 1.33x slower                                                                                                  |
| Geometric mean           | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (45): xml_etree_generate, regex_v8, mako, deepcopy_reduce, coroutines, unpack_sequence, logging_silent, subparsers, regex_compile, scimark_sor, mdp, asyncio_tcp_ssl, xml_etree_parse, json_loads, bpe_tokeniser, pidigits, async_tree_io, chaos, asyncio_tcp, python_startup_no_site, async_tree_cpu_io_mixed_tg, json_dumps, regex_effbot, async_tree_memoization, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization_tg, pickle_dict, async_tree_none, deepcopy, create_gc_cycles, sympy_str, generators, genshi_xml, scimark_fft, nqueens, pickle, sqlglot_v2_optimize, nbody, unpickle, pylint, scimark_lu, sqlalchemy_imperative, pathlib, meteor_contest

- Geometric mean (including insignificant results): 1.028x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.01x