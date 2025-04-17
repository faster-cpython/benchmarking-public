# Results vs. 3.13.0

- fork: mdboom
- ref: fast_list_dealloc
- machine: linux-x86_64
- commit hash: ce22895
- commit date: 2025-04-17
- overall geometric mean: 1.059x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                |
| html5lib       | 63.4 ms                                                | 60.7 ms: 1.04x faster                                               |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.50x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 308 ms: 1.42x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                |
| async_tree_io              | 838 ms                                                 | 606 ms: 1.38x faster                                                |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.30x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 481 ms: 1.19x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.14x faster                                                |
| async_generators           | 433 ms                                                 | 388 ms: 1.12x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                               |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.5 ms: 1.16x faster                                               |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                |
| nbody          | 87.7 ms                                                | 95.8 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.09 ms: 1.22x faster                                               |
| regex_v8       | 26.9 ms                                                | 23.1 ms: 1.16x faster                                               |
| regex_dna      | 220 ms                                                 | 206 ms: 1.07x faster                                                |
| regex_compile  | 132 ms                                                 | 124 ms: 1.06x faster                                                |
| Geometric mean | (ref)                                                  | 1.13x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.08x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 58.2 ms: 1.04x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 83.8 ms: 1.04x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 99.1 ms: 1.02x faster                                               |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                |
| pickle_pure_python   | 302 us                                                 | 311 us: 1.03x slower                                                |
| json_loads           | 27.2 us                                                | 30.0 us: 1.11x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                               |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.23 ms: 1.18x slower                                               |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.8 ms: 1.09x faster                                               |
| genshi_xml      | 50.5 ms                                                | 49.0 ms: 1.03x faster                                               |
| django_template | 31.7 ms                                                | 31.4 ms: 1.01x faster                                               |
| mako            | 10.7 ms                                                | 11.5 ms: 1.07x slower                                               |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.20 sec: 2.11x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.50x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 308 ms: 1.42x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                |
| deepcopy                   | 354 us                                                 | 253 us: 1.40x faster                                                |
| async_tree_io              | 838 ms                                                 | 606 ms: 1.38x faster                                                |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 28.3 us: 1.36x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.30x faster                                                |
| go                         | 141 ms                                                 | 110 ms: 1.28x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.09 ms: 1.22x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 481 ms: 1.19x faster                                                |
| float                      | 78.7 ms                                                | 67.5 ms: 1.16x faster                                               |
| regex_v8                   | 26.9 ms                                                | 23.1 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.14x faster                                                |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                |
| async_generators           | 433 ms                                                 | 388 ms: 1.12x faster                                                |
| richards                   | 47.5 ms                                                | 42.9 ms: 1.11x faster                                               |
| pyflate                    | 470 ms                                                 | 425 ms: 1.10x faster                                                |
| telco                      | 8.40 ms                                                | 7.70 ms: 1.09x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                |
| richards_super             | 53.7 ms                                                | 49.4 ms: 1.09x faster                                               |
| genshi_text                | 22.6 ms                                                | 20.8 ms: 1.09x faster                                               |
| dulwich_log                | 64.6 ms                                                | 59.6 ms: 1.08x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.08x faster                                              |
| logging_silent             | 101 ns                                                 | 94.2 ns: 1.07x faster                                               |
| regex_dna                  | 220 ms                                                 | 206 ms: 1.07x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                              |
| spectral_norm              | 113 ms                                                 | 106 ms: 1.07x faster                                                |
| regex_compile              | 132 ms                                                 | 124 ms: 1.06x faster                                                |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                |
| html5lib                   | 63.4 ms                                                | 60.7 ms: 1.04x faster                                               |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 58.2 ms: 1.04x faster                                               |
| meteor_contest             | 108 ms                                                 | 104 ms: 1.04x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 83.8 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                              |
| logging_simple             | 5.65 us                                                | 5.48 us: 1.03x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 49.0 ms: 1.03x faster                                               |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                              |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                                |
| scimark_fft                | 367 ms                                                 | 358 ms: 1.03x faster                                                |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.58 sec: 1.02x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 99.1 ms: 1.02x faster                                               |
| gc_traversal               | 4.90 ms                                                | 4.80 ms: 1.02x faster                                               |
| crypto_pyaes               | 74.7 ms                                                | 73.4 ms: 1.02x faster                                               |
| chaos                      | 58.0 ms                                                | 57.0 ms: 1.02x faster                                               |
| logging_format             | 6.23 us                                                | 6.13 us: 1.02x faster                                               |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.02x faster                                              |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                |
| pprint_safe_repr           | 727 ms                                                 | 716 ms: 1.01x faster                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                                |
| django_template            | 31.7 ms                                                | 31.4 ms: 1.01x faster                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 66.3 ms: 1.01x faster                                               |
| sympy_expand               | 456 ms                                                 | 453 ms: 1.01x faster                                                |
| nqueens                    | 80.9 ms                                                | 80.4 ms: 1.01x faster                                               |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.13 ms: 1.01x slower                                               |
| connected_components       | 447 ms                                                 | 452 ms: 1.01x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                |
| generators                 | 28.8 ms                                                | 29.3 ms: 1.02x slower                                               |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                                |
| shortest_path              | 487 ms                                                 | 497 ms: 1.02x slower                                                |
| pickle_pure_python         | 302 us                                                 | 311 us: 1.03x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 165 us: 1.03x slower                                                |
| fannkuch                   | 394 ms                                                 | 406 ms: 1.03x slower                                                |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                |
| deltablue                  | 3.19 ms                                                | 3.31 ms: 1.04x slower                                               |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                               |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                               |
| coverage                   | 82.8 ms                                                | 88.6 ms: 1.07x slower                                               |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.07x slower                                               |
| bench_thread_pool          | 818 us                                                 | 888 us: 1.09x slower                                                |
| many_optionals             | 857 us                                                 | 935 us: 1.09x slower                                                |
| nbody                      | 87.7 ms                                                | 95.8 ms: 1.09x slower                                               |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.11x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.23 ms: 1.18x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.1 ms: 3.42x slower                                               |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (6): scimark_sparse_mat_mult, comprehensions, sqlalchemy_imperative, docutils, asyncio_websockets, json
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250417-3.14.0a7+-ce22895/bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x