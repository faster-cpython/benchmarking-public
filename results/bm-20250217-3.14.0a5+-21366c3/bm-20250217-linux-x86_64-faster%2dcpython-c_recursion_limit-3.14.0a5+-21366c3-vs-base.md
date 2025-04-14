# Results vs. base

- fork: faster-cpython
- ref: c_recursion_limit
- machine: linux-x86_64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.002x slower
- HPT reliability: 97.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 254 ms: 1.01x slower                                                          |
| docutils       | 2.58 sec                                                               | 2.60 sec: 1.01x slower                                                        |
| html5lib       | 60.3 ms                                                                | 61.2 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| coroutines                 | 23.9 ms                                                                | 23.4 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 487 ms                                                                 | 481 ms: 1.01x faster                                                          |
| async_tree_memoization_tg  | 319 ms                                                                 | 316 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 488 ms: 1.01x faster                                                          |
| async_tree_memoization     | 320 ms                                                                 | 323 ms: 1.01x slower                                                          |
| async_generators           | 382 ms                                                                 | 389 ms: 1.02x slower                                                          |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (5): async_tree_none_tg, asyncio_websockets, async_tree_io_tg, async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                          |
| nbody          | 92.8 ms                                                                | 93.6 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 126 ms                                                                 | 125 ms: 1.01x faster                                                          |
| regex_effbot   | 3.17 ms                                                                | 3.15 ms: 1.01x faster                                                         |
| regex_v8       | 24.7 ms                                                                | 24.9 ms: 1.01x slower                                                         |
| regex_dna      | 216 ms                                                                 | 220 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps           | 11.9 ms                                                                | 11.4 ms: 1.04x faster                                                         |
| tomli_loads          | 1.99 sec                                                               | 1.94 sec: 1.03x faster                                                        |
| unpickle_pure_python | 219 us                                                                 | 216 us: 1.01x faster                                                          |
| pickle_pure_python   | 317 us                                                                 | 313 us: 1.01x faster                                                          |
| xml_etree_process    | 59.2 ms                                                                | 58.8 ms: 1.01x faster                                                         |
| xml_etree_parse      | 139 ms                                                                 | 140 ms: 1.01x slower                                                          |
| xml_etree_iterparse  | 96.3 ms                                                                | 97.4 ms: 1.01x slower                                                         |
| json_loads           | 28.8 us                                                                | 30.4 us: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 7.03 ms                                                                | 7.06 ms: 1.00x slower                                                         |
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 32.3 ms                                                                | 32.0 ms: 1.01x faster                                                         |
| mako            | 10.9 ms                                                                | 11.0 ms: 1.00x slower                                                         |
| genshi_xml      | 48.7 ms                                                                | 49.3 ms: 1.01x slower                                                         |
| genshi_text     | 21.2 ms                                                                | 21.6 ms: 1.02x slower                                                         |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20250214-linux-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps                 | 11.9 ms                                                                | 11.4 ms: 1.04x faster                                                         |
| logging_silent             | 106 ns                                                                 | 103 ns: 1.04x faster                                                          |
| scimark_sor                | 122 ms                                                                 | 119 ms: 1.03x faster                                                          |
| tomli_loads                | 1.99 sec                                                               | 1.94 sec: 1.03x faster                                                        |
| deltablue                  | 3.22 ms                                                                | 3.15 ms: 1.02x faster                                                         |
| richards                   | 44.6 ms                                                                | 43.6 ms: 1.02x faster                                                         |
| coroutines                 | 23.9 ms                                                                | 23.4 ms: 1.02x faster                                                         |
| scimark_monte_carlo        | 67.9 ms                                                                | 66.5 ms: 1.02x faster                                                         |
| go                         | 118 ms                                                                 | 115 ms: 1.02x faster                                                          |
| raytrace                   | 274 ms                                                                 | 269 ms: 1.02x faster                                                          |
| chaos                      | 58.6 ms                                                                | 57.7 ms: 1.02x faster                                                         |
| richards_super             | 50.5 ms                                                                | 49.8 ms: 1.01x faster                                                         |
| deepcopy_memo              | 30.3 us                                                                | 29.9 us: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 487 ms                                                                 | 481 ms: 1.01x faster                                                          |
| unpickle_pure_python       | 219 us                                                                 | 216 us: 1.01x faster                                                          |
| regex_compile              | 126 ms                                                                 | 125 ms: 1.01x faster                                                          |
| scimark_fft                | 346 ms                                                                 | 342 ms: 1.01x faster                                                          |
| pickle_pure_python         | 317 us                                                                 | 313 us: 1.01x faster                                                          |
| async_tree_memoization_tg  | 319 ms                                                                 | 316 ms: 1.01x faster                                                          |
| django_template            | 32.3 ms                                                                | 32.0 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 488 ms: 1.01x faster                                                          |
| regex_effbot               | 3.17 ms                                                                | 3.15 ms: 1.01x faster                                                         |
| xml_etree_process          | 59.2 ms                                                                | 58.8 ms: 1.01x faster                                                         |
| fannkuch                   | 406 ms                                                                 | 403 ms: 1.01x faster                                                          |
| mdp                        | 2.49 sec                                                               | 2.48 sec: 1.00x faster                                                        |
| sqlglot_parse              | 1.26 ms                                                                | 1.26 ms: 1.00x faster                                                         |
| sqlglot_transpile          | 1.57 ms                                                                | 1.56 ms: 1.00x faster                                                         |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                                          |
| hexiom                     | 6.14 ms                                                                | 6.15 ms: 1.00x slower                                                         |
| bench_thread_pool          | 864 us                                                                 | 866 us: 1.00x slower                                                          |
| mako                       | 10.9 ms                                                                | 11.0 ms: 1.00x slower                                                         |
| sympy_str                  | 266 ms                                                                 | 267 ms: 1.00x slower                                                          |
| meteor_contest             | 105 ms                                                                 | 105 ms: 1.00x slower                                                          |
| python_startup_no_site     | 7.03 ms                                                                | 7.06 ms: 1.00x slower                                                         |
| sqlalchemy_imperative      | 16.4 ms                                                                | 16.4 ms: 1.01x slower                                                         |
| subparsers                 | 20.5 ms                                                                | 20.6 ms: 1.01x slower                                                         |
| bench_mp_pool              | 81.1 ms                                                                | 81.6 ms: 1.01x slower                                                         |
| sympy_sum                  | 146 ms                                                                 | 147 ms: 1.01x slower                                                          |
| bpe_tokeniser              | 4.44 sec                                                               | 4.47 sec: 1.01x slower                                                        |
| 2to3                       | 253 ms                                                                 | 254 ms: 1.01x slower                                                          |
| sqlglot_normalize          | 104 ms                                                                 | 104 ms: 1.01x slower                                                          |
| docutils                   | 2.58 sec                                                               | 2.60 sec: 1.01x slower                                                        |
| python_startup             | 12.8 ms                                                                | 12.9 ms: 1.01x slower                                                         |
| async_tree_memoization     | 320 ms                                                                 | 323 ms: 1.01x slower                                                          |
| create_gc_cycles           | 2.46 ms                                                                | 2.48 ms: 1.01x slower                                                         |
| nbody                      | 92.8 ms                                                                | 93.6 ms: 1.01x slower                                                         |
| comprehensions             | 16.2 us                                                                | 16.4 us: 1.01x slower                                                         |
| logging_format             | 6.01 us                                                                | 6.07 us: 1.01x slower                                                         |
| thrift                     | 760 us                                                                 | 767 us: 1.01x slower                                                          |
| xml_etree_parse            | 139 ms                                                                 | 140 ms: 1.01x slower                                                          |
| sqlite_synth               | 2.75 us                                                                | 2.78 us: 1.01x slower                                                         |
| sympy_expand               | 448 ms                                                                 | 453 ms: 1.01x slower                                                          |
| regex_v8                   | 24.7 ms                                                                | 24.9 ms: 1.01x slower                                                         |
| xml_etree_iterparse        | 96.3 ms                                                                | 97.4 ms: 1.01x slower                                                         |
| nqueens                    | 80.8 ms                                                                | 81.7 ms: 1.01x slower                                                         |
| genshi_xml                 | 48.7 ms                                                                | 49.3 ms: 1.01x slower                                                         |
| deepcopy                   | 258 us                                                                 | 261 us: 1.01x slower                                                          |
| typing_runtime_protocols   | 156 us                                                                 | 158 us: 1.01x slower                                                          |
| pyflate                    | 449 ms                                                                 | 455 ms: 1.01x slower                                                          |
| pprint_safe_repr           | 710 ms                                                                 | 719 ms: 1.01x slower                                                          |
| html5lib                   | 60.3 ms                                                                | 61.2 ms: 1.01x slower                                                         |
| coverage                   | 89.5 ms                                                                | 90.8 ms: 1.01x slower                                                         |
| pathlib                    | 16.3 ms                                                                | 16.5 ms: 1.02x slower                                                         |
| pprint_pformat             | 1.44 sec                                                               | 1.46 sec: 1.02x slower                                                        |
| generators                 | 27.9 ms                                                                | 28.4 ms: 1.02x slower                                                         |
| async_generators           | 382 ms                                                                 | 389 ms: 1.02x slower                                                          |
| crypto_pyaes               | 71.1 ms                                                                | 72.6 ms: 1.02x slower                                                         |
| genshi_text                | 21.2 ms                                                                | 21.6 ms: 1.02x slower                                                         |
| regex_dna                  | 216 ms                                                                 | 220 ms: 1.02x slower                                                          |
| deepcopy_reduce            | 2.67 us                                                                | 2.73 us: 1.02x slower                                                         |
| gc_traversal               | 4.75 ms                                                                | 4.93 ms: 1.04x slower                                                         |
| json                       | 5.16 ms                                                                | 5.38 ms: 1.04x slower                                                         |
| json_loads                 | 28.8 us                                                                | 30.4 us: 1.06x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (23): float, telco, pycparser, connected_components, shortest_path, scimark_sparse_mat_mult, async_tree_none_tg, sqlalchemy_declarative, asyncio_websockets, dulwich_log, sphinx, spectral_norm, xml_etree_generate, sympy_integrate, sqlglot_optimize, many_optionals, scimark_lu, logging_simple, k_core, pylint, async_tree_io_tg, async_tree_io, async_tree_none

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 97.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x