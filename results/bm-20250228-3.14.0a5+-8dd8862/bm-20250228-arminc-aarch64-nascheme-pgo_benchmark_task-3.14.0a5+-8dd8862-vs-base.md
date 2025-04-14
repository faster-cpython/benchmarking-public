# Results vs. base

- fork: nascheme
- ref: pgo_benchmark_task
- machine: linux-aarch64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.016x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250226-arminc-aarch64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| html5lib       | 63.1 ms                                                                  | 58.7 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250226-arminc-aarch64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_generators       | 447 ms                                                                   | 411 ms: 1.09x faster                                                     |
| async_tree_none        | 391 ms                                                                   | 362 ms: 1.08x faster                                                     |
| async_tree_none_tg     | 385 ms                                                                   | 369 ms: 1.04x faster                                                     |
| async_tree_io_tg       | 931 ms                                                                   | 895 ms: 1.04x faster                                                     |
| async_tree_memoization | 479 ms                                                                   | 461 ms: 1.04x faster                                                     |
| async_tree_io          | 915 ms                                                                   | 887 ms: 1.03x faster                                                     |
| Geometric mean         | (ref)                                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (5): coroutines, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250226-arminc-aarch64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 250 ms                                                                   | 197 ms: 1.27x faster                                                     |
| regex_effbot   | 4.03 ms                                                                  | 3.30 ms: 1.22x faster                                                    |
| regex_v8       | 31.8 ms                                                                  | 29.2 ms: 1.09x faster                                                    |
| regex_compile  | 123 ms                                                                   | 128 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                    | 1.13x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark       | bm-20250226-arminc-aarch64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse | 183 ms                                                                   | 165 ms: 1.11x faster                                                     |
| json_loads      | 35.9 us                                                                  | 33.2 us: 1.08x faster                                                    |
| tomli_loads     | 2.56 sec                                                                 | 2.66 sec: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_iterparse, xml_etree_process, pickle_pure_python, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark               | bm-20250226-arminc-aarch64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-------------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna               | 250 ms                                                                   | 197 ms: 1.27x faster                                                     |
| regex_effbot            | 4.03 ms                                                                  | 3.30 ms: 1.22x faster                                                    |
| meteor_contest          | 117 ms                                                                   | 103 ms: 1.13x faster                                                     |
| scimark_fft             | 429 ms                                                                   | 384 ms: 1.12x faster                                                     |
| xml_etree_parse         | 183 ms                                                                   | 165 ms: 1.11x faster                                                     |
| regex_v8                | 31.8 ms                                                                  | 29.2 ms: 1.09x faster                                                    |
| async_generators        | 447 ms                                                                   | 411 ms: 1.09x faster                                                     |
| async_tree_none         | 391 ms                                                                   | 362 ms: 1.08x faster                                                     |
| json_loads              | 35.9 us                                                                  | 33.2 us: 1.08x faster                                                    |
| html5lib                | 63.1 ms                                                                  | 58.7 ms: 1.08x faster                                                    |
| scimark_sparse_mat_mult | 6.51 ms                                                                  | 6.11 ms: 1.07x faster                                                    |
| pylint                  | 324 ms                                                                   | 307 ms: 1.06x faster                                                     |
| bpe_tokeniser           | 5.69 sec                                                                 | 5.40 sec: 1.05x faster                                                   |
| telco                   | 9.50 ms                                                                  | 9.03 ms: 1.05x faster                                                    |
| pprint_safe_repr        | 960 ms                                                                   | 912 ms: 1.05x faster                                                     |
| async_tree_none_tg      | 385 ms                                                                   | 369 ms: 1.04x faster                                                     |
| async_tree_io_tg        | 931 ms                                                                   | 895 ms: 1.04x faster                                                     |
| async_tree_memoization  | 479 ms                                                                   | 461 ms: 1.04x faster                                                     |
| pprint_pformat          | 1.96 sec                                                                 | 1.90 sec: 1.03x faster                                                   |
| async_tree_io           | 915 ms                                                                   | 887 ms: 1.03x faster                                                     |
| mdp                     | 3.41 sec                                                                 | 3.31 sec: 1.03x faster                                                   |
| k_core                  | 2.83 sec                                                                 | 2.92 sec: 1.03x slower                                                   |
| tomli_loads             | 2.56 sec                                                                 | 2.66 sec: 1.04x slower                                                   |
| json                    | 5.94 ms                                                                  | 6.20 ms: 1.04x slower                                                    |
| regex_compile           | 123 ms                                                                   | 128 ms: 1.04x slower                                                     |
| sympy_str               | 260 ms                                                                   | 279 ms: 1.07x slower                                                     |
| Geometric mean          | (ref)                                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (70): xml_etree_generate, xml_etree_iterparse, xml_etree_process, gc_traversal, typing_runtime_protocols, bench_mp_pool, float, coverage, fannkuch, pidigits, coroutines, sqlite_synth, scimark_monte_carlo, async_tree_cpu_io_mixed, many_optionals, sqlglot_normalize, async_tree_cpu_io_mixed_tg, genshi_text, chaos, async_tree_memoization_tg, deepcopy_memo, genshi_xml, deepcopy, raytrace, scimark_lu, pyflate, deepcopy_reduce, pathlib, nqueens, sqlalchemy_imperative, scimark_sor, spectral_norm, django_template, generators, comprehensions, asyncio_websockets, sphinx, go, mako, pickle_pure_python, richards, shortest_path, logging_simple, docutils, json_dumps, deltablue, sympy_sum, sqlglot_parse, python_startup_no_site, crypto_pyaes, python_startup, logging_format, 2to3, pycparser, sqlalchemy_declarative, richards_super, sqlglot_optimize, sqlglot_transpile, subparsers, bench_thread_pool, connected_components, thrift, nbody, hexiom, sympy_expand, create_gc_cycles, sympy_integrate, logging_silent, dulwich_log, unpickle_pure_python

- Geometric mean (including insignificant results): 1.016x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x