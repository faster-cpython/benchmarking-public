# Results vs. base

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-aarch64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.031x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 3.78 sec                                                                 | 3.83 sec: 1.01x slower                                                         |
| html5lib       | 72.9 ms                                                                  | 76.4 ms: 1.05x slower                                                          |
| sphinx         | 1.53 sec                                                                 | 1.58 sec: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                    | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-------------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg        | 1.27 sec                                                                 | 1.30 sec: 1.02x slower                                                         |
| async_tree_cpu_io_mixed | 763 ms                                                                   | 809 ms: 1.06x slower                                                           |
| Geometric mean          | (ref)                                                                    | 1.02x slower                                                                   |

Benchmark hidden because not significant (9): asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization, async_tree_none_tg, coroutines, async_tree_none, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 95.6 ms                                                                  | 108 ms: 1.13x slower                                                           |
| nbody          | 114 ms                                                                   | 133 ms: 1.17x slower                                                           |
| Geometric mean | (ref)                                                                    | 1.10x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 263 ms                                                                   | 277 ms: 1.05x slower                                                           |
| regex_effbot   | 5.01 ms                                                                  | 5.38 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                                    | 1.05x slower                                                                   |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                   | 155 ms: 1.04x slower                                                           |
| unpickle_pure_python | 274 us                                                                   | 292 us: 1.06x slower                                                           |
| tomli_loads          | 2.61 sec                                                                 | 2.82 sec: 1.08x slower                                                         |
| Geometric mean       | (ref)                                                                    | 1.04x slower                                                                   |

Benchmark hidden because not significant (6): json_dumps, json_loads, xml_etree_parse, xml_etree_generate, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): django_template, genshi_xml, mako, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|--------------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| sqlalchemy_imperative    | 19.6 ms                                                                  | 18.5 ms: 1.06x faster                                                          |
| dulwich_log              | 83.3 ms                                                                  | 79.2 ms: 1.05x faster                                                          |
| docutils                 | 3.78 sec                                                                 | 3.83 sec: 1.01x slower                                                         |
| sympy_sum                | 212 ms                                                                   | 216 ms: 1.02x slower                                                           |
| k_core                   | 4.55 sec                                                                 | 4.65 sec: 1.02x slower                                                         |
| async_tree_io_tg         | 1.27 sec                                                                 | 1.30 sec: 1.02x slower                                                         |
| shortest_path            | 580 ms                                                                   | 594 ms: 1.02x slower                                                           |
| mdp                      | 3.62 sec                                                                 | 3.71 sec: 1.03x slower                                                         |
| connected_components     | 555 ms                                                                   | 571 ms: 1.03x slower                                                           |
| sphinx                   | 1.53 sec                                                                 | 1.58 sec: 1.03x slower                                                         |
| sympy_expand             | 597 ms                                                                   | 619 ms: 1.04x slower                                                           |
| xml_etree_iterparse      | 150 ms                                                                   | 155 ms: 1.04x slower                                                           |
| sympy_integrate          | 28.9 ms                                                                  | 30.0 ms: 1.04x slower                                                          |
| go                       | 189 ms                                                                   | 197 ms: 1.04x slower                                                           |
| pylint                   | 433 ms                                                                   | 451 ms: 1.04x slower                                                           |
| logging_format           | 8.30 us                                                                  | 8.67 us: 1.05x slower                                                          |
| html5lib                 | 72.9 ms                                                                  | 76.4 ms: 1.05x slower                                                          |
| regex_dna                | 263 ms                                                                   | 277 ms: 1.05x slower                                                           |
| bpe_tokeniser            | 5.87 sec                                                                 | 6.20 sec: 1.06x slower                                                         |
| scimark_lu               | 153 ms                                                                   | 161 ms: 1.06x slower                                                           |
| fannkuch                 | 500 ms                                                                   | 528 ms: 1.06x slower                                                           |
| pycparser                | 1.51 sec                                                                 | 1.60 sec: 1.06x slower                                                         |
| sqlglot_normalize        | 162 ms                                                                   | 171 ms: 1.06x slower                                                           |
| async_tree_cpu_io_mixed  | 763 ms                                                                   | 809 ms: 1.06x slower                                                           |
| typing_runtime_protocols | 219 us                                                                   | 233 us: 1.06x slower                                                           |
| unpickle_pure_python     | 274 us                                                                   | 292 us: 1.06x slower                                                           |
| chaos                    | 84.3 ms                                                                  | 90.0 ms: 1.07x slower                                                          |
| logging_simple           | 7.58 us                                                                  | 8.11 us: 1.07x slower                                                          |
| regex_effbot             | 5.01 ms                                                                  | 5.38 ms: 1.08x slower                                                          |
| tomli_loads              | 2.61 sec                                                                 | 2.82 sec: 1.08x slower                                                         |
| spectral_norm            | 156 ms                                                                   | 169 ms: 1.08x slower                                                           |
| scimark_fft              | 443 ms                                                                   | 483 ms: 1.09x slower                                                           |
| raytrace                 | 362 ms                                                                   | 402 ms: 1.11x slower                                                           |
| pyflate                  | 612 ms                                                                   | 678 ms: 1.11x slower                                                           |
| scimark_sor              | 158 ms                                                                   | 176 ms: 1.11x slower                                                           |
| deepcopy_memo            | 41.7 us                                                                  | 46.4 us: 1.11x slower                                                          |
| nqueens                  | 124 ms                                                                   | 139 ms: 1.12x slower                                                           |
| hexiom                   | 9.88 ms                                                                  | 11.1 ms: 1.13x slower                                                          |
| float                    | 95.6 ms                                                                  | 108 ms: 1.13x slower                                                           |
| richards_super           | 73.6 ms                                                                  | 83.2 ms: 1.13x slower                                                          |
| comprehensions           | 24.4 us                                                                  | 28.2 us: 1.16x slower                                                          |
| richards                 | 63.5 ms                                                                  | 73.5 ms: 1.16x slower                                                          |
| nbody                    | 114 ms                                                                   | 133 ms: 1.17x slower                                                           |
| generators               | 50.4 ms                                                                  | 59.5 ms: 1.18x slower                                                          |
| logging_silent           | 140 ns                                                                   | 169 ns: 1.21x slower                                                           |
| deltablue                | 4.30 ms                                                                  | 5.31 ms: 1.24x slower                                                          |
| Geometric mean           | (ref)                                                                    | 1.05x slower                                                                   |

Benchmark hidden because not significant (51): create_gc_cycles, djangocms, django_template, json_dumps, sqlite_synth, pprint_safe_repr, pprint_pformat, genshi_xml, asyncio_websockets, subparsers, bench_thread_pool, bench_mp_pool, coverage, python_startup, pidigits, python_startup_no_site, sqlalchemy_declarative, async_tree_memoization_tg, json_loads, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization, async_tree_none_tg, sympy_str, xml_etree_parse, crypto_pyaes, coroutines, thrift, regex_v8, telco, 2to3, deepcopy_reduce, scimark_sparse_mat_mult, async_tree_none, json, pathlib, gc_traversal, sqlglot_optimize, async_generators, xml_etree_generate, regex_compile, meteor_contest, xml_etree_process, mako, many_optionals, pickle_pure_python, deepcopy, sqlglot_parse, genshi_text, sqlglot_transpile, scimark_monte_carlo

- Geometric mean (including insignificant results): 1.031x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x