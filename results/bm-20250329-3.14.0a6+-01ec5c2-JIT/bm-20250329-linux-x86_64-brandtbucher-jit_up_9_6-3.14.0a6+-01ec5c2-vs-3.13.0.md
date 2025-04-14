# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_9_6
- machine: linux-x86_64
- commit hash: 01ec5c2
- commit date: 2025-03-29
- overall geometric mean: 1.036x faster
- HPT reliability: 86.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 270 ms: 1.01x slower                                               |
| docutils       | 2.58 sec                                               | 2.73 sec: 1.06x slower                                             |
| html5lib       | 63.4 ms                                                | 63.0 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 627 ms: 1.37x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 319 ms: 1.37x faster                                               |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                               |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 504 ms: 1.14x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                               |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                               |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                               |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                              |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.8 ms: 1.20x faster                                              |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.2 ms: 1.16x faster                                              |
| regex_effbot   | 3.77 ms                                                | 3.40 ms: 1.11x faster                                              |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                               |
| regex_compile  | 132 ms                                                 | 130 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|---------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads         | 2.12 sec                                               | 1.89 sec: 1.12x faster                                             |
| xml_etree_parse     | 154 ms                                                 | 140 ms: 1.10x faster                                               |
| xml_etree_generate  | 86.8 ms                                                | 80.1 ms: 1.08x faster                                              |
| xml_etree_process   | 60.5 ms                                                | 57.0 ms: 1.06x faster                                              |
| xml_etree_iterparse | 101 ms                                                 | 98.0 ms: 1.03x faster                                              |
| pickle_pure_python  | 302 us                                                 | 326 us: 1.08x slower                                               |
| json_loads          | 27.2 us                                                | 29.9 us: 1.10x slower                                              |
| json_dumps          | 10.1 ms                                                | 11.6 ms: 1.14x slower                                              |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                              |
| python_startup_no_site | 7.00 ms                                                | 8.18 ms: 1.17x slower                                              |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                              |
| genshi_xml      | 50.5 ms                                                | 50.1 ms: 1.01x faster                                              |
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                              |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                              |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 627 ms: 1.37x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 319 ms: 1.37x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 28.2 us: 1.36x faster                                              |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                               |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                               |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                               |
| richards                   | 47.5 ms                                                | 35.8 ms: 1.33x faster                                              |
| richards_super             | 53.7 ms                                                | 40.8 ms: 1.32x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                               |
| float                      | 78.7 ms                                                | 65.8 ms: 1.20x faster                                              |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                              |
| scimark_fft                | 367 ms                                                 | 316 ms: 1.16x faster                                               |
| regex_v8                   | 26.9 ms                                                | 23.2 ms: 1.16x faster                                              |
| spectral_norm              | 113 ms                                                 | 98.7 ms: 1.15x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 504 ms: 1.14x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.89 sec: 1.12x faster                                             |
| regex_effbot               | 3.77 ms                                                | 3.40 ms: 1.11x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                               |
| pylint                     | 312 ms                                                 | 287 ms: 1.08x faster                                               |
| go                         | 141 ms                                                 | 130 ms: 1.08x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 80.1 ms: 1.08x faster                                              |
| pyflate                    | 470 ms                                                 | 434 ms: 1.08x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                              |
| dulwich_log                | 64.6 ms                                                | 60.7 ms: 1.06x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 57.0 ms: 1.06x faster                                              |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.76 ms: 1.06x faster                                              |
| deltablue                  | 3.19 ms                                                | 3.05 ms: 1.05x faster                                              |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 98.0 ms: 1.03x faster                                              |
| logging_silent             | 101 ns                                                 | 98.6 ns: 1.02x faster                                              |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.59 sec: 1.02x faster                                             |
| telco                      | 8.40 ms                                                | 8.25 ms: 1.02x faster                                              |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                               |
| mdp                        | 2.54 sec                                               | 2.50 sec: 1.02x faster                                             |
| thrift                     | 800 us                                                 | 787 us: 1.02x faster                                               |
| gc_traversal               | 4.90 ms                                                | 4.83 ms: 1.01x faster                                              |
| regex_compile              | 132 ms                                                 | 130 ms: 1.01x faster                                               |
| logging_format             | 6.23 us                                                | 6.18 us: 1.01x faster                                              |
| genshi_xml                 | 50.5 ms                                                | 50.1 ms: 1.01x faster                                              |
| html5lib                   | 63.4 ms                                                | 63.0 ms: 1.01x faster                                              |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                               |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                               |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                               |
| generators                 | 28.8 ms                                                | 29.0 ms: 1.01x slower                                              |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.01x slower                                               |
| crypto_pyaes               | 74.7 ms                                                | 75.4 ms: 1.01x slower                                              |
| connected_components       | 447 ms                                                 | 451 ms: 1.01x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                              |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                              |
| 2to3                       | 266 ms                                                 | 270 ms: 1.01x slower                                               |
| sympy_str                  | 273 ms                                                 | 278 ms: 1.02x slower                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 68.6 ms: 1.03x slower                                              |
| coverage                   | 82.8 ms                                                | 85.3 ms: 1.03x slower                                              |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                              |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                               |
| sympy_integrate            | 19.8 ms                                                | 20.5 ms: 1.03x slower                                              |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                               |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                              |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                               |
| pprint_safe_repr           | 727 ms                                                 | 754 ms: 1.04x slower                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.6 ms: 1.04x slower                                              |
| sympy_expand               | 456 ms                                                 | 477 ms: 1.05x slower                                               |
| chaos                      | 58.0 ms                                                | 60.7 ms: 1.05x slower                                              |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                              |
| nqueens                    | 80.9 ms                                                | 85.0 ms: 1.05x slower                                              |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                               |
| docutils                   | 2.58 sec                                               | 2.73 sec: 1.06x slower                                             |
| sqlalchemy_declarative     | 133 ms                                                 | 141 ms: 1.06x slower                                               |
| pprint_pformat             | 1.48 sec                                               | 1.58 sec: 1.07x slower                                             |
| fannkuch                   | 394 ms                                                 | 424 ms: 1.08x slower                                               |
| pickle_pure_python         | 302 us                                                 | 326 us: 1.08x slower                                               |
| bench_thread_pool          | 818 us                                                 | 891 us: 1.09x slower                                               |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                              |
| comprehensions             | 16.5 us                                                | 18.7 us: 1.14x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                              |
| hexiom                     | 6.08 ms                                                | 6.99 ms: 1.15x slower                                              |
| python_startup_no_site     | 7.00 ms                                                | 8.18 ms: 1.17x slower                                              |
| many_optionals             | 857 us                                                 | 1.00 ms: 1.17x slower                                              |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 83.5 ms: 3.48x slower                                              |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                       |

Benchmark hidden because not significant (7): json, pycparser, nbody, logging_simple, shortest_path, sphinx, unpickle_pure_python
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250329-3.14.0a6+-01ec5c2-JIT/bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 86.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x