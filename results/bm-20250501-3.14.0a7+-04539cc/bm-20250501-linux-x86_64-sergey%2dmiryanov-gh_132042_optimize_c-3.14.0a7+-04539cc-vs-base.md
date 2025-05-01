# Results vs. base

- fork: sergey-miryanov
- ref: gh_132042_optimize_c
- machine: linux-x86_64
- commit hash: 04539cc
- commit date: 2025-05-01
- overall geometric mean: 1.002x faster
- HPT reliability: 96.30%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250430-linux-x86_64-python-94b4fcd806e7b6929551-3.14.0a7+-94b4fcd | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| html5lib       | 60.0 ms                                                                | 62.6 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250430-linux-x86_64-python-94b4fcd806e7b6929551-3.14.0a7+-94b4fcd | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|---------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| coroutines                | 26.1 ms                                                                | 25.4 ms: 1.03x faster                                                             |
| async_tree_memoization_tg | 309 ms                                                                 | 305 ms: 1.01x faster                                                              |
| async_tree_memoization    | 316 ms                                                                 | 313 ms: 1.01x faster                                                              |
| async_generators          | 411 ms                                                                 | 409 ms: 1.01x faster                                                              |
| async_tree_eager_io_tg    | 621 ms                                                                 | 618 ms: 1.00x faster                                                              |
| Geometric mean            | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (14): async_tree_eager_io, async_tree_eager_tg, async_tree_eager_memoization, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_eager, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250430-linux-x86_64-python-94b4fcd806e7b6929551-3.14.0a7+-94b4fcd | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 194 ms                                                                 | 190 ms: 1.02x faster                                                              |
| float          | 70.9 ms                                                                | 69.3 ms: 1.02x faster                                                             |
| nbody          | 97.1 ms                                                                | 101 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250430-linux-x86_64-python-94b4fcd806e7b6929551-3.14.0a7+-94b4fcd | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 23.6 ms                                                                | 22.5 ms: 1.05x faster                                                             |
| regex_dna      | 202 ms                                                                 | 208 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250430-linux-x86_64-python-94b4fcd806e7b6929551-3.14.0a7+-94b4fcd | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse      | 147 ms                                                                 | 141 ms: 1.04x faster                                                              |
| tomli_loads          | 2.03 sec                                                               | 1.98 sec: 1.03x faster                                                            |
| json_loads           | 30.7 us                                                                | 30.3 us: 1.01x faster                                                             |
| xml_etree_generate   | 86.9 ms                                                                | 85.9 ms: 1.01x faster                                                             |
| json_dumps           | 12.1 ms                                                                | 12.0 ms: 1.00x faster                                                             |
| pickle_pure_python   | 318 us                                                                 | 319 us: 1.00x slower                                                              |
| unpickle_pure_python | 217 us                                                                 | 220 us: 1.02x slower                                                              |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                                      |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250430-linux-x86_64-python-94b4fcd806e7b6929551-3.14.0a7+-94b4fcd | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                             |
| python_startup_no_site | 6.91 ms                                                                | 6.90 ms: 1.00x faster                                                             |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250430-linux-x86_64-python-94b4fcd806e7b6929551-3.14.0a7+-94b4fcd | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 11.8 ms                                                                | 11.6 ms: 1.02x faster                                                             |
| genshi_text     | 21.0 ms                                                                | 21.1 ms: 1.00x slower                                                             |
| genshi_xml      | 49.2 ms                                                                | 49.6 ms: 1.01x slower                                                             |
| django_template | 32.3 ms                                                                | 32.6 ms: 1.01x slower                                                             |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                                      |

All benchmarks:
===============

| Benchmark                 | bm-20250430-linux-x86_64-python-94b4fcd806e7b6929551-3.14.0a7+-94b4fcd | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|---------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult   | 5.32 ms                                                                | 4.82 ms: 1.10x faster                                                             |
| spectral_norm             | 110 ms                                                                 | 102 ms: 1.07x faster                                                              |
| regex_v8                  | 23.6 ms                                                                | 22.5 ms: 1.05x faster                                                             |
| scimark_fft               | 377 ms                                                                 | 363 ms: 1.04x faster                                                              |
| xml_etree_parse           | 147 ms                                                                 | 141 ms: 1.04x faster                                                              |
| shortest_path             | 512 ms                                                                 | 493 ms: 1.04x faster                                                              |
| sqlglot_v2_parse          | 1.26 ms                                                                | 1.22 ms: 1.03x faster                                                             |
| connected_components      | 466 ms                                                                 | 452 ms: 1.03x faster                                                              |
| coroutines                | 26.1 ms                                                                | 25.4 ms: 1.03x faster                                                             |
| tomli_loads               | 2.03 sec                                                               | 1.98 sec: 1.03x faster                                                            |
| generators                | 29.7 ms                                                                | 28.9 ms: 1.03x faster                                                             |
| sqlglot_v2_transpile      | 1.57 ms                                                                | 1.53 ms: 1.03x faster                                                             |
| pidigits                  | 194 ms                                                                 | 190 ms: 1.02x faster                                                              |
| float                     | 70.9 ms                                                                | 69.3 ms: 1.02x faster                                                             |
| scimark_sor               | 123 ms                                                                 | 120 ms: 1.02x faster                                                              |
| bpe_tokeniser             | 4.58 sec                                                               | 4.50 sec: 1.02x faster                                                            |
| telco                     | 7.99 ms                                                                | 7.85 ms: 1.02x faster                                                             |
| logging_silent            | 97.6 ns                                                                | 95.9 ns: 1.02x faster                                                             |
| mako                      | 11.8 ms                                                                | 11.6 ms: 1.02x faster                                                             |
| meteor_contest            | 108 ms                                                                 | 107 ms: 1.01x faster                                                              |
| mdp                       | 1.25 sec                                                               | 1.23 sec: 1.01x faster                                                            |
| bench_mp_pool             | 82.8 ms                                                                | 81.7 ms: 1.01x faster                                                             |
| coverage                  | 93.2 ms                                                                | 92.1 ms: 1.01x faster                                                             |
| json_loads                | 30.7 us                                                                | 30.3 us: 1.01x faster                                                             |
| xml_etree_generate        | 86.9 ms                                                                | 85.9 ms: 1.01x faster                                                             |
| async_tree_memoization_tg | 309 ms                                                                 | 305 ms: 1.01x faster                                                              |
| async_tree_memoization    | 316 ms                                                                 | 313 ms: 1.01x faster                                                              |
| comprehensions            | 17.2 us                                                                | 17.1 us: 1.01x faster                                                             |
| async_generators          | 411 ms                                                                 | 409 ms: 1.01x faster                                                              |
| sqlglot_v2_normalize      | 108 ms                                                                 | 107 ms: 1.01x faster                                                              |
| pprint_pformat            | 1.50 sec                                                               | 1.49 sec: 1.01x faster                                                            |
| json_dumps                | 12.1 ms                                                                | 12.0 ms: 1.00x faster                                                             |
| async_tree_eager_io_tg    | 621 ms                                                                 | 618 ms: 1.00x faster                                                              |
| crypto_pyaes              | 75.0 ms                                                                | 74.7 ms: 1.00x faster                                                             |
| sqlglot_v2_optimize       | 53.1 ms                                                                | 52.9 ms: 1.00x faster                                                             |
| python_startup            | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                             |
| python_startup_no_site    | 6.91 ms                                                                | 6.90 ms: 1.00x faster                                                             |
| sympy_str                 | 268 ms                                                                 | 269 ms: 1.00x slower                                                              |
| hexiom                    | 6.23 ms                                                                | 6.25 ms: 1.00x slower                                                             |
| pickle_pure_python        | 318 us                                                                 | 319 us: 1.00x slower                                                              |
| pprint_safe_repr          | 728 ms                                                                 | 732 ms: 1.00x slower                                                              |
| nqueens                   | 81.7 ms                                                                | 82.1 ms: 1.00x slower                                                             |
| genshi_text               | 21.0 ms                                                                | 21.1 ms: 1.00x slower                                                             |
| sympy_sum                 | 149 ms                                                                 | 150 ms: 1.01x slower                                                              |
| bench_thread_pool         | 887 us                                                                 | 891 us: 1.01x slower                                                              |
| dulwich_log               | 59.7 ms                                                                | 60.1 ms: 1.01x slower                                                             |
| many_optionals            | 937 us                                                                 | 942 us: 1.01x slower                                                              |
| typing_runtime_protocols  | 168 us                                                                 | 169 us: 1.01x slower                                                              |
| genshi_xml                | 49.2 ms                                                                | 49.6 ms: 1.01x slower                                                             |
| fannkuch                  | 420 ms                                                                 | 423 ms: 1.01x slower                                                              |
| django_template           | 32.3 ms                                                                | 32.6 ms: 1.01x slower                                                             |
| scimark_lu                | 115 ms                                                                 | 116 ms: 1.01x slower                                                              |
| pathlib                   | 17.2 ms                                                                | 17.4 ms: 1.01x slower                                                             |
| richards                  | 43.5 ms                                                                | 44.0 ms: 1.01x slower                                                             |
| deepcopy                  | 256 us                                                                 | 259 us: 1.01x slower                                                              |
| subparsers                | 21.2 ms                                                                | 21.5 ms: 1.01x slower                                                             |
| create_gc_cycles          | 2.47 ms                                                                | 2.50 ms: 1.01x slower                                                             |
| unpickle_pure_python      | 217 us                                                                 | 220 us: 1.02x slower                                                              |
| deepcopy_reduce           | 2.73 us                                                                | 2.78 us: 1.02x slower                                                             |
| pyflate                   | 447 ms                                                                 | 456 ms: 1.02x slower                                                              |
| sqlite_synth              | 2.85 us                                                                | 2.92 us: 1.02x slower                                                             |
| raytrace                  | 268 ms                                                                 | 276 ms: 1.03x slower                                                              |
| deltablue                 | 3.33 ms                                                                | 3.43 ms: 1.03x slower                                                             |
| regex_dna                 | 202 ms                                                                 | 208 ms: 1.03x slower                                                              |
| pycparser                 | 1.14 sec                                                               | 1.18 sec: 1.04x slower                                                            |
| nbody                     | 97.1 ms                                                                | 101 ms: 1.04x slower                                                              |
| html5lib                  | 60.0 ms                                                                | 62.6 ms: 1.04x slower                                                             |
| gc_traversal              | 4.60 ms                                                                | 5.08 ms: 1.10x slower                                                             |
| Geometric mean            | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (35): async_tree_eager_io, async_tree_eager_tg, scimark_monte_carlo, async_tree_eager_memoization, k_core, async_tree_none_tg, logging_format, xml_etree_iterparse, async_tree_eager_memoization_tg, async_tree_eager, deepcopy_memo, regex_compile, sphinx, async_tree_io_tg, sqlalchemy_imperative, chaos, docutils, json, asyncio_websockets, async_tree_cpu_io_mixed_tg, sqlalchemy_declarative, 2to3, async_tree_io, go, sympy_expand, sympy_integrate, logging_simple, async_tree_eager_cpu_io_mixed_tg, xml_etree_process, regex_effbot, richards_super, async_tree_eager_cpu_io_mixed, pylint, async_tree_cpu_io_mixed, async_tree_none

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 96.30% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x