# Results vs. 3.13.0

- fork: faster-cpython
- ref: no_conditional_stack
- machine: linux-x86_64
- commit hash: 6ac95d4
- commit date: 2025-01-16
- overall geometric mean: 1.041x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                             |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                           |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                            |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 303 ms: 1.53x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 587 ms: 1.47x faster                                                             |
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                             |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.31x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 465 ms: 1.17x faster                                                             |
| async_generators           | 433 ms                                                 | 380 ms: 1.14x faster                                                             |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.09x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.4 ms: 1.09x faster                                                            |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                             |
| nbody          | 87.7 ms                                                | 93.6 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.17 ms: 1.19x faster                                                            |
| regex_v8       | 26.9 ms                                                | 25.2 ms: 1.06x faster                                                            |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                                             |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                                             |
| tomli_loads          | 2.12 sec                                               | 2.00 sec: 1.06x faster                                                           |
| xml_etree_generate   | 86.8 ms                                                | 84.0 ms: 1.03x faster                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 98.5 ms: 1.03x faster                                                            |
| xml_etree_process    | 60.5 ms                                                | 61.5 ms: 1.02x slower                                                            |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                                            |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                             |
| unpickle_pure_python | 213 us                                                 | 228 us: 1.07x slower                                                             |
| json_dumps           | 10.1 ms                                                | 12.1 ms: 1.19x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.00 ms: 1.00x faster                                                            |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                            |
| genshi_xml      | 50.5 ms                                                | 49.4 ms: 1.02x faster                                                            |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                            |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-6ac95d4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 303 ms: 1.53x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 587 ms: 1.47x faster                                                             |
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                             |
| deepcopy                   | 354 us                                                 | 258 us: 1.38x faster                                                             |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.31x faster                                                             |
| deepcopy_memo              | 38.4 us                                                | 30.5 us: 1.26x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.21x faster                                                            |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                                             |
| regex_effbot               | 3.77 ms                                                | 3.17 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 465 ms: 1.17x faster                                                             |
| async_generators           | 433 ms                                                 | 380 ms: 1.14x faster                                                             |
| pylint                     | 312 ms                                                 | 275 ms: 1.13x faster                                                             |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                                             |
| float                      | 78.7 ms                                                | 72.4 ms: 1.09x faster                                                            |
| pathlib                    | 17.4 ms                                                | 16.1 ms: 1.08x faster                                                            |
| richards                   | 47.5 ms                                                | 44.5 ms: 1.07x faster                                                            |
| richards_super             | 53.7 ms                                                | 50.3 ms: 1.07x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 25.2 ms: 1.06x faster                                                            |
| telco                      | 8.40 ms                                                | 7.90 ms: 1.06x faster                                                            |
| tomli_loads                | 2.12 sec                                               | 2.00 sec: 1.06x faster                                                           |
| scimark_fft                | 367 ms                                                 | 347 ms: 1.06x faster                                                             |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.06x faster                                                           |
| spectral_norm              | 113 ms                                                 | 108 ms: 1.05x faster                                                             |
| thrift                     | 800 us                                                 | 763 us: 1.05x faster                                                             |
| generators                 | 28.8 ms                                                | 27.5 ms: 1.05x faster                                                            |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                             |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                           |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.83 ms: 1.04x faster                                                            |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                            |
| xml_etree_generate         | 86.8 ms                                                | 84.0 ms: 1.03x faster                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.54 sec: 1.03x faster                                                           |
| regex_dna                  | 220 ms                                                 | 213 ms: 1.03x faster                                                             |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                             |
| xml_etree_iterparse        | 101 ms                                                 | 98.5 ms: 1.03x faster                                                            |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.03x faster                                                             |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                             |
| deltablue                  | 3.19 ms                                                | 3.12 ms: 1.02x faster                                                            |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                             |
| genshi_xml                 | 50.5 ms                                                | 49.4 ms: 1.02x faster                                                            |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                                           |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                                             |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                             |
| shortest_path              | 487 ms                                                 | 477 ms: 1.02x faster                                                             |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                           |
| json                       | 5.32 ms                                                | 5.23 ms: 1.02x faster                                                            |
| crypto_pyaes               | 74.7 ms                                                | 73.3 ms: 1.02x faster                                                            |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                             |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                            |
| pyflate                    | 470 ms                                                 | 462 ms: 1.02x faster                                                             |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                            |
| nqueens                    | 80.9 ms                                                | 80.0 ms: 1.01x faster                                                            |
| gc_traversal               | 4.90 ms                                                | 4.86 ms: 1.01x faster                                                            |
| sympy_expand               | 456 ms                                                 | 454 ms: 1.01x faster                                                             |
| pprint_safe_repr           | 727 ms                                                 | 723 ms: 1.01x faster                                                             |
| scimark_sor                | 122 ms                                                 | 122 ms: 1.00x faster                                                             |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                             |
| sqlglot_optimize           | 53.4 ms                                                | 53.2 ms: 1.00x faster                                                            |
| python_startup_no_site     | 7.00 ms                                                | 7.00 ms: 1.00x faster                                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 67.1 ms: 1.00x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                           |
| logging_simple             | 5.65 us                                                | 5.69 us: 1.01x slower                                                            |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                           |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                            |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                            |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                                             |
| logging_format             | 6.23 us                                                | 6.31 us: 1.01x slower                                                            |
| xml_etree_process          | 60.5 ms                                                | 61.5 ms: 1.02x slower                                                            |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                            |
| logging_silent             | 101 ns                                                 | 104 ns: 1.03x slower                                                             |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.03x slower                                                             |
| chaos                      | 58.0 ms                                                | 60.0 ms: 1.03x slower                                                            |
| fannkuch                   | 394 ms                                                 | 409 ms: 1.04x slower                                                             |
| hexiom                     | 6.08 ms                                                | 6.35 ms: 1.04x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                             |
| bench_thread_pool          | 818 us                                                 | 861 us: 1.05x slower                                                             |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                            |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                            |
| nbody                      | 87.7 ms                                                | 93.6 ms: 1.07x slower                                                            |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                             |
| unpickle_pure_python       | 213 us                                                 | 228 us: 1.07x slower                                                             |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.09x slower                                                            |
| coverage                   | 82.8 ms                                                | 91.3 ms: 1.10x slower                                                            |
| many_optionals             | 857 us                                                 | 952 us: 1.11x slower                                                             |
| json_dumps                 | 10.1 ms                                                | 12.1 ms: 1.19x slower                                                            |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (5): sqlglot_parse, sympy_integrate, dulwich_log, sqlglot_transpile, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x