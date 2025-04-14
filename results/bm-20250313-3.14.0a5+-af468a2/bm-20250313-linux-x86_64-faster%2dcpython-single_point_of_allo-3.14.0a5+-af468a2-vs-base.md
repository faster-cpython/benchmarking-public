# Results vs. base

- fork: faster-cpython
- ref: single_point_of_allo
- machine: linux-x86_64
- commit hash: af468a2
- commit date: 2025-03-13
- overall geometric mean: 1.049x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 271 ms: 1.05x slower                                                             |
| docutils       | 2.62 sec                                                               | 2.71 sec: 1.04x slower                                                           |
| html5lib       | 61.2 ms                                                                | 63.2 ms: 1.03x slower                                                            |
| sphinx         | 1.01 sec                                                               | 1.07 sec: 1.06x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coroutines                 | 23.6 ms                                                                | 23.3 ms: 1.01x faster                                                            |
| async_tree_none_tg         | 251 ms                                                                 | 254 ms: 1.01x slower                                                             |
| async_tree_none            | 257 ms                                                                 | 262 ms: 1.02x slower                                                             |
| async_tree_cpu_io_mixed    | 489 ms                                                                 | 499 ms: 1.02x slower                                                             |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 488 ms: 1.03x slower                                                             |
| async_tree_memoization_tg  | 317 ms                                                                 | 330 ms: 1.04x slower                                                             |
| async_tree_memoization     | 316 ms                                                                 | 336 ms: 1.06x slower                                                             |
| async_tree_io_tg           | 617 ms                                                                 | 657 ms: 1.07x slower                                                             |
| async_generators           | 397 ms                                                                 | 454 ms: 1.14x slower                                                             |
| Geometric mean             | (ref)                                                                  | 1.03x slower                                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 196 ms                                                                 | 191 ms: 1.03x faster                                                             |
| float          | 69.7 ms                                                                | 75.7 ms: 1.09x slower                                                            |
| nbody          | 97.3 ms                                                                | 124 ms: 1.28x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.11x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                 | 227 ms: 1.01x slower                                                             |
| regex_effbot   | 3.48 ms                                                                | 3.53 ms: 1.02x slower                                                            |
| regex_v8       | 23.9 ms                                                                | 24.3 ms: 1.02x slower                                                            |
| regex_compile  | 125 ms                                                                 | 134 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                                             |
| xml_etree_parse      | 140 ms                                                                 | 142 ms: 1.02x slower                                                             |
| pickle_pure_python   | 320 us                                                                 | 325 us: 1.02x slower                                                             |
| json_dumps           | 11.5 ms                                                                | 11.7 ms: 1.02x slower                                                            |
| xml_etree_process    | 58.7 ms                                                                | 60.5 ms: 1.03x slower                                                            |
| xml_etree_generate   | 84.0 ms                                                                | 87.5 ms: 1.04x slower                                                            |
| xml_etree_iterparse  | 98.2 ms                                                                | 103 ms: 1.05x slower                                                             |
| tomli_loads          | 1.97 sec                                                               | 2.13 sec: 1.08x slower                                                           |
| json_loads           | 30.0 us                                                                | 32.6 us: 1.09x slower                                                            |
| Geometric mean       | (ref)                                                                  | 1.04x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 8.20 ms                                                                | 8.30 ms: 1.01x slower                                                            |
| python_startup         | 13.1 ms                                                                | 13.3 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                            |
| django_template | 31.5 ms                                                                | 33.6 ms: 1.07x slower                                                            |
| genshi_xml      | 49.2 ms                                                                | 52.5 ms: 1.07x slower                                                            |
| genshi_text     | 21.4 ms                                                                | 23.0 ms: 1.08x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.05x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coverage                   | 90.9 ms                                                                | 85.4 ms: 1.06x faster                                                            |
| pidigits                   | 196 ms                                                                 | 191 ms: 1.03x faster                                                             |
| generators                 | 28.3 ms                                                                | 27.9 ms: 1.02x faster                                                            |
| mako                       | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                            |
| coroutines                 | 23.6 ms                                                                | 23.3 ms: 1.01x faster                                                            |
| unpickle_pure_python       | 219 us                                                                 | 217 us: 1.01x faster                                                             |
| deepcopy_memo              | 29.7 us                                                                | 29.5 us: 1.01x faster                                                            |
| gc_traversal               | 4.78 ms                                                                | 4.75 ms: 1.01x faster                                                            |
| create_gc_cycles           | 2.47 ms                                                                | 2.48 ms: 1.00x slower                                                            |
| hexiom                     | 6.16 ms                                                                | 6.19 ms: 1.01x slower                                                            |
| deltablue                  | 3.19 ms                                                                | 3.21 ms: 1.01x slower                                                            |
| async_tree_none_tg         | 251 ms                                                                 | 254 ms: 1.01x slower                                                             |
| regex_dna                  | 225 ms                                                                 | 227 ms: 1.01x slower                                                             |
| python_startup_no_site     | 8.20 ms                                                                | 8.30 ms: 1.01x slower                                                            |
| python_startup             | 13.1 ms                                                                | 13.3 ms: 1.01x slower                                                            |
| go                         | 115 ms                                                                 | 117 ms: 1.01x slower                                                             |
| regex_effbot               | 3.48 ms                                                                | 3.53 ms: 1.02x slower                                                            |
| regex_v8                   | 23.9 ms                                                                | 24.3 ms: 1.02x slower                                                            |
| xml_etree_parse            | 140 ms                                                                 | 142 ms: 1.02x slower                                                             |
| pickle_pure_python         | 320 us                                                                 | 325 us: 1.02x slower                                                             |
| meteor_contest             | 106 ms                                                                 | 108 ms: 1.02x slower                                                             |
| json_dumps                 | 11.5 ms                                                                | 11.7 ms: 1.02x slower                                                            |
| shortest_path              | 493 ms                                                                 | 502 ms: 1.02x slower                                                             |
| async_tree_none            | 257 ms                                                                 | 262 ms: 1.02x slower                                                             |
| async_tree_cpu_io_mixed    | 489 ms                                                                 | 499 ms: 1.02x slower                                                             |
| bench_mp_pool              | 83.1 ms                                                                | 84.9 ms: 1.02x slower                                                            |
| pprint_safe_repr           | 738 ms                                                                 | 757 ms: 1.03x slower                                                             |
| connected_components       | 454 ms                                                                 | 467 ms: 1.03x slower                                                             |
| pycparser                  | 1.19 sec                                                               | 1.22 sec: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 488 ms: 1.03x slower                                                             |
| pyflate                    | 465 ms                                                                 | 479 ms: 1.03x slower                                                             |
| sympy_integrate            | 20.0 ms                                                                | 20.6 ms: 1.03x slower                                                            |
| xml_etree_process          | 58.7 ms                                                                | 60.5 ms: 1.03x slower                                                            |
| html5lib                   | 61.2 ms                                                                | 63.2 ms: 1.03x slower                                                            |
| mdp                        | 2.49 sec                                                               | 2.57 sec: 1.03x slower                                                           |
| telco                      | 7.86 ms                                                                | 8.13 ms: 1.03x slower                                                            |
| sqlglot_v2_parse           | 1.26 ms                                                                | 1.30 ms: 1.04x slower                                                            |
| sqlglot_v2_transpile       | 1.58 ms                                                                | 1.63 ms: 1.04x slower                                                            |
| docutils                   | 2.62 sec                                                               | 2.71 sec: 1.04x slower                                                           |
| bench_thread_pool          | 872 us                                                                 | 906 us: 1.04x slower                                                             |
| async_tree_memoization_tg  | 317 ms                                                                 | 330 ms: 1.04x slower                                                             |
| xml_etree_generate         | 84.0 ms                                                                | 87.5 ms: 1.04x slower                                                            |
| logging_simple             | 5.53 us                                                                | 5.76 us: 1.04x slower                                                            |
| sqlalchemy_declarative     | 130 ms                                                                 | 136 ms: 1.04x slower                                                             |
| pprint_pformat             | 1.50 sec                                                               | 1.57 sec: 1.05x slower                                                           |
| pylint                     | 276 ms                                                                 | 289 ms: 1.05x slower                                                             |
| xml_etree_iterparse        | 98.2 ms                                                                | 103 ms: 1.05x slower                                                             |
| logging_format             | 6.21 us                                                                | 6.51 us: 1.05x slower                                                            |
| deepcopy                   | 259 us                                                                 | 272 us: 1.05x slower                                                             |
| sqlite_synth               | 2.79 us                                                                | 2.93 us: 1.05x slower                                                            |
| 2to3                       | 258 ms                                                                 | 271 ms: 1.05x slower                                                             |
| subparsers                 | 20.7 ms                                                                | 21.7 ms: 1.05x slower                                                            |
| sympy_sum                  | 149 ms                                                                 | 157 ms: 1.05x slower                                                             |
| dulwich_log                | 58.3 ms                                                                | 61.4 ms: 1.05x slower                                                            |
| comprehensions             | 16.6 us                                                                | 17.5 us: 1.06x slower                                                            |
| sphinx                     | 1.01 sec                                                               | 1.07 sec: 1.06x slower                                                           |
| async_tree_memoization     | 316 ms                                                                 | 336 ms: 1.06x slower                                                             |
| regex_compile              | 125 ms                                                                 | 134 ms: 1.06x slower                                                             |
| many_optionals             | 941 us                                                                 | 1.00 ms: 1.07x slower                                                            |
| async_tree_io_tg           | 617 ms                                                                 | 657 ms: 1.07x slower                                                             |
| django_template            | 31.5 ms                                                                | 33.6 ms: 1.07x slower                                                            |
| pathlib                    | 16.5 ms                                                                | 17.6 ms: 1.07x slower                                                            |
| genshi_xml                 | 49.2 ms                                                                | 52.5 ms: 1.07x slower                                                            |
| thrift                     | 775 us                                                                 | 828 us: 1.07x slower                                                             |
| logging_silent             | 100 ns                                                                 | 108 ns: 1.07x slower                                                             |
| sqlglot_v2_normalize       | 106 ms                                                                 | 114 ms: 1.07x slower                                                             |
| genshi_text                | 21.4 ms                                                                | 23.0 ms: 1.08x slower                                                            |
| nqueens                    | 83.3 ms                                                                | 89.7 ms: 1.08x slower                                                            |
| deepcopy_reduce            | 2.70 us                                                                | 2.91 us: 1.08x slower                                                            |
| sqlalchemy_imperative      | 16.5 ms                                                                | 17.9 ms: 1.08x slower                                                            |
| tomli_loads                | 1.97 sec                                                               | 2.13 sec: 1.08x slower                                                           |
| sympy_str                  | 270 ms                                                                 | 293 ms: 1.09x slower                                                             |
| sqlglot_v2_optimize        | 53.0 ms                                                                | 57.5 ms: 1.09x slower                                                            |
| json_loads                 | 30.0 us                                                                | 32.6 us: 1.09x slower                                                            |
| float                      | 69.7 ms                                                                | 75.7 ms: 1.09x slower                                                            |
| chaos                      | 60.0 ms                                                                | 65.3 ms: 1.09x slower                                                            |
| json                       | 5.29 ms                                                                | 5.77 ms: 1.09x slower                                                            |
| sympy_expand               | 457 ms                                                                 | 501 ms: 1.10x slower                                                             |
| fannkuch                   | 425 ms                                                                 | 467 ms: 1.10x slower                                                             |
| raytrace                   | 271 ms                                                                 | 298 ms: 1.10x slower                                                             |
| scimark_monte_carlo        | 68.6 ms                                                                | 76.0 ms: 1.11x slower                                                            |
| scimark_lu                 | 115 ms                                                                 | 128 ms: 1.11x slower                                                             |
| typing_runtime_protocols   | 163 us                                                                 | 183 us: 1.13x slower                                                             |
| scimark_sor                | 119 ms                                                                 | 136 ms: 1.14x slower                                                             |
| async_generators           | 397 ms                                                                 | 454 ms: 1.14x slower                                                             |
| bpe_tokeniser              | 4.57 sec                                                               | 5.26 sec: 1.15x slower                                                           |
| scimark_fft                | 348 ms                                                                 | 423 ms: 1.22x slower                                                             |
| nbody                      | 97.3 ms                                                                | 124 ms: 1.28x slower                                                             |
| spectral_norm              | 99.3 ms                                                                | 127 ms: 1.28x slower                                                             |
| scimark_sparse_mat_mult    | 4.74 ms                                                                | 6.40 ms: 1.35x slower                                                            |
| Geometric mean             | (ref)                                                                  | 1.05x slower                                                                     |

Benchmark hidden because not significant (6): richards, crypto_pyaes, asyncio_websockets, richards_super, async_tree_io, k_core

- Geometric mean (including insignificant results): 1.049x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 0.99x