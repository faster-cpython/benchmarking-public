# Results vs. 3.13.0

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: bd38cdb
- commit date: 2025-04-30
- overall geometric mean: 1.036x slower
- HPT reliability: 99.89%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 291 ms: 1.09x slower                                                          |
| docutils       | 2.58 sec                                               | 2.78 sec: 1.07x slower                                                        |
| html5lib       | 63.4 ms                                                | 67.2 ms: 1.06x slower                                                         |
| sphinx         | 1.03 sec                                               | 1.10 sec: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 512 ms: 1.68x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 296 ms: 1.56x faster                                                          |
| async_tree_io              | 838 ms                                                 | 548 ms: 1.53x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 225 ms: 1.42x faster                                                          |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 330 ms: 1.32x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 456 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                          |
| async_generators           | 433 ms                                                 | 442 ms: 1.02x slower                                                          |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.12x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.3 ms: 1.12x faster                                                         |
| pidigits       | 186 ms                                                 | 181 ms: 1.03x faster                                                          |
| nbody          | 87.7 ms                                                | 129 ms: 1.47x slower                                                          |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.0 ms: 1.22x faster                                                         |
| regex_effbot   | 3.77 ms                                                | 3.15 ms: 1.20x faster                                                         |
| regex_dna      | 220 ms                                                 | 206 ms: 1.07x faster                                                          |
| regex_compile  | 132 ms                                                 | 144 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 96.4 ms: 1.05x faster                                                         |
| xml_etree_parse      | 154 ms                                                 | 148 ms: 1.04x faster                                                          |
| tomli_loads          | 2.12 sec                                               | 2.24 sec: 1.06x slower                                                        |
| xml_etree_generate   | 86.8 ms                                                | 96.1 ms: 1.11x slower                                                         |
| unpickle_pure_python | 213 us                                                 | 238 us: 1.12x slower                                                          |
| xml_etree_process    | 60.5 ms                                                | 68.1 ms: 1.13x slower                                                         |
| pickle_pure_python   | 302 us                                                 | 345 us: 1.14x slower                                                          |
| json_loads           | 27.2 us                                                | 32.7 us: 1.20x slower                                                         |
| json_dumps           | 10.1 ms                                                | 12.9 ms: 1.28x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.10x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.4 ms: 1.22x slower                                                         |
| python_startup_no_site | 7.00 ms                                                | 9.06 ms: 1.29x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 57.8 ms: 1.14x slower                                                         |
| genshi_text     | 22.6 ms                                                | 26.7 ms: 1.18x slower                                                         |
| django_template | 31.7 ms                                                | 38.9 ms: 1.23x slower                                                         |
| mako            | 10.7 ms                                                | 16.2 ms: 1.52x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.26x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 2.14 ms: 2.29x faster                                                         |
| mdp                        | 2.54 sec                                               | 1.40 sec: 1.82x faster                                                        |
| async_tree_io_tg           | 861 ms                                                 | 512 ms: 1.68x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 296 ms: 1.56x faster                                                          |
| async_tree_io              | 838 ms                                                 | 548 ms: 1.53x faster                                                          |
| create_gc_cycles           | 2.45 ms                                                | 1.65 ms: 1.48x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 225 ms: 1.42x faster                                                          |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 330 ms: 1.32x faster                                                          |
| regex_v8                   | 26.9 ms                                                | 22.0 ms: 1.22x faster                                                         |
| deepcopy                   | 354 us                                                 | 294 us: 1.20x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.15 ms: 1.20x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 456 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                          |
| float                      | 78.7 ms                                                | 70.3 ms: 1.12x faster                                                         |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                          |
| pycparser                  | 1.20 sec                                               | 1.10 sec: 1.09x faster                                                        |
| regex_dna                  | 220 ms                                                 | 206 ms: 1.07x faster                                                          |
| pylint                     | 312 ms                                                 | 293 ms: 1.07x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 36.0 us: 1.07x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 96.4 ms: 1.05x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 3.09 us: 1.05x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 148 ms: 1.04x faster                                                          |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                         |
| pidigits                   | 186 ms                                                 | 181 ms: 1.03x faster                                                          |
| dulwich_log                | 64.6 ms                                                | 62.8 ms: 1.03x faster                                                         |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                                          |
| k_core                     | 2.37 sec                                               | 2.41 sec: 1.02x slower                                                        |
| async_generators           | 433 ms                                                 | 442 ms: 1.02x slower                                                          |
| pathlib                    | 17.4 ms                                                | 17.8 ms: 1.02x slower                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.87 sec: 1.04x slower                                                        |
| pyflate                    | 470 ms                                                 | 489 ms: 1.04x slower                                                          |
| spectral_norm              | 113 ms                                                 | 118 ms: 1.04x slower                                                          |
| richards                   | 47.5 ms                                                | 50.2 ms: 1.06x slower                                                         |
| tomli_loads                | 2.12 sec                                               | 2.24 sec: 1.06x slower                                                        |
| json                       | 5.32 ms                                                | 5.64 ms: 1.06x slower                                                         |
| html5lib                   | 63.4 ms                                                | 67.2 ms: 1.06x slower                                                         |
| sphinx                     | 1.03 sec                                               | 1.10 sec: 1.06x slower                                                        |
| generators                 | 28.8 ms                                                | 30.6 ms: 1.06x slower                                                         |
| telco                      | 8.40 ms                                                | 9.00 ms: 1.07x slower                                                         |
| scimark_sor                | 122 ms                                                 | 131 ms: 1.07x slower                                                          |
| docutils                   | 2.58 sec                                               | 2.78 sec: 1.07x slower                                                        |
| scimark_fft                | 367 ms                                                 | 395 ms: 1.08x slower                                                          |
| regex_compile              | 132 ms                                                 | 144 ms: 1.09x slower                                                          |
| 2to3                       | 266 ms                                                 | 291 ms: 1.09x slower                                                          |
| richards_super             | 53.7 ms                                                | 59.3 ms: 1.10x slower                                                         |
| pprint_safe_repr           | 727 ms                                                 | 803 ms: 1.11x slower                                                          |
| xml_etree_generate         | 86.8 ms                                                | 96.1 ms: 1.11x slower                                                         |
| sympy_str                  | 273 ms                                                 | 304 ms: 1.11x slower                                                          |
| sympy_integrate            | 19.8 ms                                                | 22.1 ms: 1.12x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 238 us: 1.12x slower                                                          |
| pprint_pformat             | 1.48 sec                                               | 1.66 sec: 1.12x slower                                                        |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.12x slower                                                         |
| xml_etree_process          | 60.5 ms                                                | 68.1 ms: 1.13x slower                                                         |
| sympy_expand               | 456 ms                                                 | 515 ms: 1.13x slower                                                          |
| nqueens                    | 80.9 ms                                                | 91.9 ms: 1.14x slower                                                         |
| sympy_sum                  | 150 ms                                                 | 171 ms: 1.14x slower                                                          |
| deltablue                  | 3.19 ms                                                | 3.65 ms: 1.14x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 345 us: 1.14x slower                                                          |
| genshi_xml                 | 50.5 ms                                                | 57.8 ms: 1.14x slower                                                         |
| chaos                      | 58.0 ms                                                | 67.3 ms: 1.16x slower                                                         |
| scimark_lu                 | 114 ms                                                 | 134 ms: 1.17x slower                                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.89 ms: 1.17x slower                                                         |
| shortest_path              | 487 ms                                                 | 572 ms: 1.17x slower                                                          |
| logging_simple             | 5.65 us                                                | 6.66 us: 1.18x slower                                                         |
| genshi_text                | 22.6 ms                                                | 26.7 ms: 1.18x slower                                                         |
| hexiom                     | 6.08 ms                                                | 7.21 ms: 1.19x slower                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 158 ms: 1.19x slower                                                          |
| connected_components       | 447 ms                                                 | 532 ms: 1.19x slower                                                          |
| meteor_contest             | 108 ms                                                 | 129 ms: 1.19x slower                                                          |
| crypto_pyaes               | 74.7 ms                                                | 89.3 ms: 1.20x slower                                                         |
| json_loads                 | 27.2 us                                                | 32.7 us: 1.20x slower                                                         |
| many_optionals             | 857 us                                                 | 1.03 ms: 1.20x slower                                                         |
| logging_format             | 6.23 us                                                | 7.51 us: 1.21x slower                                                         |
| raytrace                   | 262 ms                                                 | 316 ms: 1.21x slower                                                          |
| comprehensions             | 16.5 us                                                | 20.0 us: 1.21x slower                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 20.5 ms: 1.21x slower                                                         |
| python_startup             | 12.7 ms                                                | 15.4 ms: 1.22x slower                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 82.0 ms: 1.23x slower                                                         |
| django_template            | 31.7 ms                                                | 38.9 ms: 1.23x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 202 us: 1.26x slower                                                          |
| fannkuch                   | 394 ms                                                 | 502 ms: 1.28x slower                                                          |
| json_dumps                 | 10.1 ms                                                | 12.9 ms: 1.28x slower                                                         |
| python_startup_no_site     | 7.00 ms                                                | 9.06 ms: 1.29x slower                                                         |
| nbody                      | 87.7 ms                                                | 129 ms: 1.47x slower                                                          |
| coverage                   | 82.8 ms                                                | 124 ms: 1.49x slower                                                          |
| subparsers                 | 15.5 ms                                                | 23.2 ms: 1.50x slower                                                         |
| mako                       | 10.7 ms                                                | 16.2 ms: 1.52x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 90.6 ms: 3.78x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 3.24 ms: 3.97x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.07x slower                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250430-3.14.0a7+-bd38cdb-NOGIL/bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-bd38cdb.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.036x slower

# HPT report

- Reliability score: 99.89% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.24x