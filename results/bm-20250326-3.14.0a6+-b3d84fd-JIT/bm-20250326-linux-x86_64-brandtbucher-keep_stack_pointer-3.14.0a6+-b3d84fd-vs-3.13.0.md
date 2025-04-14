# Results vs. 3.13.0

- fork: brandtbucher
- ref: keep_stack_pointer
- machine: linux-x86_64
- commit hash: b3d84fd
- commit date: 2025-03-26
- overall geometric mean: 1.055x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                       |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                     |
| html5lib       | 63.4 ms                                                | 62.7 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                       |
| async_tree_io              | 838 ms                                                 | 614 ms: 1.36x faster                                                       |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 472 ms: 1.15x faster                                                       |
| async_generators           | 433 ms                                                 | 411 ms: 1.06x faster                                                       |
| coroutines                 | 22.2 ms                                                | 24.0 ms: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 62.5 ms: 1.26x faster                                                      |
| nbody          | 87.7 ms                                                | 82.8 ms: 1.06x faster                                                      |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.6 ms: 1.19x faster                                                      |
| regex_effbot   | 3.77 ms                                                | 3.17 ms: 1.19x faster                                                      |
| regex_dna      | 220 ms                                                 | 211 ms: 1.04x faster                                                       |
| regex_compile  | 132 ms                                                 | 127 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                     |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                       |
| xml_etree_generate   | 86.8 ms                                                | 79.7 ms: 1.09x faster                                                      |
| xml_etree_process    | 60.5 ms                                                | 55.6 ms: 1.09x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 205 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 101 ms                                                 | 98.0 ms: 1.03x faster                                                      |
| pickle_pure_python   | 302 us                                                 | 316 us: 1.04x slower                                                       |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                      |
| python_startup_no_site | 7.00 ms                                                | 8.21 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.0 ms: 1.08x faster                                                      |
| genshi_xml      | 50.5 ms                                                | 49.4 ms: 1.02x faster                                                      |
| django_template | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                      |
| mako            | 10.7 ms                                                | 10.9 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                       |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                       |
| richards                   | 47.5 ms                                                | 34.7 ms: 1.37x faster                                                      |
| async_tree_io              | 838 ms                                                 | 614 ms: 1.36x faster                                                       |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                       |
| richards_super             | 53.7 ms                                                | 39.8 ms: 1.35x faster                                                      |
| deepcopy_memo              | 38.4 us                                                | 28.6 us: 1.34x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                       |
| float                      | 78.7 ms                                                | 62.5 ms: 1.26x faster                                                      |
| spectral_norm              | 113 ms                                                 | 90.9 ms: 1.25x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.64 us: 1.23x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 22.6 ms: 1.19x faster                                                      |
| scimark_fft                | 367 ms                                                 | 309 ms: 1.19x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.17 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 472 ms: 1.15x faster                                                       |
| go                         | 141 ms                                                 | 122 ms: 1.15x faster                                                       |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                     |
| pylint                     | 312 ms                                                 | 280 ms: 1.12x faster                                                       |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.59 ms: 1.10x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 79.7 ms: 1.09x faster                                                      |
| xml_etree_process          | 60.5 ms                                                | 55.6 ms: 1.09x faster                                                      |
| telco                      | 8.40 ms                                                | 7.72 ms: 1.09x faster                                                      |
| genshi_text                | 22.6 ms                                                | 21.0 ms: 1.08x faster                                                      |
| deltablue                  | 3.19 ms                                                | 2.97 ms: 1.08x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                     |
| dulwich_log                | 64.6 ms                                                | 60.7 ms: 1.06x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.74 us: 1.06x faster                                                      |
| nbody                      | 87.7 ms                                                | 82.8 ms: 1.06x faster                                                      |
| async_generators           | 433 ms                                                 | 411 ms: 1.06x faster                                                       |
| pyflate                    | 470 ms                                                 | 448 ms: 1.05x faster                                                       |
| regex_dna                  | 220 ms                                                 | 211 ms: 1.04x faster                                                       |
| unpickle_pure_python       | 213 us                                                 | 205 us: 1.04x faster                                                       |
| regex_compile              | 132 ms                                                 | 127 ms: 1.03x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.03x faster                                                     |
| mdp                        | 2.54 sec                                               | 2.46 sec: 1.03x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 98.0 ms: 1.03x faster                                                      |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                                      |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                       |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                     |
| thrift                     | 800 us                                                 | 781 us: 1.02x faster                                                       |
| genshi_xml                 | 50.5 ms                                                | 49.4 ms: 1.02x faster                                                      |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                       |
| logging_simple             | 5.65 us                                                | 5.59 us: 1.01x faster                                                      |
| generators                 | 28.8 ms                                                | 28.5 ms: 1.01x faster                                                      |
| html5lib                   | 63.4 ms                                                | 62.7 ms: 1.01x faster                                                      |
| logging_format             | 6.23 us                                                | 6.17 us: 1.01x faster                                                      |
| django_template            | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                      |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.00x faster                                                       |
| sympy_integrate            | 19.8 ms                                                | 20.0 ms: 1.01x slower                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                      |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                                       |
| shortest_path              | 487 ms                                                 | 495 ms: 1.02x slower                                                       |
| gc_traversal               | 4.90 ms                                                | 4.98 ms: 1.02x slower                                                      |
| connected_components       | 447 ms                                                 | 455 ms: 1.02x slower                                                       |
| chaos                      | 58.0 ms                                                | 59.2 ms: 1.02x slower                                                      |
| mako                       | 10.7 ms                                                | 10.9 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                                     |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.03x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                     |
| pprint_safe_repr           | 727 ms                                                 | 750 ms: 1.03x slower                                                       |
| sympy_expand               | 456 ms                                                 | 471 ms: 1.03x slower                                                       |
| nqueens                    | 80.9 ms                                                | 83.6 ms: 1.03x slower                                                      |
| coverage                   | 82.8 ms                                                | 85.7 ms: 1.03x slower                                                      |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 316 us: 1.04x slower                                                       |
| fannkuch                   | 394 ms                                                 | 419 ms: 1.06x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 879 us: 1.07x slower                                                       |
| coroutines                 | 22.2 ms                                                | 24.0 ms: 1.08x slower                                                      |
| hexiom                     | 6.08 ms                                                | 6.61 ms: 1.09x slower                                                      |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                                      |
| comprehensions             | 16.5 us                                                | 18.2 us: 1.10x slower                                                      |
| many_optionals             | 857 us                                                 | 969 us: 1.13x slower                                                       |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                      |
| python_startup_no_site     | 7.00 ms                                                | 8.21 ms: 1.17x slower                                                      |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 83.3 ms: 3.47x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (10): sphinx, logging_silent, json, meteor_contest, scimark_monte_carlo, sympy_str, asyncio_websockets, sympy_sum, scimark_lu, crypto_pyaes
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250326-3.14.0a6+-b3d84fd-JIT/bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x