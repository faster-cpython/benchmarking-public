# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.004x slower
- HPT reliability: 98.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| docutils       | 2.64 sec                                                              | 2.65 sec: 1.01x slower                                            |
| html5lib       | 61.4 ms                                                               | 62.3 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| coroutines             | 25.1 ms                                                               | 24.3 ms: 1.03x faster                                             |
| async_generators       | 441 ms                                                                | 433 ms: 1.02x faster                                              |
| async_tree_memoization | 315 ms                                                                | 314 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 65.1 ms                                                               | 66.3 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.31 ms                                                               | 3.32 ms: 1.00x slower                                             |
| regex_compile  | 127 ms                                                                | 128 ms: 1.01x slower                                              |
| regex_v8       | 22.4 ms                                                               | 22.8 ms: 1.02x slower                                             |
| regex_dna      | 200 ms                                                                | 219 ms: 1.09x slower                                              |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 11.2 ms                                                               | 11.0 ms: 1.02x faster                                             |
| xml_etree_parse      | 141 ms                                                                | 140 ms: 1.01x faster                                              |
| xml_etree_iterparse  | 98.5 ms                                                               | 98.3 ms: 1.00x faster                                             |
| pickle_pure_python   | 322 us                                                                | 325 us: 1.01x slower                                              |
| tomli_loads          | 1.90 sec                                                              | 1.92 sec: 1.01x slower                                            |
| xml_etree_generate   | 80.0 ms                                                               | 80.8 ms: 1.01x slower                                             |
| json_loads           | 28.4 us                                                               | 28.8 us: 1.01x slower                                             |
| unpickle_pure_python | 201 us                                                                | 205 us: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                             |
| python_startup_no_site | 6.96 ms                                                               | 6.96 ms: 1.00x faster                                             |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 32.5 ms                                                               | 32.7 ms: 1.01x slower                                             |
| genshi_xml      | 49.7 ms                                                               | 50.3 ms: 1.01x slower                                             |
| mako            | 10.6 ms                                                               | 10.8 ms: 1.02x slower                                             |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| coroutines              | 25.1 ms                                                               | 24.3 ms: 1.03x faster                                             |
| json_dumps              | 11.2 ms                                                               | 11.0 ms: 1.02x faster                                             |
| async_generators        | 441 ms                                                                | 433 ms: 1.02x faster                                              |
| meteor_contest          | 108 ms                                                                | 106 ms: 1.02x faster                                              |
| generators              | 31.0 ms                                                               | 30.5 ms: 1.02x faster                                             |
| dulwich_log             | 60.6 ms                                                               | 59.6 ms: 1.02x faster                                             |
| telco                   | 7.92 ms                                                               | 7.80 ms: 1.02x faster                                             |
| subparsers              | 23.8 ms                                                               | 23.5 ms: 1.01x faster                                             |
| scimark_monte_carlo     | 67.5 ms                                                               | 67.0 ms: 1.01x faster                                             |
| xml_etree_parse         | 141 ms                                                                | 140 ms: 1.01x faster                                              |
| scimark_sor             | 122 ms                                                                | 121 ms: 1.01x faster                                              |
| async_tree_memoization  | 315 ms                                                                | 314 ms: 1.00x faster                                              |
| xml_etree_iterparse     | 98.5 ms                                                               | 98.3 ms: 1.00x faster                                             |
| python_startup          | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                             |
| python_startup_no_site  | 6.96 ms                                                               | 6.96 ms: 1.00x faster                                             |
| create_gc_cycles        | 2.59 ms                                                               | 2.59 ms: 1.00x slower                                             |
| gc_traversal            | 4.92 ms                                                               | 4.93 ms: 1.00x slower                                             |
| chaos                   | 62.2 ms                                                               | 62.4 ms: 1.00x slower                                             |
| regex_effbot            | 3.31 ms                                                               | 3.32 ms: 1.00x slower                                             |
| coverage                | 87.7 ms                                                               | 88.1 ms: 1.00x slower                                             |
| sympy_integrate         | 19.4 ms                                                               | 19.5 ms: 1.00x slower                                             |
| docutils                | 2.64 sec                                                              | 2.65 sec: 1.01x slower                                            |
| regex_compile           | 127 ms                                                                | 128 ms: 1.01x slower                                              |
| django_template         | 32.5 ms                                                               | 32.7 ms: 1.01x slower                                             |
| sympy_sum               | 150 ms                                                                | 151 ms: 1.01x slower                                              |
| scimark_sparse_mat_mult | 5.00 ms                                                               | 5.04 ms: 1.01x slower                                             |
| pickle_pure_python      | 322 us                                                                | 325 us: 1.01x slower                                              |
| scimark_lu              | 117 ms                                                                | 119 ms: 1.01x slower                                              |
| logging_silent          | 470 ns                                                                | 474 ns: 1.01x slower                                              |
| deepcopy_memo           | 29.5 us                                                               | 29.8 us: 1.01x slower                                             |
| tomli_loads             | 1.90 sec                                                              | 1.92 sec: 1.01x slower                                            |
| connected_components    | 458 ms                                                                | 462 ms: 1.01x slower                                              |
| go                      | 122 ms                                                                | 123 ms: 1.01x slower                                              |
| xml_etree_generate      | 80.0 ms                                                               | 80.8 ms: 1.01x slower                                             |
| json                    | 5.24 ms                                                               | 5.29 ms: 1.01x slower                                             |
| fannkuch                | 411 ms                                                                | 416 ms: 1.01x slower                                              |
| deepcopy                | 258 us                                                                | 260 us: 1.01x slower                                              |
| raytrace                | 275 ms                                                                | 278 ms: 1.01x slower                                              |
| deepcopy_reduce         | 2.69 us                                                               | 2.72 us: 1.01x slower                                             |
| genshi_xml              | 49.7 ms                                                               | 50.3 ms: 1.01x slower                                             |
| shortest_path           | 492 ms                                                                | 498 ms: 1.01x slower                                              |
| json_loads              | 28.4 us                                                               | 28.8 us: 1.01x slower                                             |
| html5lib                | 61.4 ms                                                               | 62.3 ms: 1.01x slower                                             |
| regex_v8                | 22.4 ms                                                               | 22.8 ms: 1.02x slower                                             |
| comprehensions          | 17.1 us                                                               | 17.4 us: 1.02x slower                                             |
| float                   | 65.1 ms                                                               | 66.3 ms: 1.02x slower                                             |
| mako                    | 10.6 ms                                                               | 10.8 ms: 1.02x slower                                             |
| logging_simple          | 6.08 us                                                               | 6.21 us: 1.02x slower                                             |
| unpickle_pure_python    | 201 us                                                                | 205 us: 1.02x slower                                              |
| logging_format          | 6.69 us                                                               | 6.89 us: 1.03x slower                                             |
| pprint_pformat          | 1.68 sec                                                              | 1.73 sec: 1.03x slower                                            |
| deltablue               | 3.11 ms                                                               | 3.22 ms: 1.04x slower                                             |
| spectral_norm           | 101 ms                                                                | 105 ms: 1.04x slower                                              |
| pyflate                 | 412 ms                                                                | 432 ms: 1.05x slower                                              |
| regex_dna               | 200 ms                                                                | 219 ms: 1.09x slower                                              |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (38): richards_super, k_core, thrift, async_tree_io_tg, pycparser, genshi_text, sqlglot_v2_normalize, sqlite_synth, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none, many_optionals, sympy_str, typing_runtime_protocols, async_tree_cpu_io_mixed_tg, sqlglot_v2_transpile, 2to3, pylint, pidigits, asyncio_websockets, sympy_expand, sqlglot_v2_optimize, async_tree_io, hexiom, bpe_tokeniser, nqueens, djangocms, mdp, pathlib, xml_etree_process, scimark_fft, crypto_pyaes, sqlglot_v2_parse, async_tree_memoization_tg, nbody, sphinx, richards, pprint_safe_repr

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 98.93% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x