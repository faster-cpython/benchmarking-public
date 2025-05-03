# Results vs. 3.13.0

- fork: faster-cpython
- ref: current_executor
- machine: linux-x86_64
- commit hash: a30e444
- commit date: 2025-05-03
- overall geometric mean: 1.048x faster
- HPT reliability: 98.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                         |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                       |
| html5lib       | 63.4 ms                                                | 60.9 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 608 ms: 1.42x faster                                                         |
| async_tree_io              | 838 ms                                                 | 595 ms: 1.41x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                         |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                         |
| async_generators           | 433 ms                                                 | 423 ms: 1.02x faster                                                         |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.7 ms: 1.22x faster                                                        |
| nbody          | 87.7 ms                                                | 93.9 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                        |
| regex_effbot   | 3.77 ms                                                | 3.39 ms: 1.11x faster                                                        |
| regex_dna      | 220 ms                                                 | 210 ms: 1.05x faster                                                         |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                       |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 80.6 ms: 1.08x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 56.6 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 209 us: 1.02x faster                                                         |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                         |
| json_loads           | 27.2 us                                                | 30.1 us: 1.11x slower                                                        |
| json_dumps           | 10.1 ms                                                | 12.0 ms: 1.19x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.97 ms: 1.00x faster                                                        |
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.8 ms: 1.08x faster                                                        |
| genshi_xml      | 50.5 ms                                                | 49.1 ms: 1.03x faster                                                        |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                        |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                       |
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 608 ms: 1.42x faster                                                         |
| async_tree_io              | 838 ms                                                 | 595 ms: 1.41x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                         |
| deepcopy                   | 354 us                                                 | 254 us: 1.39x faster                                                         |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                         |
| richards                   | 47.5 ms                                                | 35.4 ms: 1.34x faster                                                        |
| richards_super             | 53.7 ms                                                | 40.6 ms: 1.32x faster                                                        |
| deepcopy_memo              | 38.4 us                                                | 29.5 us: 1.30x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                         |
| float                      | 78.7 ms                                                | 64.7 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.21x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                       |
| go                         | 141 ms                                                 | 125 ms: 1.12x faster                                                         |
| scimark_fft                | 367 ms                                                 | 328 ms: 1.12x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.39 ms: 1.11x faster                                                        |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.10x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                         |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                         |
| genshi_text                | 22.6 ms                                                | 20.8 ms: 1.08x faster                                                        |
| xml_etree_generate         | 86.8 ms                                                | 80.6 ms: 1.08x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 56.6 ms: 1.07x faster                                                        |
| telco                      | 8.40 ms                                                | 7.87 ms: 1.07x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.41 sec: 1.06x faster                                                       |
| dulwich_log                | 64.6 ms                                                | 60.9 ms: 1.06x faster                                                        |
| pyflate                    | 470 ms                                                 | 444 ms: 1.06x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                                        |
| regex_dna                  | 220 ms                                                 | 210 ms: 1.05x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.05x faster                                                       |
| logging_silent             | 101 ns                                                 | 96.8 ns: 1.04x faster                                                        |
| html5lib                   | 63.4 ms                                                | 60.9 ms: 1.04x faster                                                        |
| deltablue                  | 3.19 ms                                                | 3.08 ms: 1.04x faster                                                        |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                       |
| genshi_xml                 | 50.5 ms                                                | 49.1 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                                        |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                                        |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                        |
| async_generators           | 433 ms                                                 | 423 ms: 1.02x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.92 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 209 us: 1.02x faster                                                         |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                                         |
| sympy_str                  | 273 ms                                                 | 271 ms: 1.01x faster                                                         |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                         |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x faster                                                         |
| python_startup_no_site     | 7.00 ms                                                | 6.97 ms: 1.00x faster                                                        |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 135 ms: 1.01x slower                                                         |
| logging_simple             | 5.65 us                                                | 5.76 us: 1.02x slower                                                        |
| logging_format             | 6.23 us                                                | 6.35 us: 1.02x slower                                                        |
| crypto_pyaes               | 74.7 ms                                                | 76.2 ms: 1.02x slower                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                                        |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.4 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 747 ms: 1.03x slower                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.52 sec: 1.03x slower                                                       |
| scimark_monte_carlo        | 66.8 ms                                                | 68.8 ms: 1.03x slower                                                        |
| fannkuch                   | 394 ms                                                 | 407 ms: 1.03x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                       |
| gc_traversal               | 4.90 ms                                                | 5.08 ms: 1.04x slower                                                        |
| sympy_expand               | 456 ms                                                 | 473 ms: 1.04x slower                                                         |
| generators                 | 28.8 ms                                                | 30.0 ms: 1.04x slower                                                        |
| chaos                      | 58.0 ms                                                | 60.6 ms: 1.04x slower                                                        |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                        |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.05x slower                                                         |
| raytrace                   | 262 ms                                                 | 276 ms: 1.05x slower                                                         |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                         |
| nbody                      | 87.7 ms                                                | 93.9 ms: 1.07x slower                                                        |
| typing_runtime_protocols   | 160 us                                                 | 173 us: 1.08x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 894 us: 1.09x slower                                                         |
| json_loads                 | 27.2 us                                                | 30.1 us: 1.11x slower                                                        |
| hexiom                     | 6.08 ms                                                | 6.74 ms: 1.11x slower                                                        |
| comprehensions             | 16.5 us                                                | 18.3 us: 1.11x slower                                                        |
| coverage                   | 82.8 ms                                                | 93.4 ms: 1.13x slower                                                        |
| many_optionals             | 857 us                                                 | 970 us: 1.13x slower                                                         |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 12.0 ms: 1.19x slower                                                        |
| subparsers                 | 15.5 ms                                                | 22.7 ms: 1.47x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.46x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (6): sphinx, pidigits, asyncio_websockets, connected_components, json, nqueens
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250503-3.14.0a7+-a30e444-JIT/bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 98.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x