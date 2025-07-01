# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_10_9
- machine: linux-x86_64
- commit hash: 2f53411
- commit date: 2025-06-30
- overall geometric mean: 1.059x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                               |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.02x slower                                             |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                               |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 640 ms: 1.34x faster                                               |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 504 ms: 1.14x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 499 ms: 1.09x faster                                               |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                              |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                       |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.3 ms: 1.19x faster                                              |
| pidigits       | 186 ms                                                 | 193 ms: 1.03x slower                                               |
| nbody          | 87.7 ms                                                | 94.3 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.0 ms: 1.22x faster                                              |
| regex_effbot   | 3.77 ms                                                | 3.27 ms: 1.15x faster                                              |
| regex_dna      | 220 ms                                                 | 203 ms: 1.08x faster                                               |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.12x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.82 sec: 1.16x faster                                             |
| unpickle_pure_python | 213 us                                                 | 190 us: 1.12x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 55.2 ms: 1.09x faster                                              |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 80.3 ms: 1.08x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                              |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                              |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| python_startup_no_site | 7.00 ms                                                | 6.93 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.05x faster                                              |
| mako            | 10.7 ms                                                | 10.4 ms: 1.02x faster                                              |
| genshi_xml      | 50.5 ms                                                | 50.8 ms: 1.01x slower                                              |
| django_template | 31.7 ms                                                | 32.8 ms: 1.04x slower                                              |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.06x faster                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                               |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                               |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 640 ms: 1.34x faster                                               |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 29.7 us: 1.29x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                               |
| spectral_norm              | 113 ms                                                 | 89.9 ms: 1.26x faster                                              |
| richards_super             | 53.7 ms                                                | 43.5 ms: 1.24x faster                                              |
| richards                   | 47.5 ms                                                | 38.7 ms: 1.23x faster                                              |
| go                         | 141 ms                                                 | 115 ms: 1.22x faster                                               |
| regex_v8                   | 26.9 ms                                                | 22.0 ms: 1.22x faster                                              |
| float                      | 78.7 ms                                                | 66.3 ms: 1.19x faster                                              |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                              |
| scimark_fft                | 367 ms                                                 | 312 ms: 1.18x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.82 sec: 1.16x faster                                             |
| regex_effbot               | 3.77 ms                                                | 3.27 ms: 1.15x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 504 ms: 1.14x faster                                               |
| pyflate                    | 470 ms                                                 | 415 ms: 1.13x faster                                               |
| unpickle_pure_python       | 213 us                                                 | 190 us: 1.12x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 55.2 ms: 1.09x faster                                              |
| pylint                     | 312 ms                                                 | 285 ms: 1.09x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 499 ms: 1.09x faster                                               |
| regex_dna                  | 220 ms                                                 | 203 ms: 1.08x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 80.3 ms: 1.08x faster                                              |
| dulwich_log                | 64.6 ms                                                | 59.8 ms: 1.08x faster                                              |
| telco                      | 8.40 ms                                                | 7.78 ms: 1.08x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.36 sec: 1.08x faster                                             |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.08x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.74 ms: 1.06x faster                                              |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                              |
| crypto_pyaes               | 74.7 ms                                                | 71.6 ms: 1.04x faster                                              |
| deltablue                  | 3.19 ms                                                | 3.07 ms: 1.04x faster                                              |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                              |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                             |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                              |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.82 us: 1.03x faster                                              |
| gc_traversal               | 4.90 ms                                                | 4.76 ms: 1.03x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                              |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.03x faster                                               |
| mako                       | 10.7 ms                                                | 10.4 ms: 1.02x faster                                              |
| pprint_safe_repr           | 727 ms                                                 | 710 ms: 1.02x faster                                               |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                             |
| thrift                     | 800 us                                                 | 783 us: 1.02x faster                                               |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                               |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                              |
| logging_simple             | 5.65 us                                                | 5.58 us: 1.01x faster                                              |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                              |
| python_startup_no_site     | 7.00 ms                                                | 6.93 ms: 1.01x faster                                              |
| genshi_xml                 | 50.5 ms                                                | 50.8 ms: 1.01x slower                                              |
| shortest_path              | 487 ms                                                 | 491 ms: 1.01x slower                                               |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                               |
| logging_format             | 6.23 us                                                | 6.32 us: 1.01x slower                                              |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.02x slower                                              |
| fannkuch                   | 394 ms                                                 | 402 ms: 1.02x slower                                               |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.02x slower                                             |
| sympy_expand               | 456 ms                                                 | 468 ms: 1.03x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.23 ms: 1.03x slower                                              |
| pidigits                   | 186 ms                                                 | 193 ms: 1.03x slower                                               |
| django_template            | 31.7 ms                                                | 32.8 ms: 1.04x slower                                              |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                               |
| djangocms                  | 22.3 us                                                | 23.1 us: 1.04x slower                                              |
| nqueens                    | 80.9 ms                                                | 84.1 ms: 1.04x slower                                              |
| raytrace                   | 262 ms                                                 | 273 ms: 1.05x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.57 ms: 1.05x slower                                              |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                               |
| chaos                      | 58.0 ms                                                | 61.2 ms: 1.06x slower                                              |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                              |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                               |
| coverage                   | 82.8 ms                                                | 88.3 ms: 1.07x slower                                              |
| generators                 | 28.8 ms                                                | 30.8 ms: 1.07x slower                                              |
| nbody                      | 87.7 ms                                                | 94.3 ms: 1.08x slower                                              |
| connected_components       | 447 ms                                                 | 485 ms: 1.09x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                              |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                              |
| many_optionals             | 857 us                                                 | 997 us: 1.16x slower                                               |
| subparsers                 | 15.5 ms                                                | 23.8 ms: 1.54x slower                                              |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (7): sphinx, logging_silent, async_generators, json, scimark_monte_carlo, sympy_str, asyncio_websockets
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250630-3.15.0a0-2f53411-JIT/bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x