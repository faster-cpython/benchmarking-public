# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: method_jit_bench
- machine: linux-x86_64
- commit hash: 2b1c0da
- commit date: 2025-03-14
- overall geometric mean: 1.487x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.92x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 2.58 sec                                               | 5.32 sec: 2.06x slower                                                       |
| html5lib       | 63.4 ms                                                | 128 ms: 2.02x slower                                                         |
| sphinx         | 1.03 sec                                               | 2.04 sec: 1.98x slower                                                       |
| Geometric mean | (ref)                                                  | 2.02x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 645 ms: 1.39x slower                                                         |
| async_tree_io_tg           | 861 ms                                                 | 1.22 sec: 1.42x slower                                                       |
| async_tree_io              | 838 ms                                                 | 1.20 sec: 1.44x slower                                                       |
| async_tree_none            | 350 ms                                                 | 519 ms: 1.48x slower                                                         |
| async_tree_memoization     | 437 ms                                                 | 647 ms: 1.48x slower                                                         |
| async_tree_none_tg         | 319 ms                                                 | 495 ms: 1.55x slower                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 989 ms: 1.73x slower                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 960 ms: 1.77x slower                                                         |
| async_generators           | 433 ms                                                 | 791 ms: 1.82x slower                                                         |
| asyncio_websockets         | 551 ms                                                 | 1.08 sec: 1.97x slower                                                       |
| coroutines                 | 22.2 ms                                                | 47.8 ms: 2.15x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.64x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 139 ms: 1.76x slower                                                         |
| pidigits       | 186 ms                                                 | 378 ms: 2.02x slower                                                         |
| nbody          | 87.7 ms                                                | 193 ms: 2.21x slower                                                         |
| Geometric mean | (ref)                                                  | 1.99x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 6.44 ms: 1.71x slower                                                        |
| regex_v8       | 26.9 ms                                                | 48.8 ms: 1.82x slower                                                        |
| regex_dna      | 220 ms                                                 | 436 ms: 1.98x slower                                                         |
| regex_compile  | 132 ms                                                 | 265 ms: 2.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.88x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 279 ms: 1.81x slower                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 188 ms: 1.86x slower                                                         |
| xml_etree_process    | 60.5 ms                                                | 116 ms: 1.92x slower                                                         |
| xml_etree_generate   | 86.8 ms                                                | 168 ms: 1.93x slower                                                         |
| tomli_loads          | 2.12 sec                                               | 4.20 sec: 1.98x slower                                                       |
| unpickle_pure_python | 213 us                                                 | 430 us: 2.02x slower                                                         |
| pickle_pure_python   | 302 us                                                 | 649 us: 2.15x slower                                                         |
| json_loads           | 27.2 us                                                | 60.1 us: 2.21x slower                                                        |
| json_dumps           | 10.1 ms                                                | 23.2 ms: 2.29x slower                                                        |
| Geometric mean       | (ref)                                                  | 2.01x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 31.2 ms: 2.46x slower                                                        |
| python_startup_no_site | 7.00 ms                                                | 31.0 ms: 4.43x slower                                                        |
| Geometric mean         | (ref)                                                  | 3.30x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 98.8 ms: 1.96x slower                                                        |
| genshi_text     | 22.6 ms                                                | 44.3 ms: 1.96x slower                                                        |
| django_template | 31.7 ms                                                | 64.4 ms: 2.04x slower                                                        |
| mako            | 10.7 ms                                                | 23.4 ms: 2.19x slower                                                        |
| Geometric mean  | (ref)                                                  | 2.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 645 ms: 1.39x slower                                                         |
| async_tree_io_tg           | 861 ms                                                 | 1.22 sec: 1.42x slower                                                       |
| async_tree_io              | 838 ms                                                 | 1.20 sec: 1.44x slower                                                       |
| deepcopy                   | 354 us                                                 | 524 us: 1.48x slower                                                         |
| async_tree_none            | 350 ms                                                 | 519 ms: 1.48x slower                                                         |
| async_tree_memoization     | 437 ms                                                 | 647 ms: 1.48x slower                                                         |
| deepcopy_memo              | 38.4 us                                                | 58.9 us: 1.53x slower                                                        |
| async_tree_none_tg         | 319 ms                                                 | 495 ms: 1.55x slower                                                         |
| deepcopy_reduce            | 3.24 us                                                | 5.34 us: 1.65x slower                                                        |
| regex_effbot               | 3.77 ms                                                | 6.44 ms: 1.71x slower                                                        |
| go                         | 141 ms                                                 | 242 ms: 1.73x slower                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 989 ms: 1.73x slower                                                         |
| float                      | 78.7 ms                                                | 139 ms: 1.76x slower                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 960 ms: 1.77x slower                                                         |
| spectral_norm              | 113 ms                                                 | 202 ms: 1.79x slower                                                         |
| pylint                     | 312 ms                                                 | 563 ms: 1.81x slower                                                         |
| xml_etree_parse            | 154 ms                                                 | 279 ms: 1.81x slower                                                         |
| regex_v8                   | 26.9 ms                                                | 48.8 ms: 1.82x slower                                                        |
| async_generators           | 433 ms                                                 | 791 ms: 1.82x slower                                                         |
| dulwich_log                | 64.6 ms                                                | 118 ms: 1.83x slower                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 9.29 ms: 1.85x slower                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 188 ms: 1.86x slower                                                         |
| richards_super             | 53.7 ms                                                | 100 ms: 1.86x slower                                                         |
| pyflate                    | 470 ms                                                 | 875 ms: 1.86x slower                                                         |
| richards                   | 47.5 ms                                                | 88.7 ms: 1.87x slower                                                        |
| scimark_fft                | 367 ms                                                 | 686 ms: 1.87x slower                                                         |
| gc_traversal               | 4.90 ms                                                | 9.25 ms: 1.89x slower                                                        |
| pycparser                  | 1.20 sec                                               | 2.28 sec: 1.90x slower                                                       |
| scimark_sor                | 122 ms                                                 | 233 ms: 1.90x slower                                                         |
| sqlite_synth               | 2.90 us                                                | 5.55 us: 1.91x slower                                                        |
| xml_etree_process          | 60.5 ms                                                | 116 ms: 1.92x slower                                                         |
| telco                      | 8.40 ms                                                | 16.2 ms: 1.93x slower                                                        |
| xml_etree_generate         | 86.8 ms                                                | 168 ms: 1.93x slower                                                         |
| thrift                     | 800 us                                                 | 1.55 ms: 1.94x slower                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 9.12 sec: 1.94x slower                                                       |
| k_core                     | 2.37 sec                                               | 4.61 sec: 1.95x slower                                                       |
| pathlib                    | 17.4 ms                                                | 33.8 ms: 1.95x slower                                                        |
| logging_silent             | 101 ns                                                 | 197 ns: 1.95x slower                                                         |
| logging_simple             | 5.65 us                                                | 11.0 us: 1.95x slower                                                        |
| genshi_xml                 | 50.5 ms                                                | 98.8 ms: 1.96x slower                                                        |
| meteor_contest             | 108 ms                                                 | 212 ms: 1.96x slower                                                         |
| logging_format             | 6.23 us                                                | 12.2 us: 1.96x slower                                                        |
| genshi_text                | 22.6 ms                                                | 44.3 ms: 1.96x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 1.08 sec: 1.97x slower                                                       |
| sphinx                     | 1.03 sec                                               | 2.04 sec: 1.98x slower                                                       |
| json                       | 5.32 ms                                                | 10.5 ms: 1.98x slower                                                        |
| regex_dna                  | 220 ms                                                 | 436 ms: 1.98x slower                                                         |
| tomli_loads                | 2.12 sec                                               | 4.20 sec: 1.98x slower                                                       |
| sympy_str                  | 273 ms                                                 | 542 ms: 1.99x slower                                                         |
| mdp                        | 2.54 sec                                               | 5.06 sec: 1.99x slower                                                       |
| sqlalchemy_imperative      | 16.9 ms                                                | 33.6 ms: 1.99x slower                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 133 ms: 2.00x slower                                                         |
| sympy_sum                  | 150 ms                                                 | 301 ms: 2.00x slower                                                         |
| generators                 | 28.8 ms                                                | 57.8 ms: 2.01x slower                                                        |
| sympy_expand               | 456 ms                                                 | 916 ms: 2.01x slower                                                         |
| regex_compile              | 132 ms                                                 | 265 ms: 2.01x slower                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 268 ms: 2.02x slower                                                         |
| html5lib                   | 63.4 ms                                                | 128 ms: 2.02x slower                                                         |
| scimark_lu                 | 114 ms                                                 | 231 ms: 2.02x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 430 us: 2.02x slower                                                         |
| hexiom                     | 6.08 ms                                                | 12.3 ms: 2.02x slower                                                        |
| pidigits                   | 186 ms                                                 | 378 ms: 2.02x slower                                                         |
| pprint_safe_repr           | 727 ms                                                 | 1.47 sec: 2.02x slower                                                       |
| sympy_integrate            | 19.8 ms                                                | 40.3 ms: 2.03x slower                                                        |
| crypto_pyaes               | 74.7 ms                                                | 152 ms: 2.03x slower                                                         |
| django_template            | 31.7 ms                                                | 64.4 ms: 2.04x slower                                                        |
| pprint_pformat             | 1.48 sec                                               | 3.01 sec: 2.04x slower                                                       |
| typing_runtime_protocols   | 160 us                                                 | 327 us: 2.04x slower                                                         |
| chaos                      | 58.0 ms                                                | 119 ms: 2.05x slower                                                         |
| docutils                   | 2.58 sec                                               | 5.32 sec: 2.06x slower                                                       |
| comprehensions             | 16.5 us                                                | 34.1 us: 2.07x slower                                                        |
| shortest_path              | 487 ms                                                 | 1.01 sec: 2.07x slower                                                       |
| coverage                   | 82.8 ms                                                | 172 ms: 2.07x slower                                                         |
| connected_components       | 447 ms                                                 | 927 ms: 2.07x slower                                                         |
| create_gc_cycles           | 2.45 ms                                                | 5.10 ms: 2.08x slower                                                        |
| nqueens                    | 80.9 ms                                                | 169 ms: 2.09x slower                                                         |
| fannkuch                   | 394 ms                                                 | 831 ms: 2.11x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 649 us: 2.15x slower                                                         |
| raytrace                   | 262 ms                                                 | 562 ms: 2.15x slower                                                         |
| coroutines                 | 22.2 ms                                                | 47.8 ms: 2.15x slower                                                        |
| mako                       | 10.7 ms                                                | 23.4 ms: 2.19x slower                                                        |
| many_optionals             | 857 us                                                 | 1.89 ms: 2.20x slower                                                        |
| nbody                      | 87.7 ms                                                | 193 ms: 2.21x slower                                                         |
| json_loads                 | 27.2 us                                                | 60.1 us: 2.21x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 23.2 ms: 2.29x slower                                                        |
| deltablue                  | 3.19 ms                                                | 7.42 ms: 2.32x slower                                                        |
| python_startup             | 12.7 ms                                                | 31.2 ms: 2.46x slower                                                        |
| subparsers                 | 15.5 ms                                                | 40.7 ms: 2.63x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 31.0 ms: 4.43x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 136 ms: 5.66x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 30.2 ms: 36.99x slower                                                       |
| Geometric mean             | (ref)                                                  | 2.04x slower                                                                 |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: 2to3, chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250314-3.14.0a5+-2b1c0da-JIT/bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.487x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.94x
- 95% likely to have a slowdown of 1.93x
- 99% likely to have a slowdown of 1.92x

# Memory
- memory change: 1.05x