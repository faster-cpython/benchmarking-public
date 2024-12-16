# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-x86_64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.048x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.03x faster                                                             |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                           |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                                             |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                             |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 333 ms: 1.31x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                             |
| async_generators           | 433 ms                                                 | 422 ms: 1.03x faster                                                             |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                             |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.5 ms: 1.07x faster                                                            |
| nbody          | 87.7 ms                                                | 82.8 ms: 1.06x faster                                                            |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.21 ms: 1.17x faster                                                            |
| regex_v8       | 26.9 ms                                                | 25.0 ms: 1.08x faster                                                            |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                             |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.82 sec: 1.16x faster                                                           |
| xml_etree_parse      | 154 ms                                                 | 136 ms: 1.13x faster                                                             |
| xml_etree_generate   | 86.8 ms                                                | 76.9 ms: 1.13x faster                                                            |
| xml_etree_process    | 60.5 ms                                                | 54.3 ms: 1.11x faster                                                            |
| unpickle_pure_python | 213 us                                                 | 193 us: 1.10x faster                                                             |
| xml_etree_iterparse  | 101 ms                                                 | 96.0 ms: 1.06x faster                                                            |
| json_loads           | 27.2 us                                                | 25.9 us: 1.05x faster                                                            |
| pickle_pure_python   | 302 us                                                 | 314 us: 1.04x slower                                                             |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                            |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.1 ms: 1.05x faster                                                            |
| genshi_text     | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                            |
| genshi_xml      | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                            |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                                             |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                             |
| deepcopy                   | 354 us                                                 | 263 us: 1.35x faster                                                             |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 333 ms: 1.31x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                             |
| deepcopy_memo              | 38.4 us                                                | 31.5 us: 1.22x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                                            |
| scimark_fft                | 367 ms                                                 | 312 ms: 1.18x faster                                                             |
| regex_effbot               | 3.77 ms                                                | 3.21 ms: 1.17x faster                                                            |
| tomli_loads                | 2.12 sec                                               | 1.82 sec: 1.16x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                                             |
| go                         | 141 ms                                                 | 123 ms: 1.15x faster                                                             |
| xml_etree_parse            | 154 ms                                                 | 136 ms: 1.13x faster                                                             |
| xml_etree_generate         | 86.8 ms                                                | 76.9 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                             |
| crypto_pyaes               | 74.7 ms                                                | 66.6 ms: 1.12x faster                                                            |
| telco                      | 8.40 ms                                                | 7.51 ms: 1.12x faster                                                            |
| xml_etree_process          | 60.5 ms                                                | 54.3 ms: 1.11x faster                                                            |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.55 ms: 1.11x faster                                                            |
| unpickle_pure_python       | 213 us                                                 | 193 us: 1.10x faster                                                             |
| json                       | 5.32 ms                                                | 4.83 ms: 1.10x faster                                                            |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.10x faster                                                             |
| regex_v8                   | 26.9 ms                                                | 25.0 ms: 1.08x faster                                                            |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.08x faster                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                                           |
| float                      | 78.7 ms                                                | 73.5 ms: 1.07x faster                                                            |
| sqlite_synth               | 2.90 us                                                | 2.71 us: 1.07x faster                                                            |
| nbody                      | 87.7 ms                                                | 82.8 ms: 1.06x faster                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 63.1 ms: 1.06x faster                                                            |
| pyflate                    | 470 ms                                                 | 445 ms: 1.06x faster                                                             |
| xml_etree_iterparse        | 101 ms                                                 | 96.0 ms: 1.06x faster                                                            |
| mako                       | 10.7 ms                                                | 10.1 ms: 1.05x faster                                                            |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                                             |
| json_loads                 | 27.2 us                                                | 25.9 us: 1.05x faster                                                            |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                             |
| richards                   | 47.5 ms                                                | 45.5 ms: 1.04x faster                                                            |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                           |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                             |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                            |
| 2to3                       | 266 ms                                                 | 257 ms: 1.03x faster                                                             |
| fannkuch                   | 394 ms                                                 | 381 ms: 1.03x faster                                                             |
| richards_super             | 53.7 ms                                                | 52.2 ms: 1.03x faster                                                            |
| thrift                     | 800 us                                                 | 778 us: 1.03x faster                                                             |
| gc_traversal               | 4.90 ms                                                | 4.76 ms: 1.03x faster                                                            |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                            |
| generators                 | 28.8 ms                                                | 28.0 ms: 1.03x faster                                                            |
| async_generators           | 433 ms                                                 | 422 ms: 1.03x faster                                                             |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.03x faster                                                           |
| connected_components       | 447 ms                                                 | 436 ms: 1.02x faster                                                             |
| djangocms                  | 22.3 us                                                | 21.8 us: 1.02x faster                                                            |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.02x faster                                                             |
| shortest_path              | 487 ms                                                 | 478 ms: 1.02x faster                                                             |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.01x faster                                                           |
| genshi_xml                 | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                            |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x faster                                                             |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                             |
| create_gc_cycles           | 2.45 ms                                                | 2.45 ms: 1.00x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                             |
| sqlglot_optimize           | 53.4 ms                                                | 53.6 ms: 1.00x slower                                                            |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                                             |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                            |
| nqueens                    | 80.9 ms                                                | 81.6 ms: 1.01x slower                                                            |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                                            |
| python_startup_no_site     | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                            |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                            |
| sympy_str                  | 273 ms                                                 | 277 ms: 1.01x slower                                                             |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                            |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                             |
| logging_format             | 6.23 us                                                | 6.35 us: 1.02x slower                                                            |
| scimark_sor                | 122 ms                                                 | 125 ms: 1.02x slower                                                             |
| sympy_integrate            | 19.8 ms                                                | 20.4 ms: 1.03x slower                                                            |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.03x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 165 us: 1.03x slower                                                             |
| sympy_expand               | 456 ms                                                 | 472 ms: 1.03x slower                                                             |
| dulwich_log                | 64.6 ms                                                | 66.9 ms: 1.04x slower                                                            |
| pprint_safe_repr           | 727 ms                                                 | 752 ms: 1.04x slower                                                             |
| pickle_pure_python         | 302 us                                                 | 314 us: 1.04x slower                                                             |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                           |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                                             |
| pprint_pformat             | 1.48 sec                                               | 1.56 sec: 1.06x slower                                                           |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                            |
| chaos                      | 58.0 ms                                                | 61.7 ms: 1.06x slower                                                            |
| bench_thread_pool          | 818 us                                                 | 872 us: 1.07x slower                                                             |
| logging_silent             | 101 ns                                                 | 109 ns: 1.08x slower                                                             |
| deltablue                  | 3.19 ms                                                | 3.51 ms: 1.10x slower                                                            |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                            |
| hexiom                     | 6.08 ms                                                | 6.71 ms: 1.10x slower                                                            |
| many_optionals             | 857 us                                                 | 975 us: 1.14x slower                                                             |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 81.5 ms: 3.40x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (4): sphinx, sqlalchemy_imperative, coverage, logging_simple
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: mypy2

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x