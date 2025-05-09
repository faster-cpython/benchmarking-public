# Results vs. 3.13.0

- fork: brandtbucher
- ref: load_const_borrow
- machine: linux-x86_64
- commit hash: 60413da
- commit date: 2025-05-08
- overall geometric mean: 1.028x slower
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 263 ms: 1.01x faster                                                     |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                   |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                     |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 636 ms: 1.35x faster                                                     |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                     |
| async_generators           | 433 ms                                                 | 426 ms: 1.02x faster                                                     |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.2 ms: 1.23x faster                                                    |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                     |
| nbody          | 87.7 ms                                                | 89.5 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.01 ms: 1.25x faster                                                    |
| regex_v8       | 26.9 ms                                                | 22.7 ms: 1.18x faster                                                    |
| regex_dna      | 220 ms                                                 | 197 ms: 1.12x faster                                                     |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.14x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.87 sec: 1.13x faster                                                   |
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                     |
| xml_etree_generate   | 86.8 ms                                                | 80.4 ms: 1.08x faster                                                    |
| xml_etree_process    | 60.5 ms                                                | 56.0 ms: 1.08x faster                                                    |
| unpickle_pure_python | 213 us                                                 | 205 us: 1.04x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 98.5 ms: 1.03x faster                                                    |
| pickle_pure_python   | 302 us                                                 | 329 us: 1.09x slower                                                     |
| json_loads           | 27.2 us                                                | 29.7 us: 1.09x slower                                                    |
| json_dumps           | 10.1 ms                                                | 11.9 ms: 1.17x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.3 ms: 1.03x faster                                                    |
| python_startup_no_site | 7.00 ms                                                | 6.96 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                    |
| genshi_xml      | 50.5 ms                                                | 49.1 ms: 1.03x faster                                                    |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                    |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.25 sec: 2.04x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                     |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                     |
| richards_super             | 53.7 ms                                                | 38.6 ms: 1.39x faster                                                    |
| richards                   | 47.5 ms                                                | 34.2 ms: 1.39x faster                                                    |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 636 ms: 1.35x faster                                                     |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                     |
| deepcopy_memo              | 38.4 us                                                | 30.4 us: 1.26x faster                                                    |
| regex_effbot               | 3.77 ms                                                | 3.01 ms: 1.25x faster                                                    |
| float                      | 78.7 ms                                                | 64.2 ms: 1.23x faster                                                    |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                                    |
| regex_v8                   | 26.9 ms                                                | 22.7 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                     |
| scimark_fft                | 367 ms                                                 | 320 ms: 1.14x faster                                                     |
| spectral_norm              | 113 ms                                                 | 99.3 ms: 1.14x faster                                                    |
| tomli_loads                | 2.12 sec                                               | 1.87 sec: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                     |
| go                         | 141 ms                                                 | 126 ms: 1.12x faster                                                     |
| regex_dna                  | 220 ms                                                 | 197 ms: 1.12x faster                                                     |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                     |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                     |
| telco                      | 8.40 ms                                                | 7.77 ms: 1.08x faster                                                    |
| xml_etree_generate         | 86.8 ms                                                | 80.4 ms: 1.08x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.34 sec: 1.08x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 56.0 ms: 1.08x faster                                                    |
| pyflate                    | 470 ms                                                 | 447 ms: 1.05x faster                                                     |
| dulwich_log                | 64.6 ms                                                | 61.6 ms: 1.05x faster                                                    |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                   |
| genshi_text                | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                    |
| unpickle_pure_python       | 213 us                                                 | 205 us: 1.04x faster                                                     |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                    |
| deltablue                  | 3.19 ms                                                | 3.08 ms: 1.04x faster                                                    |
| python_startup             | 12.7 ms                                                | 12.3 ms: 1.03x faster                                                    |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                   |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 98.5 ms: 1.03x faster                                                    |
| genshi_xml                 | 50.5 ms                                                | 49.1 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.92 ms: 1.02x faster                                                    |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                    |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                    |
| async_generators           | 433 ms                                                 | 426 ms: 1.02x faster                                                     |
| 2to3                       | 266 ms                                                 | 263 ms: 1.01x faster                                                     |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                     |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x faster                                                     |
| python_startup_no_site     | 7.00 ms                                                | 6.96 ms: 1.01x faster                                                    |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                     |
| scimark_monte_carlo        | 66.8 ms                                                | 67.3 ms: 1.01x slower                                                    |
| gc_traversal               | 4.90 ms                                                | 4.94 ms: 1.01x slower                                                    |
| crypto_pyaes               | 74.7 ms                                                | 75.5 ms: 1.01x slower                                                    |
| nbody                      | 87.7 ms                                                | 89.5 ms: 1.02x slower                                                    |
| pprint_pformat             | 1.48 sec                                               | 1.52 sec: 1.03x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                     |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                    |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                    |
| sympy_expand               | 456 ms                                                 | 474 ms: 1.04x slower                                                     |
| create_gc_cycles           | 2.45 ms                                                | 2.56 ms: 1.04x slower                                                    |
| fannkuch                   | 394 ms                                                 | 413 ms: 1.05x slower                                                     |
| nqueens                    | 80.9 ms                                                | 85.1 ms: 1.05x slower                                                    |
| chaos                      | 58.0 ms                                                | 61.1 ms: 1.05x slower                                                    |
| raytrace                   | 262 ms                                                 | 276 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                                     |
| comprehensions             | 16.5 us                                                | 17.9 us: 1.09x slower                                                    |
| pickle_pure_python         | 302 us                                                 | 329 us: 1.09x slower                                                     |
| generators                 | 28.8 ms                                                | 31.3 ms: 1.09x slower                                                    |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                                    |
| logging_simple             | 5.65 us                                                | 6.20 us: 1.10x slower                                                    |
| hexiom                     | 6.08 ms                                                | 6.72 ms: 1.11x slower                                                    |
| bench_thread_pool          | 818 us                                                 | 907 us: 1.11x slower                                                     |
| logging_format             | 6.23 us                                                | 6.93 us: 1.11x slower                                                    |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                                    |
| many_optionals             | 857 us                                                 | 986 us: 1.15x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.9 ms: 1.17x slower                                                    |
| subparsers                 | 15.5 ms                                                | 23.1 ms: 1.49x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 93.7 ms: 3.91x slower                                                    |
| logging_silent             | 101 ns                                                 | 476 ns: 4.71x slower                                                     |
| coverage                   | 82.8 ms                                                | 430 ms: 5.20x slower                                                     |
| thrift                     | 800 us                                                 | 148 ms: 185.41x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                             |

Benchmark hidden because not significant (8): json, sphinx, connected_components, sympy_str, asyncio_websockets, shortest_path, pprint_safe_repr, pathlib
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250508-3.15.0a0-60413da-JIT/bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.028x slower

# HPT report

- Reliability score: 99.51% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x