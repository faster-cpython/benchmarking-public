# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.037x slower
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                            |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                          |
| html5lib       | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                           |
| sphinx         | 1.03 sec                                               | 998 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                            |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.38x faster                                                            |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 492 ms: 1.10x faster                                                            |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                            |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.8 ms: 1.08x faster                                                           |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody          | 87.7 ms                                                | 97.8 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.2 ms: 1.21x faster                                                           |
| regex_effbot   | 3.77 ms                                                | 3.15 ms: 1.19x faster                                                           |
| regex_dna      | 220 ms                                                 | 191 ms: 1.15x faster                                                            |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 143 ms: 1.07x faster                                                            |
| tomli_loads          | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                          |
| xml_etree_iterparse  | 101 ms                                                 | 99.3 ms: 1.02x faster                                                           |
| xml_etree_generate   | 86.8 ms                                                | 85.9 ms: 1.01x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                            |
| json_loads           | 27.2 us                                                | 28.5 us: 1.05x slower                                                           |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.05x slower                                                            |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| python_startup_no_site | 7.00 ms                                                | 6.93 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                           |
| genshi_xml      | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                           |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                           |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                            |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.38x faster                                                            |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                            |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                            |
| deepcopy_memo              | 38.4 us                                                | 29.2 us: 1.32x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                            |
| go                         | 141 ms                                                 | 111 ms: 1.27x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 22.2 ms: 1.21x faster                                                           |
| regex_effbot               | 3.77 ms                                                | 3.15 ms: 1.19x faster                                                           |
| deepcopy_reduce            | 3.24 us                                                | 2.79 us: 1.16x faster                                                           |
| regex_dna                  | 220 ms                                                 | 191 ms: 1.15x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                            |
| pylint                     | 312 ms                                                 | 277 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 492 ms: 1.10x faster                                                            |
| richards                   | 47.5 ms                                                | 43.5 ms: 1.09x faster                                                           |
| dulwich_log                | 64.6 ms                                                | 59.2 ms: 1.09x faster                                                           |
| richards_super             | 53.7 ms                                                | 49.4 ms: 1.09x faster                                                           |
| float                      | 78.7 ms                                                | 72.8 ms: 1.08x faster                                                           |
| pyflate                    | 470 ms                                                 | 435 ms: 1.08x faster                                                            |
| xml_etree_parse            | 154 ms                                                 | 143 ms: 1.07x faster                                                            |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                          |
| telco                      | 8.40 ms                                                | 7.98 ms: 1.05x faster                                                           |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                            |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                            |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                                           |
| tomli_loads                | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                          |
| genshi_text                | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                                          |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                            |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                          |
| sphinx                     | 1.03 sec                                               | 998 ms: 1.03x faster                                                            |
| comprehensions             | 16.5 us                                                | 16.0 us: 1.03x faster                                                           |
| html5lib                   | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                           |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                                            |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                            |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                           |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                            |
| spectral_norm              | 113 ms                                                 | 111 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 99.3 ms: 1.02x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                            |
| sqlite_synth               | 2.90 us                                                | 2.86 us: 1.01x faster                                                           |
| xml_etree_generate         | 86.8 ms                                                | 85.9 ms: 1.01x faster                                                           |
| genshi_xml                 | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                           |
| python_startup_no_site     | 7.00 ms                                                | 6.93 ms: 1.01x faster                                                           |
| sympy_expand               | 456 ms                                                 | 452 ms: 1.01x faster                                                            |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                          |
| crypto_pyaes               | 74.7 ms                                                | 74.2 ms: 1.01x faster                                                           |
| hexiom                     | 6.08 ms                                                | 6.05 ms: 1.00x faster                                                           |
| scimark_monte_carlo        | 66.8 ms                                                | 67.2 ms: 1.01x slower                                                           |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.11 ms: 1.02x slower                                                           |
| chaos                      | 58.0 ms                                                | 59.2 ms: 1.02x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                            |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                           |
| raytrace                   | 262 ms                                                 | 269 ms: 1.03x slower                                                            |
| generators                 | 28.8 ms                                                | 29.6 ms: 1.03x slower                                                           |
| gc_traversal               | 4.90 ms                                                | 5.07 ms: 1.04x slower                                                           |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                                            |
| scimark_fft                | 367 ms                                                 | 383 ms: 1.04x slower                                                            |
| json_loads                 | 27.2 us                                                | 28.5 us: 1.05x slower                                                           |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.05x slower                                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                           |
| fannkuch                   | 394 ms                                                 | 418 ms: 1.06x slower                                                            |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                           |
| connected_components       | 447 ms                                                 | 475 ms: 1.06x slower                                                            |
| shortest_path              | 487 ms                                                 | 521 ms: 1.07x slower                                                            |
| logging_simple             | 5.65 us                                                | 6.07 us: 1.07x slower                                                           |
| logging_format             | 6.23 us                                                | 6.77 us: 1.09x slower                                                           |
| deltablue                  | 3.19 ms                                                | 3.49 ms: 1.09x slower                                                           |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                           |
| pprint_pformat             | 1.48 sec                                               | 1.65 sec: 1.11x slower                                                          |
| many_optionals             | 857 us                                                 | 954 us: 1.11x slower                                                            |
| pprint_safe_repr           | 727 ms                                                 | 810 ms: 1.11x slower                                                            |
| nbody                      | 87.7 ms                                                | 97.8 ms: 1.12x slower                                                           |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                                           |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                                           |
| logging_silent             | 101 ns                                                 | 475 ns: 4.70x slower                                                            |
| coverage                   | 82.8 ms                                                | 418 ms: 5.04x slower                                                            |
| thrift                     | 800 us                                                 | 149 ms: 185.86x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                                    |

Benchmark hidden because not significant (4): json, nqueens, asyncio_websockets, xml_etree_process
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250616-3.15.0a0-c41d531/bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.037x slower

# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x