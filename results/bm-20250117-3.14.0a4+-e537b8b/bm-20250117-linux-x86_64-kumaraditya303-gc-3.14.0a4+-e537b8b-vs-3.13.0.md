# Results vs. 3.13.0

- fork: kumaraditya303
- ref: gc
- machine: linux-x86_64
- commit hash: e537b8b
- commit date: 2025-01-17
- overall geometric mean: 1.050x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 253 ms: 1.05x faster                                         |
| html5lib       | 63.4 ms                                                | 59.8 ms: 1.06x faster                                        |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 305 ms: 1.52x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 584 ms: 1.47x faster                                         |
| async_tree_io              | 838 ms                                                 | 604 ms: 1.39x faster                                         |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 244 ms: 1.31x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 458 ms: 1.19x faster                                         |
| async_generators           | 433 ms                                                 | 382 ms: 1.14x faster                                         |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                        |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.3 ms: 1.12x faster                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| nbody          | 87.7 ms                                                | 94.3 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.29 ms: 1.15x faster                                        |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                         |
| regex_dna      | 220 ms                                                 | 211 ms: 1.04x faster                                         |
| regex_v8       | 26.9 ms                                                | 26.1 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                         |
| tomli_loads          | 2.12 sec                                               | 1.94 sec: 1.09x faster                                       |
| xml_etree_iterparse  | 101 ms                                                 | 97.7 ms: 1.04x faster                                        |
| xml_etree_generate   | 86.8 ms                                                | 84.5 ms: 1.03x faster                                        |
| xml_etree_process    | 60.5 ms                                                | 59.1 ms: 1.02x faster                                        |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                         |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                         |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                        |
| json_dumps           | 10.1 ms                                                | 12.0 ms: 1.19x slower                                        |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.05 ms: 1.01x slower                                        |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                        |
| genshi_xml      | 50.5 ms                                                | 48.7 ms: 1.04x faster                                        |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                        |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                        |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 305 ms: 1.52x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 584 ms: 1.47x faster                                         |
| async_tree_io              | 838 ms                                                 | 604 ms: 1.39x faster                                         |
| deepcopy                   | 354 us                                                 | 256 us: 1.39x faster                                         |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 244 ms: 1.31x faster                                         |
| deepcopy_memo              | 38.4 us                                                | 30.4 us: 1.26x faster                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.60 us: 1.25x faster                                        |
| spectral_norm              | 113 ms                                                 | 93.5 ms: 1.21x faster                                        |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 458 ms: 1.19x faster                                         |
| regex_effbot               | 3.77 ms                                                | 3.29 ms: 1.15x faster                                        |
| pylint                     | 312 ms                                                 | 274 ms: 1.14x faster                                         |
| async_generators           | 433 ms                                                 | 382 ms: 1.14x faster                                         |
| float                      | 78.7 ms                                                | 70.3 ms: 1.12x faster                                        |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                         |
| richards                   | 47.5 ms                                                | 43.4 ms: 1.10x faster                                        |
| tomli_loads                | 2.12 sec                                               | 1.94 sec: 1.09x faster                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.63 ms: 1.09x faster                                        |
| telco                      | 8.40 ms                                                | 7.77 ms: 1.08x faster                                        |
| pathlib                    | 17.4 ms                                                | 16.1 ms: 1.08x faster                                        |
| richards_super             | 53.7 ms                                                | 49.9 ms: 1.08x faster                                        |
| scimark_fft                | 367 ms                                                 | 343 ms: 1.07x faster                                         |
| html5lib                   | 63.4 ms                                                | 59.8 ms: 1.06x faster                                        |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                        |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                         |
| thrift                     | 800 us                                                 | 761 us: 1.05x faster                                         |
| k_core                     | 2.37 sec                                               | 2.26 sec: 1.05x faster                                       |
| 2to3                       | 266 ms                                                 | 253 ms: 1.05x faster                                         |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                        |
| logging_simple             | 5.65 us                                                | 5.41 us: 1.05x faster                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.05x faster                                       |
| regex_dna                  | 220 ms                                                 | 211 ms: 1.04x faster                                         |
| crypto_pyaes               | 74.7 ms                                                | 71.7 ms: 1.04x faster                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.2 ms: 1.04x faster                                        |
| logging_format             | 6.23 us                                                | 6.01 us: 1.04x faster                                        |
| sympy_str                  | 273 ms                                                 | 263 ms: 1.04x faster                                         |
| xml_etree_iterparse        | 101 ms                                                 | 97.7 ms: 1.04x faster                                        |
| genshi_xml                 | 50.5 ms                                                | 48.7 ms: 1.04x faster                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.03x faster                                         |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                       |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                         |
| regex_v8                   | 26.9 ms                                                | 26.1 ms: 1.03x faster                                        |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.03x faster                                         |
| generators                 | 28.8 ms                                                | 28.0 ms: 1.03x faster                                        |
| mdp                        | 2.54 sec                                               | 2.47 sec: 1.03x faster                                       |
| xml_etree_generate         | 86.8 ms                                                | 84.5 ms: 1.03x faster                                        |
| gc_traversal               | 4.90 ms                                                | 4.78 ms: 1.03x faster                                        |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                       |
| sympy_expand               | 456 ms                                                 | 446 ms: 1.02x faster                                         |
| xml_etree_process          | 60.5 ms                                                | 59.1 ms: 1.02x faster                                        |
| sqlglot_optimize           | 53.4 ms                                                | 52.4 ms: 1.02x faster                                        |
| nqueens                    | 80.9 ms                                                | 79.8 ms: 1.01x faster                                        |
| dulwich_log                | 64.6 ms                                                | 63.8 ms: 1.01x faster                                        |
| json                       | 5.32 ms                                                | 5.26 ms: 1.01x faster                                        |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                         |
| pprint_safe_repr           | 727 ms                                                 | 719 ms: 1.01x faster                                         |
| sqlglot_parse              | 1.26 ms                                                | 1.25 ms: 1.01x faster                                        |
| sympy_integrate            | 19.8 ms                                                | 19.7 ms: 1.01x faster                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.56 ms: 1.01x faster                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.05 ms: 1.01x slower                                        |
| deltablue                  | 3.19 ms                                                | 3.22 ms: 1.01x slower                                        |
| pyflate                    | 470 ms                                                 | 474 ms: 1.01x slower                                         |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                         |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 68.1 ms: 1.02x slower                                        |
| fannkuch                   | 394 ms                                                 | 401 ms: 1.02x slower                                         |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                         |
| hexiom                     | 6.08 ms                                                | 6.24 ms: 1.03x slower                                        |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                        |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                        |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                         |
| logging_silent             | 101 ns                                                 | 106 ns: 1.05x slower                                         |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                        |
| bench_thread_pool          | 818 us                                                 | 863 us: 1.06x slower                                         |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                         |
| nbody                      | 87.7 ms                                                | 94.3 ms: 1.08x slower                                        |
| many_optionals             | 857 us                                                 | 933 us: 1.09x slower                                         |
| coverage                   | 82.8 ms                                                | 90.7 ms: 1.09x slower                                        |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                        |
| json_dumps                 | 10.1 ms                                                | 12.0 ms: 1.19x slower                                        |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.33x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.38x slower                                        |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                 |

Benchmark hidden because not significant (9): shortest_path, scimark_sor, pprint_pformat, typing_runtime_protocols, asyncio_websockets, chaos, create_gc_cycles, docutils, connected_components
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x