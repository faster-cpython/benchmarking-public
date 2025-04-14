# Results vs. base

- fork: Fidget-Spinner
- ref: method_jit_bench
- machine: linux-x86_64
- commit hash: 2b1c0da
- commit date: 2025-03-14
- overall geometric mean: 1.512x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.99x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 2.69 sec                                                               | 5.32 sec: 1.98x slower                                                       |
| html5lib       | 61.6 ms                                                                | 128 ms: 2.08x slower                                                         |
| sphinx         | 1.02 sec                                                               | 2.04 sec: 1.99x slower                                                       |
| Geometric mean | (ref)                                                                  | 2.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators           | 411 ms                                                                 | 791 ms: 1.92x slower                                                         |
| asyncio_websockets         | 552 ms                                                                 | 1.08 sec: 1.96x slower                                                       |
| async_tree_none_tg         | 252 ms                                                                 | 495 ms: 1.97x slower                                                         |
| async_tree_io              | 612 ms                                                                 | 1.20 sec: 1.97x slower                                                       |
| async_tree_io_tg           | 615 ms                                                                 | 1.22 sec: 1.99x slower                                                       |
| async_tree_none            | 259 ms                                                                 | 519 ms: 2.00x slower                                                         |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 989 ms: 2.01x slower                                                         |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 960 ms: 2.02x slower                                                         |
| async_tree_memoization_tg  | 318 ms                                                                 | 645 ms: 2.03x slower                                                         |
| async_tree_memoization     | 319 ms                                                                 | 647 ms: 2.03x slower                                                         |
| coroutines                 | 23.5 ms                                                                | 47.8 ms: 2.03x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.99x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 378 ms: 2.03x slower                                                         |
| float          | 64.6 ms                                                                | 139 ms: 2.15x slower                                                         |
| nbody          | 87.5 ms                                                                | 193 ms: 2.21x slower                                                         |
| Geometric mean | (ref)                                                                  | 2.13x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                                | 6.44 ms: 1.84x slower                                                        |
| regex_dna      | 225 ms                                                                 | 436 ms: 1.93x slower                                                         |
| regex_v8       | 23.5 ms                                                                | 48.8 ms: 2.08x slower                                                        |
| regex_compile  | 126 ms                                                                 | 265 ms: 2.10x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.99x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 97.6 ms                                                                | 188 ms: 1.93x slower                                                         |
| xml_etree_parse      | 139 ms                                                                 | 279 ms: 2.01x slower                                                         |
| json_loads           | 29.8 us                                                                | 60.1 us: 2.02x slower                                                        |
| unpickle_pure_python | 212 us                                                                 | 430 us: 2.03x slower                                                         |
| pickle_pure_python   | 319 us                                                                 | 649 us: 2.04x slower                                                         |
| json_dumps           | 11.4 ms                                                                | 23.2 ms: 2.04x slower                                                        |
| xml_etree_process    | 55.2 ms                                                                | 116 ms: 2.10x slower                                                         |
| xml_etree_generate   | 79.0 ms                                                                | 168 ms: 2.13x slower                                                         |
| tomli_loads          | 1.83 sec                                                               | 4.20 sec: 2.29x slower                                                       |
| Geometric mean       | (ref)                                                                  | 2.06x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 31.2 ms: 2.37x slower                                                        |
| python_startup_no_site | 8.21 ms                                                                | 31.0 ms: 3.77x slower                                                        |
| Geometric mean         | (ref)                                                                  | 2.99x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 49.8 ms                                                                | 98.8 ms: 1.98x slower                                                        |
| django_template | 31.2 ms                                                                | 64.4 ms: 2.07x slower                                                        |
| genshi_text     | 21.4 ms                                                                | 44.3 ms: 2.07x slower                                                        |
| mako            | 11.0 ms                                                                | 23.4 ms: 2.13x slower                                                        |
| Geometric mean  | (ref)                                                                  | 2.06x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| bench_mp_pool              | 83.2 ms                                                                | 136 ms: 1.63x slower                                                         |
| comprehensions             | 18.8 us                                                                | 34.1 us: 1.82x slower                                                        |
| gc_traversal               | 5.05 ms                                                                | 9.25 ms: 1.83x slower                                                        |
| regex_effbot               | 3.50 ms                                                                | 6.44 ms: 1.84x slower                                                        |
| hexiom                     | 6.64 ms                                                                | 12.3 ms: 1.85x slower                                                        |
| go                         | 127 ms                                                                 | 242 ms: 1.91x slower                                                         |
| crypto_pyaes               | 79.3 ms                                                                | 152 ms: 1.92x slower                                                         |
| async_generators           | 411 ms                                                                 | 791 ms: 1.92x slower                                                         |
| xml_etree_iterparse        | 97.6 ms                                                                | 188 ms: 1.93x slower                                                         |
| regex_dna                  | 225 ms                                                                 | 436 ms: 1.93x slower                                                         |
| meteor_contest             | 109 ms                                                                 | 212 ms: 1.94x slower                                                         |
| sympy_expand               | 469 ms                                                                 | 916 ms: 1.95x slower                                                         |
| dulwich_log                | 60.7 ms                                                                | 118 ms: 1.95x slower                                                         |
| pprint_pformat             | 1.54 sec                                                               | 3.01 sec: 1.95x slower                                                       |
| pyflate                    | 447 ms                                                                 | 875 ms: 1.96x slower                                                         |
| pycparser                  | 1.17 sec                                                               | 2.28 sec: 1.96x slower                                                       |
| scimark_sor                | 119 ms                                                                 | 233 ms: 1.96x slower                                                         |
| subparsers                 | 20.7 ms                                                                | 40.7 ms: 1.96x slower                                                        |
| asyncio_websockets         | 552 ms                                                                 | 1.08 sec: 1.96x slower                                                       |
| async_tree_none_tg         | 252 ms                                                                 | 495 ms: 1.97x slower                                                         |
| async_tree_io              | 612 ms                                                                 | 1.20 sec: 1.97x slower                                                       |
| typing_runtime_protocols   | 166 us                                                                 | 327 us: 1.97x slower                                                         |
| pprint_safe_repr           | 745 ms                                                                 | 1.47 sec: 1.97x slower                                                       |
| json                       | 5.33 ms                                                                | 10.5 ms: 1.97x slower                                                        |
| fannkuch                   | 421 ms                                                                 | 831 ms: 1.97x slower                                                         |
| scimark_sparse_mat_mult    | 4.70 ms                                                                | 9.29 ms: 1.98x slower                                                        |
| logging_simple             | 5.58 us                                                                | 11.0 us: 1.98x slower                                                        |
| logging_format             | 6.17 us                                                                | 12.2 us: 1.98x slower                                                        |
| docutils                   | 2.69 sec                                                               | 5.32 sec: 1.98x slower                                                       |
| genshi_xml                 | 49.8 ms                                                                | 98.8 ms: 1.98x slower                                                        |
| many_optionals             | 953 us                                                                 | 1.89 ms: 1.98x slower                                                        |
| scimark_monte_carlo        | 67.2 ms                                                                | 133 ms: 1.99x slower                                                         |
| k_core                     | 2.32 sec                                                               | 4.61 sec: 1.99x slower                                                       |
| bpe_tokeniser              | 4.59 sec                                                               | 9.12 sec: 1.99x slower                                                       |
| async_tree_io_tg           | 615 ms                                                                 | 1.22 sec: 1.99x slower                                                       |
| sympy_str                  | 273 ms                                                                 | 542 ms: 1.99x slower                                                         |
| sqlglot_v2_normalize       | 107 ms                                                                 | 213 ms: 1.99x slower                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                                | 33.6 ms: 1.99x slower                                                        |
| sphinx                     | 1.02 sec                                                               | 2.04 sec: 1.99x slower                                                       |
| deepcopy_memo              | 29.5 us                                                                | 58.9 us: 1.99x slower                                                        |
| sympy_sum                  | 151 ms                                                                 | 301 ms: 2.00x slower                                                         |
| sympy_integrate            | 20.2 ms                                                                | 40.3 ms: 2.00x slower                                                        |
| scimark_lu                 | 115 ms                                                                 | 231 ms: 2.00x slower                                                         |
| async_tree_none            | 259 ms                                                                 | 519 ms: 2.00x slower                                                         |
| sqlglot_v2_optimize        | 53.6 ms                                                                | 108 ms: 2.01x slower                                                         |
| xml_etree_parse            | 139 ms                                                                 | 279 ms: 2.01x slower                                                         |
| coverage                   | 85.4 ms                                                                | 172 ms: 2.01x slower                                                         |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 989 ms: 2.01x slower                                                         |
| pylint                     | 280 ms                                                                 | 563 ms: 2.01x slower                                                         |
| deepcopy_reduce            | 2.65 us                                                                | 5.34 us: 2.01x slower                                                        |
| thrift                     | 770 us                                                                 | 1.55 ms: 2.01x slower                                                        |
| json_loads                 | 29.8 us                                                                | 60.1 us: 2.02x slower                                                        |
| nqueens                    | 83.6 ms                                                                | 169 ms: 2.02x slower                                                         |
| chaos                      | 58.9 ms                                                                | 119 ms: 2.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 960 ms: 2.02x slower                                                         |
| connected_components       | 458 ms                                                                 | 927 ms: 2.02x slower                                                         |
| async_tree_memoization_tg  | 318 ms                                                                 | 645 ms: 2.03x slower                                                         |
| async_tree_memoization     | 319 ms                                                                 | 647 ms: 2.03x slower                                                         |
| unpickle_pure_python       | 212 us                                                                 | 430 us: 2.03x slower                                                         |
| coroutines                 | 23.5 ms                                                                | 47.8 ms: 2.03x slower                                                        |
| sqlalchemy_declarative     | 132 ms                                                                 | 268 ms: 2.03x slower                                                         |
| pidigits                   | 186 ms                                                                 | 378 ms: 2.03x slower                                                         |
| pickle_pure_python         | 319 us                                                                 | 649 us: 2.04x slower                                                         |
| sqlite_synth               | 2.72 us                                                                | 5.55 us: 2.04x slower                                                        |
| shortest_path              | 493 ms                                                                 | 1.01 sec: 2.04x slower                                                       |
| json_dumps                 | 11.4 ms                                                                | 23.2 ms: 2.04x slower                                                        |
| telco                      | 7.92 ms                                                                | 16.2 ms: 2.04x slower                                                        |
| deepcopy                   | 256 us                                                                 | 524 us: 2.05x slower                                                         |
| create_gc_cycles           | 2.49 ms                                                                | 5.10 ms: 2.05x slower                                                        |
| mdp                        | 2.46 sec                                                               | 5.06 sec: 2.05x slower                                                       |
| django_template            | 31.2 ms                                                                | 64.4 ms: 2.07x slower                                                        |
| pathlib                    | 16.3 ms                                                                | 33.8 ms: 2.07x slower                                                        |
| genshi_text                | 21.4 ms                                                                | 44.3 ms: 2.07x slower                                                        |
| html5lib                   | 61.6 ms                                                                | 128 ms: 2.08x slower                                                         |
| logging_silent             | 94.7 ns                                                                | 197 ns: 2.08x slower                                                         |
| regex_v8                   | 23.5 ms                                                                | 48.8 ms: 2.08x slower                                                        |
| generators                 | 27.5 ms                                                                | 57.8 ms: 2.10x slower                                                        |
| xml_etree_process          | 55.2 ms                                                                | 116 ms: 2.10x slower                                                         |
| regex_compile              | 126 ms                                                                 | 265 ms: 2.10x slower                                                         |
| raytrace                   | 266 ms                                                                 | 562 ms: 2.11x slower                                                         |
| xml_etree_generate         | 79.0 ms                                                                | 168 ms: 2.13x slower                                                         |
| mako                       | 11.0 ms                                                                | 23.4 ms: 2.13x slower                                                        |
| float                      | 64.6 ms                                                                | 139 ms: 2.15x slower                                                         |
| spectral_norm              | 93.2 ms                                                                | 202 ms: 2.17x slower                                                         |
| nbody                      | 87.5 ms                                                                | 193 ms: 2.21x slower                                                         |
| scimark_fft                | 308 ms                                                                 | 686 ms: 2.23x slower                                                         |
| tomli_loads                | 1.83 sec                                                               | 4.20 sec: 2.29x slower                                                       |
| python_startup             | 13.1 ms                                                                | 31.2 ms: 2.37x slower                                                        |
| sqlglot_v2_transpile       | 1.59 ms                                                                | 3.87 ms: 2.43x slower                                                        |
| richards_super             | 40.8 ms                                                                | 100 ms: 2.45x slower                                                         |
| deltablue                  | 3.02 ms                                                                | 7.42 ms: 2.46x slower                                                        |
| richards                   | 35.5 ms                                                                | 88.7 ms: 2.50x slower                                                        |
| sqlglot_v2_parse           | 1.28 ms                                                                | 3.25 ms: 2.54x slower                                                        |
| python_startup_no_site     | 8.21 ms                                                                | 31.0 ms: 3.77x slower                                                        |
| bench_thread_pool          | 876 us                                                                 | 30.2 ms: 34.54x slower                                                       |
| Geometric mean             | (ref)                                                                  | 2.11x slower                                                                 |
Ignored benchmarks (1) of results/bm-20250311-3.14.0a5+-e0bc9d2-JIT/bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2.json: 2to3

- Geometric mean (including insignificant results): 1.512x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.99x
- 95% likely to have a slowdown of 1.99x
- 99% likely to have a slowdown of 1.99x

# Memory
- memory change: 1.00x