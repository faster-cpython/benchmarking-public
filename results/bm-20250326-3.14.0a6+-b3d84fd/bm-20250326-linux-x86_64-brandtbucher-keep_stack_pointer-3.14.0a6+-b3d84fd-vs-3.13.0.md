# Results vs. 3.13.0

- fork: brandtbucher
- ref: keep_stack_pointer
- machine: linux-x86_64
- commit hash: b3d84fd
- commit date: 2025-03-26
- overall geometric mean: 1.039x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                       |
| docutils       | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                     |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                       |
| async_tree_io              | 838 ms                                                 | 612 ms: 1.37x faster                                                       |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 485 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 469 ms: 1.16x faster                                                       |
| async_generators           | 433 ms                                                 | 395 ms: 1.10x faster                                                       |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.9 ms: 1.13x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| nbody          | 87.7 ms                                                | 97.6 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                      |
| regex_v8       | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                      |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                       |
| regex_dna      | 220 ms                                                 | 225 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                       |
| tomli_loads          | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                     |
| xml_etree_generate   | 86.8 ms                                                | 84.9 ms: 1.02x faster                                                      |
| xml_etree_process    | 60.5 ms                                                | 59.3 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 99.4 ms: 1.02x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                       |
| pickle_pure_python   | 302 us                                                 | 314 us: 1.04x slower                                                       |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.3 ms: 1.05x slower                                                      |
| python_startup_no_site | 7.00 ms                                                | 8.28 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                      |
| genshi_xml      | 50.5 ms                                                | 48.5 ms: 1.04x faster                                                      |
| django_template | 31.7 ms                                                | 31.3 ms: 1.01x faster                                                      |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                       |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                       |
| async_tree_io              | 838 ms                                                 | 612 ms: 1.37x faster                                                       |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                       |
| deepcopy_memo              | 38.4 us                                                | 29.0 us: 1.33x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                       |
| go                         | 141 ms                                                 | 114 ms: 1.23x faster                                                       |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 485 ms: 1.18x faster                                                       |
| spectral_norm              | 113 ms                                                 | 97.6 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 469 ms: 1.16x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                      |
| float                      | 78.7 ms                                                | 69.9 ms: 1.13x faster                                                      |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                       |
| async_generators           | 433 ms                                                 | 395 ms: 1.10x faster                                                       |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                       |
| tomli_loads                | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                     |
| richards                   | 47.5 ms                                                | 43.9 ms: 1.08x faster                                                      |
| telco                      | 8.40 ms                                                | 7.81 ms: 1.08x faster                                                      |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                      |
| richards_super             | 53.7 ms                                                | 50.6 ms: 1.06x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.78 ms: 1.05x faster                                                      |
| scimark_fft                | 367 ms                                                 | 349 ms: 1.05x faster                                                       |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                       |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                      |
| genshi_xml                 | 50.5 ms                                                | 48.5 ms: 1.04x faster                                                      |
| dulwich_log                | 64.6 ms                                                | 62.3 ms: 1.04x faster                                                      |
| logging_silent             | 101 ns                                                 | 97.5 ns: 1.04x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                     |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                       |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                       |
| pyflate                    | 470 ms                                                 | 456 ms: 1.03x faster                                                       |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                      |
| logging_simple             | 5.65 us                                                | 5.50 us: 1.03x faster                                                      |
| thrift                     | 800 us                                                 | 779 us: 1.03x faster                                                       |
| gc_traversal               | 4.90 ms                                                | 4.79 ms: 1.02x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 84.9 ms: 1.02x faster                                                      |
| crypto_pyaes               | 74.7 ms                                                | 73.1 ms: 1.02x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.59 sec: 1.02x faster                                                     |
| xml_etree_process          | 60.5 ms                                                | 59.3 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 99.4 ms: 1.02x faster                                                      |
| mdp                        | 2.54 sec                                               | 2.50 sec: 1.02x faster                                                     |
| deltablue                  | 3.19 ms                                                | 3.15 ms: 1.02x faster                                                      |
| generators                 | 28.8 ms                                                | 28.4 ms: 1.01x faster                                                      |
| django_template            | 31.7 ms                                                | 31.3 ms: 1.01x faster                                                      |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                       |
| logging_format             | 6.23 us                                                | 6.19 us: 1.01x faster                                                      |
| pprint_safe_repr           | 727 ms                                                 | 723 ms: 1.01x faster                                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.00x faster                                                       |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                      |
| sympy_expand               | 456 ms                                                 | 459 ms: 1.01x slower                                                       |
| sympy_integrate            | 19.8 ms                                                | 20.0 ms: 1.01x slower                                                      |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                                       |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                                       |
| shortest_path              | 487 ms                                                 | 494 ms: 1.01x slower                                                       |
| connected_components       | 447 ms                                                 | 454 ms: 1.02x slower                                                       |
| nqueens                    | 80.9 ms                                                | 82.3 ms: 1.02x slower                                                      |
| docutils                   | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                     |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                       |
| regex_dna                  | 220 ms                                                 | 225 ms: 1.02x slower                                                       |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                       |
| hexiom                     | 6.08 ms                                                | 6.27 ms: 1.03x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 314 us: 1.04x slower                                                       |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                      |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                      |
| python_startup             | 12.7 ms                                                | 13.3 ms: 1.05x slower                                                      |
| fannkuch                   | 394 ms                                                 | 425 ms: 1.08x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 889 us: 1.09x slower                                                       |
| sqlalchemy_imperative      | 16.9 ms                                                | 18.4 ms: 1.09x slower                                                      |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                                      |
| nbody                      | 87.7 ms                                                | 97.6 ms: 1.11x slower                                                      |
| coverage                   | 82.8 ms                                                | 92.6 ms: 1.12x slower                                                      |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                      |
| many_optionals             | 857 us                                                 | 982 us: 1.15x slower                                                       |
| python_startup_no_site     | 7.00 ms                                                | 8.28 ms: 1.18x slower                                                      |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.36x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 85.3 ms: 3.56x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (8): sphinx, json, sympy_str, typing_runtime_protocols, asyncio_websockets, pprint_pformat, scimark_monte_carlo, chaos
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250326-3.14.0a6+-b3d84fd/bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x