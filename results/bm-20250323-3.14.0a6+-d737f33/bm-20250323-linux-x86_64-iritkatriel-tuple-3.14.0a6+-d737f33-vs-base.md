# Results vs. base

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: d737f33
- commit date: 2025-03-23
- overall geometric mean: 1.001x faster
- HPT reliability: 93.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 257 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|--------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines         | 24.1 ms                                                                | 23.1 ms: 1.04x faster                                        |
| async_tree_none_tg | 250 ms                                                                 | 247 ms: 1.01x faster                                         |
| async_generators   | 391 ms                                                                 | 399 ms: 1.02x slower                                         |
| Geometric mean     | (ref)                                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_io, async_tree_none, async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 99.0 ms                                                                | 97.4 ms: 1.02x faster                                        |
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                 | 127 ms: 1.00x slower                                         |
| regex_effbot   | 3.47 ms                                                                | 3.49 ms: 1.01x slower                                        |
| regex_dna      | 223 ms                                                                 | 227 ms: 1.02x slower                                         |
| regex_v8       | 23.7 ms                                                                | 24.2 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 142 ms                                                                 | 141 ms: 1.01x faster                                         |
| xml_etree_process    | 58.9 ms                                                                | 58.3 ms: 1.01x faster                                        |
| unpickle_pure_python | 222 us                                                                 | 220 us: 1.01x faster                                         |
| tomli_loads          | 1.96 sec                                                               | 1.97 sec: 1.01x slower                                       |
| json_dumps           | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                        |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (4): xml_etree_iterparse, pickle_pure_python, xml_etree_generate, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.19 ms                                                                | 8.24 ms: 1.01x slower                                        |
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                        |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 31.8 ms                                                                | 31.3 ms: 1.02x faster                                        |
| mako            | 11.4 ms                                                                | 11.4 ms: 1.01x slower                                        |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250318-linux-x86_64-python-49234c065cf2b1ea32c5-3.14.0a6+-49234c0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| gc_traversal             | 5.07 ms                                                                | 4.78 ms: 1.06x faster                                        |
| coroutines               | 24.1 ms                                                                | 23.1 ms: 1.04x faster                                        |
| sympy_str                | 268 ms                                                                 | 260 ms: 1.03x faster                                         |
| telco                    | 8.06 ms                                                                | 7.82 ms: 1.03x faster                                        |
| chaos                    | 59.7 ms                                                                | 58.7 ms: 1.02x faster                                        |
| sympy_sum                | 147 ms                                                                 | 145 ms: 1.02x faster                                         |
| nbody                    | 99.0 ms                                                                | 97.4 ms: 1.02x faster                                        |
| django_template          | 31.8 ms                                                                | 31.3 ms: 1.02x faster                                        |
| sqlglot_v2_normalize     | 107 ms                                                                 | 105 ms: 1.02x faster                                         |
| pathlib                  | 16.8 ms                                                                | 16.5 ms: 1.01x faster                                        |
| async_tree_none_tg       | 250 ms                                                                 | 247 ms: 1.01x faster                                         |
| go                       | 115 ms                                                                 | 114 ms: 1.01x faster                                         |
| scimark_sparse_mat_mult  | 4.94 ms                                                                | 4.89 ms: 1.01x faster                                        |
| thrift                   | 773 us                                                                 | 765 us: 1.01x faster                                         |
| mdp                      | 2.49 sec                                                               | 2.47 sec: 1.01x faster                                       |
| logging_silent           | 99.9 ns                                                                | 98.9 ns: 1.01x faster                                        |
| sqlglot_v2_optimize      | 53.1 ms                                                                | 52.5 ms: 1.01x faster                                        |
| xml_etree_parse          | 142 ms                                                                 | 141 ms: 1.01x faster                                         |
| xml_etree_process        | 58.9 ms                                                                | 58.3 ms: 1.01x faster                                        |
| scimark_monte_carlo      | 69.2 ms                                                                | 68.6 ms: 1.01x faster                                        |
| meteor_contest           | 107 ms                                                                 | 106 ms: 1.01x faster                                         |
| sympy_integrate          | 19.9 ms                                                                | 19.7 ms: 1.01x faster                                        |
| unpickle_pure_python     | 222 us                                                                 | 220 us: 1.01x faster                                         |
| richards_super           | 49.8 ms                                                                | 49.4 ms: 1.01x faster                                        |
| sqlglot_v2_transpile     | 1.58 ms                                                                | 1.57 ms: 1.01x faster                                        |
| pprint_pformat           | 1.50 sec                                                               | 1.49 sec: 1.01x faster                                       |
| hexiom                   | 6.30 ms                                                                | 6.27 ms: 1.01x faster                                        |
| sqlglot_v2_parse         | 1.27 ms                                                                | 1.27 ms: 1.01x faster                                        |
| richards                 | 43.4 ms                                                                | 43.2 ms: 1.00x faster                                        |
| raytrace                 | 268 ms                                                                 | 267 ms: 1.00x faster                                         |
| bpe_tokeniser            | 4.64 sec                                                               | 4.62 sec: 1.00x faster                                       |
| create_gc_cycles         | 2.48 ms                                                                | 2.48 ms: 1.00x faster                                        |
| regex_compile            | 127 ms                                                                 | 127 ms: 1.00x slower                                         |
| pidigits                 | 186 ms                                                                 | 187 ms: 1.00x slower                                         |
| 2to3                     | 256 ms                                                                 | 257 ms: 1.00x slower                                         |
| scimark_fft              | 351 ms                                                                 | 351 ms: 1.00x slower                                         |
| generators               | 28.5 ms                                                                | 28.6 ms: 1.01x slower                                        |
| logging_format           | 6.11 us                                                                | 6.14 us: 1.01x slower                                        |
| python_startup_no_site   | 8.19 ms                                                                | 8.24 ms: 1.01x slower                                        |
| regex_effbot             | 3.47 ms                                                                | 3.49 ms: 1.01x slower                                        |
| mako                     | 11.4 ms                                                                | 11.4 ms: 1.01x slower                                        |
| bench_mp_pool            | 83.0 ms                                                                | 83.6 ms: 1.01x slower                                        |
| tomli_loads              | 1.96 sec                                                               | 1.97 sec: 1.01x slower                                       |
| crypto_pyaes             | 75.4 ms                                                                | 76.1 ms: 1.01x slower                                        |
| many_optionals           | 945 us                                                                 | 953 us: 1.01x slower                                         |
| subparsers               | 20.6 ms                                                                | 20.8 ms: 1.01x slower                                        |
| python_startup           | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                        |
| logging_simple           | 5.51 us                                                                | 5.57 us: 1.01x slower                                        |
| connected_components     | 451 ms                                                                 | 456 ms: 1.01x slower                                         |
| json_dumps               | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                        |
| bench_thread_pool        | 868 us                                                                 | 879 us: 1.01x slower                                         |
| typing_runtime_protocols | 162 us                                                                 | 164 us: 1.01x slower                                         |
| sqlalchemy_imperative    | 16.6 ms                                                                | 16.9 ms: 1.02x slower                                        |
| regex_dna                | 223 ms                                                                 | 227 ms: 1.02x slower                                         |
| regex_v8                 | 23.7 ms                                                                | 24.2 ms: 1.02x slower                                        |
| async_generators         | 391 ms                                                                 | 399 ms: 1.02x slower                                         |
| dulwich_log              | 57.9 ms                                                                | 59.2 ms: 1.02x slower                                        |
| nqueens                  | 83.4 ms                                                                | 85.7 ms: 1.03x slower                                        |
| fannkuch                 | 417 ms                                                                 | 436 ms: 1.04x slower                                         |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (37): async_tree_memoization_tg, async_tree_io, k_core, scimark_lu, async_tree_none, json, async_tree_io_tg, spectral_norm, async_tree_memoization, pprint_safe_repr, async_tree_cpu_io_mixed_tg, scimark_sor, deepcopy, comprehensions, float, xml_etree_iterparse, html5lib, pickle_pure_python, sqlalchemy_declarative, xml_etree_generate, asyncio_websockets, async_tree_cpu_io_mixed, deepcopy_reduce, sympy_expand, docutils, deepcopy_memo, shortest_path, coverage, json_loads, genshi_text, pyflate, sqlite_synth, pycparser, deltablue, genshi_xml, sphinx, pylint

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 93.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x