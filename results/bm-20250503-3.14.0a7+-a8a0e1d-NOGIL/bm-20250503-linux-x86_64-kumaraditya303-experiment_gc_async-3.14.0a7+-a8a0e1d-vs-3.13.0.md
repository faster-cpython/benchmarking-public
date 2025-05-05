# Results vs. 3.13.0

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: a8a0e1d
- commit date: 2025-05-03
- overall geometric mean: 1.047x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 291 ms: 1.10x slower                                                          |
| docutils       | 2.58 sec                                               | 2.80 sec: 1.08x slower                                                        |
| html5lib       | 63.4 ms                                                | 66.4 ms: 1.05x slower                                                         |
| sphinx         | 1.03 sec                                               | 1.10 sec: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 519 ms: 1.66x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 296 ms: 1.56x faster                                                          |
| async_tree_io              | 838 ms                                                 | 552 ms: 1.52x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 227 ms: 1.41x faster                                                          |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 333 ms: 1.31x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 463 ms: 1.17x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 503 ms: 1.14x faster                                                          |
| coroutines                 | 22.2 ms                                                | 25.8 ms: 1.16x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                                  |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.2 ms: 1.10x faster                                                         |
| pidigits       | 186 ms                                                 | 182 ms: 1.03x faster                                                          |
| nbody          | 87.7 ms                                                | 128 ms: 1.46x slower                                                          |
| Geometric mean | (ref)                                                  | 1.09x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.9 ms: 1.17x faster                                                         |
| regex_effbot   | 3.77 ms                                                | 3.32 ms: 1.13x faster                                                         |
| regex_dna      | 220 ms                                                 | 204 ms: 1.08x faster                                                          |
| regex_compile  | 132 ms                                                 | 144 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 95.8 ms: 1.06x faster                                                         |
| xml_etree_parse      | 154 ms                                                 | 151 ms: 1.02x faster                                                          |
| tomli_loads          | 2.12 sec                                               | 2.23 sec: 1.05x slower                                                        |
| xml_etree_generate   | 86.8 ms                                                | 96.6 ms: 1.11x slower                                                         |
| xml_etree_process    | 60.5 ms                                                | 68.0 ms: 1.12x slower                                                         |
| unpickle_pure_python | 213 us                                                 | 241 us: 1.13x slower                                                          |
| pickle_pure_python   | 302 us                                                 | 343 us: 1.13x slower                                                          |
| json_loads           | 27.2 us                                                | 32.9 us: 1.21x slower                                                         |
| json_dumps           | 10.1 ms                                                | 13.1 ms: 1.30x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.5 ms: 1.22x slower                                                         |
| python_startup_no_site | 7.00 ms                                                | 9.11 ms: 1.30x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 58.1 ms: 1.15x slower                                                         |
| genshi_text     | 22.6 ms                                                | 27.1 ms: 1.20x slower                                                         |
| django_template | 31.7 ms                                                | 39.7 ms: 1.25x slower                                                         |
| mako            | 10.7 ms                                                | 16.3 ms: 1.53x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.28x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 2.28 ms: 2.15x faster                                                         |
| mdp                        | 2.54 sec                                               | 1.40 sec: 1.81x faster                                                        |
| async_tree_io_tg           | 861 ms                                                 | 519 ms: 1.66x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 296 ms: 1.56x faster                                                          |
| async_tree_io              | 838 ms                                                 | 552 ms: 1.52x faster                                                          |
| create_gc_cycles           | 2.45 ms                                                | 1.67 ms: 1.46x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 227 ms: 1.41x faster                                                          |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 333 ms: 1.31x faster                                                          |
| deepcopy                   | 354 us                                                 | 297 us: 1.19x faster                                                          |
| regex_v8                   | 26.9 ms                                                | 22.9 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 463 ms: 1.17x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 503 ms: 1.14x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.32 ms: 1.13x faster                                                         |
| float                      | 78.7 ms                                                | 71.2 ms: 1.10x faster                                                         |
| regex_dna                  | 220 ms                                                 | 204 ms: 1.08x faster                                                          |
| go                         | 141 ms                                                 | 132 ms: 1.06x faster                                                          |
| xml_etree_iterparse        | 101 ms                                                 | 95.8 ms: 1.06x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 36.4 us: 1.05x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 3.08 us: 1.05x faster                                                         |
| dulwich_log                | 64.6 ms                                                | 62.7 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.82 us: 1.03x faster                                                         |
| pidigits                   | 186 ms                                                 | 182 ms: 1.03x faster                                                          |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                        |
| xml_etree_parse            | 154 ms                                                 | 151 ms: 1.02x faster                                                          |
| pyflate                    | 470 ms                                                 | 480 ms: 1.02x slower                                                          |
| pathlib                    | 17.4 ms                                                | 17.8 ms: 1.02x slower                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.86 sec: 1.04x slower                                                        |
| html5lib                   | 63.4 ms                                                | 66.4 ms: 1.05x slower                                                         |
| spectral_norm              | 113 ms                                                 | 119 ms: 1.05x slower                                                          |
| tomli_loads                | 2.12 sec                                               | 2.23 sec: 1.05x slower                                                        |
| json                       | 5.32 ms                                                | 5.64 ms: 1.06x slower                                                         |
| logging_silent             | 101 ns                                                 | 108 ns: 1.06x slower                                                          |
| sphinx                     | 1.03 sec                                               | 1.10 sec: 1.07x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.80 sec: 1.08x slower                                                        |
| richards                   | 47.5 ms                                                | 51.6 ms: 1.08x slower                                                         |
| scimark_sor                | 122 ms                                                 | 133 ms: 1.09x slower                                                          |
| regex_compile              | 132 ms                                                 | 144 ms: 1.09x slower                                                          |
| 2to3                       | 266 ms                                                 | 291 ms: 1.10x slower                                                          |
| generators                 | 28.8 ms                                                | 31.7 ms: 1.10x slower                                                         |
| scimark_fft                | 367 ms                                                 | 406 ms: 1.11x slower                                                          |
| xml_etree_generate         | 86.8 ms                                                | 96.6 ms: 1.11x slower                                                         |
| telco                      | 8.40 ms                                                | 9.35 ms: 1.11x slower                                                         |
| richards_super             | 53.7 ms                                                | 60.1 ms: 1.12x slower                                                         |
| sympy_integrate            | 19.8 ms                                                | 22.2 ms: 1.12x slower                                                         |
| xml_etree_process          | 60.5 ms                                                | 68.0 ms: 1.12x slower                                                         |
| sympy_str                  | 273 ms                                                 | 308 ms: 1.13x slower                                                          |
| unpickle_pure_python       | 213 us                                                 | 241 us: 1.13x slower                                                          |
| pprint_safe_repr           | 727 ms                                                 | 822 ms: 1.13x slower                                                          |
| nqueens                    | 80.9 ms                                                | 91.7 ms: 1.13x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 343 us: 1.13x slower                                                          |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.14x slower                                                          |
| pprint_pformat             | 1.48 sec                                               | 1.70 sec: 1.15x slower                                                        |
| sympy_expand               | 456 ms                                                 | 525 ms: 1.15x slower                                                          |
| genshi_xml                 | 50.5 ms                                                | 58.1 ms: 1.15x slower                                                         |
| coroutines                 | 22.2 ms                                                | 25.8 ms: 1.16x slower                                                         |
| chaos                      | 58.0 ms                                                | 67.7 ms: 1.17x slower                                                         |
| shortest_path              | 487 ms                                                 | 571 ms: 1.17x slower                                                          |
| logging_simple             | 5.65 us                                                | 6.64 us: 1.18x slower                                                         |
| deltablue                  | 3.19 ms                                                | 3.76 ms: 1.18x slower                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.94 ms: 1.18x slower                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 158 ms: 1.19x slower                                                          |
| connected_components       | 447 ms                                                 | 532 ms: 1.19x slower                                                          |
| scimark_lu                 | 114 ms                                                 | 137 ms: 1.19x slower                                                          |
| comprehensions             | 16.5 us                                                | 19.7 us: 1.20x slower                                                         |
| meteor_contest             | 108 ms                                                 | 130 ms: 1.20x slower                                                          |
| genshi_text                | 22.6 ms                                                | 27.1 ms: 1.20x slower                                                         |
| hexiom                     | 6.08 ms                                                | 7.31 ms: 1.20x slower                                                         |
| logging_format             | 6.23 us                                                | 7.51 us: 1.21x slower                                                         |
| crypto_pyaes               | 74.7 ms                                                | 90.1 ms: 1.21x slower                                                         |
| json_loads                 | 27.2 us                                                | 32.9 us: 1.21x slower                                                         |
| python_startup             | 12.7 ms                                                | 15.5 ms: 1.22x slower                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 20.8 ms: 1.23x slower                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 82.6 ms: 1.24x slower                                                         |
| raytrace                   | 262 ms                                                 | 323 ms: 1.24x slower                                                          |
| many_optionals             | 857 us                                                 | 1.06 ms: 1.24x slower                                                         |
| django_template            | 31.7 ms                                                | 39.7 ms: 1.25x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 201 us: 1.25x slower                                                          |
| fannkuch                   | 394 ms                                                 | 498 ms: 1.26x slower                                                          |
| json_dumps                 | 10.1 ms                                                | 13.1 ms: 1.30x slower                                                         |
| python_startup_no_site     | 7.00 ms                                                | 9.11 ms: 1.30x slower                                                         |
| nbody                      | 87.7 ms                                                | 128 ms: 1.46x slower                                                          |
| coverage                   | 82.8 ms                                                | 125 ms: 1.50x slower                                                          |
| mako                       | 10.7 ms                                                | 16.3 ms: 1.53x slower                                                         |
| subparsers                 | 15.5 ms                                                | 26.0 ms: 1.68x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 90.7 ms: 3.78x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 3.26 ms: 3.99x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                                  |

Benchmark hidden because not significant (4): pylint, async_generators, asyncio_websockets, k_core
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250503-3.14.0a7+-a8a0e1d-NOGIL/bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.047x slower

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.24x