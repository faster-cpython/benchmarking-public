# Results vs. 3.13.0

- fork: faster-cpython
- ref: fix_tier2_for_iter
- machine: linux-x86_64
- commit hash: 5725821
- commit date: 2025-06-04
- overall geometric mean: 1.031x slower
- HPT reliability: 98.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                          |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                        |
| html5lib       | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                          |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                                          |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                          |
| async_generators           | 433 ms                                                 | 427 ms: 1.02x faster                                                          |
| coroutines                 | 22.2 ms                                                | 26.0 ms: 1.17x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.2 ms: 1.22x faster                                                         |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                          |
| nbody          | 87.7 ms                                                | 90.2 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.27 ms: 1.15x faster                                                         |
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                         |
| regex_dna      | 220 ms                                                 | 207 ms: 1.06x faster                                                          |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.91 sec: 1.11x faster                                                        |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                          |
| xml_etree_process    | 60.5 ms                                                | 55.7 ms: 1.09x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 200 us: 1.07x faster                                                          |
| xml_etree_generate   | 86.8 ms                                                | 82.0 ms: 1.06x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                                         |
| json_loads           | 27.2 us                                                | 28.5 us: 1.05x slower                                                         |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                          |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                         |
| python_startup_no_site | 7.00 ms                                                | 6.98 ms: 1.00x faster                                                         |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                         |
| genshi_xml      | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                         |
| mako            | 10.7 ms                                                | 10.7 ms: 1.00x faster                                                         |
| django_template | 31.7 ms                                                | 33.1 ms: 1.05x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.26 sec: 2.01x faster                                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                                          |
| richards                   | 47.5 ms                                                | 34.0 ms: 1.40x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                          |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                                          |
| deepcopy                   | 354 us                                                 | 260 us: 1.37x faster                                                          |
| richards_super             | 53.7 ms                                                | 40.0 ms: 1.34x faster                                                         |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 29.9 us: 1.28x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                          |
| float                      | 78.7 ms                                                | 64.2 ms: 1.22x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.27 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                          |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                         |
| pyflate                    | 470 ms                                                 | 410 ms: 1.15x faster                                                          |
| go                         | 141 ms                                                 | 123 ms: 1.14x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                          |
| tomli_loads                | 2.12 sec                                               | 1.91 sec: 1.11x faster                                                        |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                          |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                          |
| scimark_fft                | 367 ms                                                 | 334 ms: 1.10x faster                                                          |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                                          |
| telco                      | 8.40 ms                                                | 7.70 ms: 1.09x faster                                                         |
| xml_etree_process          | 60.5 ms                                                | 55.7 ms: 1.09x faster                                                         |
| unpickle_pure_python       | 213 us                                                 | 200 us: 1.07x faster                                                          |
| regex_dna                  | 220 ms                                                 | 207 ms: 1.06x faster                                                          |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                        |
| xml_etree_generate         | 86.8 ms                                                | 82.0 ms: 1.06x faster                                                         |
| dulwich_log                | 64.6 ms                                                | 61.2 ms: 1.06x faster                                                         |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                         |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                          |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                        |
| html5lib                   | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.84 us: 1.02x faster                                                         |
| json                       | 5.32 ms                                                | 5.21 ms: 1.02x faster                                                         |
| deltablue                  | 3.19 ms                                                | 3.12 ms: 1.02x faster                                                         |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.93 ms: 1.02x faster                                                         |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.02x faster                                                         |
| async_generators           | 433 ms                                                 | 427 ms: 1.02x faster                                                          |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.01x faster                                                          |
| genshi_xml                 | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                         |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                          |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                                         |
| python_startup_no_site     | 7.00 ms                                                | 6.98 ms: 1.00x faster                                                         |
| mako                       | 10.7 ms                                                | 10.7 ms: 1.00x faster                                                         |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                          |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                                          |
| crypto_pyaes               | 74.7 ms                                                | 75.9 ms: 1.02x slower                                                         |
| shortest_path              | 487 ms                                                 | 497 ms: 1.02x slower                                                          |
| connected_components       | 447 ms                                                 | 457 ms: 1.02x slower                                                          |
| sympy_expand               | 456 ms                                                 | 468 ms: 1.03x slower                                                          |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                        |
| nbody                      | 87.7 ms                                                | 90.2 ms: 1.03x slower                                                         |
| gc_traversal               | 4.90 ms                                                | 5.08 ms: 1.04x slower                                                         |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                          |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                         |
| nqueens                    | 80.9 ms                                                | 84.3 ms: 1.04x slower                                                         |
| django_template            | 31.7 ms                                                | 33.1 ms: 1.05x slower                                                         |
| fannkuch                   | 394 ms                                                 | 413 ms: 1.05x slower                                                          |
| json_loads                 | 27.2 us                                                | 28.5 us: 1.05x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                          |
| raytrace                   | 262 ms                                                 | 275 ms: 1.05x slower                                                          |
| generators                 | 28.8 ms                                                | 30.3 ms: 1.05x slower                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.06x slower                                                         |
| hexiom                     | 6.08 ms                                                | 6.45 ms: 1.06x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                          |
| chaos                      | 58.0 ms                                                | 62.0 ms: 1.07x slower                                                         |
| logging_simple             | 5.65 us                                                | 6.13 us: 1.08x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                         |
| logging_format             | 6.23 us                                                | 6.79 us: 1.09x slower                                                         |
| pprint_safe_repr           | 727 ms                                                 | 818 ms: 1.13x slower                                                          |
| many_optionals             | 857 us                                                 | 979 us: 1.14x slower                                                          |
| pprint_pformat             | 1.48 sec                                               | 1.70 sec: 1.15x slower                                                        |
| coroutines                 | 22.2 ms                                                | 26.0 ms: 1.17x slower                                                         |
| subparsers                 | 15.5 ms                                                | 23.5 ms: 1.52x slower                                                         |
| logging_silent             | 101 ns                                                 | 474 ns: 4.69x slower                                                          |
| coverage                   | 82.8 ms                                                | 436 ms: 5.27x slower                                                          |
| thrift                     | 800 us                                                 | 148 ms: 185.17x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                                  |

Benchmark hidden because not significant (4): sphinx, sympy_str, asyncio_websockets, scimark_monte_carlo
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250604-3.15.0a0-5725821-JIT/bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.031x slower

# HPT report

- Reliability score: 98.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x