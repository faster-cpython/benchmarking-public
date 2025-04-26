# Results vs. 3.13.0

- fork: mdboom
- ref: python_startup_time
- machine: linux-x86_64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.052x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 251 ms: 1.06x faster                                                  |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.00x slower                                                |
| html5lib       | 63.4 ms                                                | 62.1 ms: 1.02x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                  |
| async_tree_io              | 838 ms                                                 | 612 ms: 1.37x faster                                                  |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 480 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                  |
| async_generators           | 433 ms                                                 | 398 ms: 1.09x faster                                                  |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.0 ms: 1.14x faster                                                 |
| pidigits       | 186 ms                                                 | 194 ms: 1.04x slower                                                  |
| nbody          | 87.7 ms                                                | 98.7 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.5 ms: 1.19x faster                                                 |
| regex_effbot   | 3.77 ms                                                | 3.19 ms: 1.18x faster                                                 |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                                  |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 1.99 sec: 1.06x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 99.1 ms: 1.02x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 85.5 ms: 1.02x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 313 us: 1.04x slower                                                  |
| json_loads           | 27.2 us                                                | 30.2 us: 1.11x slower                                                 |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.31 ms: 1.04x slower                                                 |
| python_startup         | 12.7 ms                                                | 13.3 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.7 ms: 1.09x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                 |
| django_template | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                 |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                  |
| deepcopy                   | 354 us                                                 | 250 us: 1.42x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                  |
| async_tree_io              | 838 ms                                                 | 612 ms: 1.37x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 28.3 us: 1.36x faster                                                 |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                  |
| go                         | 141 ms                                                 | 111 ms: 1.27x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 22.5 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 480 ms: 1.19x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.19 ms: 1.18x faster                                                 |
| float                      | 78.7 ms                                                | 69.0 ms: 1.14x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                  |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                  |
| richards                   | 47.5 ms                                                | 42.7 ms: 1.11x faster                                                 |
| richards_super             | 53.7 ms                                                | 48.5 ms: 1.11x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 59.0 ms: 1.09x faster                                                 |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                  |
| genshi_text                | 22.6 ms                                                | 20.7 ms: 1.09x faster                                                 |
| async_generators           | 433 ms                                                 | 398 ms: 1.09x faster                                                  |
| telco                      | 8.40 ms                                                | 7.76 ms: 1.08x faster                                                 |
| pyflate                    | 470 ms                                                 | 439 ms: 1.07x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.99 sec: 1.06x faster                                                |
| 2to3                       | 266 ms                                                 | 251 ms: 1.06x faster                                                  |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                                  |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.04x faster                                                 |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                                |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                |
| logging_silent             | 101 ns                                                 | 98.0 ns: 1.03x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                 |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                  |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.44 sec: 1.03x faster                                                |
| pprint_safe_repr           | 727 ms                                                 | 709 ms: 1.02x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 99.1 ms: 1.02x faster                                                 |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| scimark_fft                | 367 ms                                                 | 360 ms: 1.02x faster                                                  |
| html5lib                   | 63.4 ms                                                | 62.1 ms: 1.02x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.85 us: 1.02x faster                                                 |
| logging_simple             | 5.65 us                                                | 5.56 us: 1.02x faster                                                 |
| chaos                      | 58.0 ms                                                | 57.1 ms: 1.02x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 85.5 ms: 1.02x faster                                                 |
| crypto_pyaes               | 74.7 ms                                                | 73.6 ms: 1.02x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| sympy_expand               | 456 ms                                                 | 451 ms: 1.01x faster                                                  |
| django_template            | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.00 ms: 1.01x faster                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.00x slower                                                |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                 |
| generators                 | 28.8 ms                                                | 29.4 ms: 1.02x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.00 ms: 1.02x slower                                                 |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                  |
| connected_components       | 447 ms                                                 | 459 ms: 1.03x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 313 us: 1.04x slower                                                  |
| json                       | 5.32 ms                                                | 5.53 ms: 1.04x slower                                                 |
| pidigits                   | 186 ms                                                 | 194 ms: 1.04x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.33 ms: 1.04x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.31 ms: 1.04x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.34 ms: 1.04x slower                                                 |
| shortest_path              | 487 ms                                                 | 509 ms: 1.05x slower                                                  |
| python_startup             | 12.7 ms                                                | 13.3 ms: 1.05x slower                                                 |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                 |
| fannkuch                   | 394 ms                                                 | 425 ms: 1.08x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 883 us: 1.08x slower                                                  |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                 |
| many_optionals             | 857 us                                                 | 936 us: 1.09x slower                                                  |
| json_loads                 | 27.2 us                                                | 30.2 us: 1.11x slower                                                 |
| nbody                      | 87.7 ms                                                | 98.7 ms: 1.13x slower                                                 |
| coverage                   | 82.8 ms                                                | 93.3 ms: 1.13x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                 |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (5): scimark_monte_carlo, logging_format, nqueens, asyncio_websockets, raytrace
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250425-3.14.0a7+-9fc1238/bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x