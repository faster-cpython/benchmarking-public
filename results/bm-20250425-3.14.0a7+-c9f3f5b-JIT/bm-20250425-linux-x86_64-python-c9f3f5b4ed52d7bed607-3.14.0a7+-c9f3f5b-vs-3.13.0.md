# Results vs. 3.13.0

- fork: python
- ref: c9f3f5b4ed52d7bed607
- machine: linux-x86_64
- commit hash: c9f3f5b
- commit date: 2025-04-25
- overall geometric mean: 1.054x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                   |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                 |
| html5lib       | 63.4 ms                                                | 59.8 ms: 1.06x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 306 ms: 1.51x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 598 ms: 1.44x faster                                                   |
| async_tree_io              | 838 ms                                                 | 594 ms: 1.41x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                   |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                   |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                   |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.2 ms: 1.10x faster                                                  |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.06 ms: 1.23x faster                                                  |
| regex_v8       | 26.9 ms                                                | 22.4 ms: 1.20x faster                                                  |
| regex_dna      | 220 ms                                                 | 201 ms: 1.09x faster                                                   |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.81 sec: 1.17x faster                                                 |
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 80.4 ms: 1.08x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 56.8 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 98.3 ms: 1.03x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 209 us: 1.02x faster                                                   |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.08x slower                                                   |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.05x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.22 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                  |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                  |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.21 sec: 2.11x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 306 ms: 1.51x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 598 ms: 1.44x faster                                                   |
| async_tree_io              | 838 ms                                                 | 594 ms: 1.41x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                   |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                                   |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.0 us: 1.32x faster                                                  |
| richards                   | 47.5 ms                                                | 36.6 ms: 1.30x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                   |
| richards_super             | 53.7 ms                                                | 42.0 ms: 1.28x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.06 ms: 1.23x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.22x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 22.4 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                   |
| scimark_fft                | 367 ms                                                 | 312 ms: 1.18x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.81 sec: 1.17x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                   |
| float                      | 78.7 ms                                                | 71.2 ms: 1.10x faster                                                  |
| go                         | 141 ms                                                 | 128 ms: 1.10x faster                                                   |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                   |
| regex_dna                  | 220 ms                                                 | 201 ms: 1.09x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                   |
| spectral_norm              | 113 ms                                                 | 105 ms: 1.08x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 80.4 ms: 1.08x faster                                                  |
| telco                      | 8.40 ms                                                | 7.78 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.67 ms: 1.08x faster                                                  |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 56.8 ms: 1.06x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.41 sec: 1.06x faster                                                 |
| html5lib                   | 63.4 ms                                                | 59.8 ms: 1.06x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 61.1 ms: 1.06x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.26 sec: 1.05x faster                                                 |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                   |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                   |
| deltablue                  | 3.19 ms                                                | 3.07 ms: 1.04x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.3 ms: 1.03x faster                                                  |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                   |
| logging_silent             | 101 ns                                                 | 98.4 ns: 1.03x faster                                                  |
| pyflate                    | 470 ms                                                 | 457 ms: 1.03x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 209 us: 1.02x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.83 ms: 1.01x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                  |
| sympy_str                  | 273 ms                                                 | 270 ms: 1.01x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.61 us: 1.01x faster                                                  |
| scimark_sor                | 122 ms                                                 | 122 ms: 1.00x faster                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                                  |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| nqueens                    | 80.9 ms                                                | 81.5 ms: 1.01x slower                                                  |
| connected_components       | 447 ms                                                 | 450 ms: 1.01x slower                                                   |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 67.4 ms: 1.01x slower                                                  |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.01x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.01x slower                                                 |
| chaos                      | 58.0 ms                                                | 59.2 ms: 1.02x slower                                                  |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                 |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.5 ms: 1.03x slower                                                  |
| json                       | 5.32 ms                                                | 5.52 ms: 1.04x slower                                                  |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                                   |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.04x slower                                                   |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.05x slower                                                  |
| generators                 | 28.8 ms                                                | 30.2 ms: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.08x slower                                                   |
| fannkuch                   | 394 ms                                                 | 424 ms: 1.08x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 173 us: 1.08x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 895 us: 1.09x slower                                                   |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.71 ms: 1.10x slower                                                  |
| many_optionals             | 857 us                                                 | 957 us: 1.12x slower                                                   |
| comprehensions             | 16.5 us                                                | 18.5 us: 1.12x slower                                                  |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                                  |
| coverage                   | 82.8 ms                                                | 94.0 ms: 1.13x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.22 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.42x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (7): nbody, logging_format, pprint_safe_repr, asyncio_websockets, crypto_pyaes, sqlalchemy_declarative, shortest_path
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250425-3.14.0a7+-c9f3f5b-JIT/bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.054x faster

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x