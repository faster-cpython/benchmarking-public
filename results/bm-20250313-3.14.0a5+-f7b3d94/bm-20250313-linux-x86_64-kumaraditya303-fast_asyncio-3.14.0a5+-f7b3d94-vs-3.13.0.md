# Results vs. 3.13.0

- fork: kumaraditya303
- ref: fast_asyncio
- machine: linux-x86_64
- commit hash: f7b3d94
- commit date: 2025-03-13
- overall geometric mean: 1.488x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.93x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 522 ms: 1.96x slower                                                   |
| docutils       | 2.58 sec                                               | 5.25 sec: 2.03x slower                                                 |
| html5lib       | 63.4 ms                                                | 123 ms: 1.95x slower                                                   |
| sphinx         | 1.03 sec                                               | 2.03 sec: 1.96x slower                                                 |
| Geometric mean | (ref)                                                  | 1.98x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 637 ms: 1.38x slower                                                   |
| async_tree_io_tg           | 861 ms                                                 | 1.22 sec: 1.42x slower                                                 |
| async_tree_io              | 838 ms                                                 | 1.21 sec: 1.45x slower                                                 |
| async_tree_none            | 350 ms                                                 | 515 ms: 1.47x slower                                                   |
| async_tree_memoization     | 437 ms                                                 | 646 ms: 1.48x slower                                                   |
| async_tree_none_tg         | 319 ms                                                 | 498 ms: 1.56x slower                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 1.00 sec: 1.75x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 973 ms: 1.79x slower                                                   |
| async_generators           | 433 ms                                                 | 787 ms: 1.82x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 1.09 sec: 1.97x slower                                                 |
| coroutines                 | 22.2 ms                                                | 47.8 ms: 2.15x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.64x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 144 ms: 1.83x slower                                                   |
| pidigits       | 186 ms                                                 | 372 ms: 2.00x slower                                                   |
| nbody          | 87.7 ms                                                | 203 ms: 2.31x slower                                                   |
| Geometric mean | (ref)                                                  | 2.04x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 46.5 ms: 1.73x slower                                                  |
| regex_effbot   | 3.77 ms                                                | 6.83 ms: 1.81x slower                                                  |
| regex_compile  | 132 ms                                                 | 256 ms: 1.94x slower                                                   |
| regex_dna      | 220 ms                                                 | 427 ms: 1.94x slower                                                   |
| Geometric mean | (ref)                                                  | 1.85x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 3.88 sec: 1.83x slower                                                 |
| xml_etree_parse      | 154 ms                                                 | 287 ms: 1.86x slower                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 189 ms: 1.87x slower                                                   |
| xml_etree_process    | 60.5 ms                                                | 119 ms: 1.97x slower                                                   |
| xml_etree_generate   | 86.8 ms                                                | 171 ms: 1.97x slower                                                   |
| unpickle_pure_python | 213 us                                                 | 444 us: 2.08x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 640 us: 2.12x slower                                                   |
| json_loads           | 27.2 us                                                | 59.5 us: 2.19x slower                                                  |
| json_dumps           | 10.1 ms                                                | 22.8 ms: 2.26x slower                                                  |
| Geometric mean       | (ref)                                                  | 2.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 31.0 ms: 2.45x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 31.4 ms: 4.48x slower                                                  |
| Geometric mean         | (ref)                                                  | 3.32x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 43.8 ms: 1.94x slower                                                  |
| genshi_xml      | 50.5 ms                                                | 98.4 ms: 1.95x slower                                                  |
| django_template | 31.7 ms                                                | 64.3 ms: 2.03x slower                                                  |
| mako            | 10.7 ms                                                | 22.5 ms: 2.11x slower                                                  |
| Geometric mean  | (ref)                                                  | 2.01x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 637 ms: 1.38x slower                                                   |
| async_tree_io_tg           | 861 ms                                                 | 1.22 sec: 1.42x slower                                                 |
| async_tree_io              | 838 ms                                                 | 1.21 sec: 1.45x slower                                                 |
| async_tree_none            | 350 ms                                                 | 515 ms: 1.47x slower                                                   |
| async_tree_memoization     | 437 ms                                                 | 646 ms: 1.48x slower                                                   |
| deepcopy                   | 354 us                                                 | 529 us: 1.49x slower                                                   |
| deepcopy_memo              | 38.4 us                                                | 59.8 us: 1.56x slower                                                  |
| async_tree_none_tg         | 319 ms                                                 | 498 ms: 1.56x slower                                                   |
| deepcopy_reduce            | 3.24 us                                                | 5.40 us: 1.67x slower                                                  |
| go                         | 141 ms                                                 | 235 ms: 1.67x slower                                                   |
| regex_v8                   | 26.9 ms                                                | 46.5 ms: 1.73x slower                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 1.00 sec: 1.75x slower                                                 |
| pylint                     | 312 ms                                                 | 554 ms: 1.78x slower                                                   |
| spectral_norm              | 113 ms                                                 | 202 ms: 1.78x slower                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 973 ms: 1.79x slower                                                   |
| regex_effbot               | 3.77 ms                                                | 6.83 ms: 1.81x slower                                                  |
| async_generators           | 433 ms                                                 | 787 ms: 1.82x slower                                                   |
| dulwich_log                | 64.6 ms                                                | 118 ms: 1.82x slower                                                   |
| float                      | 78.7 ms                                                | 144 ms: 1.83x slower                                                   |
| tomli_loads                | 2.12 sec                                               | 3.88 sec: 1.83x slower                                                 |
| xml_etree_parse            | 154 ms                                                 | 287 ms: 1.86x slower                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 189 ms: 1.87x slower                                                   |
| richards                   | 47.5 ms                                                | 89.1 ms: 1.87x slower                                                  |
| richards_super             | 53.7 ms                                                | 101 ms: 1.88x slower                                                   |
| telco                      | 8.40 ms                                                | 16.0 ms: 1.90x slower                                                  |
| sqlite_synth               | 2.90 us                                                | 5.58 us: 1.92x slower                                                  |
| logging_format             | 6.23 us                                                | 12.0 us: 1.93x slower                                                  |
| logging_simple             | 5.65 us                                                | 10.9 us: 1.93x slower                                                  |
| pathlib                    | 17.4 ms                                                | 33.6 ms: 1.94x slower                                                  |
| genshi_text                | 22.6 ms                                                | 43.8 ms: 1.94x slower                                                  |
| regex_compile              | 132 ms                                                 | 256 ms: 1.94x slower                                                   |
| regex_dna                  | 220 ms                                                 | 427 ms: 1.94x slower                                                   |
| html5lib                   | 63.4 ms                                                | 123 ms: 1.95x slower                                                   |
| genshi_xml                 | 50.5 ms                                                | 98.4 ms: 1.95x slower                                                  |
| pyflate                    | 470 ms                                                 | 916 ms: 1.95x slower                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 33.0 ms: 1.95x slower                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 9.15 sec: 1.95x slower                                                 |
| k_core                     | 2.37 sec                                               | 4.63 sec: 1.95x slower                                                 |
| thrift                     | 800 us                                                 | 1.56 ms: 1.95x slower                                                  |
| scimark_fft                | 367 ms                                                 | 717 ms: 1.95x slower                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 9.84 ms: 1.96x slower                                                  |
| sympy_str                  | 273 ms                                                 | 535 ms: 1.96x slower                                                   |
| mdp                        | 2.54 sec                                               | 4.98 sec: 1.96x slower                                                 |
| pycparser                  | 1.20 sec                                               | 2.35 sec: 1.96x slower                                                 |
| meteor_contest             | 108 ms                                                 | 213 ms: 1.96x slower                                                   |
| 2to3                       | 266 ms                                                 | 522 ms: 1.96x slower                                                   |
| sphinx                     | 1.03 sec                                               | 2.03 sec: 1.96x slower                                                 |
| xml_etree_process          | 60.5 ms                                                | 119 ms: 1.97x slower                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 262 ms: 1.97x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 1.09 sec: 1.97x slower                                                 |
| xml_etree_generate         | 86.8 ms                                                | 171 ms: 1.97x slower                                                   |
| scimark_sor                | 122 ms                                                 | 241 ms: 1.97x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 297 ms: 1.98x slower                                                   |
| sympy_expand               | 456 ms                                                 | 905 ms: 1.98x slower                                                   |
| logging_silent             | 101 ns                                                 | 201 ns: 1.99x slower                                                   |
| json                       | 5.32 ms                                                | 10.6 ms: 1.99x slower                                                  |
| pidigits                   | 186 ms                                                 | 372 ms: 2.00x slower                                                   |
| generators                 | 28.8 ms                                                | 57.6 ms: 2.00x slower                                                  |
| deltablue                  | 3.19 ms                                                | 6.40 ms: 2.00x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 39.9 ms: 2.01x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 323 us: 2.01x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 2.99 sec: 2.02x slower                                                 |
| comprehensions             | 16.5 us                                                | 33.4 us: 2.03x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 1.47 sec: 2.03x slower                                                 |
| docutils                   | 2.58 sec                                               | 5.25 sec: 2.03x slower                                                 |
| django_template            | 31.7 ms                                                | 64.3 ms: 2.03x slower                                                  |
| hexiom                     | 6.08 ms                                                | 12.5 ms: 2.05x slower                                                  |
| nqueens                    | 80.9 ms                                                | 166 ms: 2.05x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 236 ms: 2.07x slower                                                   |
| crypto_pyaes               | 74.7 ms                                                | 154 ms: 2.07x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 5.07 ms: 2.07x slower                                                  |
| raytrace                   | 262 ms                                                 | 542 ms: 2.07x slower                                                   |
| unpickle_pure_python       | 213 us                                                 | 444 us: 2.08x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 139 ms: 2.09x slower                                                   |
| mako                       | 10.7 ms                                                | 22.5 ms: 2.11x slower                                                  |
| shortest_path              | 487 ms                                                 | 1.03 sec: 2.11x slower                                                 |
| chaos                      | 58.0 ms                                                | 123 ms: 2.12x slower                                                   |
| gc_traversal               | 4.90 ms                                                | 10.4 ms: 2.12x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 640 us: 2.12x slower                                                   |
| connected_components       | 447 ms                                                 | 948 ms: 2.12x slower                                                   |
| coroutines                 | 22.2 ms                                                | 47.8 ms: 2.15x slower                                                  |
| fannkuch                   | 394 ms                                                 | 860 ms: 2.18x slower                                                   |
| json_loads                 | 27.2 us                                                | 59.5 us: 2.19x slower                                                  |
| coverage                   | 82.8 ms                                                | 183 ms: 2.21x slower                                                   |
| many_optionals             | 857 us                                                 | 1.90 ms: 2.21x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 22.8 ms: 2.26x slower                                                  |
| nbody                      | 87.7 ms                                                | 203 ms: 2.31x slower                                                   |
| python_startup             | 12.7 ms                                                | 31.0 ms: 2.45x slower                                                  |
| subparsers                 | 15.5 ms                                                | 40.7 ms: 2.63x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 31.4 ms: 4.48x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 130 ms: 5.42x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 29.8 ms: 36.50x slower                                                 |
| Geometric mean             | (ref)                                                  | 2.04x slower                                                           |
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250313-3.14.0a5+-f7b3d94/bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.488x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.94x
- 95% likely to have a slowdown of 1.94x
- 99% likely to have a slowdown of 1.93x

# Memory
- memory change: 1.02x