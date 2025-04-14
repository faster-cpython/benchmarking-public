# Results vs. 3.13.0

- fork: kumaraditya303
- ref: per_thread_cur_task
- machine: linux-x86_64
- commit hash: ba92dfb
- commit date: 2025-02-10
- overall geometric mean: 1.081x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 304 ms: 1.15x slower                                                          |
| docutils       | 2.58 sec                                               | 2.82 sec: 1.09x slower                                                        |
| html5lib       | 63.4 ms                                                | 69.9 ms: 1.10x slower                                                         |
| sphinx         | 1.03 sec                                               | 1.12 sec: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.11x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 546 ms: 1.58x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 320 ms: 1.45x faster                                                          |
| async_tree_io              | 838 ms                                                 | 590 ms: 1.42x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 241 ms: 1.32x faster                                                          |
| async_tree_none            | 350 ms                                                 | 281 ms: 1.25x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 360 ms: 1.21x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 516 ms: 1.11x faster                                                          |
| async_generators           | 433 ms                                                 | 438 ms: 1.01x slower                                                          |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 76.9 ms: 1.02x faster                                                         |
| pidigits       | 186 ms                                                 | 192 ms: 1.03x slower                                                          |
| nbody          | 87.7 ms                                                | 136 ms: 1.55x slower                                                          |
| Geometric mean | (ref)                                                  | 1.16x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.46 ms: 1.09x faster                                                         |
| regex_v8       | 26.9 ms                                                | 25.7 ms: 1.05x faster                                                         |
| regex_dna      | 220 ms                                                 | 227 ms: 1.03x slower                                                          |
| regex_compile  | 132 ms                                                 | 146 ms: 1.11x slower                                                          |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 95.2 ms: 1.06x faster                                                         |
| xml_etree_parse      | 154 ms                                                 | 149 ms: 1.03x faster                                                          |
| tomli_loads          | 2.12 sec                                               | 2.31 sec: 1.09x slower                                                        |
| xml_etree_generate   | 86.8 ms                                                | 94.9 ms: 1.09x slower                                                         |
| xml_etree_process    | 60.5 ms                                                | 67.3 ms: 1.11x slower                                                         |
| unpickle_pure_python | 213 us                                                 | 257 us: 1.21x slower                                                          |
| json_loads           | 27.2 us                                                | 33.0 us: 1.21x slower                                                         |
| pickle_pure_python   | 302 us                                                 | 370 us: 1.22x slower                                                          |
| json_dumps           | 10.1 ms                                                | 12.8 ms: 1.26x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.12x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.0 ms: 1.18x slower                                                         |
| python_startup_no_site | 7.00 ms                                                | 9.31 ms: 1.33x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.25x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 60.2 ms: 1.19x slower                                                         |
| genshi_text     | 22.6 ms                                                | 27.7 ms: 1.23x slower                                                         |
| django_template | 31.7 ms                                                | 40.4 ms: 1.28x slower                                                         |
| mako            | 10.7 ms                                                | 16.3 ms: 1.53x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.30x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 1.98 ms: 2.47x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 546 ms: 1.58x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 320 ms: 1.45x faster                                                          |
| async_tree_io              | 838 ms                                                 | 590 ms: 1.42x faster                                                          |
| create_gc_cycles           | 2.45 ms                                                | 1.74 ms: 1.40x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 241 ms: 1.32x faster                                                          |
| async_tree_none            | 350 ms                                                 | 281 ms: 1.25x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 360 ms: 1.21x faster                                                          |
| deepcopy                   | 354 us                                                 | 305 us: 1.16x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 516 ms: 1.11x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.46 ms: 1.09x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 95.2 ms: 1.06x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 25.7 ms: 1.05x faster                                                         |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 149 ms: 1.03x faster                                                          |
| float                      | 78.7 ms                                                | 76.9 ms: 1.02x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 38.2 us: 1.01x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 3.23 us: 1.00x faster                                                         |
| go                         | 141 ms                                                 | 141 ms: 1.00x slower                                                          |
| spectral_norm              | 113 ms                                                 | 114 ms: 1.01x slower                                                          |
| async_generators           | 433 ms                                                 | 438 ms: 1.01x slower                                                          |
| pidigits                   | 186 ms                                                 | 192 ms: 1.03x slower                                                          |
| regex_dna                  | 220 ms                                                 | 227 ms: 1.03x slower                                                          |
| k_core                     | 2.37 sec                                               | 2.45 sec: 1.04x slower                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.92 sec: 1.05x slower                                                        |
| dulwich_log                | 64.6 ms                                                | 68.5 ms: 1.06x slower                                                         |
| json                       | 5.32 ms                                                | 5.65 ms: 1.06x slower                                                         |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                         |
| pyflate                    | 470 ms                                                 | 506 ms: 1.08x slower                                                          |
| sphinx                     | 1.03 sec                                               | 1.12 sec: 1.08x slower                                                        |
| sqlglot_normalize          | 108 ms                                                 | 117 ms: 1.09x slower                                                          |
| tomli_loads                | 2.12 sec                                               | 2.31 sec: 1.09x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.82 sec: 1.09x slower                                                        |
| xml_etree_generate         | 86.8 ms                                                | 94.9 ms: 1.09x slower                                                         |
| generators                 | 28.8 ms                                                | 31.6 ms: 1.10x slower                                                         |
| html5lib                   | 63.4 ms                                                | 69.9 ms: 1.10x slower                                                         |
| logging_silent             | 101 ns                                                 | 112 ns: 1.11x slower                                                          |
| regex_compile              | 132 ms                                                 | 146 ms: 1.11x slower                                                          |
| xml_etree_process          | 60.5 ms                                                | 67.3 ms: 1.11x slower                                                         |
| telco                      | 8.40 ms                                                | 9.38 ms: 1.12x slower                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 59.8 ms: 1.12x slower                                                         |
| mdp                        | 2.54 sec                                               | 2.85 sec: 1.12x slower                                                        |
| scimark_fft                | 367 ms                                                 | 413 ms: 1.13x slower                                                          |
| scimark_sor                | 122 ms                                                 | 138 ms: 1.13x slower                                                          |
| richards                   | 47.5 ms                                                | 54.0 ms: 1.14x slower                                                         |
| 2to3                       | 266 ms                                                 | 304 ms: 1.15x slower                                                          |
| sympy_str                  | 273 ms                                                 | 315 ms: 1.16x slower                                                          |
| sympy_expand               | 456 ms                                                 | 529 ms: 1.16x slower                                                          |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.17x slower                                                          |
| richards_super             | 53.7 ms                                                | 63.1 ms: 1.17x slower                                                         |
| logging_simple             | 5.65 us                                                | 6.67 us: 1.18x slower                                                         |
| pprint_safe_repr           | 727 ms                                                 | 859 ms: 1.18x slower                                                          |
| python_startup             | 12.7 ms                                                | 15.0 ms: 1.18x slower                                                         |
| thrift                     | 800 us                                                 | 947 us: 1.18x slower                                                          |
| sympy_integrate            | 19.8 ms                                                | 23.5 ms: 1.18x slower                                                         |
| crypto_pyaes               | 74.7 ms                                                | 88.6 ms: 1.19x slower                                                         |
| comprehensions             | 16.5 us                                                | 19.6 us: 1.19x slower                                                         |
| genshi_xml                 | 50.5 ms                                                | 60.2 ms: 1.19x slower                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.76 sec: 1.19x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.88 ms: 1.19x slower                                                         |
| logging_format             | 6.23 us                                                | 7.46 us: 1.20x slower                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 159 ms: 1.20x slower                                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.06 ms: 1.20x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 257 us: 1.21x slower                                                          |
| shortest_path              | 487 ms                                                 | 587 ms: 1.21x slower                                                          |
| json_loads                 | 27.2 us                                                | 33.0 us: 1.21x slower                                                         |
| meteor_contest             | 108 ms                                                 | 132 ms: 1.21x slower                                                          |
| sqlglot_parse              | 1.26 ms                                                | 1.54 ms: 1.22x slower                                                         |
| nqueens                    | 80.9 ms                                                | 98.8 ms: 1.22x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 370 us: 1.22x slower                                                          |
| genshi_text                | 22.6 ms                                                | 27.7 ms: 1.23x slower                                                         |
| scimark_lu                 | 114 ms                                                 | 141 ms: 1.23x slower                                                          |
| connected_components       | 447 ms                                                 | 551 ms: 1.23x slower                                                          |
| sqlalchemy_imperative      | 16.9 ms                                                | 20.9 ms: 1.24x slower                                                         |
| many_optionals             | 857 us                                                 | 1.07 ms: 1.25x slower                                                         |
| chaos                      | 58.0 ms                                                | 73.1 ms: 1.26x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 12.8 ms: 1.26x slower                                                         |
| hexiom                     | 6.08 ms                                                | 7.69 ms: 1.27x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 203 us: 1.27x slower                                                          |
| django_template            | 31.7 ms                                                | 40.4 ms: 1.28x slower                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 85.7 ms: 1.28x slower                                                         |
| coverage                   | 82.8 ms                                                | 106 ms: 1.28x slower                                                          |
| fannkuch                   | 394 ms                                                 | 512 ms: 1.30x slower                                                          |
| python_startup_no_site     | 7.00 ms                                                | 9.31 ms: 1.33x slower                                                         |
| raytrace                   | 262 ms                                                 | 351 ms: 1.34x slower                                                          |
| deltablue                  | 3.19 ms                                                | 4.72 ms: 1.48x slower                                                         |
| mako                       | 10.7 ms                                                | 16.3 ms: 1.53x slower                                                         |
| nbody                      | 87.7 ms                                                | 136 ms: 1.55x slower                                                          |
| subparsers                 | 15.5 ms                                                | 24.3 ms: 1.57x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 88.6 ms: 3.69x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 3.46 ms: 4.23x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.12x slower                                                                  |

Benchmark hidden because not significant (3): pylint, asyncio_websockets, pycparser
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.081x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.22x