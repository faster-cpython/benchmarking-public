# Results vs. base

- fork: brandtbucher
- ref: jit_targets
- machine: linux-x86_64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.003x slower
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250707-pythonperf2_clang-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2_clang-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 286 ms                                                                            | 287 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                             | 1.00x slower                                                                   |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250707-pythonperf2_clang-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2_clang-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|--------------------|:---------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_websockets | 393 ms                                                                            | 386 ms: 1.02x faster                                                           |
| async_tree_io_tg   | 635 ms                                                                            | 628 ms: 1.01x faster                                                           |
| async_generators   | 455 ms                                                                            | 453 ms: 1.00x faster                                                           |
| async_tree_none    | 275 ms                                                                            | 276 ms: 1.00x slower                                                           |
| Geometric mean     | (ref)                                                                             | 1.00x faster                                                                   |

Benchmark hidden because not significant (7): coroutines, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250707-pythonperf2_clang-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2_clang-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.76 ms                                                                           | 3.68 ms: 1.02x faster                                                          |
| regex_v8       | 23.4 ms                                                                           | 23.3 ms: 1.00x faster                                                          |
| regex_dna      | 227 ms                                                                            | 228 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                             | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250707-pythonperf2_clang-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2_clang-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:---------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 26.5 us                                                                           | 25.3 us: 1.05x faster                                                          |
| xml_etree_process    | 56.7 ms                                                                           | 56.2 ms: 1.01x faster                                                          |
| xml_etree_generate   | 80.1 ms                                                                           | 79.5 ms: 1.01x faster                                                          |
| unpickle_pure_python | 196 us                                                                            | 195 us: 1.01x faster                                                           |
| pickle_pure_python   | 331 us                                                                            | 334 us: 1.01x slower                                                           |
| xml_etree_iterparse  | 99.0 ms                                                                           | 100 ms: 1.01x slower                                                           |
| json_dumps           | 11.0 ms                                                                           | 11.2 ms: 1.01x slower                                                          |
| xml_etree_parse      | 140 ms                                                                            | 144 ms: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                                             | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250707-pythonperf2_clang-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2_clang-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:---------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 15.3 ms                                                                           | 15.4 ms: 1.00x slower                                                          |
| python_startup_no_site | 8.81 ms                                                                           | 8.87 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                                             | 1.01x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250707-pythonperf2_clang-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2_clang-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:---------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 55.3 ms                                                                           | 54.8 ms: 1.01x faster                                                          |
| genshi_text     | 23.0 ms                                                                           | 23.3 ms: 1.01x slower                                                          |
| django_template | 35.0 ms                                                                           | 35.6 ms: 1.02x slower                                                          |
| mako            | 9.78 ms                                                                           | 9.97 ms: 1.02x slower                                                          |
| Geometric mean  | (ref)                                                                             | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20250707-pythonperf2_clang-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2_clang-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|--------------------------|:---------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads               | 26.5 us                                                                           | 25.3 us: 1.05x faster                                                          |
| scimark_sparse_mat_mult  | 5.02 ms                                                                           | 4.86 ms: 1.03x faster                                                          |
| json                     | 5.42 ms                                                                           | 5.31 ms: 1.02x faster                                                          |
| regex_effbot             | 3.76 ms                                                                           | 3.68 ms: 1.02x faster                                                          |
| asyncio_websockets       | 393 ms                                                                            | 386 ms: 1.02x faster                                                           |
| pycparser                | 1.23 sec                                                                          | 1.21 sec: 1.01x faster                                                         |
| generators               | 30.5 ms                                                                           | 30.1 ms: 1.01x faster                                                          |
| thrift                   | 841 us                                                                            | 830 us: 1.01x faster                                                           |
| nqueens                  | 94.4 ms                                                                           | 93.3 ms: 1.01x faster                                                          |
| async_tree_io_tg         | 635 ms                                                                            | 628 ms: 1.01x faster                                                           |
| genshi_xml               | 55.3 ms                                                                           | 54.8 ms: 1.01x faster                                                          |
| xml_etree_process        | 56.7 ms                                                                           | 56.2 ms: 1.01x faster                                                          |
| scimark_fft              | 302 ms                                                                            | 300 ms: 1.01x faster                                                           |
| xml_etree_generate       | 80.1 ms                                                                           | 79.5 ms: 1.01x faster                                                          |
| unpickle_pure_python     | 196 us                                                                            | 195 us: 1.01x faster                                                           |
| sympy_integrate          | 22.5 ms                                                                           | 22.4 ms: 1.01x faster                                                          |
| meteor_contest           | 121 ms                                                                            | 121 ms: 1.01x faster                                                           |
| async_generators         | 455 ms                                                                            | 453 ms: 1.00x faster                                                           |
| scimark_lu               | 96.6 ms                                                                           | 96.2 ms: 1.00x faster                                                          |
| logging_silent           | 93.4 ns                                                                           | 93.0 ns: 1.00x faster                                                          |
| sympy_sum                | 152 ms                                                                            | 151 ms: 1.00x faster                                                           |
| regex_v8                 | 23.4 ms                                                                           | 23.3 ms: 1.00x faster                                                          |
| deepcopy_memo            | 27.8 us                                                                           | 27.9 us: 1.00x slower                                                          |
| async_tree_none          | 275 ms                                                                            | 276 ms: 1.00x slower                                                           |
| 2to3                     | 286 ms                                                                            | 287 ms: 1.00x slower                                                           |
| sqlglot_v2_optimize      | 58.2 ms                                                                           | 58.5 ms: 1.00x slower                                                          |
| python_startup           | 15.3 ms                                                                           | 15.4 ms: 1.00x slower                                                          |
| connected_components     | 406 ms                                                                            | 408 ms: 1.01x slower                                                           |
| hexiom                   | 6.19 ms                                                                           | 6.22 ms: 1.01x slower                                                          |
| dulwich_log              | 59.0 ms                                                                           | 59.4 ms: 1.01x slower                                                          |
| sympy_str                | 290 ms                                                                            | 292 ms: 1.01x slower                                                           |
| regex_dna                | 227 ms                                                                            | 228 ms: 1.01x slower                                                           |
| python_startup_no_site   | 8.81 ms                                                                           | 8.87 ms: 1.01x slower                                                          |
| sqlglot_v2_transpile     | 1.70 ms                                                                           | 1.71 ms: 1.01x slower                                                          |
| pickle_pure_python       | 331 us                                                                            | 334 us: 1.01x slower                                                           |
| sqlglot_v2_parse         | 1.32 ms                                                                           | 1.33 ms: 1.01x slower                                                          |
| pprint_pformat           | 1.52 sec                                                                          | 1.53 sec: 1.01x slower                                                         |
| shortest_path            | 441 ms                                                                            | 445 ms: 1.01x slower                                                           |
| genshi_text              | 23.0 ms                                                                           | 23.3 ms: 1.01x slower                                                          |
| xml_etree_iterparse      | 99.0 ms                                                                           | 100 ms: 1.01x slower                                                           |
| sympy_expand             | 497 ms                                                                            | 503 ms: 1.01x slower                                                           |
| comprehensions           | 17.6 us                                                                           | 17.8 us: 1.01x slower                                                          |
| sqlglot_v2_normalize     | 115 ms                                                                            | 116 ms: 1.01x slower                                                           |
| pathlib                  | 16.9 ms                                                                           | 17.1 ms: 1.01x slower                                                          |
| telco                    | 158 ms                                                                            | 160 ms: 1.01x slower                                                           |
| json_dumps               | 11.0 ms                                                                           | 11.2 ms: 1.01x slower                                                          |
| chaos                    | 59.5 ms                                                                           | 60.4 ms: 1.01x slower                                                          |
| coverage                 | 81.2 ms                                                                           | 82.4 ms: 1.01x slower                                                          |
| pyflate                  | 424 ms                                                                            | 430 ms: 1.02x slower                                                           |
| typing_runtime_protocols | 168 us                                                                            | 171 us: 1.02x slower                                                           |
| logging_format           | 6.67 us                                                                           | 6.78 us: 1.02x slower                                                          |
| logging_simple           | 6.07 us                                                                           | 6.17 us: 1.02x slower                                                          |
| django_template          | 35.0 ms                                                                           | 35.6 ms: 1.02x slower                                                          |
| bpe_tokeniser            | 4.62 sec                                                                          | 4.71 sec: 1.02x slower                                                         |
| mako                     | 9.78 ms                                                                           | 9.97 ms: 1.02x slower                                                          |
| create_gc_cycles         | 2.83 ms                                                                           | 2.90 ms: 1.02x slower                                                          |
| xml_etree_parse          | 140 ms                                                                            | 144 ms: 1.03x slower                                                           |
| raytrace                 | 291 ms                                                                            | 298 ms: 1.03x slower                                                           |
| scimark_sor              | 102 ms                                                                            | 105 ms: 1.03x slower                                                           |
| scimark_monte_carlo      | 63.5 ms                                                                           | 65.2 ms: 1.03x slower                                                          |
| spectral_norm            | 81.1 ms                                                                           | 83.5 ms: 1.03x slower                                                          |
| gc_traversal             | 6.27 ms                                                                           | 6.71 ms: 1.07x slower                                                          |
| Geometric mean           | (ref)                                                                             | 1.00x slower                                                                   |

Benchmark hidden because not significant (31): pprint_safe_repr, coroutines, k_core, async_tree_cpu_io_mixed, fannkuch, go, tomli_loads, richards, sqlite_synth, regex_compile, async_tree_memoization, async_tree_cpu_io_mixed_tg, docutils, pidigits, sphinx, pylint, djangocms, subparsers, mdp, deepcopy, many_optionals, async_tree_memoization_tg, deepcopy_reduce, crypto_pyaes, deltablue, float, html5lib, async_tree_none_tg, richards_super, async_tree_io, nbody

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 99.52% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x