# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-x86_64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.042x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                             |
| html5lib       | 63.4 ms                                                | 60.7 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                             |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                             |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                             |
| async_generators           | 433 ms                                                 | 391 ms: 1.11x faster                                                             |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.5 ms: 1.13x faster                                                            |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                             |
| nbody          | 87.7 ms                                                | 88.9 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.36 ms: 1.12x faster                                                            |
| regex_v8       | 26.9 ms                                                | 24.6 ms: 1.09x faster                                                            |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                             |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                           |
| xml_etree_generate   | 86.8 ms                                                | 78.8 ms: 1.10x faster                                                            |
| xml_etree_process    | 60.5 ms                                                | 55.2 ms: 1.10x faster                                                            |
| xml_etree_parse      | 154 ms                                                 | 147 ms: 1.05x faster                                                             |
| unpickle_pure_python | 213 us                                                 | 206 us: 1.03x faster                                                             |
| xml_etree_iterparse  | 101 ms                                                 | 101 ms: 1.01x faster                                                             |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                             |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                                            |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                            |
| python_startup_no_site | 7.00 ms                                                | 8.19 ms: 1.17x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.2 ms: 1.05x faster                                                            |
| genshi_text     | 22.6 ms                                                | 21.9 ms: 1.03x faster                                                            |
| genshi_xml      | 50.5 ms                                                | 50.1 ms: 1.01x faster                                                            |
| django_template | 31.7 ms                                                | 32.1 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                             |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                                             |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                             |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                             |
| deepcopy_memo              | 38.4 us                                                | 30.9 us: 1.24x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                             |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                                             |
| go                         | 141 ms                                                 | 121 ms: 1.16x faster                                                             |
| spectral_norm              | 113 ms                                                 | 97.8 ms: 1.16x faster                                                            |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                             |
| float                      | 78.7 ms                                                | 69.5 ms: 1.13x faster                                                            |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                             |
| regex_effbot               | 3.77 ms                                                | 3.36 ms: 1.12x faster                                                            |
| async_generators           | 433 ms                                                 | 391 ms: 1.11x faster                                                             |
| xml_etree_generate         | 86.8 ms                                                | 78.8 ms: 1.10x faster                                                            |
| xml_etree_process          | 60.5 ms                                                | 55.2 ms: 1.10x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 24.6 ms: 1.09x faster                                                            |
| telco                      | 8.40 ms                                                | 7.74 ms: 1.08x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.65 ms: 1.08x faster                                                            |
| sqlite_synth               | 2.90 us                                                | 2.71 us: 1.07x faster                                                            |
| thrift                     | 800 us                                                 | 747 us: 1.07x faster                                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.44 sec: 1.06x faster                                                           |
| xml_etree_parse            | 154 ms                                                 | 147 ms: 1.05x faster                                                             |
| pyflate                    | 470 ms                                                 | 448 ms: 1.05x faster                                                             |
| mako                       | 10.7 ms                                                | 10.2 ms: 1.05x faster                                                            |
| html5lib                   | 63.4 ms                                                | 60.7 ms: 1.04x faster                                                            |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                           |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                            |
| richards                   | 47.5 ms                                                | 45.9 ms: 1.03x faster                                                            |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                             |
| unpickle_pure_python       | 213 us                                                 | 206 us: 1.03x faster                                                             |
| richards_super             | 53.7 ms                                                | 52.0 ms: 1.03x faster                                                            |
| shortest_path              | 487 ms                                                 | 472 ms: 1.03x faster                                                             |
| logging_format             | 6.23 us                                                | 6.04 us: 1.03x faster                                                            |
| genshi_text                | 22.6 ms                                                | 21.9 ms: 1.03x faster                                                            |
| logging_simple             | 5.65 us                                                | 5.48 us: 1.03x faster                                                            |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                           |
| connected_components       | 447 ms                                                 | 436 ms: 1.02x faster                                                             |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                                            |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                             |
| mdp                        | 2.54 sec                                               | 2.51 sec: 1.02x faster                                                           |
| crypto_pyaes               | 74.7 ms                                                | 73.7 ms: 1.01x faster                                                            |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                                             |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                                             |
| genshi_xml                 | 50.5 ms                                                | 50.1 ms: 1.01x faster                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 101 ms: 1.01x faster                                                             |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                             |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 161 us: 1.01x slower                                                             |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                             |
| json                       | 5.32 ms                                                | 5.39 ms: 1.01x slower                                                            |
| coverage                   | 82.8 ms                                                | 83.8 ms: 1.01x slower                                                            |
| nbody                      | 87.7 ms                                                | 88.9 ms: 1.01x slower                                                            |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.02x slower                                                            |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.02x slower                                                            |
| sympy_expand               | 456 ms                                                 | 464 ms: 1.02x slower                                                             |
| gc_traversal               | 4.90 ms                                                | 5.02 ms: 1.02x slower                                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.03x slower                                                            |
| sqlglot_parse              | 1.26 ms                                                | 1.30 ms: 1.03x slower                                                            |
| fannkuch                   | 394 ms                                                 | 406 ms: 1.03x slower                                                             |
| dulwich_log                | 64.6 ms                                                | 66.8 ms: 1.03x slower                                                            |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                            |
| chaos                      | 58.0 ms                                                | 60.4 ms: 1.04x slower                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 69.8 ms: 1.05x slower                                                            |
| hexiom                     | 6.08 ms                                                | 6.36 ms: 1.05x slower                                                            |
| comprehensions             | 16.5 us                                                | 17.3 us: 1.05x slower                                                            |
| deltablue                  | 3.19 ms                                                | 3.36 ms: 1.05x slower                                                            |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                             |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                            |
| raytrace                   | 262 ms                                                 | 277 ms: 1.06x slower                                                             |
| bench_thread_pool          | 818 us                                                 | 878 us: 1.07x slower                                                             |
| logging_silent             | 101 ns                                                 | 111 ns: 1.10x slower                                                             |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                                            |
| many_optionals             | 857 us                                                 | 956 us: 1.12x slower                                                             |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                            |
| python_startup_no_site     | 7.00 ms                                                | 8.19 ms: 1.17x slower                                                            |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.36x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 82.4 ms: 3.44x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (8): sphinx, sympy_str, meteor_contest, sqlalchemy_imperative, scimark_sor, asyncio_websockets, sympy_sum, nqueens
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, docutils, gevent_hub, gunicorn, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x