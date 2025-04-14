# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: linux-x86_64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.038x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                                             |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                           |
| html5lib       | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                            |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 632 ms: 1.36x faster                                                             |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 331 ms: 1.32x faster                                                             |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                             |
| async_generators           | 433 ms                                                 | 396 ms: 1.09x faster                                                             |
| coroutines                 | 22.2 ms                                                | 24.1 ms: 1.08x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.0 ms: 1.12x faster                                                            |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                             |
| nbody          | 87.7 ms                                                | 98.1 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.50 ms: 1.08x faster                                                            |
| regex_v8       | 26.9 ms                                                | 25.0 ms: 1.07x faster                                                            |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                             |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.95 sec: 1.08x faster                                                           |
| xml_etree_generate   | 86.8 ms                                                | 83.8 ms: 1.04x faster                                                            |
| xml_etree_parse      | 154 ms                                                 | 150 ms: 1.03x faster                                                             |
| xml_etree_process    | 60.5 ms                                                | 58.7 ms: 1.03x faster                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 100.0 ms: 1.01x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                             |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.05x slower                                                             |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                                            |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.19 ms: 1.03x slower                                                            |
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                            |
| genshi_xml     | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                            |
| mako           | 10.7 ms                                                | 11.8 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                             |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 632 ms: 1.36x faster                                                             |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                             |
| deepcopy_memo              | 38.4 us                                                | 29.0 us: 1.32x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 331 ms: 1.32x faster                                                             |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                             |
| go                         | 141 ms                                                 | 114 ms: 1.24x faster                                                             |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                             |
| spectral_norm              | 113 ms                                                 | 98.8 ms: 1.15x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                             |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                             |
| float                      | 78.7 ms                                                | 70.0 ms: 1.12x faster                                                            |
| richards                   | 47.5 ms                                                | 43.2 ms: 1.10x faster                                                            |
| async_generators           | 433 ms                                                 | 396 ms: 1.09x faster                                                             |
| richards_super             | 53.7 ms                                                | 49.5 ms: 1.09x faster                                                            |
| tomli_loads                | 2.12 sec                                               | 1.95 sec: 1.08x faster                                                           |
| pyflate                    | 470 ms                                                 | 436 ms: 1.08x faster                                                             |
| regex_effbot               | 3.77 ms                                                | 3.50 ms: 1.08x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 25.0 ms: 1.07x faster                                                            |
| telco                      | 8.40 ms                                                | 7.82 ms: 1.07x faster                                                            |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                            |
| logging_silent             | 101 ns                                                 | 95.0 ns: 1.06x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.76 ms: 1.06x faster                                                            |
| scimark_fft                | 367 ms                                                 | 347 ms: 1.06x faster                                                             |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                             |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                             |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                                            |
| thrift                     | 800 us                                                 | 770 us: 1.04x faster                                                             |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                                             |
| xml_etree_generate         | 86.8 ms                                                | 83.8 ms: 1.04x faster                                                            |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                           |
| mdp                        | 2.54 sec                                               | 2.46 sec: 1.03x faster                                                           |
| xml_etree_parse            | 154 ms                                                 | 150 ms: 1.03x faster                                                             |
| xml_etree_process          | 60.5 ms                                                | 58.7 ms: 1.03x faster                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.56 sec: 1.03x faster                                                           |
| html5lib                   | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                            |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                            |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.03x faster                                                             |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                             |
| deltablue                  | 3.19 ms                                                | 3.12 ms: 1.02x faster                                                            |
| logging_simple             | 5.65 us                                                | 5.52 us: 1.02x faster                                                            |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                             |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                                            |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                             |
| logging_format             | 6.23 us                                                | 6.11 us: 1.02x faster                                                            |
| genshi_xml                 | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                            |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.02x faster                                                            |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                           |
| sqlglot_optimize           | 53.4 ms                                                | 52.6 ms: 1.01x faster                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 100.0 ms: 1.01x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                             |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                                           |
| gc_traversal               | 4.90 ms                                                | 4.87 ms: 1.01x faster                                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                            |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                                            |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                             |
| crypto_pyaes               | 74.7 ms                                                | 75.4 ms: 1.01x slower                                                            |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                                            |
| dulwich_log                | 64.6 ms                                                | 65.3 ms: 1.01x slower                                                            |
| hexiom                     | 6.08 ms                                                | 6.15 ms: 1.01x slower                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 67.8 ms: 1.01x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                             |
| regex_dna                  | 220 ms                                                 | 224 ms: 1.02x slower                                                             |
| connected_components       | 447 ms                                                 | 455 ms: 1.02x slower                                                             |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                             |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                             |
| python_startup_no_site     | 7.00 ms                                                | 7.19 ms: 1.03x slower                                                            |
| chaos                      | 58.0 ms                                                | 59.7 ms: 1.03x slower                                                            |
| raytrace                   | 262 ms                                                 | 269 ms: 1.03x slower                                                             |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                            |
| nqueens                    | 80.9 ms                                                | 83.8 ms: 1.04x slower                                                            |
| fannkuch                   | 394 ms                                                 | 412 ms: 1.05x slower                                                             |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.05x slower                                                             |
| bench_thread_pool          | 818 us                                                 | 871 us: 1.07x slower                                                             |
| coroutines                 | 22.2 ms                                                | 24.1 ms: 1.08x slower                                                            |
| many_optionals             | 857 us                                                 | 930 us: 1.09x slower                                                             |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                                            |
| mako                       | 10.7 ms                                                | 11.8 ms: 1.10x slower                                                            |
| coverage                   | 82.8 ms                                                | 92.5 ms: 1.12x slower                                                            |
| nbody                      | 87.7 ms                                                | 98.1 ms: 1.12x slower                                                            |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                            |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 82.2 ms: 3.43x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (8): pycparser, sympy_integrate, asyncio_websockets, sympy_expand, pprint_safe_repr, shortest_path, django_template, json
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x