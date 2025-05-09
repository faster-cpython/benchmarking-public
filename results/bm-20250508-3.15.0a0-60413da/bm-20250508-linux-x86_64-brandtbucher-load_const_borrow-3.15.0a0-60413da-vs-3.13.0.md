# Results vs. 3.13.0

- fork: brandtbucher
- ref: load_const_borrow
- machine: linux-x86_64
- commit hash: 60413da
- commit date: 2025-05-08
- overall geometric mean: 1.037x slower
- HPT reliability: 98.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.04x faster                                                     |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                   |
| html5lib       | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                    |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                     |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.37x faster                                                     |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                     |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                     |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.6 ms: 1.08x faster                                                    |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                     |
| nbody          | 87.7 ms                                                | 96.0 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.19 ms: 1.18x faster                                                    |
| regex_v8       | 26.9 ms                                                | 23.4 ms: 1.15x faster                                                    |
| regex_dna      | 220 ms                                                 | 204 ms: 1.08x faster                                                     |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                     |
| tomli_loads          | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 97.6 ms: 1.04x faster                                                    |
| xml_etree_generate   | 86.8 ms                                                | 85.4 ms: 1.02x faster                                                    |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                     |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.05x slower                                                     |
| json_loads           | 27.2 us                                                | 30.3 us: 1.11x slower                                                    |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                    |
| python_startup_no_site | 7.00 ms                                                | 6.91 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.0 ms: 1.08x faster                                                    |
| genshi_xml      | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                    |
| django_template | 31.7 ms                                                | 32.7 ms: 1.03x slower                                                    |
| mako            | 10.7 ms                                                | 11.9 ms: 1.11x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                     |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.37x faster                                                     |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                                     |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                     |
| deepcopy_memo              | 38.4 us                                                | 29.5 us: 1.30x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                     |
| go                         | 141 ms                                                 | 115 ms: 1.23x faster                                                     |
| regex_effbot               | 3.77 ms                                                | 3.19 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                     |
| deepcopy_reduce            | 3.24 us                                                | 2.81 us: 1.15x faster                                                    |
| regex_v8                   | 26.9 ms                                                | 23.4 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                     |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                                     |
| richards                   | 47.5 ms                                                | 43.4 ms: 1.09x faster                                                    |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                     |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                                     |
| float                      | 78.7 ms                                                | 72.6 ms: 1.08x faster                                                    |
| richards_super             | 53.7 ms                                                | 49.6 ms: 1.08x faster                                                    |
| regex_dna                  | 220 ms                                                 | 204 ms: 1.08x faster                                                     |
| genshi_text                | 22.6 ms                                                | 21.0 ms: 1.08x faster                                                    |
| dulwich_log                | 64.6 ms                                                | 60.1 ms: 1.07x faster                                                    |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                     |
| pyflate                    | 470 ms                                                 | 448 ms: 1.05x faster                                                     |
| telco                      | 8.40 ms                                                | 8.03 ms: 1.05x faster                                                    |
| tomli_loads                | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                   |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                     |
| sympy_integrate            | 19.8 ms                                                | 19.1 ms: 1.04x faster                                                    |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                    |
| xml_etree_iterparse        | 101 ms                                                 | 97.6 ms: 1.04x faster                                                    |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.04x faster                                                   |
| 2to3                       | 266 ms                                                 | 257 ms: 1.04x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                   |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.03x faster                                                     |
| genshi_xml                 | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                    |
| html5lib                   | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                    |
| sqlite_synth               | 2.90 us                                                | 2.84 us: 1.02x faster                                                    |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                     |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 85.4 ms: 1.02x faster                                                    |
| python_startup_no_site     | 7.00 ms                                                | 6.91 ms: 1.01x faster                                                    |
| crypto_pyaes               | 74.7 ms                                                | 73.8 ms: 1.01x faster                                                    |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                     |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.00 ms: 1.01x faster                                                    |
| gc_traversal               | 4.90 ms                                                | 4.91 ms: 1.00x slower                                                    |
| sympy_expand               | 456 ms                                                 | 458 ms: 1.00x slower                                                     |
| pprint_safe_repr           | 727 ms                                                 | 730 ms: 1.01x slower                                                     |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                     |
| nqueens                    | 80.9 ms                                                | 81.5 ms: 1.01x slower                                                    |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                   |
| pathlib                    | 17.4 ms                                                | 17.6 ms: 1.01x slower                                                    |
| scimark_monte_carlo        | 66.8 ms                                                | 67.7 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.02x slower                                                   |
| scimark_fft                | 367 ms                                                 | 374 ms: 1.02x slower                                                     |
| connected_components       | 447 ms                                                 | 455 ms: 1.02x slower                                                     |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                     |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                     |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                    |
| shortest_path              | 487 ms                                                 | 499 ms: 1.03x slower                                                     |
| chaos                      | 58.0 ms                                                | 59.8 ms: 1.03x slower                                                    |
| generators                 | 28.8 ms                                                | 29.7 ms: 1.03x slower                                                    |
| django_template            | 31.7 ms                                                | 32.7 ms: 1.03x slower                                                    |
| fannkuch                   | 394 ms                                                 | 407 ms: 1.03x slower                                                     |
| hexiom                     | 6.08 ms                                                | 6.29 ms: 1.04x slower                                                    |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                                     |
| create_gc_cycles           | 2.45 ms                                                | 2.56 ms: 1.05x slower                                                    |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                     |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.05x slower                                                     |
| deltablue                  | 3.19 ms                                                | 3.40 ms: 1.07x slower                                                    |
| logging_simple             | 5.65 us                                                | 6.10 us: 1.08x slower                                                    |
| bench_thread_pool          | 818 us                                                 | 886 us: 1.08x slower                                                     |
| nbody                      | 87.7 ms                                                | 96.0 ms: 1.10x slower                                                    |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                    |
| logging_format             | 6.23 us                                                | 6.85 us: 1.10x slower                                                    |
| mako                       | 10.7 ms                                                | 11.9 ms: 1.11x slower                                                    |
| json_loads                 | 27.2 us                                                | 30.3 us: 1.11x slower                                                    |
| many_optionals             | 857 us                                                 | 966 us: 1.13x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                    |
| subparsers                 | 15.5 ms                                                | 22.6 ms: 1.46x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 93.3 ms: 3.89x slower                                                    |
| logging_silent             | 101 ns                                                 | 481 ns: 4.76x slower                                                     |
| coverage                   | 82.8 ms                                                | 419 ms: 5.06x slower                                                     |
| thrift                     | 800 us                                                 | 148 ms: 185.52x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.07x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_process, asyncio_websockets, json
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250508-3.15.0a0-60413da/bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.037x slower

# HPT report

- Reliability score: 98.96% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x