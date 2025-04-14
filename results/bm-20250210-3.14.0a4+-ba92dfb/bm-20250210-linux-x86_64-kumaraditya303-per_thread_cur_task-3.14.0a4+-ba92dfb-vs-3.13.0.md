# Results vs. 3.13.0

- fork: kumaraditya303
- ref: per_thread_cur_task
- machine: linux-x86_64
- commit hash: ba92dfb
- commit date: 2025-02-10
- overall geometric mean: 1.053x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.06x faster                                                          |
| docutils       | 2.58 sec                                               | 2.58 sec: 1.00x faster                                                        |
| html5lib       | 63.4 ms                                                | 61.4 ms: 1.03x faster                                                         |
| sphinx         | 1.03 sec                                               | 996 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                                          |
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 318 ms: 1.37x faster                                                          |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                          |
| async_generators           | 433 ms                                                 | 377 ms: 1.15x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                          |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.0 ms: 1.14x faster                                                         |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                          |
| nbody          | 87.7 ms                                                | 94.3 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.24 ms: 1.16x faster                                                         |
| regex_v8       | 26.9 ms                                                | 24.3 ms: 1.11x faster                                                         |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                          |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                          |
| tomli_loads          | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 96.5 ms: 1.05x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 83.6 ms: 1.04x faster                                                         |
| xml_etree_process    | 60.5 ms                                                | 58.6 ms: 1.03x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                          |
| json_loads           | 27.2 us                                                | 28.7 us: 1.06x slower                                                         |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                          |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                         |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                         |
| genshi_xml      | 50.5 ms                                                | 47.8 ms: 1.06x faster                                                         |
| mako            | 10.7 ms                                                | 10.6 ms: 1.01x faster                                                         |
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                                          |
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 318 ms: 1.37x faster                                                          |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                          |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 30.9 us: 1.24x faster                                                         |
| go                         | 141 ms                                                 | 116 ms: 1.21x faster                                                          |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                          |
| spectral_norm              | 113 ms                                                 | 97.1 ms: 1.17x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.24 ms: 1.16x faster                                                         |
| pylint                     | 312 ms                                                 | 271 ms: 1.15x faster                                                          |
| async_generators           | 433 ms                                                 | 377 ms: 1.15x faster                                                          |
| float                      | 78.7 ms                                                | 69.0 ms: 1.14x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                          |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                          |
| regex_v8                   | 26.9 ms                                                | 24.3 ms: 1.11x faster                                                         |
| telco                      | 8.40 ms                                                | 7.76 ms: 1.08x faster                                                         |
| richards                   | 47.5 ms                                                | 44.0 ms: 1.08x faster                                                         |
| scimark_fft                | 367 ms                                                 | 341 ms: 1.08x faster                                                          |
| tomli_loads                | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                        |
| richards_super             | 53.7 ms                                                | 50.2 ms: 1.07x faster                                                         |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.07x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 70.1 ms: 1.07x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                        |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                         |
| pyflate                    | 470 ms                                                 | 443 ms: 1.06x faster                                                          |
| genshi_xml                 | 50.5 ms                                                | 47.8 ms: 1.06x faster                                                         |
| 2to3                       | 266 ms                                                 | 252 ms: 1.06x faster                                                          |
| xml_etree_iterparse        | 101 ms                                                 | 96.5 ms: 1.05x faster                                                         |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                          |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                          |
| generators                 | 28.8 ms                                                | 27.5 ms: 1.05x faster                                                         |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.04x faster                                                          |
| logging_simple             | 5.65 us                                                | 5.42 us: 1.04x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                        |
| meteor_contest             | 108 ms                                                 | 104 ms: 1.04x faster                                                          |
| logging_format             | 6.23 us                                                | 5.99 us: 1.04x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 83.6 ms: 1.04x faster                                                         |
| sphinx                     | 1.03 sec                                               | 996 ms: 1.04x faster                                                          |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.3 ms: 1.04x faster                                                         |
| json                       | 5.32 ms                                                | 5.14 ms: 1.04x faster                                                         |
| sympy_str                  | 273 ms                                                 | 264 ms: 1.03x faster                                                          |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.87 ms: 1.03x faster                                                         |
| html5lib                   | 63.4 ms                                                | 61.4 ms: 1.03x faster                                                         |
| xml_etree_process          | 60.5 ms                                                | 58.6 ms: 1.03x faster                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 51.7 ms: 1.03x faster                                                         |
| thrift                     | 800 us                                                 | 779 us: 1.03x faster                                                          |
| gc_traversal               | 4.90 ms                                                | 4.78 ms: 1.02x faster                                                         |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.02x faster                                                        |
| connected_components       | 447 ms                                                 | 436 ms: 1.02x faster                                                          |
| sqlglot_parse              | 1.26 ms                                                | 1.24 ms: 1.02x faster                                                         |
| nqueens                    | 80.9 ms                                                | 79.4 ms: 1.02x faster                                                         |
| shortest_path              | 487 ms                                                 | 478 ms: 1.02x faster                                                          |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                                         |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                          |
| sympy_expand               | 456 ms                                                 | 449 ms: 1.02x faster                                                          |
| sqlglot_transpile          | 1.57 ms                                                | 1.55 ms: 1.01x faster                                                         |
| deltablue                  | 3.19 ms                                                | 3.15 ms: 1.01x faster                                                         |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                         |
| typing_runtime_protocols   | 160 us                                                 | 159 us: 1.01x faster                                                          |
| mako                       | 10.7 ms                                                | 10.6 ms: 1.01x faster                                                         |
| dulwich_log                | 64.6 ms                                                | 64.2 ms: 1.01x faster                                                         |
| docutils                   | 2.58 sec                                               | 2.58 sec: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                          |
| python_startup_no_site     | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                                         |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                         |
| chaos                      | 58.0 ms                                                | 58.6 ms: 1.01x slower                                                         |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 67.7 ms: 1.01x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                          |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                          |
| hexiom                     | 6.08 ms                                                | 6.24 ms: 1.03x slower                                                         |
| fannkuch                   | 394 ms                                                 | 407 ms: 1.03x slower                                                          |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                         |
| logging_silent             | 101 ns                                                 | 105 ns: 1.04x slower                                                          |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                          |
| bench_thread_pool          | 818 us                                                 | 860 us: 1.05x slower                                                          |
| json_loads                 | 27.2 us                                                | 28.7 us: 1.06x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                          |
| nbody                      | 87.7 ms                                                | 94.3 ms: 1.08x slower                                                         |
| many_optionals             | 857 us                                                 | 929 us: 1.08x slower                                                          |
| coverage                   | 82.8 ms                                                | 91.6 ms: 1.11x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                         |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.32x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                  |

Benchmark hidden because not significant (4): pprint_safe_repr, scimark_sor, pprint_pformat, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x