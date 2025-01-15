# Results vs. 3.13.0

- fork: faster-cpython
- ref: no_conditional_stack
- machine: linux-x86_64
- commit hash: d85c001
- commit date: 2025-01-15
- overall geometric mean: 1.036x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                             |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                           |
| html5lib       | 63.4 ms                                                | 62.4 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 592 ms: 1.45x faster                                                             |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                             |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 326 ms: 1.34x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 464 ms: 1.17x faster                                                             |
| async_generators           | 433 ms                                                 | 387 ms: 1.12x faster                                                             |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.9 ms: 1.08x faster                                                            |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                             |
| nbody          | 87.7 ms                                                | 98.0 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.41 ms: 1.11x faster                                                            |
| regex_v8       | 26.9 ms                                                | 25.3 ms: 1.06x faster                                                            |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                             |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                             |
| tomli_loads          | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                           |
| xml_etree_iterparse  | 101 ms                                                 | 97.8 ms: 1.04x faster                                                            |
| xml_etree_generate   | 86.8 ms                                                | 84.1 ms: 1.03x faster                                                            |
| xml_etree_process    | 60.5 ms                                                | 61.6 ms: 1.02x slower                                                            |
| unpickle_pure_python | 213 us                                                 | 228 us: 1.07x slower                                                             |
| json_loads           | 27.2 us                                                | 29.2 us: 1.07x slower                                                            |
| pickle_pure_python   | 302 us                                                 | 328 us: 1.09x slower                                                             |
| json_dumps           | 10.1 ms                                                | 11.9 ms: 1.17x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.03 ms: 1.00x slower                                                            |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                            |
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.01x faster                                                            |
| django_template | 31.7 ms                                                | 32.8 ms: 1.04x slower                                                            |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d85c001 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 592 ms: 1.45x faster                                                             |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                             |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                                             |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 326 ms: 1.34x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                             |
| deepcopy_memo              | 38.4 us                                                | 31.6 us: 1.22x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                            |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 464 ms: 1.17x faster                                                             |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                             |
| async_generators           | 433 ms                                                 | 387 ms: 1.12x faster                                                             |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                             |
| regex_effbot               | 3.77 ms                                                | 3.41 ms: 1.11x faster                                                            |
| pathlib                    | 17.4 ms                                                | 15.8 ms: 1.10x faster                                                            |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                                             |
| float                      | 78.7 ms                                                | 72.9 ms: 1.08x faster                                                            |
| telco                      | 8.40 ms                                                | 7.91 ms: 1.06x faster                                                            |
| richards                   | 47.5 ms                                                | 44.8 ms: 1.06x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 25.3 ms: 1.06x faster                                                            |
| richards_super             | 53.7 ms                                                | 50.7 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.76 ms: 1.06x faster                                                            |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                            |
| generators                 | 28.8 ms                                                | 27.4 ms: 1.05x faster                                                            |
| scimark_fft                | 367 ms                                                 | 350 ms: 1.05x faster                                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.05x faster                                                           |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                             |
| tomli_loads                | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                           |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                           |
| crypto_pyaes               | 74.7 ms                                                | 72.1 ms: 1.04x faster                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 97.8 ms: 1.04x faster                                                            |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.03x faster                                                            |
| xml_etree_generate         | 86.8 ms                                                | 84.1 ms: 1.03x faster                                                            |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.03x faster                                                             |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.03x faster                                                           |
| gc_traversal               | 4.90 ms                                                | 4.78 ms: 1.03x faster                                                            |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                             |
| shortest_path              | 487 ms                                                 | 475 ms: 1.02x faster                                                             |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                             |
| thrift                     | 800 us                                                 | 782 us: 1.02x faster                                                             |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                           |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                             |
| connected_components       | 447 ms                                                 | 439 ms: 1.02x faster                                                             |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                             |
| html5lib                   | 63.4 ms                                                | 62.4 ms: 1.02x faster                                                            |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.01x faster                                                            |
| sympy_str                  | 273 ms                                                 | 270 ms: 1.01x faster                                                             |
| json                       | 5.32 ms                                                | 5.26 ms: 1.01x faster                                                            |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                             |
| deltablue                  | 3.19 ms                                                | 3.17 ms: 1.01x faster                                                            |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                            |
| sqlglot_parse              | 1.26 ms                                                | 1.26 ms: 1.01x faster                                                            |
| scimark_sor                | 122 ms                                                 | 122 ms: 1.00x faster                                                             |
| sqlglot_optimize           | 53.4 ms                                                | 53.2 ms: 1.00x faster                                                            |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                             |
| pyflate                    | 470 ms                                                 | 471 ms: 1.00x slower                                                             |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.00x slower                                                            |
| python_startup_no_site     | 7.00 ms                                                | 7.03 ms: 1.00x slower                                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                                            |
| dulwich_log                | 64.6 ms                                                | 65.0 ms: 1.01x slower                                                            |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                                             |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                           |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                            |
| pprint_safe_repr           | 727 ms                                                 | 736 ms: 1.01x slower                                                             |
| xml_etree_process          | 60.5 ms                                                | 61.6 ms: 1.02x slower                                                            |
| fannkuch                   | 394 ms                                                 | 402 ms: 1.02x slower                                                             |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                                           |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.03x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 165 us: 1.03x slower                                                             |
| scimark_monte_carlo        | 66.8 ms                                                | 68.6 ms: 1.03x slower                                                            |
| logging_format             | 6.23 us                                                | 6.41 us: 1.03x slower                                                            |
| logging_simple             | 5.65 us                                                | 5.82 us: 1.03x slower                                                            |
| hexiom                     | 6.08 ms                                                | 6.28 ms: 1.03x slower                                                            |
| django_template            | 31.7 ms                                                | 32.8 ms: 1.04x slower                                                            |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                                             |
| chaos                      | 58.0 ms                                                | 60.8 ms: 1.05x slower                                                            |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                            |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                            |
| bench_thread_pool          | 818 us                                                 | 870 us: 1.06x slower                                                             |
| logging_silent             | 101 ns                                                 | 108 ns: 1.07x slower                                                             |
| unpickle_pure_python       | 213 us                                                 | 228 us: 1.07x slower                                                             |
| json_loads                 | 27.2 us                                                | 29.2 us: 1.07x slower                                                            |
| pickle_pure_python         | 302 us                                                 | 328 us: 1.09x slower                                                             |
| coverage                   | 82.8 ms                                                | 90.3 ms: 1.09x slower                                                            |
| many_optionals             | 857 us                                                 | 943 us: 1.10x slower                                                             |
| nbody                      | 87.7 ms                                                | 98.0 ms: 1.12x slower                                                            |
| json_dumps                 | 10.1 ms                                                | 11.9 ms: 1.17x slower                                                            |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.32x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.39x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (5): sphinx, nqueens, sqlglot_transpile, asyncio_websockets, sympy_expand
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x