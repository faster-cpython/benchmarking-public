# Results vs. 3.13.0

- fork: kumaraditya303
- ref: per_thread_cur_task
- machine: linux-x86_64
- commit hash: ba92dfb
- commit date: 2025-02-10
- overall geometric mean: 1.044x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.03x faster                                                          |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                        |
| html5lib       | 63.4 ms                                                | 62.1 ms: 1.02x faster                                                         |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                          |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                          |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 486 ms: 1.12x faster                                                          |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                                          |
| coroutines                 | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.8 ms: 1.11x faster                                                         |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                          |
| nbody          | 87.7 ms                                                | 94.5 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.23 ms: 1.17x faster                                                         |
| regex_v8       | 26.9 ms                                                | 24.1 ms: 1.11x faster                                                         |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                          |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                        |
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                          |
| xml_etree_generate   | 86.8 ms                                                | 78.5 ms: 1.11x faster                                                         |
| xml_etree_process    | 60.5 ms                                                | 55.1 ms: 1.10x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 198 us: 1.08x faster                                                          |
| xml_etree_iterparse  | 101 ms                                                 | 96.0 ms: 1.05x faster                                                         |
| pickle_pure_python   | 302 us                                                 | 315 us: 1.04x slower                                                          |
| json_loads           | 27.2 us                                                | 29.0 us: 1.07x slower                                                         |
| json_dumps           | 10.1 ms                                                | 12.0 ms: 1.19x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                         |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.2 ms: 1.05x faster                                                         |
| genshi_text     | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                         |
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                         |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                          |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                          |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                          |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 30.7 us: 1.25x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                          |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                         |
| spectral_norm              | 113 ms                                                 | 95.7 ms: 1.18x faster                                                         |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.23 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                                          |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.48 ms: 1.12x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 486 ms: 1.12x faster                                                          |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                          |
| regex_v8                   | 26.9 ms                                                | 24.1 ms: 1.11x faster                                                         |
| float                      | 78.7 ms                                                | 70.8 ms: 1.11x faster                                                         |
| telco                      | 8.40 ms                                                | 7.59 ms: 1.11x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 78.5 ms: 1.11x faster                                                         |
| xml_etree_process          | 60.5 ms                                                | 55.1 ms: 1.10x faster                                                         |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                          |
| richards                   | 47.5 ms                                                | 44.1 ms: 1.08x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 198 us: 1.08x faster                                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                                        |
| richards_super             | 53.7 ms                                                | 50.3 ms: 1.07x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 70.0 ms: 1.07x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.74 us: 1.06x faster                                                         |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                          |
| xml_etree_iterparse        | 101 ms                                                 | 96.0 ms: 1.05x faster                                                         |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                                         |
| pyflate                    | 470 ms                                                 | 446 ms: 1.05x faster                                                          |
| mako                       | 10.7 ms                                                | 10.2 ms: 1.05x faster                                                         |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                                          |
| thrift                     | 800 us                                                 | 768 us: 1.04x faster                                                          |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                          |
| gc_traversal               | 4.90 ms                                                | 4.72 ms: 1.04x faster                                                         |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                         |
| 2to3                       | 266 ms                                                 | 257 ms: 1.03x faster                                                          |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                          |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                        |
| logging_simple             | 5.65 us                                                | 5.51 us: 1.03x faster                                                         |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.02x faster                                                          |
| logging_format             | 6.23 us                                                | 6.10 us: 1.02x faster                                                         |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                        |
| html5lib                   | 63.4 ms                                                | 62.1 ms: 1.02x faster                                                         |
| json                       | 5.32 ms                                                | 5.22 ms: 1.02x faster                                                         |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                          |
| generators                 | 28.8 ms                                                | 28.4 ms: 1.01x faster                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                         |
| connected_components       | 447 ms                                                 | 443 ms: 1.01x faster                                                          |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                          |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                          |
| sqlglot_optimize           | 53.4 ms                                                | 53.5 ms: 1.00x slower                                                         |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.00x slower                                                          |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.01x slower                                                         |
| chaos                      | 58.0 ms                                                | 58.4 ms: 1.01x slower                                                         |
| fannkuch                   | 394 ms                                                 | 397 ms: 1.01x slower                                                          |
| sympy_str                  | 273 ms                                                 | 275 ms: 1.01x slower                                                          |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                          |
| python_startup_no_site     | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                         |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.01x slower                                                         |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                         |
| coroutines                 | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                         |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                         |
| dulwich_log                | 64.6 ms                                                | 66.0 ms: 1.02x slower                                                         |
| sympy_expand               | 456 ms                                                 | 468 ms: 1.03x slower                                                          |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 749 ms: 1.03x slower                                                          |
| pickle_pure_python         | 302 us                                                 | 315 us: 1.04x slower                                                          |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.54 sec: 1.04x slower                                                        |
| logging_silent             | 101 ns                                                 | 106 ns: 1.05x slower                                                          |
| raytrace                   | 262 ms                                                 | 276 ms: 1.06x slower                                                          |
| deltablue                  | 3.19 ms                                                | 3.38 ms: 1.06x slower                                                         |
| json_loads                 | 27.2 us                                                | 29.0 us: 1.07x slower                                                         |
| nbody                      | 87.7 ms                                                | 94.5 ms: 1.08x slower                                                         |
| coverage                   | 82.8 ms                                                | 89.5 ms: 1.08x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 885 us: 1.08x slower                                                          |
| nqueens                    | 80.9 ms                                                | 88.2 ms: 1.09x slower                                                         |
| many_optionals             | 857 us                                                 | 957 us: 1.12x slower                                                          |
| hexiom                     | 6.08 ms                                                | 6.86 ms: 1.13x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 12.0 ms: 1.19x slower                                                         |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                  |

Benchmark hidden because not significant (5): scimark_monte_carlo, shortest_path, scimark_lu, asyncio_websockets, mdp
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x