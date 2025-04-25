# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 0706fb6
- commit date: 2025-04-24
- overall geometric mean: 1.056x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                      |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                    |
| html5lib       | 63.4 ms                                                | 62.1 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                      |
| async_tree_io              | 838 ms                                                 | 593 ms: 1.41x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                      |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                      |
| async_generators           | 433 ms                                                 | 422 ms: 1.03x faster                                                      |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.8 ms: 1.11x faster                                                     |
| nbody          | 87.7 ms                                                | 88.3 ms: 1.01x slower                                                     |
| pidigits       | 186 ms                                                 | 194 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.05 ms: 1.23x faster                                                     |
| regex_v8       | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                     |
| regex_dna      | 220 ms                                                 | 198 ms: 1.11x faster                                                      |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                    |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                      |
| xml_etree_generate   | 86.8 ms                                                | 80.0 ms: 1.09x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 56.2 ms: 1.08x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 208 us: 1.03x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 99.3 ms: 1.02x faster                                                     |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.06x slower                                                      |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                                     |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                     |
| python_startup_no_site | 7.00 ms                                                | 8.22 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                     |
| genshi_xml      | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                     |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                     |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.21 sec: 2.10x faster                                                    |
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                      |
| async_tree_io              | 838 ms                                                 | 593 ms: 1.41x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                      |
| deepcopy                   | 354 us                                                 | 256 us: 1.39x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                      |
| deepcopy_memo              | 38.4 us                                                | 28.7 us: 1.34x faster                                                     |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                      |
| richards                   | 47.5 ms                                                | 35.9 ms: 1.33x faster                                                     |
| richards_super             | 53.7 ms                                                | 41.7 ms: 1.29x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                      |
| regex_effbot               | 3.77 ms                                                | 3.05 ms: 1.23x faster                                                     |
| deepcopy_reduce            | 3.24 us                                                | 2.65 us: 1.22x faster                                                     |
| scimark_fft                | 367 ms                                                 | 308 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                     |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                      |
| go                         | 141 ms                                                 | 125 ms: 1.12x faster                                                      |
| float                      | 78.7 ms                                                | 70.8 ms: 1.11x faster                                                     |
| regex_dna                  | 220 ms                                                 | 198 ms: 1.11x faster                                                      |
| spectral_norm              | 113 ms                                                 | 102 ms: 1.11x faster                                                      |
| pyflate                    | 470 ms                                                 | 427 ms: 1.10x faster                                                      |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 80.0 ms: 1.09x faster                                                     |
| telco                      | 8.40 ms                                                | 7.80 ms: 1.08x faster                                                     |
| xml_etree_process          | 60.5 ms                                                | 56.2 ms: 1.08x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.68 ms: 1.07x faster                                                     |
| deltablue                  | 3.19 ms                                                | 2.98 ms: 1.07x faster                                                     |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                     |
| dulwich_log                | 64.6 ms                                                | 60.6 ms: 1.07x faster                                                     |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                                    |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                    |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                      |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                     |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                    |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                      |
| async_generators           | 433 ms                                                 | 422 ms: 1.03x faster                                                      |
| unpickle_pure_python       | 213 us                                                 | 208 us: 1.03x faster                                                      |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                      |
| logging_format             | 6.23 us                                                | 6.08 us: 1.02x faster                                                     |
| gc_traversal               | 4.90 ms                                                | 4.79 ms: 1.02x faster                                                     |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                     |
| html5lib                   | 63.4 ms                                                | 62.1 ms: 1.02x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 99.3 ms: 1.02x faster                                                     |
| logging_simple             | 5.65 us                                                | 5.54 us: 1.02x faster                                                     |
| crypto_pyaes               | 74.7 ms                                                | 73.4 ms: 1.02x faster                                                     |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.01x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                                      |
| genshi_xml                 | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                     |
| shortest_path              | 487 ms                                                 | 489 ms: 1.01x slower                                                      |
| nbody                      | 87.7 ms                                                | 88.3 ms: 1.01x slower                                                     |
| chaos                      | 58.0 ms                                                | 58.7 ms: 1.01x slower                                                     |
| nqueens                    | 80.9 ms                                                | 81.9 ms: 1.01x slower                                                     |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                     |
| connected_components       | 447 ms                                                 | 454 ms: 1.01x slower                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 68.0 ms: 1.02x slower                                                     |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                     |
| pprint_safe_repr           | 727 ms                                                 | 742 ms: 1.02x slower                                                      |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                     |
| sympy_expand               | 456 ms                                                 | 467 ms: 1.02x slower                                                      |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                    |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                      |
| json                       | 5.32 ms                                                | 5.50 ms: 1.03x slower                                                     |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                     |
| generators                 | 28.8 ms                                                | 29.9 ms: 1.04x slower                                                     |
| pidigits                   | 186 ms                                                 | 194 ms: 1.04x slower                                                      |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                      |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                     |
| fannkuch                   | 394 ms                                                 | 414 ms: 1.05x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.06x slower                                                      |
| typing_runtime_protocols   | 160 us                                                 | 174 us: 1.09x slower                                                      |
| bench_thread_pool          | 818 us                                                 | 894 us: 1.09x slower                                                      |
| hexiom                     | 6.08 ms                                                | 6.65 ms: 1.09x slower                                                     |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                     |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                                     |
| many_optionals             | 857 us                                                 | 947 us: 1.11x slower                                                      |
| coverage                   | 82.8 ms                                                | 93.2 ms: 1.13x slower                                                     |
| comprehensions             | 16.5 us                                                | 18.6 us: 1.13x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                     |
| python_startup_no_site     | 7.00 ms                                                | 8.22 ms: 1.17x slower                                                     |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (6): logging_silent, sphinx, sqlalchemy_declarative, asyncio_websockets, pprint_pformat, meteor_contest
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250424-3.14.0a7+-0706fb6-JIT/bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-0706fb6.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x