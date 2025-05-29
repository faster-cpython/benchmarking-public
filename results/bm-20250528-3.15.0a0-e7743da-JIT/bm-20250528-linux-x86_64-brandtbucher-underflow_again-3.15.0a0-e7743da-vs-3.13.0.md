# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_again
- machine: linux-x86_64
- commit hash: e7743da
- commit date: 2025-05-28
- overall geometric mean: 1.377x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                   |
| docutils       | 2.58 sec                                               | 1.02 sec: 2.54x faster                                                 |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                   |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 320 ms: 1.36x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 634 ms: 1.36x faster                                                   |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 507 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 501 ms: 1.08x faster                                                   |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                                   |
| coroutines                 | 22.2 ms                                                | 26.0 ms: 1.17x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.6 ms: 1.22x faster                                                  |
| nbody          | 87.7 ms                                                | 89.0 ms: 1.01x slower                                                  |
| pidigits       | 186 ms                                                 | 191 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.08 ms: 1.22x faster                                                  |
| regex_v8       | 26.9 ms                                                | 22.0 ms: 1.22x faster                                                  |
| regex_dna      | 220 ms                                                 | 189 ms: 1.16x faster                                                   |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 200 us: 1.06x faster                                                   |
| xml_etree_process    | 60.5 ms                                                | 57.0 ms: 1.06x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 82.0 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 97.5 ms: 1.04x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.07x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.09x slower                                                  |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                  |
| python_startup_no_site | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 50.1 ms: 1.01x faster                                                  |
| mako            | 10.7 ms                                                | 10.6 ms: 1.01x faster                                                  |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pprint_pformat             | 1.48 sec                                               | 1.45 us: 1018490.16x faster                                            |
| pprint_safe_repr           | 727 ms                                                 | 861 ns: 843954.53x faster                                              |
| docutils                   | 2.58 sec                                               | 1.02 sec: 2.54x faster                                                 |
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.04x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                   |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                                   |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 320 ms: 1.36x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 634 ms: 1.36x faster                                                   |
| richards                   | 47.5 ms                                                | 35.7 ms: 1.33x faster                                                  |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                                   |
| richards_super             | 53.7 ms                                                | 41.4 ms: 1.30x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.08 ms: 1.22x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 22.0 ms: 1.22x faster                                                  |
| float                      | 78.7 ms                                                | 64.6 ms: 1.22x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.78 us: 1.17x faster                                                  |
| regex_dna                  | 220 ms                                                 | 189 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 507 ms: 1.13x faster                                                   |
| pylint                     | 312 ms                                                 | 282 ms: 1.10x faster                                                   |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.10x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                                   |
| scimark_fft                | 367 ms                                                 | 336 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 501 ms: 1.08x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                 |
| pyflate                    | 470 ms                                                 | 441 ms: 1.07x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.40 sec: 1.07x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 200 us: 1.06x faster                                                   |
| telco                      | 8.40 ms                                                | 7.91 ms: 1.06x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 57.0 ms: 1.06x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 82.0 ms: 1.06x faster                                                  |
| genshi_text                | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 62.0 ms: 1.04x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 97.5 ms: 1.04x faster                                                  |
| go                         | 141 ms                                                 | 135 ms: 1.04x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                  |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                 |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                 |
| deltablue                  | 3.19 ms                                                | 3.12 ms: 1.02x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                  |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                   |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.95 ms: 1.02x faster                                                  |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                  |
| json                       | 5.32 ms                                                | 5.25 ms: 1.01x faster                                                  |
| async_generators           | 433 ms                                                 | 428 ms: 1.01x faster                                                   |
| python_startup_no_site     | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 50.1 ms: 1.01x faster                                                  |
| mako                       | 10.7 ms                                                | 10.6 ms: 1.01x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.00x faster                                                   |
| shortest_path              | 487 ms                                                 | 490 ms: 1.01x slower                                                   |
| connected_components       | 447 ms                                                 | 451 ms: 1.01x slower                                                   |
| nbody                      | 87.7 ms                                                | 89.0 ms: 1.01x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                   |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 68.4 ms: 1.02x slower                                                  |
| pidigits                   | 186 ms                                                 | 191 ms: 1.03x slower                                                   |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                  |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                  |
| generators                 | 28.8 ms                                                | 29.9 ms: 1.04x slower                                                  |
| nqueens                    | 80.9 ms                                                | 84.3 ms: 1.04x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 5.11 ms: 1.04x slower                                                  |
| fannkuch                   | 394 ms                                                 | 412 ms: 1.05x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                  |
| raytrace                   | 262 ms                                                 | 277 ms: 1.06x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.47 ms: 1.06x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.07x slower                                                   |
| chaos                      | 58.0 ms                                                | 62.7 ms: 1.08x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.09x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 897 us: 1.10x slower                                                   |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                                  |
| logging_simple             | 5.65 us                                                | 6.24 us: 1.10x slower                                                  |
| logging_format             | 6.23 us                                                | 6.98 us: 1.12x slower                                                  |
| many_optionals             | 857 us                                                 | 987 us: 1.15x slower                                                   |
| coroutines                 | 22.2 ms                                                | 26.0 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 23.4 ms: 1.52x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 92.9 ms: 3.87x slower                                                  |
| logging_silent             | 101 ns                                                 | 475 ns: 4.70x slower                                                   |
| coverage                   | 82.8 ms                                                | 426 ms: 5.14x slower                                                   |
| thrift                     | 800 us                                                 | 149 ms: 185.81x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (5): sympy_str, pathlib, scimark_sor, crypto_pyaes, asyncio_websockets
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250528-3.15.0a0-e7743da-JIT/bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.377x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x