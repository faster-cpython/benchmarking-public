# Results vs. base

- fork: brandtbucher
- ref: chain_depth_3
- machine: linux-x86_64
- commit hash: bf40531
- commit date: 2024-12-12
- overall geometric mean: 1.003x faster
- HPT reliability: 99.16%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 257 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|---------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization    | 342 ms                                                                 | 339 ms: 1.01x faster                                                  |
| async_tree_memoization_tg | 317 ms                                                                 | 315 ms: 1.01x faster                                                  |
| Geometric mean            | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (9): async_tree_io_tg, async_tree_none, async_generators, async_tree_io, asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed_tg, coroutines, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                                | 3.47 ms: 1.01x faster                                                 |
| regex_dna      | 220 ms                                                                 | 218 ms: 1.01x faster                                                  |
| regex_v8       | 25.1 ms                                                                | 25.0 ms: 1.01x faster                                                 |
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|--------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads        | 1.93 sec                                                               | 1.90 sec: 1.01x faster                                                |
| xml_etree_generate | 78.2 ms                                                                | 77.3 ms: 1.01x faster                                                 |
| xml_etree_process  | 54.9 ms                                                                | 54.5 ms: 1.01x faster                                                 |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (6): unpickle_pure_python, pickle_pure_python, json_loads, json_dumps, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                 |
| python_startup_no_site | 7.04 ms                                                                | 7.07 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.2 ms                                                                | 9.99 ms: 1.02x faster                                                 |
| django_template | 34.2 ms                                                                | 33.8 ms: 1.01x faster                                                 |
| genshi_text     | 24.0 ms                                                                | 24.4 ms: 1.01x slower                                                 |
| genshi_xml      | 57.0 ms                                                                | 58.9 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2+-94b8f8b | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|---------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                       | 2.77 sec                                                               | 2.57 sec: 1.08x faster                                                |
| richards_super            | 44.7 ms                                                                | 42.6 ms: 1.05x faster                                                 |
| deepcopy_reduce           | 2.81 us                                                                | 2.73 us: 1.03x faster                                                 |
| go                        | 135 ms                                                                 | 131 ms: 1.03x faster                                                  |
| spectral_norm             | 114 ms                                                                 | 111 ms: 1.02x faster                                                  |
| mako                      | 10.2 ms                                                                | 9.99 ms: 1.02x faster                                                 |
| richards                  | 37.3 ms                                                                | 36.7 ms: 1.02x faster                                                 |
| deepcopy                  | 275 us                                                                 | 271 us: 1.02x faster                                                  |
| nqueens                   | 91.0 ms                                                                | 89.5 ms: 1.02x faster                                                 |
| scimark_lu                | 111 ms                                                                 | 110 ms: 1.02x faster                                                  |
| typing_runtime_protocols  | 169 us                                                                 | 166 us: 1.02x faster                                                  |
| tomli_loads               | 1.93 sec                                                               | 1.90 sec: 1.01x faster                                                |
| xml_etree_generate        | 78.2 ms                                                                | 77.3 ms: 1.01x faster                                                 |
| sqlglot_parse             | 1.32 ms                                                                | 1.30 ms: 1.01x faster                                                 |
| regex_effbot              | 3.51 ms                                                                | 3.47 ms: 1.01x faster                                                 |
| thrift                    | 786 us                                                                 | 778 us: 1.01x faster                                                  |
| django_template           | 34.2 ms                                                                | 33.8 ms: 1.01x faster                                                 |
| scimark_monte_carlo       | 64.8 ms                                                                | 64.1 ms: 1.01x faster                                                 |
| regex_dna                 | 220 ms                                                                 | 218 ms: 1.01x faster                                                  |
| meteor_contest            | 108 ms                                                                 | 107 ms: 1.01x faster                                                  |
| logging_format            | 6.30 us                                                                | 6.25 us: 1.01x faster                                                 |
| scimark_fft               | 321 ms                                                                 | 318 ms: 1.01x faster                                                  |
| async_tree_memoization    | 342 ms                                                                 | 339 ms: 1.01x faster                                                  |
| crypto_pyaes              | 68.6 ms                                                                | 68.1 ms: 1.01x faster                                                 |
| xml_etree_process         | 54.9 ms                                                                | 54.5 ms: 1.01x faster                                                 |
| sqlglot_transpile         | 1.64 ms                                                                | 1.63 ms: 1.01x faster                                                 |
| async_tree_memoization_tg | 317 ms                                                                 | 315 ms: 1.01x faster                                                  |
| pathlib                   | 16.2 ms                                                                | 16.1 ms: 1.01x faster                                                 |
| regex_v8                  | 25.1 ms                                                                | 25.0 ms: 1.01x faster                                                 |
| regex_compile             | 128 ms                                                                 | 128 ms: 1.00x faster                                                  |
| 2to3                      | 258 ms                                                                 | 257 ms: 1.00x faster                                                  |
| dulwich_log               | 67.6 ms                                                                | 67.4 ms: 1.00x faster                                                 |
| pidigits                  | 187 ms                                                                 | 186 ms: 1.00x faster                                                  |
| bench_thread_pool         | 877 us                                                                 | 875 us: 1.00x faster                                                  |
| python_startup            | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                 |
| sympy_integrate           | 20.5 ms                                                                | 20.6 ms: 1.00x slower                                                 |
| python_startup_no_site    | 7.04 ms                                                                | 7.07 ms: 1.00x slower                                                 |
| connected_components      | 434 ms                                                                 | 436 ms: 1.00x slower                                                  |
| raytrace                  | 282 ms                                                                 | 283 ms: 1.01x slower                                                  |
| gc_traversal              | 4.75 ms                                                                | 4.78 ms: 1.01x slower                                                 |
| create_gc_cycles          | 2.44 ms                                                                | 2.46 ms: 1.01x slower                                                 |
| sympy_expand              | 473 ms                                                                 | 477 ms: 1.01x slower                                                  |
| coverage                  | 82.6 ms                                                                | 83.3 ms: 1.01x slower                                                 |
| genshi_text               | 24.0 ms                                                                | 24.4 ms: 1.01x slower                                                 |
| sympy_sum                 | 153 ms                                                                 | 156 ms: 1.01x slower                                                  |
| logging_silent            | 101 ns                                                                 | 102 ns: 1.02x slower                                                  |
| genshi_xml                | 57.0 ms                                                                | 58.9 ms: 1.03x slower                                                 |
| Geometric mean            | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (51): pycparser, djangocms, async_tree_io_tg, logging_simple, unpickle_pure_python, scimark_sor, chaos, pylint, sqlite_synth, html5lib, telco, async_tree_none, k_core, sqlalchemy_imperative, async_generators, bench_mp_pool, pickle_pure_python, docutils, sqlalchemy_declarative, sphinx, mypy2, generators, json_loads, comprehensions, subparsers, async_tree_io, deltablue, sqlglot_normalize, float, json_dumps, shortest_path, pprint_safe_repr, fannkuch, asyncio_websockets, bpe_tokeniser, sqlglot_optimize, scimark_sparse_mat_mult, async_tree_none_tg, async_tree_cpu_io_mixed_tg, deepcopy_memo, hexiom, sympy_str, json, xml_etree_iterparse, pyflate, coroutines, many_optionals, xml_etree_parse, nbody, pprint_pformat, async_tree_cpu_io_mixed

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 99.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x