# Results vs. base

- fork: kumaraditya303
- ref: current_task
- machine: linux-x86_64
- commit hash: b20a605
- commit date: 2025-01-02
- overall geometric mean: 1.006x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 349 ms                                                                 | 346 ms: 1.01x faster                                                   |
| html5lib       | 85.5 ms                                                                | 87.3 ms: 1.02x slower                                                  |
| sphinx         | 1.16 sec                                                               | 1.16 sec: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 535 ms                                                                 | 529 ms: 1.01x faster                                                   |
| coroutines                 | 26.5 ms                                                                | 26.7 ms: 1.01x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io, asyncio_websockets, async_tree_none_tg, async_generators, async_tree_none, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 138 ms                                                                 | 135 ms: 1.02x faster                                                   |
| float          | 109 ms                                                                 | 107 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.5 ms                                                                | 26.2 ms: 1.01x faster                                                  |
| regex_compile  | 164 ms                                                                 | 164 ms: 1.00x slower                                                   |
| regex_effbot   | 3.27 ms                                                                | 3.33 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.53 sec                                                               | 2.48 sec: 1.02x faster                                                 |
| json_dumps           | 13.4 ms                                                                | 13.2 ms: 1.02x faster                                                  |
| xml_etree_process    | 73.5 ms                                                                | 72.4 ms: 1.02x faster                                                  |
| xml_etree_generate   | 97.3 ms                                                                | 96.2 ms: 1.01x faster                                                  |
| unpickle_pure_python | 315 us                                                                 | 313 us: 1.01x faster                                                   |
| pickle_pure_python   | 478 us                                                                 | 475 us: 1.01x faster                                                   |
| json_loads           | 29.5 us                                                                | 29.4 us: 1.00x faster                                                  |
| xml_etree_parse      | 148 ms                                                                 | 149 ms: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.61 ms                                                                | 9.60 ms: 1.00x faster                                                  |
| python_startup         | 15.5 ms                                                                | 15.5 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 18.0 ms                                                                | 18.2 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal               | 4.07 ms                                                                | 3.67 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult    | 6.35 ms                                                                | 6.08 ms: 1.04x faster                                                  |
| richards                   | 64.9 ms                                                                | 62.5 ms: 1.04x faster                                                  |
| generators                 | 38.1 ms                                                                | 36.9 ms: 1.03x faster                                                  |
| logging_simple             | 8.07 us                                                                | 7.84 us: 1.03x faster                                                  |
| scimark_sor                | 217 ms                                                                 | 211 ms: 1.03x faster                                                   |
| scimark_fft                | 429 ms                                                                 | 419 ms: 1.03x faster                                                   |
| nbody                      | 138 ms                                                                 | 135 ms: 1.02x faster                                                   |
| tomli_loads                | 2.53 sec                                                               | 2.48 sec: 1.02x faster                                                 |
| deltablue                  | 7.17 ms                                                                | 7.04 ms: 1.02x faster                                                  |
| json_dumps                 | 13.4 ms                                                                | 13.2 ms: 1.02x faster                                                  |
| scimark_monte_carlo        | 107 ms                                                                 | 105 ms: 1.02x faster                                                   |
| float                      | 109 ms                                                                 | 107 ms: 1.02x faster                                                   |
| xml_etree_process          | 73.5 ms                                                                | 72.4 ms: 1.02x faster                                                  |
| logging_format             | 8.93 us                                                                | 8.79 us: 1.02x faster                                                  |
| create_gc_cycles           | 2.38 ms                                                                | 2.34 ms: 1.02x faster                                                  |
| regex_v8                   | 26.5 ms                                                                | 26.2 ms: 1.01x faster                                                  |
| sympy_sum                  | 185 ms                                                                 | 183 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 971 ms                                                                 | 958 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg | 535 ms                                                                 | 529 ms: 1.01x faster                                                   |
| sqlglot_normalize          | 130 ms                                                                 | 129 ms: 1.01x faster                                                   |
| meteor_contest             | 133 ms                                                                 | 131 ms: 1.01x faster                                                   |
| go                         | 225 ms                                                                 | 222 ms: 1.01x faster                                                   |
| xml_etree_generate         | 97.3 ms                                                                | 96.2 ms: 1.01x faster                                                  |
| scimark_lu                 | 156 ms                                                                 | 155 ms: 1.01x faster                                                   |
| deepcopy_memo              | 40.6 us                                                                | 40.2 us: 1.01x faster                                                  |
| typing_runtime_protocols   | 211 us                                                                 | 208 us: 1.01x faster                                                   |
| 2to3                       | 349 ms                                                                 | 346 ms: 1.01x faster                                                   |
| dulwich_log                | 75.7 ms                                                                | 75.1 ms: 1.01x faster                                                  |
| hexiom                     | 9.57 ms                                                                | 9.49 ms: 1.01x faster                                                  |
| unpickle_pure_python       | 315 us                                                                 | 313 us: 1.01x faster                                                   |
| comprehensions             | 25.5 us                                                                | 25.4 us: 1.01x faster                                                  |
| pickle_pure_python         | 478 us                                                                 | 475 us: 1.01x faster                                                   |
| pprint_pformat             | 2.02 sec                                                               | 2.00 sec: 1.01x faster                                                 |
| sympy_integrate            | 24.7 ms                                                                | 24.5 ms: 1.01x faster                                                  |
| json                       | 5.34 ms                                                                | 5.31 ms: 1.01x faster                                                  |
| sphinx                     | 1.16 sec                                                               | 1.16 sec: 1.01x faster                                                 |
| fannkuch                   | 528 ms                                                                 | 525 ms: 1.01x faster                                                   |
| subparsers                 | 26.8 ms                                                                | 26.6 ms: 1.01x faster                                                  |
| sqlalchemy_declarative     | 182 ms                                                                 | 181 ms: 1.00x faster                                                   |
| json_loads                 | 29.5 us                                                                | 29.4 us: 1.00x faster                                                  |
| deepcopy                   | 317 us                                                                 | 316 us: 1.00x faster                                                   |
| python_startup_no_site     | 9.61 ms                                                                | 9.60 ms: 1.00x faster                                                  |
| python_startup             | 15.5 ms                                                                | 15.5 ms: 1.00x slower                                                  |
| k_core                     | 2.50 sec                                                               | 2.50 sec: 1.00x slower                                                 |
| regex_compile              | 164 ms                                                                 | 164 ms: 1.00x slower                                                   |
| shortest_path              | 578 ms                                                                 | 579 ms: 1.00x slower                                                   |
| crypto_pyaes               | 91.6 ms                                                                | 91.9 ms: 1.00x slower                                                  |
| bench_thread_pool          | 3.55 ms                                                                | 3.56 ms: 1.00x slower                                                  |
| nqueens                    | 100.0 ms                                                               | 100 ms: 1.01x slower                                                   |
| connected_components       | 536 ms                                                                 | 539 ms: 1.01x slower                                                   |
| coroutines                 | 26.5 ms                                                                | 26.7 ms: 1.01x slower                                                  |
| mako                       | 18.0 ms                                                                | 18.2 ms: 1.01x slower                                                  |
| xml_etree_parse            | 148 ms                                                                 | 149 ms: 1.01x slower                                                   |
| sqlite_synth               | 2.80 us                                                                | 2.84 us: 1.01x slower                                                  |
| regex_effbot               | 3.27 ms                                                                | 3.33 ms: 1.02x slower                                                  |
| html5lib                   | 85.5 ms                                                                | 87.3 ms: 1.02x slower                                                  |
| richards_super             | 71.9 ms                                                                | 73.9 ms: 1.03x slower                                                  |
| mdp                        | 2.86 sec                                                               | 3.03 sec: 1.06x slower                                                 |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (37): sqlglot_transpile, pylint, async_tree_cpu_io_mixed, logging_silent, async_tree_memoization_tg, sqlalchemy_imperative, sympy_expand, docutils, sqlglot_optimize, pycparser, spectral_norm, raytrace, sympy_str, genshi_text, thrift, django_template, pyflate, async_tree_io, sqlglot_parse, bench_mp_pool, pidigits, asyncio_websockets, chaos, async_tree_none_tg, telco, many_optionals, bpe_tokeniser, regex_dna, async_generators, pathlib, xml_etree_iterparse, coverage, async_tree_none, deepcopy_reduce, async_tree_io_tg, genshi_xml, async_tree_memoization

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x