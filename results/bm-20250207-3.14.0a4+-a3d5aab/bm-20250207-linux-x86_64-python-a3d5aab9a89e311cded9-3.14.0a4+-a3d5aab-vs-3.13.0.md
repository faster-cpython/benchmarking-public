# Results vs. 3.13.0

- fork: python
- ref: a3d5aab9a89e311cded9
- machine: linux-x86_64
- commit hash: a3d5aab
- commit date: 2025-02-07
- overall geometric mean: 1.050x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                   |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.00x faster                                                 |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                  |
| sphinx         | 1.03 sec                                               | 996 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 320 ms: 1.45x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 259 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                   |
| async_generators           | 433 ms                                                 | 387 ms: 1.12x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.0 ms: 1.12x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| nbody          | 87.7 ms                                                | 95.1 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.24 ms: 1.16x faster                                                  |
| regex_v8       | 26.9 ms                                                | 25.2 ms: 1.07x faster                                                  |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                   |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.07x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 96.2 ms: 1.05x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 83.6 ms: 1.04x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 58.4 ms: 1.04x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                   |
| json_loads           | 27.2 us                                                | 28.4 us: 1.05x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 50.5 ms                                                | 47.4 ms: 1.06x faster                                                  |
| genshi_text    | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                  |
| mako           | 10.7 ms                                                | 11.2 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-python-a3d5aab9a89e311cded9-3.14.0a4+-a3d5aab |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 320 ms: 1.45x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                   |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                   |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 30.8 us: 1.25x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 259 ms: 1.23x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                                  |
| spectral_norm              | 113 ms                                                 | 94.8 ms: 1.19x faster                                                  |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.24 ms: 1.16x faster                                                  |
| pylint                     | 312 ms                                                 | 272 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                   |
| float                      | 78.7 ms                                                | 70.0 ms: 1.12x faster                                                  |
| async_generators           | 433 ms                                                 | 387 ms: 1.12x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                   |
| pathlib                    | 17.4 ms                                                | 15.8 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.64 ms: 1.08x faster                                                  |
| pyflate                    | 470 ms                                                 | 437 ms: 1.08x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.07x faster                                                 |
| scimark_fft                | 367 ms                                                 | 342 ms: 1.07x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 25.2 ms: 1.07x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 70.1 ms: 1.07x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 47.4 ms: 1.06x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                 |
| gc_traversal               | 4.90 ms                                                | 4.61 ms: 1.06x faster                                                  |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                  |
| telco                      | 8.40 ms                                                | 7.95 ms: 1.06x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.05x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 96.2 ms: 1.05x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.46 sec: 1.05x faster                                                 |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                   |
| thrift                     | 800 us                                                 | 762 us: 1.05x faster                                                   |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                   |
| richards                   | 47.5 ms                                                | 45.5 ms: 1.04x faster                                                  |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                 |
| logging_simple             | 5.65 us                                                | 5.42 us: 1.04x faster                                                  |
| logging_format             | 6.23 us                                                | 5.98 us: 1.04x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 83.6 ms: 1.04x faster                                                  |
| richards_super             | 53.7 ms                                                | 51.9 ms: 1.04x faster                                                  |
| sphinx                     | 1.03 sec                                               | 996 ms: 1.04x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 58.4 ms: 1.04x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                   |
| json                       | 5.32 ms                                                | 5.15 ms: 1.03x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                   |
| generators                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                  |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                  |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                                   |
| typing_runtime_protocols   | 160 us                                                 | 156 us: 1.03x faster                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 52.2 ms: 1.02x faster                                                  |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                                 |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                                   |
| shortest_path              | 487 ms                                                 | 477 ms: 1.02x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 63.6 ms: 1.02x faster                                                  |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.01x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                  |
| nqueens                    | 80.9 ms                                                | 79.9 ms: 1.01x faster                                                  |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                                   |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 727 ms                                                 | 721 ms: 1.01x faster                                                   |
| sympy_expand               | 456 ms                                                 | 453 ms: 1.01x faster                                                   |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.01x faster                                                  |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.00x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.57 ms: 1.00x faster                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| chaos                      | 58.0 ms                                                | 58.5 ms: 1.01x slower                                                  |
| fannkuch                   | 394 ms                                                 | 397 ms: 1.01x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 67.6 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.26 ms: 1.03x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.32 ms: 1.04x slower                                                  |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.04x slower                                                  |
| json_loads                 | 27.2 us                                                | 28.4 us: 1.05x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 856 us: 1.05x slower                                                   |
| raytrace                   | 262 ms                                                 | 275 ms: 1.05x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                   |
| many_optionals             | 857 us                                                 | 923 us: 1.08x slower                                                   |
| coverage                   | 82.8 ms                                                | 89.5 ms: 1.08x slower                                                  |
| nbody                      | 87.7 ms                                                | 95.1 ms: 1.08x slower                                                  |
| logging_silent             | 101 ns                                                 | 112 ns: 1.11x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.3 ms: 1.31x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (5): sqlglot_parse, create_gc_cycles, pprint_pformat, django_template, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x