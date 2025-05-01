# Results vs. 3.13.0

- fork: sergey-miryanov
- ref: gh_132042_optimize_c
- machine: linux-x86_64
- commit hash: 04539cc
- commit date: 2025-05-01
- overall geometric mean: 1.042x faster
- HPT reliability: 99.19%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                              |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.02x slower                                                            |
| html5lib       | 63.4 ms                                                | 62.6 ms: 1.01x faster                                                             |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 305 ms: 1.52x faster                                                              |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                              |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                              |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                                              |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                              |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                              |
| async_generators           | 433 ms                                                 | 409 ms: 1.06x faster                                                              |
| coroutines                 | 22.2 ms                                                | 25.4 ms: 1.14x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                      |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.3 ms: 1.13x faster                                                             |
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                                              |
| nbody          | 87.7 ms                                                | 101 ms: 1.15x slower                                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.14 ms: 1.20x faster                                                             |
| regex_v8       | 26.9 ms                                                | 22.5 ms: 1.19x faster                                                             |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                                              |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                              |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                              |
| tomli_loads          | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 99.5 ms: 1.02x faster                                                             |
| xml_etree_generate   | 86.8 ms                                                | 85.9 ms: 1.01x faster                                                             |
| xml_etree_process    | 60.5 ms                                                | 60.1 ms: 1.01x faster                                                             |
| unpickle_pure_python | 213 us                                                 | 220 us: 1.03x slower                                                              |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.05x slower                                                              |
| json_loads           | 27.2 us                                                | 30.3 us: 1.12x slower                                                             |
| json_dumps           | 10.1 ms                                                | 12.0 ms: 1.19x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.90 ms: 1.01x faster                                                             |
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                             |
| genshi_xml      | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                             |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                             |
| mako            | 10.7 ms                                                | 11.6 ms: 1.08x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.06x faster                                                            |
| async_tree_memoization_tg  | 463 ms                                                 | 305 ms: 1.52x faster                                                              |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                              |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                              |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                                              |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                              |
| deepcopy_memo              | 38.4 us                                                | 28.8 us: 1.33x faster                                                             |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                              |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                              |
| go                         | 141 ms                                                 | 112 ms: 1.25x faster                                                              |
| regex_effbot               | 3.77 ms                                                | 3.14 ms: 1.20x faster                                                             |
| regex_v8                   | 26.9 ms                                                | 22.5 ms: 1.19x faster                                                             |
| deepcopy_reduce            | 3.24 us                                                | 2.78 us: 1.17x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                              |
| float                      | 78.7 ms                                                | 69.3 ms: 1.13x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                              |
| spectral_norm              | 113 ms                                                 | 102 ms: 1.11x faster                                                              |
| pylint                     | 312 ms                                                 | 282 ms: 1.10x faster                                                              |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                              |
| richards                   | 47.5 ms                                                | 44.0 ms: 1.08x faster                                                             |
| dulwich_log                | 64.6 ms                                                | 60.1 ms: 1.08x faster                                                             |
| richards_super             | 53.7 ms                                                | 50.1 ms: 1.07x faster                                                             |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                             |
| tomli_loads                | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                            |
| telco                      | 8.40 ms                                                | 7.85 ms: 1.07x faster                                                             |
| async_generators           | 433 ms                                                 | 409 ms: 1.06x faster                                                              |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                                              |
| logging_silent             | 101 ns                                                 | 95.9 ns: 1.05x faster                                                             |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.82 ms: 1.04x faster                                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                                            |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                              |
| sympy_integrate            | 19.8 ms                                                | 19.2 ms: 1.03x faster                                                             |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                            |
| pyflate                    | 470 ms                                                 | 456 ms: 1.03x faster                                                              |
| genshi_xml                 | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                             |
| xml_etree_iterparse        | 101 ms                                                 | 99.5 ms: 1.02x faster                                                             |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                              |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                            |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                                              |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                                              |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                            |
| python_startup_no_site     | 7.00 ms                                                | 6.90 ms: 1.01x faster                                                             |
| html5lib                   | 63.4 ms                                                | 62.6 ms: 1.01x faster                                                             |
| scimark_fft                | 367 ms                                                 | 363 ms: 1.01x faster                                                              |
| xml_etree_generate         | 86.8 ms                                                | 85.9 ms: 1.01x faster                                                             |
| xml_etree_process          | 60.5 ms                                                | 60.1 ms: 1.01x faster                                                             |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.00x faster                                                              |
| generators                 | 28.8 ms                                                | 28.9 ms: 1.01x slower                                                             |
| sympy_expand               | 456 ms                                                 | 459 ms: 1.01x slower                                                              |
| pprint_safe_repr           | 727 ms                                                 | 732 ms: 1.01x slower                                                              |
| logging_format             | 6.23 us                                                | 6.28 us: 1.01x slower                                                             |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 67.5 ms: 1.01x slower                                                             |
| connected_components       | 447 ms                                                 | 452 ms: 1.01x slower                                                              |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                              |
| nqueens                    | 80.9 ms                                                | 82.1 ms: 1.01x slower                                                             |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                              |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.02x slower                                                            |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                                              |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                             |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                                             |
| hexiom                     | 6.08 ms                                                | 6.25 ms: 1.03x slower                                                             |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                             |
| chaos                      | 58.0 ms                                                | 59.8 ms: 1.03x slower                                                             |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                             |
| unpickle_pure_python       | 213 us                                                 | 220 us: 1.03x slower                                                              |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                             |
| json                       | 5.32 ms                                                | 5.52 ms: 1.04x slower                                                             |
| gc_traversal               | 4.90 ms                                                | 5.08 ms: 1.04x slower                                                             |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                                              |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.05x slower                                                              |
| raytrace                   | 262 ms                                                 | 276 ms: 1.06x slower                                                              |
| fannkuch                   | 394 ms                                                 | 423 ms: 1.07x slower                                                              |
| deltablue                  | 3.19 ms                                                | 3.43 ms: 1.08x slower                                                             |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.08x slower                                                             |
| bench_thread_pool          | 818 us                                                 | 891 us: 1.09x slower                                                              |
| many_optionals             | 857 us                                                 | 942 us: 1.10x slower                                                              |
| coverage                   | 82.8 ms                                                | 92.1 ms: 1.11x slower                                                             |
| json_loads                 | 27.2 us                                                | 30.3 us: 1.12x slower                                                             |
| coroutines                 | 22.2 ms                                                | 25.4 ms: 1.14x slower                                                             |
| nbody                      | 87.7 ms                                                | 101 ms: 1.15x slower                                                              |
| json_dumps                 | 10.1 ms                                                | 12.0 ms: 1.19x slower                                                             |
| subparsers                 | 15.5 ms                                                | 21.5 ms: 1.39x slower                                                             |
| bench_mp_pool              | 24.0 ms                                                | 81.7 ms: 3.41x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (6): logging_simple, crypto_pyaes, sqlalchemy_declarative, pathlib, asyncio_websockets, sqlite_synth
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250501-3.14.0a7+-04539cc/bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 99.19% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x