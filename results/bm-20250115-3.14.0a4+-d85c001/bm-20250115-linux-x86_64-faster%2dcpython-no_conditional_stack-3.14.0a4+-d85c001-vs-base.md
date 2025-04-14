# Results vs. base

- fork: faster-cpython
- ref: no_conditional_stack
- machine: linux-x86_64
- commit hash: d85c001
- commit date: 2025-01-15
- overall geometric mean: 1.008x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 255 ms: 1.01x slower                                                             |
| docutils       | 2.58 sec                                                               | 2.61 sec: 1.01x slower                                                           |
| html5lib       | 59.8 ms                                                                | 62.4 ms: 1.04x slower                                                            |
| sphinx         | 1.01 sec                                                               | 1.02 sec: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coroutines                 | 24.0 ms                                                                | 23.4 ms: 1.02x faster                                                            |
| async_generators           | 393 ms                                                                 | 387 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed_tg | 460 ms                                                                 | 464 ms: 1.01x slower                                                             |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_none, asyncio_websockets, async_tree_memoization, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 96.4 ms                                                                | 98.0 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 210 ms                                                                 | 215 ms: 1.02x slower                                                             |
| regex_compile  | 126 ms                                                                 | 130 ms: 1.03x slower                                                             |
| regex_v8       | 24.5 ms                                                                | 25.3 ms: 1.04x slower                                                            |
| regex_effbot   | 3.16 ms                                                                | 3.41 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 140 ms                                                                 | 138 ms: 1.02x faster                                                             |
| json_loads           | 29.5 us                                                                | 29.2 us: 1.01x faster                                                            |
| json_dumps           | 11.8 ms                                                                | 11.9 ms: 1.00x slower                                                            |
| xml_etree_iterparse  | 97.2 ms                                                                | 97.8 ms: 1.01x slower                                                            |
| pickle_pure_python   | 322 us                                                                 | 328 us: 1.02x slower                                                             |
| tomli_loads          | 1.97 sec                                                               | 2.03 sec: 1.03x slower                                                           |
| xml_etree_process    | 59.4 ms                                                                | 61.6 ms: 1.04x slower                                                            |
| unpickle_pure_python | 216 us                                                                 | 228 us: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                            |
| python_startup_no_site | 7.03 ms                                                                | 7.03 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.3 ms                                                                | 11.2 ms: 1.01x faster                                                            |
| genshi_text     | 21.2 ms                                                                | 21.5 ms: 1.01x slower                                                            |
| django_template | 32.0 ms                                                                | 32.8 ms: 1.02x slower                                                            |
| genshi_xml      | 48.5 ms                                                                | 49.7 ms: 1.03x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| spectral_norm              | 107 ms                                                                 | 104 ms: 1.03x faster                                                             |
| coroutines                 | 24.0 ms                                                                | 23.4 ms: 1.02x faster                                                            |
| coverage                   | 92.1 ms                                                                | 90.3 ms: 1.02x faster                                                            |
| crypto_pyaes               | 73.3 ms                                                                | 72.1 ms: 1.02x faster                                                            |
| xml_etree_parse            | 140 ms                                                                 | 138 ms: 1.02x faster                                                             |
| async_generators           | 393 ms                                                                 | 387 ms: 1.02x faster                                                             |
| hexiom                     | 6.37 ms                                                                | 6.28 ms: 1.01x faster                                                            |
| json_loads                 | 29.5 us                                                                | 29.2 us: 1.01x faster                                                            |
| mako                       | 11.3 ms                                                                | 11.2 ms: 1.01x faster                                                            |
| deltablue                  | 3.20 ms                                                                | 3.17 ms: 1.01x faster                                                            |
| generators                 | 27.6 ms                                                                | 27.4 ms: 1.01x faster                                                            |
| scimark_sor                | 122 ms                                                                 | 122 ms: 1.01x faster                                                             |
| sqlglot_parse              | 1.27 ms                                                                | 1.26 ms: 1.01x faster                                                            |
| sqlglot_transpile          | 1.58 ms                                                                | 1.57 ms: 1.01x faster                                                            |
| gc_traversal               | 4.80 ms                                                                | 4.78 ms: 1.00x faster                                                            |
| bpe_tokeniser              | 4.50 sec                                                               | 4.49 sec: 1.00x faster                                                           |
| scimark_fft                | 351 ms                                                                 | 350 ms: 1.00x faster                                                             |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                            |
| python_startup_no_site     | 7.03 ms                                                                | 7.03 ms: 1.00x slower                                                            |
| raytrace                   | 270 ms                                                                 | 271 ms: 1.00x slower                                                             |
| json_dumps                 | 11.8 ms                                                                | 11.9 ms: 1.00x slower                                                            |
| sqlglot_normalize          | 104 ms                                                                 | 105 ms: 1.00x slower                                                             |
| go                         | 118 ms                                                                 | 119 ms: 1.00x slower                                                             |
| comprehensions             | 16.8 us                                                                | 16.9 us: 1.00x slower                                                            |
| xml_etree_iterparse        | 97.2 ms                                                                | 97.8 ms: 1.01x slower                                                            |
| bench_mp_pool              | 80.7 ms                                                                | 81.2 ms: 1.01x slower                                                            |
| 2to3                       | 254 ms                                                                 | 255 ms: 1.01x slower                                                             |
| many_optionals             | 937 us                                                                 | 943 us: 1.01x slower                                                             |
| async_tree_cpu_io_mixed_tg | 460 ms                                                                 | 464 ms: 1.01x slower                                                             |
| richards_super             | 50.4 ms                                                                | 50.7 ms: 1.01x slower                                                            |
| dulwich_log                | 64.6 ms                                                                | 65.0 ms: 1.01x slower                                                            |
| bench_thread_pool          | 863 us                                                                 | 870 us: 1.01x slower                                                             |
| chaos                      | 60.3 ms                                                                | 60.8 ms: 1.01x slower                                                            |
| docutils                   | 2.58 sec                                                               | 2.61 sec: 1.01x slower                                                           |
| sqlglot_optimize           | 52.5 ms                                                                | 53.2 ms: 1.01x slower                                                            |
| richards                   | 44.3 ms                                                                | 44.8 ms: 1.01x slower                                                            |
| scimark_monte_carlo        | 67.8 ms                                                                | 68.6 ms: 1.01x slower                                                            |
| sympy_expand               | 451 ms                                                                 | 457 ms: 1.01x slower                                                             |
| genshi_text                | 21.2 ms                                                                | 21.5 ms: 1.01x slower                                                            |
| sympy_integrate            | 19.6 ms                                                                | 19.9 ms: 1.01x slower                                                            |
| deepcopy_reduce            | 2.66 us                                                                | 2.70 us: 1.01x slower                                                            |
| sphinx                     | 1.01 sec                                                               | 1.02 sec: 1.01x slower                                                           |
| sympy_str                  | 265 ms                                                                 | 270 ms: 1.02x slower                                                             |
| nbody                      | 96.4 ms                                                                | 98.0 ms: 1.02x slower                                                            |
| pickle_pure_python         | 322 us                                                                 | 328 us: 1.02x slower                                                             |
| pprint_safe_repr           | 722 ms                                                                 | 736 ms: 1.02x slower                                                             |
| sqlalchemy_declarative     | 129 ms                                                                 | 131 ms: 1.02x slower                                                             |
| regex_dna                  | 210 ms                                                                 | 215 ms: 1.02x slower                                                             |
| telco                      | 7.73 ms                                                                | 7.91 ms: 1.02x slower                                                            |
| django_template            | 32.0 ms                                                                | 32.8 ms: 1.02x slower                                                            |
| genshi_xml                 | 48.5 ms                                                                | 49.7 ms: 1.03x slower                                                            |
| pprint_pformat             | 1.47 sec                                                               | 1.51 sec: 1.03x slower                                                           |
| thrift                     | 762 us                                                                 | 782 us: 1.03x slower                                                             |
| deepcopy                   | 255 us                                                                 | 262 us: 1.03x slower                                                             |
| sqlalchemy_imperative      | 16.4 ms                                                                | 16.8 ms: 1.03x slower                                                            |
| regex_compile              | 126 ms                                                                 | 130 ms: 1.03x slower                                                             |
| tomli_loads                | 1.97 sec                                                               | 2.03 sec: 1.03x slower                                                           |
| regex_v8                   | 24.5 ms                                                                | 25.3 ms: 1.04x slower                                                            |
| typing_runtime_protocols   | 159 us                                                                 | 165 us: 1.04x slower                                                             |
| xml_etree_process          | 59.4 ms                                                                | 61.6 ms: 1.04x slower                                                            |
| logging_format             | 6.16 us                                                                | 6.41 us: 1.04x slower                                                            |
| logging_simple             | 5.58 us                                                                | 5.82 us: 1.04x slower                                                            |
| logging_silent             | 103 ns                                                                 | 108 ns: 1.04x slower                                                             |
| html5lib                   | 59.8 ms                                                                | 62.4 ms: 1.04x slower                                                            |
| pycparser                  | 1.13 sec                                                               | 1.17 sec: 1.04x slower                                                           |
| deepcopy_memo              | 30.2 us                                                                | 31.6 us: 1.04x slower                                                            |
| unpickle_pure_python       | 216 us                                                                 | 228 us: 1.06x slower                                                             |
| regex_effbot               | 3.16 ms                                                                | 3.41 ms: 1.08x slower                                                            |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (28): scimark_sparse_mat_mult, async_tree_none_tg, shortest_path, pathlib, float, json, xml_etree_generate, async_tree_none, sympy_sum, scimark_lu, meteor_contest, sqlite_synth, nqueens, pyflate, pidigits, asyncio_websockets, create_gc_cycles, mdp, fannkuch, async_tree_memoization, subparsers, async_tree_memoization_tg, pylint, async_tree_io, connected_components, k_core, async_tree_cpu_io_mixed, async_tree_io_tg

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x