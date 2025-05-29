# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_again
- machine: linux-x86_64
- commit hash: 601d379
- commit date: 2025-05-29
- overall geometric mean: 1.337x faster
- HPT reliability: 99.39%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                   |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                 |
| html5lib       | 63.4 ms                                                | 62.2 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.49x faster                                                   |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 629 ms: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                   |
| async_generators           | 433 ms                                                 | 429 ms: 1.01x faster                                                   |
| coroutines                 | 22.2 ms                                                | 25.9 ms: 1.16x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.3 ms: 1.22x faster                                                  |
| nbody          | 87.7 ms                                                | 89.7 ms: 1.02x slower                                                  |
| pidigits       | 186 ms                                                 | 195 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.37 ms: 1.12x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                  |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.89 sec: 1.12x faster                                                 |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                   |
| xml_etree_process    | 60.5 ms                                                | 55.6 ms: 1.09x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 79.9 ms: 1.09x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 202 us: 1.05x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                  |
| json_loads           | 27.2 us                                                | 30.7 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                  |
| python_startup_no_site | 7.00 ms                                                | 6.96 ms: 1.01x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 50.2 ms: 1.01x faster                                                  |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pprint_pformat             | 1.48 sec                                               | 1.47 us: 1004691.23x faster                                            |
| pprint_safe_repr           | 727 ms                                                 | 857 ns: 847933.52x faster                                              |
| mdp                        | 2.54 sec                                               | 1.25 sec: 2.04x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.49x faster                                                   |
| richards                   | 47.5 ms                                                | 33.7 ms: 1.41x faster                                                  |
| richards_super             | 53.7 ms                                                | 38.2 ms: 1.41x faster                                                  |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                   |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 629 ms: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 30.1 us: 1.28x faster                                                  |
| float                      | 78.7 ms                                                | 64.3 ms: 1.22x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                   |
| spectral_norm              | 113 ms                                                 | 99.8 ms: 1.14x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.37 ms: 1.12x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.89 sec: 1.12x faster                                                 |
| scimark_fft                | 367 ms                                                 | 328 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                  |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 55.6 ms: 1.09x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 79.9 ms: 1.09x faster                                                  |
| pyflate                    | 470 ms                                                 | 441 ms: 1.06x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                 |
| telco                      | 8.40 ms                                                | 7.93 ms: 1.06x faster                                                  |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                                   |
| unpickle_pure_python       | 213 us                                                 | 202 us: 1.05x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 61.6 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.82 ms: 1.04x faster                                                  |
| genshi_text                | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                  |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                  |
| deltablue                  | 3.19 ms                                                | 3.08 ms: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                 |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                   |
| html5lib                   | 63.4 ms                                                | 62.2 ms: 1.02x faster                                                  |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.02x faster                                                  |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                                  |
| async_generators           | 433 ms                                                 | 429 ms: 1.01x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 50.2 ms: 1.01x faster                                                  |
| python_startup_no_site     | 7.00 ms                                                | 6.96 ms: 1.01x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                                   |
| connected_components       | 447 ms                                                 | 451 ms: 1.01x slower                                                   |
| crypto_pyaes               | 74.7 ms                                                | 75.5 ms: 1.01x slower                                                  |
| json                       | 5.32 ms                                                | 5.40 ms: 1.01x slower                                                  |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                                   |
| nbody                      | 87.7 ms                                                | 89.7 ms: 1.02x slower                                                  |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 5.02 ms: 1.03x slower                                                  |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                  |
| fannkuch                   | 394 ms                                                 | 407 ms: 1.03x slower                                                   |
| nqueens                    | 80.9 ms                                                | 84.3 ms: 1.04x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                 |
| pidigits                   | 186 ms                                                 | 195 ms: 1.05x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.05x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 70.3 ms: 1.05x slower                                                  |
| generators                 | 28.8 ms                                                | 30.3 ms: 1.05x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.42 ms: 1.06x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                  |
| raytrace                   | 262 ms                                                 | 278 ms: 1.06x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 171 us: 1.06x slower                                                   |
| logging_simple             | 5.65 us                                                | 6.19 us: 1.09x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 897 us: 1.10x slower                                                   |
| chaos                      | 58.0 ms                                                | 63.9 ms: 1.10x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                  |
| logging_format             | 6.23 us                                                | 6.88 us: 1.10x slower                                                  |
| json_loads                 | 27.2 us                                                | 30.7 us: 1.13x slower                                                  |
| many_optionals             | 857 us                                                 | 981 us: 1.14x slower                                                   |
| coroutines                 | 22.2 ms                                                | 25.9 ms: 1.16x slower                                                  |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 93.5 ms: 3.90x slower                                                  |
| logging_silent             | 101 ns                                                 | 476 ns: 4.71x slower                                                   |
| coverage                   | 82.8 ms                                                | 432 ms: 5.21x slower                                                   |
| thrift                     | 800 us                                                 | 148 ms: 185.57x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.28x faster                                                           |

Benchmark hidden because not significant (6): sphinx, mako, asyncio_websockets, sympy_str, go, shortest_path
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250529-3.15.0a0-601d379-JIT/bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.337x faster

# HPT report

- Reliability score: 99.39% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x