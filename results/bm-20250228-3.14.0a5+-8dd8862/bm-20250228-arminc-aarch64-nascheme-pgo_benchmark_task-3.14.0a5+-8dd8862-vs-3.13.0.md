# Results vs. 3.13.0

- fork: nascheme
- ref: pgo_benchmark_task
- machine: linux-aarch64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.063x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.01 sec: 1.02x slower                                                   |
| html5lib       | 65.6 ms                                                  | 58.7 ms: 1.12x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 461 ms: 1.44x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                     |
| async_tree_none            | 504 ms                                                   | 362 ms: 1.39x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 369 ms: 1.31x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 895 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 887 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 645 ms: 1.24x faster                                                     |
| async_generators           | 500 ms                                                   | 411 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 656 ms: 1.20x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.25x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.3 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.30 ms: 1.55x faster                                                    |
| regex_dna      | 263 ms                                                   | 197 ms: 1.33x faster                                                     |
| regex_v8       | 32.5 ms                                                  | 29.2 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                    | 1.24x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 165 ms: 1.23x faster                                                     |
| xml_etree_iterparse  | 159 ms                                                   | 138 ms: 1.15x faster                                                     |
| xml_etree_generate   | 118 ms                                                   | 109 ms: 1.09x faster                                                     |
| unpickle_pure_python | 265 us                                                   | 287 us: 1.08x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (5): xml_etree_process, tomli_loads, json_loads, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 16.7 ms: 1.04x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 9.33 ms: 1.06x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.05x slower                                                             |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot               | 5.10 ms                                                  | 3.30 ms: 1.55x faster                                                    |
| deepcopy                   | 479 us                                                   | 325 us: 1.47x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 461 ms: 1.44x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                     |
| async_tree_none            | 504 ms                                                   | 362 ms: 1.39x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 39.1 us: 1.36x faster                                                    |
| regex_dna                  | 263 ms                                                   | 197 ms: 1.33x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 369 ms: 1.31x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 895 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 887 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 645 ms: 1.24x faster                                                     |
| spectral_norm              | 143 ms                                                   | 116 ms: 1.24x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 165 ms: 1.23x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.47 us: 1.22x faster                                                    |
| async_generators           | 500 ms                                                   | 411 ms: 1.22x faster                                                     |
| scimark_fft                | 463 ms                                                   | 384 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 656 ms: 1.20x faster                                                     |
| go                         | 164 ms                                                   | 141 ms: 1.17x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.03 ms: 1.16x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 138 ms: 1.15x faster                                                     |
| meteor_contest             | 117 ms                                                   | 103 ms: 1.13x faster                                                     |
| pylint                     | 345 ms                                                   | 307 ms: 1.13x faster                                                     |
| html5lib                   | 65.6 ms                                                  | 58.7 ms: 1.12x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 29.2 ms: 1.11x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.40 sec: 1.11x faster                                                   |
| float                      | 95.8 ms                                                  | 86.3 ms: 1.11x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.8 ms: 1.10x faster                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.11 ms: 1.09x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 109 ms: 1.09x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 22.5 ms: 1.08x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.2 ms: 1.08x faster                                                    |
| scimark_lu                 | 146 ms                                                   | 138 ms: 1.06x faster                                                     |
| scimark_sor                | 164 ms                                                   | 155 ms: 1.06x faster                                                     |
| pprint_safe_repr           | 962 ms                                                   | 912 ms: 1.05x faster                                                     |
| pyflate                    | 582 ms                                                   | 553 ms: 1.05x faster                                                     |
| pprint_pformat             | 1.99 sec                                                 | 1.90 sec: 1.05x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.29 sec: 1.04x faster                                                   |
| mdp                        | 3.45 sec                                                 | 3.31 sec: 1.04x faster                                                   |
| sqlglot_normalize          | 131 ms                                                   | 126 ms: 1.04x faster                                                     |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.92 sec: 1.02x faster                                                   |
| docutils                   | 2.96 sec                                                 | 3.01 sec: 1.02x slower                                                   |
| python_startup             | 16.0 ms                                                  | 16.7 ms: 1.04x slower                                                    |
| sympy_str                  | 265 ms                                                   | 279 ms: 1.05x slower                                                     |
| python_startup_no_site     | 8.79 ms                                                  | 9.33 ms: 1.06x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 90.7 ms: 1.07x slower                                                    |
| unpickle_pure_python       | 265 us                                                   | 287 us: 1.08x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.74 ms: 1.10x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.64 ms: 1.12x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.9 ms: 1.32x slower                                                    |
| many_optionals             | 626 us                                                   | 842 us: 1.34x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 5.37 sec: 665.88x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (43): chaos, xml_etree_process, nqueens, regex_compile, sympy_sum, richards, coroutines, sqlalchemy_imperative, pidigits, sqlite_synth, fannkuch, richards_super, sqlalchemy_declarative, logging_format, genshi_text, coverage, typing_runtime_protocols, logging_simple, sqlglot_optimize, 2to3, thrift, asyncio_websockets, comprehensions, deltablue, mako, tomli_loads, shortest_path, hexiom, json_loads, sqlglot_transpile, django_template, bench_thread_pool, sympy_expand, connected_components, genshi_xml, json_dumps, raytrace, sqlglot_parse, sympy_integrate, nbody, json, logging_silent, pickle_pure_python
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250228-3.14.0a5+-8dd8862/bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862.json: dulwich_log

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.02x