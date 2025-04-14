# Results vs. base

- fork: Fidget-Spinner
- ref: baseline_jit
- machine: linux-aarch64
- commit hash: e55b89a
- commit date: 2025-03-19
- overall geometric mean: 1.009x faster
- HPT reliability: 99.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 311 ms                                                                   | 307 ms: 1.01x faster                                                       |
| docutils       | 3.23 sec                                                                 | 3.10 sec: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                               |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|--------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators   | 488 ms                                                                   | 470 ms: 1.04x faster                                                       |
| async_tree_none_tg | 379 ms                                                                   | 375 ms: 1.01x faster                                                       |
| Geometric mean     | (ref)                                                                    | 1.01x faster                                                               |

Benchmark hidden because not significant (9): async_tree_memoization_tg, coroutines, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none, asyncio_websockets, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 86.6 ms                                                                  | 89.9 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                               |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 28.0 ms                                                                  | 27.5 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                               |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|--------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python | 408 us                                                                   | 400 us: 1.02x faster                                                       |
| tomli_loads        | 2.45 sec                                                                 | 2.41 sec: 1.02x faster                                                     |
| xml_etree_generate | 109 ms                                                                   | 114 ms: 1.04x slower                                                       |
| Geometric mean     | (ref)                                                                    | 1.01x slower                                                               |

Benchmark hidden because not significant (6): json_dumps, json_loads, xml_etree_iterparse, xml_etree_parse, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 16.1 ms                                                                  | 16.3 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 13.8 ms                                                                  | 15.0 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                               |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark            | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pprint_pformat       | 2.59 sec                                                                 | 2.04 sec: 1.27x faster                                                     |
| pprint_safe_repr     | 1.25 sec                                                                 | 1.01 sec: 1.24x faster                                                     |
| go                   | 185 ms                                                                   | 156 ms: 1.19x faster                                                       |
| crypto_pyaes         | 102 ms                                                                   | 94.3 ms: 1.08x faster                                                      |
| pycparser            | 1.42 sec                                                                 | 1.34 sec: 1.06x faster                                                     |
| spectral_norm        | 138 ms                                                                   | 131 ms: 1.05x faster                                                       |
| sympy_expand         | 509 ms                                                                   | 488 ms: 1.04x faster                                                       |
| pylint               | 332 ms                                                                   | 319 ms: 1.04x faster                                                       |
| docutils             | 3.23 sec                                                                 | 3.10 sec: 1.04x faster                                                     |
| k_core               | 2.96 sec                                                                 | 2.85 sec: 1.04x faster                                                     |
| async_generators     | 488 ms                                                                   | 470 ms: 1.04x faster                                                       |
| meteor_contest       | 122 ms                                                                   | 118 ms: 1.03x faster                                                       |
| shortest_path        | 598 ms                                                                   | 580 ms: 1.03x faster                                                       |
| scimark_lu           | 153 ms                                                                   | 150 ms: 1.02x faster                                                       |
| logging_simple       | 7.15 us                                                                  | 6.98 us: 1.02x faster                                                      |
| dulwich_log          | 56.4 ms                                                                  | 55.1 ms: 1.02x faster                                                      |
| scimark_fft          | 431 ms                                                                   | 422 ms: 1.02x faster                                                       |
| regex_v8             | 28.0 ms                                                                  | 27.5 ms: 1.02x faster                                                      |
| pickle_pure_python   | 408 us                                                                   | 400 us: 1.02x faster                                                       |
| sympy_sum            | 149 ms                                                                   | 147 ms: 1.02x faster                                                       |
| sqlglot_v2_normalize | 132 ms                                                                   | 129 ms: 1.02x faster                                                       |
| tomli_loads          | 2.45 sec                                                                 | 2.41 sec: 1.02x faster                                                     |
| 2to3                 | 311 ms                                                                   | 307 ms: 1.01x faster                                                       |
| pathlib              | 22.5 ms                                                                  | 22.2 ms: 1.01x faster                                                      |
| async_tree_none_tg   | 379 ms                                                                   | 375 ms: 1.01x faster                                                       |
| connected_components | 574 ms                                                                   | 568 ms: 1.01x faster                                                       |
| sympy_str            | 279 ms                                                                   | 277 ms: 1.01x faster                                                       |
| sqlglot_v2_optimize  | 64.8 ms                                                                  | 64.3 ms: 1.01x faster                                                      |
| nqueens              | 107 ms                                                                   | 106 ms: 1.01x faster                                                       |
| coverage             | 97.5 ms                                                                  | 98.3 ms: 1.01x slower                                                      |
| python_startup       | 16.1 ms                                                                  | 16.3 ms: 1.01x slower                                                      |
| hexiom               | 8.63 ms                                                                  | 8.74 ms: 1.01x slower                                                      |
| thrift               | 929 us                                                                   | 949 us: 1.02x slower                                                       |
| bench_thread_pool    | 1.35 ms                                                                  | 1.38 ms: 1.02x slower                                                      |
| fannkuch             | 515 ms                                                                   | 528 ms: 1.03x slower                                                       |
| bpe_tokeniser        | 5.71 sec                                                                 | 5.88 sec: 1.03x slower                                                     |
| scimark_monte_carlo  | 89.3 ms                                                                  | 91.9 ms: 1.03x slower                                                      |
| float                | 86.6 ms                                                                  | 89.9 ms: 1.04x slower                                                      |
| pyflate              | 575 ms                                                                   | 597 ms: 1.04x slower                                                       |
| deltablue            | 4.17 ms                                                                  | 4.34 ms: 1.04x slower                                                      |
| xml_etree_generate   | 109 ms                                                                   | 114 ms: 1.04x slower                                                       |
| richards_super       | 56.8 ms                                                                  | 61.4 ms: 1.08x slower                                                      |
| mako                 | 13.8 ms                                                                  | 15.0 ms: 1.08x slower                                                      |
| comprehensions       | 25.4 us                                                                  | 27.7 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                                    | 1.01x faster                                                               |

Benchmark hidden because not significant (52): genshi_xml, sqlite_synth, scimark_sparse_mat_mult, create_gc_cycles, raytrace, gc_traversal, pidigits, nbody, logging_silent, async_tree_memoization_tg, deepcopy_memo, scimark_sor, coroutines, logging_format, sphinx, regex_dna, sqlglot_v2_transpile, async_tree_cpu_io_mixed, sqlglot_v2_parse, generators, deepcopy_reduce, async_tree_cpu_io_mixed_tg, async_tree_io_tg, json_dumps, python_startup_no_site, json_loads, mdp, xml_etree_iterparse, genshi_text, async_tree_none, xml_etree_parse, asyncio_websockets, sqlalchemy_declarative, async_tree_memoization, deepcopy, async_tree_io, sqlalchemy_imperative, sympy_integrate, django_template, many_optionals, richards, json, typing_runtime_protocols, html5lib, telco, regex_effbot, unpickle_pure_python, xml_etree_process, subparsers, regex_compile, chaos, bench_mp_pool

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 99.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x