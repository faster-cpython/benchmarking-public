# Results vs. base

- fork: kumaraditya303
- ref: current_task
- machine: linux-x86_64
- commit hash: b20a605
- commit date: 2025-01-02
- overall geometric mean: 1.005x faster
- HPT reliability: 99.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 255 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                 | 25.0 ms                                                                | 23.2 ms: 1.08x faster                                                  |
| async_tree_memoization_tg  | 302 ms                                                                 | 300 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg | 472 ms                                                                 | 475 ms: 1.01x slower                                                   |
| async_generators           | 418 ms                                                                 | 422 ms: 1.01x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (7): async_tree_io, async_tree_none, async_tree_memoization, async_tree_io_tg, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.6 ms                                                                | 94.7 ms: 1.03x faster                                                  |
| pidigits       | 190 ms                                                                 | 189 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.47 ms                                                                | 3.20 ms: 1.08x faster                                                  |
| regex_dna      | 221 ms                                                                 | 213 ms: 1.04x faster                                                   |
| regex_v8       | 25.4 ms                                                                | 25.3 ms: 1.01x faster                                                  |
| regex_compile  | 127 ms                                                                 | 128 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 323 us                                                                 | 318 us: 1.02x faster                                                   |
| xml_etree_process    | 59.4 ms                                                                | 58.5 ms: 1.02x faster                                                  |
| xml_etree_generate   | 85.1 ms                                                                | 84.1 ms: 1.01x faster                                                  |
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 97.4 ms                                                                | 96.8 ms: 1.01x faster                                                  |
| xml_etree_parse      | 138 ms                                                                 | 138 ms: 1.01x faster                                                   |
| json_loads           | 26.3 us                                                                | 26.4 us: 1.01x slower                                                  |
| tomli_loads          | 1.97 sec                                                               | 1.99 sec: 1.01x slower                                                 |
| json_dumps           | 11.3 ms                                                                | 11.4 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                  |
| python_startup_no_site | 7.05 ms                                                                | 7.02 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.7 ms                                                                | 22.4 ms: 1.01x faster                                                  |
| django_template | 31.6 ms                                                                | 31.3 ms: 1.01x faster                                                  |
| mako            | 11.4 ms                                                                | 11.7 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot               | 3.47 ms                                                                | 3.20 ms: 1.08x faster                                                  |
| pyflate                    | 478 ms                                                                 | 444 ms: 1.08x faster                                                   |
| coroutines                 | 25.0 ms                                                                | 23.2 ms: 1.08x faster                                                  |
| crypto_pyaes               | 72.2 ms                                                                | 68.8 ms: 1.05x faster                                                  |
| fannkuch                   | 413 ms                                                                 | 395 ms: 1.04x faster                                                   |
| gc_traversal               | 4.97 ms                                                                | 4.76 ms: 1.04x faster                                                  |
| regex_dna                  | 221 ms                                                                 | 213 ms: 1.04x faster                                                   |
| nbody                      | 97.6 ms                                                                | 94.7 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.85 us                                                                | 2.80 us: 1.02x faster                                                  |
| pprint_pformat             | 1.50 sec                                                               | 1.47 sec: 1.02x faster                                                 |
| hexiom                     | 6.39 ms                                                                | 6.28 ms: 1.02x faster                                                  |
| pickle_pure_python         | 323 us                                                                 | 318 us: 1.02x faster                                                   |
| xml_etree_process          | 59.4 ms                                                                | 58.5 ms: 1.02x faster                                                  |
| logging_format             | 6.30 us                                                                | 6.20 us: 1.02x faster                                                  |
| connected_components       | 442 ms                                                                 | 435 ms: 1.02x faster                                                   |
| richards_super             | 51.4 ms                                                                | 50.6 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 727 ms                                                                 | 716 ms: 1.01x faster                                                   |
| logging_simple             | 5.71 us                                                                | 5.64 us: 1.01x faster                                                  |
| xml_etree_generate         | 85.1 ms                                                                | 84.1 ms: 1.01x faster                                                  |
| unpickle_pure_python       | 219 us                                                                 | 217 us: 1.01x faster                                                   |
| spectral_norm              | 105 ms                                                                 | 104 ms: 1.01x faster                                                   |
| scimark_monte_carlo        | 68.0 ms                                                                | 67.3 ms: 1.01x faster                                                  |
| genshi_text                | 22.7 ms                                                                | 22.4 ms: 1.01x faster                                                  |
| chaos                      | 60.8 ms                                                                | 60.2 ms: 1.01x faster                                                  |
| richards                   | 44.8 ms                                                                | 44.5 ms: 1.01x faster                                                  |
| django_template            | 31.6 ms                                                                | 31.3 ms: 1.01x faster                                                  |
| coverage                   | 82.9 ms                                                                | 82.4 ms: 1.01x faster                                                  |
| regex_v8                   | 25.4 ms                                                                | 25.3 ms: 1.01x faster                                                  |
| deepcopy                   | 259 us                                                                 | 257 us: 1.01x faster                                                   |
| xml_etree_iterparse        | 97.4 ms                                                                | 96.8 ms: 1.01x faster                                                  |
| create_gc_cycles           | 2.45 ms                                                                | 2.44 ms: 1.01x faster                                                  |
| async_tree_memoization_tg  | 302 ms                                                                 | 300 ms: 1.01x faster                                                   |
| xml_etree_parse            | 138 ms                                                                 | 138 ms: 1.01x faster                                                   |
| thrift                     | 762 us                                                                 | 758 us: 1.00x faster                                                   |
| bpe_tokeniser              | 4.57 sec                                                               | 4.55 sec: 1.00x faster                                                 |
| dulwich_log                | 64.1 ms                                                                | 63.8 ms: 1.00x faster                                                  |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                  |
| nqueens                    | 80.0 ms                                                                | 79.6 ms: 1.00x faster                                                  |
| python_startup_no_site     | 7.05 ms                                                                | 7.02 ms: 1.00x faster                                                  |
| pidigits                   | 190 ms                                                                 | 189 ms: 1.00x faster                                                   |
| 2to3                       | 254 ms                                                                 | 255 ms: 1.00x slower                                                   |
| meteor_contest             | 108 ms                                                                 | 108 ms: 1.00x slower                                                   |
| raytrace                   | 271 ms                                                                 | 272 ms: 1.00x slower                                                   |
| many_optionals             | 948 us                                                                 | 952 us: 1.00x slower                                                   |
| scimark_fft                | 348 ms                                                                 | 350 ms: 1.00x slower                                                   |
| bench_thread_pool          | 864 us                                                                 | 868 us: 1.00x slower                                                   |
| regex_compile              | 127 ms                                                                 | 128 ms: 1.01x slower                                                   |
| json_loads                 | 26.3 us                                                                | 26.4 us: 1.01x slower                                                  |
| json                       | 4.91 ms                                                                | 4.95 ms: 1.01x slower                                                  |
| sqlalchemy_declarative     | 128 ms                                                                 | 129 ms: 1.01x slower                                                   |
| sqlalchemy_imperative      | 16.5 ms                                                                | 16.6 ms: 1.01x slower                                                  |
| pathlib                    | 16.1 ms                                                                | 16.2 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 472 ms                                                                 | 475 ms: 1.01x slower                                                   |
| telco                      | 7.77 ms                                                                | 7.84 ms: 1.01x slower                                                  |
| tomli_loads                | 1.97 sec                                                               | 1.99 sec: 1.01x slower                                                 |
| async_generators           | 418 ms                                                                 | 422 ms: 1.01x slower                                                   |
| json_dumps                 | 11.3 ms                                                                | 11.4 ms: 1.01x slower                                                  |
| go                         | 117 ms                                                                 | 119 ms: 1.01x slower                                                   |
| comprehensions             | 17.0 us                                                                | 17.2 us: 1.01x slower                                                  |
| typing_runtime_protocols   | 159 us                                                                 | 162 us: 1.01x slower                                                   |
| deepcopy_memo              | 30.6 us                                                                | 31.1 us: 1.02x slower                                                  |
| scimark_sparse_mat_mult    | 4.71 ms                                                                | 4.84 ms: 1.03x slower                                                  |
| mako                       | 11.4 ms                                                                | 11.7 ms: 1.03x slower                                                  |
| pycparser                  | 1.12 sec                                                               | 1.17 sec: 1.04x slower                                                 |
| mdp                        | 2.50 sec                                                               | 2.67 sec: 1.07x slower                                                 |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (32): async_tree_io, async_tree_none, async_tree_memoization, k_core, float, html5lib, deepcopy_reduce, sphinx, genshi_xml, bench_mp_pool, sqlglot_transpile, shortest_path, sqlglot_optimize, sqlglot_parse, docutils, sympy_str, logging_silent, async_tree_io_tg, sqlglot_normalize, sympy_integrate, scimark_sor, async_tree_none_tg, sympy_expand, asyncio_websockets, generators, async_tree_cpu_io_mixed, deltablue, sympy_sum, subparsers, pylint, scimark_lu, djangocms
Ignored benchmarks (1) of results/bm-20250102-3.14.0a3+-e1baa77/bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77.json: mypy2

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x