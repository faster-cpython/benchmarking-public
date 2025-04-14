# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_guard_float_int_
- machine: linux-x86_64
- commit hash: 602f0e9
- commit date: 2025-03-27
- overall geometric mean: 1.059x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                         |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                       |
| html5lib       | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 612 ms: 1.37x faster                                                         |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                         |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                         |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 63.4 ms: 1.24x faster                                                        |
| nbody          | 87.7 ms                                                | 86.3 ms: 1.02x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.23 ms: 1.17x faster                                                        |
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                                        |
| regex_compile  | 132 ms                                                 | 126 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|---------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads         | 2.12 sec                                               | 1.87 sec: 1.13x faster                                                       |
| xml_etree_parse     | 154 ms                                                 | 139 ms: 1.11x faster                                                         |
| xml_etree_generate  | 86.8 ms                                                | 79.0 ms: 1.10x faster                                                        |
| xml_etree_process   | 60.5 ms                                                | 56.0 ms: 1.08x faster                                                        |
| xml_etree_iterparse | 101 ms                                                 | 98.5 ms: 1.03x faster                                                        |
| pickle_pure_python  | 302 us                                                 | 325 us: 1.07x slower                                                         |
| json_loads          | 27.2 us                                                | 29.7 us: 1.09x slower                                                        |
| json_dumps          | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                        |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                        |
| python_startup_no_site | 7.00 ms                                                | 8.19 ms: 1.17x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                        |
| genshi_xml      | 50.5 ms                                                | 49.4 ms: 1.02x faster                                                        |
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                                        |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                       |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 612 ms: 1.37x faster                                                         |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                                         |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                         |
| richards                   | 47.5 ms                                                | 35.5 ms: 1.34x faster                                                        |
| richards_super             | 53.7 ms                                                | 40.8 ms: 1.32x faster                                                        |
| deepcopy_memo              | 38.4 us                                                | 29.2 us: 1.32x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                         |
| float                      | 78.7 ms                                                | 63.4 ms: 1.24x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                        |
| spectral_norm              | 113 ms                                                 | 94.6 ms: 1.20x faster                                                        |
| scimark_fft                | 367 ms                                                 | 310 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.23 ms: 1.17x faster                                                        |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.87 sec: 1.13x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.48 ms: 1.12x faster                                                        |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                         |
| go                         | 141 ms                                                 | 126 ms: 1.11x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 79.0 ms: 1.10x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 56.0 ms: 1.08x faster                                                        |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                        |
| dulwich_log                | 64.6 ms                                                | 60.2 ms: 1.07x faster                                                        |
| pyflate                    | 470 ms                                                 | 441 ms: 1.06x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                       |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                                        |
| logging_silent             | 101 ns                                                 | 96.2 ns: 1.05x faster                                                        |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                         |
| telco                      | 8.40 ms                                                | 8.02 ms: 1.05x faster                                                        |
| regex_compile              | 132 ms                                                 | 126 ms: 1.04x faster                                                         |
| deltablue                  | 3.19 ms                                                | 3.07 ms: 1.04x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                                       |
| gc_traversal               | 4.90 ms                                                | 4.76 ms: 1.03x faster                                                        |
| html5lib                   | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 98.5 ms: 1.03x faster                                                        |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                       |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                         |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.02x faster                                                        |
| genshi_xml                 | 50.5 ms                                                | 49.4 ms: 1.02x faster                                                        |
| logging_format             | 6.23 us                                                | 6.11 us: 1.02x faster                                                        |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                         |
| logging_simple             | 5.65 us                                                | 5.55 us: 1.02x faster                                                        |
| nbody                      | 87.7 ms                                                | 86.3 ms: 1.02x faster                                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                         |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| sympy_integrate            | 19.8 ms                                                | 19.8 ms: 1.00x faster                                                        |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                                         |
| chaos                      | 58.0 ms                                                | 58.4 ms: 1.01x slower                                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                        |
| coverage                   | 82.8 ms                                                | 83.7 ms: 1.01x slower                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 67.5 ms: 1.01x slower                                                        |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                                        |
| crypto_pyaes               | 74.7 ms                                                | 75.9 ms: 1.02x slower                                                        |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                         |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                         |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                       |
| sympy_expand               | 456 ms                                                 | 472 ms: 1.03x slower                                                         |
| nqueens                    | 80.9 ms                                                | 83.7 ms: 1.03x slower                                                        |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                                         |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                        |
| fannkuch                   | 394 ms                                                 | 419 ms: 1.06x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.07x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 880 us: 1.08x slower                                                         |
| pprint_safe_repr           | 727 ms                                                 | 783 ms: 1.08x slower                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.60 sec: 1.08x slower                                                       |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                                        |
| hexiom                     | 6.08 ms                                                | 6.69 ms: 1.10x slower                                                        |
| many_optionals             | 857 us                                                 | 964 us: 1.13x slower                                                         |
| comprehensions             | 16.5 us                                                | 18.7 us: 1.13x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 8.19 ms: 1.17x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 83.0 ms: 3.46x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (8): sphinx, regex_dna, asyncio_websockets, shortest_path, sympy_str, json, connected_components, unpickle_pure_python
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250327-3.14.0a6+-602f0e9-JIT/bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x