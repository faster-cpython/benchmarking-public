# Results vs. 3.13.0

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: a8a0e1d
- commit date: 2025-05-03
- overall geometric mean: 1.021x faster
- HPT reliability: 99.02%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 253 ms: 1.05x faster                                                          |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                        |
| html5lib       | 63.4 ms                                                | 61.4 ms: 1.03x faster                                                         |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 386 ms: 1.20x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 383 ms: 1.14x faster                                                          |
| async_tree_none            | 350 ms                                                 | 321 ms: 1.09x faster                                                          |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 824 ms: 1.04x faster                                                          |
| async_tree_io              | 838 ms                                                 | 804 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 561 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 567 ms: 1.04x slower                                                          |
| coroutines                 | 22.2 ms                                                | 25.8 ms: 1.16x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                  |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.1 ms: 1.11x faster                                                         |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                          |
| nbody          | 87.7 ms                                                | 96.3 ms: 1.10x slower                                                         |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.8 ms: 1.18x faster                                                         |
| regex_effbot   | 3.77 ms                                                | 3.33 ms: 1.13x faster                                                         |
| regex_dna      | 220 ms                                                 | 207 ms: 1.06x faster                                                          |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 145 ms: 1.06x faster                                                          |
| tomli_loads          | 2.12 sec                                               | 2.02 sec: 1.05x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 99.8 ms: 1.01x faster                                                         |
| xml_etree_process    | 60.5 ms                                                | 59.8 ms: 1.01x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 86.1 ms: 1.01x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                          |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                          |
| json_loads           | 27.2 us                                                | 30.0 us: 1.10x slower                                                         |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                         |
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                         |
| genshi_xml      | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                         |
| django_template | 31.7 ms                                                | 31.8 ms: 1.01x slower                                                         |
| mako            | 10.7 ms                                                | 11.8 ms: 1.10x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                        |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                                         |
| go                         | 141 ms                                                 | 113 ms: 1.24x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 386 ms: 1.20x faster                                                          |
| regex_v8                   | 26.9 ms                                                | 22.8 ms: 1.18x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.76 us: 1.18x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 383 ms: 1.14x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.33 ms: 1.13x faster                                                         |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                                          |
| float                      | 78.7 ms                                                | 71.1 ms: 1.11x faster                                                         |
| pyflate                    | 470 ms                                                 | 426 ms: 1.10x faster                                                          |
| async_tree_none            | 350 ms                                                 | 321 ms: 1.09x faster                                                          |
| dulwich_log                | 64.6 ms                                                | 59.9 ms: 1.08x faster                                                         |
| richards                   | 47.5 ms                                                | 44.4 ms: 1.07x faster                                                         |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                         |
| richards_super             | 53.7 ms                                                | 50.5 ms: 1.06x faster                                                         |
| regex_dna                  | 220 ms                                                 | 207 ms: 1.06x faster                                                          |
| xml_etree_parse            | 154 ms                                                 | 145 ms: 1.06x faster                                                          |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                        |
| 2to3                       | 266 ms                                                 | 253 ms: 1.05x faster                                                          |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                          |
| spectral_norm              | 113 ms                                                 | 108 ms: 1.05x faster                                                          |
| telco                      | 8.40 ms                                                | 8.02 ms: 1.05x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 2.02 sec: 1.05x faster                                                        |
| async_tree_io_tg           | 861 ms                                                 | 824 ms: 1.04x faster                                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.04x faster                                                        |
| async_tree_io              | 838 ms                                                 | 804 ms: 1.04x faster                                                          |
| sympy_integrate            | 19.8 ms                                                | 19.1 ms: 1.04x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                        |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                          |
| html5lib                   | 63.4 ms                                                | 61.4 ms: 1.03x faster                                                         |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                         |
| genshi_xml                 | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                         |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 561 ms: 1.02x faster                                                          |
| logging_silent             | 101 ns                                                 | 99.4 ns: 1.02x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 99.8 ms: 1.01x faster                                                         |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                        |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                          |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                          |
| logging_simple             | 5.65 us                                                | 5.59 us: 1.01x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.87 us: 1.01x faster                                                         |
| xml_etree_process          | 60.5 ms                                                | 59.8 ms: 1.01x faster                                                         |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                          |
| xml_etree_generate         | 86.8 ms                                                | 86.1 ms: 1.01x faster                                                         |
| python_startup_no_site     | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                         |
| sympy_expand               | 456 ms                                                 | 454 ms: 1.01x faster                                                          |
| sqlalchemy_declarative     | 133 ms                                                 | 133 ms: 1.00x faster                                                          |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                          |
| pprint_pformat             | 1.48 sec                                               | 1.48 sec: 1.00x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 730 ms: 1.00x slower                                                          |
| scimark_fft                | 367 ms                                                 | 369 ms: 1.01x slower                                                          |
| django_template            | 31.7 ms                                                | 31.8 ms: 1.01x slower                                                         |
| crypto_pyaes               | 74.7 ms                                                | 75.2 ms: 1.01x slower                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 67.7 ms: 1.01x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                        |
| connected_components       | 447 ms                                                 | 454 ms: 1.02x slower                                                          |
| generators                 | 28.8 ms                                                | 29.2 ms: 1.02x slower                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.14 ms: 1.02x slower                                                         |
| gc_traversal               | 4.90 ms                                                | 5.01 ms: 1.02x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.51 ms: 1.02x slower                                                         |
| chaos                      | 58.0 ms                                                | 59.5 ms: 1.03x slower                                                         |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                          |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                                          |
| hexiom                     | 6.08 ms                                                | 6.32 ms: 1.04x slower                                                         |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                          |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                         |
| fannkuch                   | 394 ms                                                 | 410 ms: 1.04x slower                                                          |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 567 ms: 1.04x slower                                                          |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                          |
| deltablue                  | 3.19 ms                                                | 3.38 ms: 1.06x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 888 us: 1.09x slower                                                          |
| nbody                      | 87.7 ms                                                | 96.3 ms: 1.10x slower                                                         |
| mako                       | 10.7 ms                                                | 11.8 ms: 1.10x slower                                                         |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.10x slower                                                         |
| many_optionals             | 857 us                                                 | 952 us: 1.11x slower                                                          |
| coverage                   | 82.8 ms                                                | 94.5 ms: 1.14x slower                                                         |
| coroutines                 | 22.2 ms                                                | 25.8 ms: 1.16x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                         |
| subparsers                 | 15.5 ms                                                | 22.7 ms: 1.47x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 83.5 ms: 3.48x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (6): json, asyncio_websockets, nqueens, shortest_path, logging_format, async_tree_none_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250503-3.14.0a7+-a8a0e1d/bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.021x faster

# HPT report

- Reliability score: 99.02% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x