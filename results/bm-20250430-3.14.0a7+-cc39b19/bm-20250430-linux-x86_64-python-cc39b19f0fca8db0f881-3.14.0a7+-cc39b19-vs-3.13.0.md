# Results vs. 3.13.0

- fork: python
- ref: cc39b19f0fca8db0f881
- machine: linux-x86_64
- commit hash: cc39b19
- commit date: 2025-04-30
- overall geometric mean: 1.039x faster
- HPT reliability: 98.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                   |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                 |
| html5lib       | 63.4 ms                                                | 61.3 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                                   |
| async_tree_io              | 838 ms                                                 | 596 ms: 1.41x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                   |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                   |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                   |
| coroutines                 | 22.2 ms                                                | 26.1 ms: 1.18x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.5 ms: 1.10x faster                                                  |
| pidigits       | 186 ms                                                 | 195 ms: 1.04x slower                                                   |
| nbody          | 87.7 ms                                                | 102 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.5 ms: 1.19x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                  |
| regex_dna      | 220 ms                                                 | 210 ms: 1.05x faster                                                   |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 143 ms: 1.08x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 99.6 ms: 1.02x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 85.7 ms: 1.01x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                   |
| json_loads           | 27.2 us                                                | 30.7 us: 1.13x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                  |
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                  |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                  |
| mako            | 10.7 ms                                                | 11.6 ms: 1.09x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.04x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                                   |
| async_tree_io              | 838 ms                                                 | 596 ms: 1.41x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                   |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                                   |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.0 us: 1.32x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                   |
| go                         | 141 ms                                                 | 113 ms: 1.25x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 22.5 ms: 1.19x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                   |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                   |
| richards                   | 47.5 ms                                                | 42.8 ms: 1.11x faster                                                  |
| float                      | 78.7 ms                                                | 71.5 ms: 1.10x faster                                                  |
| richards_super             | 53.7 ms                                                | 49.4 ms: 1.09x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 143 ms: 1.08x faster                                                   |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 60.4 ms: 1.07x faster                                                  |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                   |
| regex_dna                  | 220 ms                                                 | 210 ms: 1.05x faster                                                   |
| telco                      | 8.40 ms                                                | 8.01 ms: 1.05x faster                                                  |
| spectral_norm              | 113 ms                                                 | 108 ms: 1.05x faster                                                   |
| logging_silent             | 101 ns                                                 | 96.5 ns: 1.05x faster                                                  |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                 |
| sympy_integrate            | 19.8 ms                                                | 19.1 ms: 1.04x faster                                                  |
| html5lib                   | 63.4 ms                                                | 61.3 ms: 1.03x faster                                                  |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| pyflate                    | 470 ms                                                 | 455 ms: 1.03x faster                                                   |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.85 us: 1.02x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.60 sec: 1.02x faster                                                 |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 99.6 ms: 1.02x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 85.7 ms: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                  |
| python_startup_no_site     | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.62 us: 1.01x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 727 ms                                                 | 733 ms: 1.01x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                 |
| sympy_expand               | 456 ms                                                 | 461 ms: 1.01x slower                                                   |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                 |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.01x slower                                                   |
| nqueens                    | 80.9 ms                                                | 81.9 ms: 1.01x slower                                                  |
| generators                 | 28.8 ms                                                | 29.2 ms: 1.01x slower                                                  |
| logging_format             | 6.23 us                                                | 6.32 us: 1.01x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.99 ms: 1.02x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 76.1 ms: 1.02x slower                                                  |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                   |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 68.3 ms: 1.02x slower                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                  |
| chaos                      | 58.0 ms                                                | 60.0 ms: 1.03x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.29 ms: 1.04x slower                                                  |
| scimark_fft                | 367 ms                                                 | 380 ms: 1.04x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.31 ms: 1.04x slower                                                  |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                  |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 222 us: 1.04x slower                                                   |
| pidigits                   | 186 ms                                                 | 195 ms: 1.04x slower                                                   |
| json                       | 5.32 ms                                                | 5.56 ms: 1.05x slower                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.27 ms: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.06x slower                                                   |
| fannkuch                   | 394 ms                                                 | 425 ms: 1.08x slower                                                   |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.09x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 893 us: 1.09x slower                                                   |
| many_optionals             | 857 us                                                 | 940 us: 1.10x slower                                                   |
| coverage                   | 82.8 ms                                                | 93.2 ms: 1.12x slower                                                  |
| json_loads                 | 27.2 us                                                | 30.7 us: 1.13x slower                                                  |
| nbody                      | 87.7 ms                                                | 102 ms: 1.16x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                  |
| coroutines                 | 22.2 ms                                                | 26.1 ms: 1.18x slower                                                  |
| subparsers                 | 15.5 ms                                                | 21.3 ms: 1.38x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 83.0 ms: 3.46x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (4): sphinx, sqlalchemy_declarative, asyncio_websockets, connected_components
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250430-3.14.0a7+-cc39b19/bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 98.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x