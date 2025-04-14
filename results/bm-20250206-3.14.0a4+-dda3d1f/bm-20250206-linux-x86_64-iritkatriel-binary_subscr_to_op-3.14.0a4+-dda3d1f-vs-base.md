# Results vs. base

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: dda3d1f
- commit date: 2025-02-06
- overall geometric mean: 1.002x faster
- HPT reliability: 74.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 251 ms: 1.00x faster                                                       |
| docutils       | 2.58 sec                                                               | 2.57 sec: 1.00x faster                                                     |
| html5lib       | 59.8 ms                                                                | 60.6 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 499 ms                                                                 | 488 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 479 ms: 1.02x faster                                                       |
| async_tree_memoization_tg  | 321 ms                                                                 | 316 ms: 1.02x faster                                                       |
| coroutines                 | 23.3 ms                                                                | 23.1 ms: 1.01x faster                                                      |
| async_generators           | 383 ms                                                                 | 390 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (6): async_tree_none, async_tree_io, async_tree_none_tg, async_tree_memoization, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 92.7 ms                                                                | 91.2 ms: 1.02x faster                                                      |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 210 ms                                                                 | 209 ms: 1.01x faster                                                       |
| regex_v8       | 25.4 ms                                                                | 25.5 ms: 1.00x slower                                                      |
| regex_effbot   | 3.30 ms                                                                | 3.32 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 11.9 ms                                                                | 11.8 ms: 1.01x faster                                                      |
| pickle_pure_python   | 317 us                                                                 | 315 us: 1.01x faster                                                       |
| unpickle_pure_python | 216 us                                                                 | 217 us: 1.01x slower                                                       |
| xml_etree_parse      | 139 ms                                                                 | 140 ms: 1.01x slower                                                       |
| xml_etree_generate   | 82.9 ms                                                                | 83.7 ms: 1.01x slower                                                      |
| tomli_loads          | 1.94 sec                                                               | 1.97 sec: 1.01x slower                                                     |
| xml_etree_iterparse  | 97.1 ms                                                                | 98.6 ms: 1.02x slower                                                      |
| json_loads           | 28.5 us                                                                | 29.3 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                                      |
| python_startup_no_site | 7.05 ms                                                                | 7.00 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 21.1 ms                                                                | 20.9 ms: 1.01x faster                                                      |
| mako           | 11.0 ms                                                                | 11.1 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 5.03 ms                                                                | 4.60 ms: 1.09x faster                                                      |
| logging_silent             | 107 ns                                                                 | 104 ns: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 499 ms                                                                 | 488 ms: 1.02x faster                                                       |
| thrift                     | 766 us                                                                 | 750 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 479 ms: 1.02x faster                                                       |
| hexiom                     | 6.27 ms                                                                | 6.16 ms: 1.02x faster                                                      |
| nbody                      | 92.7 ms                                                                | 91.2 ms: 1.02x faster                                                      |
| async_tree_memoization_tg  | 321 ms                                                                 | 316 ms: 1.02x faster                                                       |
| create_gc_cycles           | 2.48 ms                                                                | 2.44 ms: 1.01x faster                                                      |
| meteor_contest             | 106 ms                                                                 | 105 ms: 1.01x faster                                                       |
| sympy_expand               | 454 ms                                                                 | 448 ms: 1.01x faster                                                       |
| json_dumps                 | 11.9 ms                                                                | 11.8 ms: 1.01x faster                                                      |
| genshi_text                | 21.1 ms                                                                | 20.9 ms: 1.01x faster                                                      |
| pathlib                    | 16.1 ms                                                                | 15.9 ms: 1.01x faster                                                      |
| deepcopy_memo              | 30.0 us                                                                | 29.7 us: 1.01x faster                                                      |
| coroutines                 | 23.3 ms                                                                | 23.1 ms: 1.01x faster                                                      |
| bpe_tokeniser              | 4.42 sec                                                               | 4.38 sec: 1.01x faster                                                     |
| logging_format             | 6.12 us                                                                | 6.07 us: 1.01x faster                                                      |
| scimark_sor                | 121 ms                                                                 | 120 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 67.4 ms                                                                | 66.8 ms: 1.01x faster                                                      |
| many_optionals             | 932 us                                                                 | 924 us: 1.01x faster                                                       |
| subparsers                 | 20.5 ms                                                                | 20.3 ms: 1.01x faster                                                      |
| python_startup             | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                                      |
| pyflate                    | 452 ms                                                                 | 449 ms: 1.01x faster                                                       |
| pickle_pure_python         | 317 us                                                                 | 315 us: 1.01x faster                                                       |
| comprehensions             | 16.3 us                                                                | 16.2 us: 1.01x faster                                                      |
| sqlglot_parse              | 1.26 ms                                                                | 1.25 ms: 1.01x faster                                                      |
| go                         | 119 ms                                                                 | 119 ms: 1.01x faster                                                       |
| regex_dna                  | 210 ms                                                                 | 209 ms: 1.01x faster                                                       |
| python_startup_no_site     | 7.05 ms                                                                | 7.00 ms: 1.01x faster                                                      |
| bench_mp_pool              | 81.0 ms                                                                | 80.6 ms: 1.01x faster                                                      |
| bench_thread_pool          | 864 us                                                                 | 861 us: 1.00x faster                                                       |
| deltablue                  | 3.22 ms                                                                | 3.21 ms: 1.00x faster                                                      |
| fannkuch                   | 396 ms                                                                 | 395 ms: 1.00x faster                                                       |
| sqlalchemy_declarative     | 128 ms                                                                 | 128 ms: 1.00x faster                                                       |
| 2to3                       | 252 ms                                                                 | 251 ms: 1.00x faster                                                       |
| crypto_pyaes               | 70.2 ms                                                                | 69.9 ms: 1.00x faster                                                      |
| docutils                   | 2.58 sec                                                               | 2.57 sec: 1.00x faster                                                     |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                                       |
| regex_v8                   | 25.4 ms                                                                | 25.5 ms: 1.00x slower                                                      |
| raytrace                   | 269 ms                                                                 | 269 ms: 1.00x slower                                                       |
| sqlglot_normalize          | 103 ms                                                                 | 103 ms: 1.00x slower                                                       |
| regex_effbot               | 3.30 ms                                                                | 3.32 ms: 1.00x slower                                                      |
| mako                       | 11.0 ms                                                                | 11.1 ms: 1.01x slower                                                      |
| nqueens                    | 79.6 ms                                                                | 80.1 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 216 us                                                                 | 217 us: 1.01x slower                                                       |
| xml_etree_parse            | 139 ms                                                                 | 140 ms: 1.01x slower                                                       |
| deepcopy                   | 255 us                                                                 | 258 us: 1.01x slower                                                       |
| xml_etree_generate         | 82.9 ms                                                                | 83.7 ms: 1.01x slower                                                      |
| mdp                        | 2.46 sec                                                               | 2.48 sec: 1.01x slower                                                     |
| shortest_path              | 471 ms                                                                 | 475 ms: 1.01x slower                                                       |
| richards_super             | 50.2 ms                                                                | 50.7 ms: 1.01x slower                                                      |
| chaos                      | 57.6 ms                                                                | 58.3 ms: 1.01x slower                                                      |
| tomli_loads                | 1.94 sec                                                               | 1.97 sec: 1.01x slower                                                     |
| html5lib                   | 59.8 ms                                                                | 60.6 ms: 1.01x slower                                                      |
| deepcopy_reduce            | 2.68 us                                                                | 2.72 us: 1.01x slower                                                      |
| xml_etree_iterparse        | 97.1 ms                                                                | 98.6 ms: 1.02x slower                                                      |
| async_generators           | 383 ms                                                                 | 390 ms: 1.02x slower                                                       |
| richards                   | 43.8 ms                                                                | 44.9 ms: 1.02x slower                                                      |
| json_loads                 | 28.5 us                                                                | 29.3 us: 1.03x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (36): async_tree_none, spectral_norm, typing_runtime_protocols, async_tree_io, async_tree_none_tg, telco, pylint, float, sqlalchemy_imperative, regex_compile, genshi_xml, scimark_lu, django_template, sympy_sum, scimark_sparse_mat_mult, sympy_str, async_tree_memoization, sqlglot_transpile, asyncio_websockets, dulwich_log, logging_simple, generators, xml_etree_process, sympy_integrate, sqlglot_optimize, sphinx, scimark_fft, pprint_pformat, pycparser, pprint_safe_repr, k_core, sqlite_synth, json, async_tree_io_tg, coverage, connected_components

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 74.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x