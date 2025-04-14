# Results vs. 3.13.0

- fork: kumaraditya303
- ref: fast_asyncio
- machine: linux-x86_64
- commit hash: f7b3d94
- commit date: 2025-03-13
- overall geometric mean: 1.539x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 2.10x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 607 ms: 2.28x slower                                                   |
| docutils       | 2.58 sec                                               | 5.62 sec: 2.17x slower                                                 |
| html5lib       | 63.4 ms                                                | 138 ms: 2.17x slower                                                   |
| sphinx         | 1.03 sec                                               | 2.23 sec: 2.16x slower                                                 |
| Geometric mean | (ref)                                                  | 2.20x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 1.04 sec: 1.21x slower                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 615 ms: 1.33x slower                                                   |
| async_tree_io              | 838 ms                                                 | 1.14 sec: 1.36x slower                                                 |
| async_tree_none_tg         | 319 ms                                                 | 458 ms: 1.44x slower                                                   |
| async_tree_none            | 350 ms                                                 | 547 ms: 1.56x slower                                                   |
| async_tree_memoization     | 437 ms                                                 | 693 ms: 1.59x slower                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 925 ms: 1.70x slower                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 1.01 sec: 1.77x slower                                                 |
| async_generators           | 433 ms                                                 | 862 ms: 1.99x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 1.11 sec: 2.02x slower                                                 |
| coroutines                 | 22.2 ms                                                | 46.2 ms: 2.08x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.62x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 153 ms: 1.95x slower                                                   |
| pidigits       | 186 ms                                                 | 379 ms: 2.03x slower                                                   |
| nbody          | 87.7 ms                                                | 277 ms: 3.16x slower                                                   |
| Geometric mean | (ref)                                                  | 2.32x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 45.1 ms: 1.68x slower                                                  |
| regex_effbot   | 3.77 ms                                                | 6.75 ms: 1.79x slower                                                  |
| regex_dna      | 220 ms                                                 | 432 ms: 1.97x slower                                                   |
| regex_compile  | 132 ms                                                 | 297 ms: 2.25x slower                                                   |
| Geometric mean | (ref)                                                  | 1.91x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 185 ms: 1.83x slower                                                   |
| xml_etree_parse      | 154 ms                                                 | 298 ms: 1.93x slower                                                   |
| tomli_loads          | 2.12 sec                                               | 4.64 sec: 2.19x slower                                                 |
| xml_etree_generate   | 86.8 ms                                                | 197 ms: 2.27x slower                                                   |
| xml_etree_process    | 60.5 ms                                                | 138 ms: 2.28x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 698 us: 2.31x slower                                                   |
| unpickle_pure_python | 213 us                                                 | 503 us: 2.36x slower                                                   |
| json_loads           | 27.2 us                                                | 65.4 us: 2.41x slower                                                  |
| json_dumps           | 10.1 ms                                                | 25.6 ms: 2.53x slower                                                  |
| Geometric mean       | (ref)                                                  | 2.22x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 32.6 ms: 2.58x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 30.9 ms: 4.41x slower                                                  |
| Geometric mean         | (ref)                                                  | 3.37x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 123 ms: 2.43x slower                                                   |
| genshi_text     | 22.6 ms                                                | 56.6 ms: 2.50x slower                                                  |
| django_template | 31.7 ms                                                | 80.4 ms: 2.54x slower                                                  |
| mako            | 10.7 ms                                                | 32.3 ms: 3.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 2.61x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 4.55 ms: 1.08x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 1.04 sec: 1.21x slower                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 615 ms: 1.33x slower                                                   |
| async_tree_io              | 838 ms                                                 | 1.14 sec: 1.36x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 3.47 ms: 1.42x slower                                                  |
| async_tree_none_tg         | 319 ms                                                 | 458 ms: 1.44x slower                                                   |
| async_tree_none            | 350 ms                                                 | 547 ms: 1.56x slower                                                   |
| async_tree_memoization     | 437 ms                                                 | 693 ms: 1.59x slower                                                   |
| regex_v8                   | 26.9 ms                                                | 45.1 ms: 1.68x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 925 ms: 1.70x slower                                                   |
| deepcopy                   | 354 us                                                 | 615 us: 1.74x slower                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 1.01 sec: 1.77x slower                                                 |
| regex_effbot               | 3.77 ms                                                | 6.75 ms: 1.79x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 185 ms: 1.83x slower                                                   |
| pycparser                  | 1.20 sec                                               | 2.27 sec: 1.89x slower                                                 |
| sqlite_synth               | 2.90 us                                                | 5.49 us: 1.89x slower                                                  |
| xml_etree_parse            | 154 ms                                                 | 298 ms: 1.93x slower                                                   |
| dulwich_log                | 64.6 ms                                                | 126 ms: 1.94x slower                                                   |
| float                      | 78.7 ms                                                | 153 ms: 1.95x slower                                                   |
| regex_dna                  | 220 ms                                                 | 432 ms: 1.97x slower                                                   |
| spectral_norm              | 113 ms                                                 | 224 ms: 1.98x slower                                                   |
| pylint                     | 312 ms                                                 | 619 ms: 1.98x slower                                                   |
| async_generators           | 433 ms                                                 | 862 ms: 1.99x slower                                                   |
| pathlib                    | 17.4 ms                                                | 34.9 ms: 2.01x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 1.11 sec: 2.02x slower                                                 |
| go                         | 141 ms                                                 | 284 ms: 2.02x slower                                                   |
| deepcopy_reduce            | 3.24 us                                                | 6.58 us: 2.03x slower                                                  |
| pidigits                   | 186 ms                                                 | 379 ms: 2.03x slower                                                   |
| k_core                     | 2.37 sec                                               | 4.90 sec: 2.07x slower                                                 |
| deepcopy_memo              | 38.4 us                                                | 79.7 us: 2.07x slower                                                  |
| coroutines                 | 22.2 ms                                                | 46.2 ms: 2.08x slower                                                  |
| generators                 | 28.8 ms                                                | 60.3 ms: 2.10x slower                                                  |
| json                       | 5.32 ms                                                | 11.4 ms: 2.14x slower                                                  |
| mdp                        | 2.54 sec                                               | 5.49 sec: 2.16x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 10.1 sec: 2.16x slower                                                 |
| sphinx                     | 1.03 sec                                               | 2.23 sec: 2.16x slower                                                 |
| docutils                   | 2.58 sec                                               | 5.62 sec: 2.17x slower                                                 |
| html5lib                   | 63.4 ms                                                | 138 ms: 2.17x slower                                                   |
| tomli_loads                | 2.12 sec                                               | 4.64 sec: 2.19x slower                                                 |
| logging_silent             | 101 ns                                                 | 222 ns: 2.20x slower                                                   |
| thrift                     | 800 us                                                 | 1.78 ms: 2.23x slower                                                  |
| pyflate                    | 470 ms                                                 | 1.05 sec: 2.24x slower                                                 |
| richards                   | 47.5 ms                                                | 107 ms: 2.25x slower                                                   |
| regex_compile              | 132 ms                                                 | 297 ms: 2.25x slower                                                   |
| telco                      | 8.40 ms                                                | 19.0 ms: 2.27x slower                                                  |
| xml_etree_generate         | 86.8 ms                                                | 197 ms: 2.27x slower                                                   |
| scimark_sor                | 122 ms                                                 | 278 ms: 2.28x slower                                                   |
| xml_etree_process          | 60.5 ms                                                | 138 ms: 2.28x slower                                                   |
| 2to3                       | 266 ms                                                 | 607 ms: 2.28x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 698 us: 2.31x slower                                                   |
| logging_simple             | 5.65 us                                                | 13.1 us: 2.32x slower                                                  |
| scimark_fft                | 367 ms                                                 | 854 ms: 2.33x slower                                                   |
| pprint_safe_repr           | 727 ms                                                 | 1.69 sec: 2.33x slower                                                 |
| sympy_str                  | 273 ms                                                 | 637 ms: 2.33x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 352 ms: 2.34x slower                                                   |
| sympy_expand               | 456 ms                                                 | 1.07 sec: 2.34x slower                                                 |
| logging_format             | 6.23 us                                                | 14.7 us: 2.36x slower                                                  |
| richards_super             | 53.7 ms                                                | 127 ms: 2.36x slower                                                   |
| unpickle_pure_python       | 213 us                                                 | 503 us: 2.36x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 3.50 sec: 2.37x slower                                                 |
| sympy_integrate            | 19.8 ms                                                | 47.1 ms: 2.37x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 179 ms: 2.40x slower                                                   |
| json_loads                 | 27.2 us                                                | 65.4 us: 2.41x slower                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 320 ms: 2.41x slower                                                   |
| comprehensions             | 16.5 us                                                | 39.7 us: 2.41x slower                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 40.8 ms: 2.41x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 123 ms: 2.43x slower                                                   |
| nqueens                    | 80.9 ms                                                | 196 ms: 2.43x slower                                                   |
| shortest_path              | 487 ms                                                 | 1.18 sec: 2.43x slower                                                 |
| meteor_contest             | 108 ms                                                 | 267 ms: 2.46x slower                                                   |
| deltablue                  | 3.19 ms                                                | 7.88 ms: 2.47x slower                                                  |
| chaos                      | 58.0 ms                                                | 144 ms: 2.48x slower                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 12.5 ms: 2.49x slower                                                  |
| genshi_text                | 22.6 ms                                                | 56.6 ms: 2.50x slower                                                  |
| connected_components       | 447 ms                                                 | 1.12 sec: 2.51x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 288 ms: 2.52x slower                                                   |
| hexiom                     | 6.08 ms                                                | 15.3 ms: 2.52x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 25.6 ms: 2.53x slower                                                  |
| many_optionals             | 857 us                                                 | 2.17 ms: 2.53x slower                                                  |
| django_template            | 31.7 ms                                                | 80.4 ms: 2.54x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 408 us: 2.55x slower                                                   |
| raytrace                   | 262 ms                                                 | 667 ms: 2.55x slower                                                   |
| python_startup             | 12.7 ms                                                | 32.6 ms: 2.58x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 174 ms: 2.61x slower                                                   |
| coverage                   | 82.8 ms                                                | 218 ms: 2.63x slower                                                   |
| fannkuch                   | 394 ms                                                 | 1.05 sec: 2.66x slower                                                 |
| mako                       | 10.7 ms                                                | 32.3 ms: 3.02x slower                                                  |
| subparsers                 | 15.5 ms                                                | 48.6 ms: 3.15x slower                                                  |
| nbody                      | 87.7 ms                                                | 277 ms: 3.16x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 30.9 ms: 4.41x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 142 ms: 5.92x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 36.5 ms: 44.63x slower                                                 |
| Geometric mean             | (ref)                                                  | 2.27x slower                                                           |
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250313-3.14.0a5+-f7b3d94-NOGIL/bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.539x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 2.16x
- 95% likely to have a slowdown of 2.14x
- 99% likely to have a slowdown of 2.10x

# Memory
- memory change: 1.22x