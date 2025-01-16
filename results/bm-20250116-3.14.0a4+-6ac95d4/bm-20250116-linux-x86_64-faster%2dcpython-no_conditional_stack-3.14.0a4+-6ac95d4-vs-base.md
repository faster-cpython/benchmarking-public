# Results vs. base

- fork: faster-cpython
- ref: no_conditional_stack
- machine: linux-x86_64
- commit hash: 6ac95d4
- commit date: 2025-01-16
- overall geometric mean: 1.004x slower
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 255 ms: 1.00x slower                                                             |
| docutils       | 2.58 sec                                                               | 2.60 sec: 1.01x slower                                                           |
| html5lib       | 59.8 ms                                                                | 62.3 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_generators           | 393 ms                                                                 | 380 ms: 1.03x faster                                                             |
| async_tree_none            | 261 ms                                                                 | 257 ms: 1.02x faster                                                             |
| async_tree_none_tg         | 248 ms                                                                 | 245 ms: 1.02x faster                                                             |
| async_tree_memoization_tg  | 306 ms                                                                 | 303 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed    | 485 ms                                                                 | 489 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed_tg | 460 ms                                                                 | 465 ms: 1.01x slower                                                             |
| coroutines                 | 24.0 ms                                                                | 24.3 ms: 1.01x slower                                                            |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_memoization, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 96.4 ms                                                                | 93.6 ms: 1.03x faster                                                            |
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.16 ms                                                                | 3.17 ms: 1.00x slower                                                            |
| regex_dna      | 210 ms                                                                 | 213 ms: 1.02x slower                                                             |
| regex_compile  | 126 ms                                                                 | 128 ms: 1.02x slower                                                             |
| regex_v8       | 24.5 ms                                                                | 25.2 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 29.5 us                                                                | 28.8 us: 1.03x faster                                                            |
| xml_etree_generate   | 84.3 ms                                                                | 84.0 ms: 1.00x faster                                                            |
| pickle_pure_python   | 322 us                                                                 | 323 us: 1.00x slower                                                             |
| xml_etree_iterparse  | 97.2 ms                                                                | 98.5 ms: 1.01x slower                                                            |
| tomli_loads          | 1.97 sec                                                               | 2.00 sec: 1.02x slower                                                           |
| json_dumps           | 11.8 ms                                                                | 12.1 ms: 1.02x slower                                                            |
| xml_etree_process    | 59.4 ms                                                                | 61.5 ms: 1.04x slower                                                            |
| unpickle_pure_python | 216 us                                                                 | 228 us: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.03 ms                                                                | 7.00 ms: 1.00x faster                                                            |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.3 ms                                                                | 11.3 ms: 1.01x faster                                                            |
| django_template | 32.0 ms                                                                | 31.9 ms: 1.00x faster                                                            |
| genshi_xml      | 48.5 ms                                                                | 49.4 ms: 1.02x slower                                                            |
| genshi_text     | 21.2 ms                                                                | 21.8 ms: 1.03x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20250115-linux-x86_64-python-ae7f621c33c854334c69-3.14.0a4+-ae7f621 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_generators           | 393 ms                                                                 | 380 ms: 1.03x faster                                                             |
| nbody                      | 96.4 ms                                                                | 93.6 ms: 1.03x faster                                                            |
| json_loads                 | 29.5 us                                                                | 28.8 us: 1.03x faster                                                            |
| deltablue                  | 3.20 ms                                                                | 3.12 ms: 1.02x faster                                                            |
| raytrace                   | 270 ms                                                                 | 265 ms: 1.02x faster                                                             |
| pyflate                    | 471 ms                                                                 | 462 ms: 1.02x faster                                                             |
| async_tree_none            | 261 ms                                                                 | 257 ms: 1.02x faster                                                             |
| async_tree_none_tg         | 248 ms                                                                 | 245 ms: 1.02x faster                                                             |
| async_tree_memoization_tg  | 306 ms                                                                 | 303 ms: 1.01x faster                                                             |
| scimark_fft                | 351 ms                                                                 | 347 ms: 1.01x faster                                                             |
| scimark_monte_carlo        | 67.8 ms                                                                | 67.1 ms: 1.01x faster                                                            |
| go                         | 118 ms                                                                 | 117 ms: 1.01x faster                                                             |
| json                       | 5.27 ms                                                                | 5.23 ms: 1.01x faster                                                            |
| sqlite_synth               | 2.81 us                                                                | 2.78 us: 1.01x faster                                                            |
| scimark_sor                | 122 ms                                                                 | 122 ms: 1.01x faster                                                             |
| nqueens                    | 80.5 ms                                                                | 80.0 ms: 1.01x faster                                                            |
| sqlglot_transpile          | 1.58 ms                                                                | 1.57 ms: 1.01x faster                                                            |
| generators                 | 27.6 ms                                                                | 27.5 ms: 1.01x faster                                                            |
| mako                       | 11.3 ms                                                                | 11.3 ms: 1.01x faster                                                            |
| sqlglot_parse              | 1.27 ms                                                                | 1.26 ms: 1.00x faster                                                            |
| chaos                      | 60.3 ms                                                                | 60.0 ms: 1.00x faster                                                            |
| python_startup_no_site     | 7.03 ms                                                                | 7.00 ms: 1.00x faster                                                            |
| django_template            | 32.0 ms                                                                | 31.9 ms: 1.00x faster                                                            |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.00x faster                                                             |
| hexiom                     | 6.37 ms                                                                | 6.35 ms: 1.00x faster                                                            |
| xml_etree_generate         | 84.3 ms                                                                | 84.0 ms: 1.00x faster                                                            |
| bench_thread_pool          | 863 us                                                                 | 861 us: 1.00x faster                                                             |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                            |
| meteor_contest             | 106 ms                                                                 | 106 ms: 1.00x faster                                                             |
| regex_effbot               | 3.16 ms                                                                | 3.17 ms: 1.00x slower                                                            |
| 2to3                       | 254 ms                                                                 | 255 ms: 1.00x slower                                                             |
| logging_silent             | 103 ns                                                                 | 104 ns: 1.00x slower                                                             |
| richards                   | 44.3 ms                                                                | 44.5 ms: 1.00x slower                                                            |
| pickle_pure_python         | 322 us                                                                 | 323 us: 1.00x slower                                                             |
| sympy_expand               | 451 ms                                                                 | 454 ms: 1.00x slower                                                             |
| deepcopy_reduce            | 2.66 us                                                                | 2.67 us: 1.01x slower                                                            |
| docutils                   | 2.58 sec                                                               | 2.60 sec: 1.01x slower                                                           |
| sympy_str                  | 265 ms                                                                 | 267 ms: 1.01x slower                                                             |
| sqlglot_normalize          | 104 ms                                                                 | 105 ms: 1.01x slower                                                             |
| mdp                        | 2.47 sec                                                               | 2.49 sec: 1.01x slower                                                           |
| bpe_tokeniser              | 4.50 sec                                                               | 4.54 sec: 1.01x slower                                                           |
| deepcopy_memo              | 30.2 us                                                                | 30.5 us: 1.01x slower                                                            |
| sympy_integrate            | 19.6 ms                                                                | 19.8 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed    | 485 ms                                                                 | 489 ms: 1.01x slower                                                             |
| deepcopy                   | 255 us                                                                 | 258 us: 1.01x slower                                                             |
| pprint_pformat             | 1.47 sec                                                               | 1.49 sec: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 460 ms                                                                 | 465 ms: 1.01x slower                                                             |
| gc_traversal               | 4.80 ms                                                                | 4.86 ms: 1.01x slower                                                            |
| sqlglot_optimize           | 52.5 ms                                                                | 53.2 ms: 1.01x slower                                                            |
| xml_etree_iterparse        | 97.2 ms                                                                | 98.5 ms: 1.01x slower                                                            |
| coroutines                 | 24.0 ms                                                                | 24.3 ms: 1.01x slower                                                            |
| regex_dna                  | 210 ms                                                                 | 213 ms: 1.02x slower                                                             |
| scimark_lu                 | 116 ms                                                                 | 117 ms: 1.02x slower                                                             |
| tomli_loads                | 1.97 sec                                                               | 2.00 sec: 1.02x slower                                                           |
| many_optionals             | 937 us                                                                 | 952 us: 1.02x slower                                                             |
| sqlalchemy_declarative     | 129 ms                                                                 | 131 ms: 1.02x slower                                                             |
| pathlib                    | 15.9 ms                                                                | 16.1 ms: 1.02x slower                                                            |
| logging_simple             | 5.58 us                                                                | 5.69 us: 1.02x slower                                                            |
| genshi_xml                 | 48.5 ms                                                                | 49.4 ms: 1.02x slower                                                            |
| regex_compile              | 126 ms                                                                 | 128 ms: 1.02x slower                                                             |
| fannkuch                   | 401 ms                                                                 | 409 ms: 1.02x slower                                                             |
| subparsers                 | 20.4 ms                                                                | 20.8 ms: 1.02x slower                                                            |
| sqlalchemy_imperative      | 16.4 ms                                                                | 16.7 ms: 1.02x slower                                                            |
| json_dumps                 | 11.8 ms                                                                | 12.1 ms: 1.02x slower                                                            |
| telco                      | 7.73 ms                                                                | 7.90 ms: 1.02x slower                                                            |
| logging_format             | 6.16 us                                                                | 6.31 us: 1.02x slower                                                            |
| genshi_text                | 21.2 ms                                                                | 21.8 ms: 1.03x slower                                                            |
| regex_v8                   | 24.5 ms                                                                | 25.2 ms: 1.03x slower                                                            |
| xml_etree_process          | 59.4 ms                                                                | 61.5 ms: 1.04x slower                                                            |
| html5lib                   | 59.8 ms                                                                | 62.3 ms: 1.04x slower                                                            |
| unpickle_pure_python       | 216 us                                                                 | 228 us: 1.06x slower                                                             |
| typing_runtime_protocols   | 159 us                                                                 | 168 us: 1.06x slower                                                             |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (24): float, coverage, async_tree_io_tg, comprehensions, sympy_sum, richards_super, create_gc_cycles, dulwich_log, crypto_pyaes, async_tree_memoization, async_tree_io, thrift, shortest_path, asyncio_websockets, pylint, k_core, pprint_safe_repr, connected_components, spectral_norm, bench_mp_pool, xml_etree_parse, scimark_sparse_mat_mult, sphinx, pycparser

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.52% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x