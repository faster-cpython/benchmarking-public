# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: eliminate_func_guard
- machine: linux-x86_64
- commit hash: 6d6263c
- commit date: 2024-11-04
- overall geometric mean: 1.006x slower
- HPT reliability: 84.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 280 ms: 1.05x slower                                                             |
| docutils       | 2.59 sec                                               | 2.95 sec: 1.14x slower                                                           |
| html5lib       | 64.2 ms                                                | 67.0 ms: 1.04x slower                                                            |
| sphinx         | 1.03 sec                                               | 1.17 sec: 1.13x slower                                                           |
| tornado_http   | 92.4 ms                                                | 94.9 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 381 ms: 1.22x faster                                                             |
| async_tree_none            | 351 ms                                                 | 331 ms: 1.06x faster                                                             |
| async_tree_memoization     | 442 ms                                                 | 419 ms: 1.06x faster                                                             |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 555 ms: 1.02x slower                                                             |
| async_tree_io              | 842 ms                                                 | 863 ms: 1.02x slower                                                             |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                            |
| async_generators           | 436 ms                                                 | 448 ms: 1.03x slower                                                             |
| async_tree_io_tg           | 857 ms                                                 | 983 ms: 1.15x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.7 ms: 1.05x faster                                                            |
| float          | 79.2 ms                                                | 76.1 ms: 1.04x faster                                                            |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                            |
| regex_dna      | 218 ms                                                 | 220 ms: 1.01x slower                                                             |
| regex_effbot   | 3.73 ms                                                | 3.81 ms: 1.02x slower                                                            |
| regex_compile  | 132 ms                                                 | 140 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                           |
| xml_etree_generate   | 86.7 ms                                                | 79.0 ms: 1.10x faster                                                            |
| xml_etree_process    | 60.6 ms                                                | 56.2 ms: 1.08x faster                                                            |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                             |
| json_loads           | 27.2 us                                                | 26.8 us: 1.02x faster                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 100 ms: 1.01x faster                                                             |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                                             |
| pickle_pure_python   | 310 us                                                 | 325 us: 1.05x slower                                                             |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.11 ms: 1.02x slower                                                            |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                            |
| django_template | 35.2 ms                                                | 36.2 ms: 1.03x slower                                                            |
| genshi_text     | 23.5 ms                                                | 24.7 ms: 1.05x slower                                                            |
| genshi_xml      | 50.9 ms                                                | 58.6 ms: 1.15x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 271 us: 1.32x faster                                                             |
| deepcopy_memo              | 39.1 us                                                | 29.6 us: 1.32x faster                                                            |
| async_tree_memoization_tg  | 464 ms                                                 | 381 ms: 1.22x faster                                                             |
| deepcopy_reduce            | 3.20 us                                                | 2.69 us: 1.19x faster                                                            |
| richards                   | 48.7 ms                                                | 41.9 ms: 1.16x faster                                                            |
| scimark_fft                | 364 ms                                                 | 320 ms: 1.14x faster                                                             |
| richards_super             | 54.9 ms                                                | 48.2 ms: 1.14x faster                                                            |
| telco                      | 8.54 ms                                                | 7.68 ms: 1.11x faster                                                            |
| crypto_pyaes               | 75.3 ms                                                | 68.1 ms: 1.11x faster                                                            |
| tomli_loads                | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                           |
| xml_etree_generate         | 86.7 ms                                                | 79.0 ms: 1.10x faster                                                            |
| mako                       | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                            |
| json                       | 5.36 ms                                                | 4.96 ms: 1.08x faster                                                            |
| xml_etree_process          | 60.6 ms                                                | 56.2 ms: 1.08x faster                                                            |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                            |
| go                         | 144 ms                                                 | 133 ms: 1.08x faster                                                             |
| mdp                        | 2.72 sec                                               | 2.55 sec: 1.07x faster                                                           |
| bpe_tokeniser              | 4.75 sec                                               | 4.46 sec: 1.07x faster                                                           |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                             |
| async_tree_none            | 351 ms                                                 | 331 ms: 1.06x faster                                                             |
| async_tree_memoization     | 442 ms                                                 | 419 ms: 1.06x faster                                                             |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.78 ms: 1.05x faster                                                            |
| nbody                      | 87.0 ms                                                | 82.7 ms: 1.05x faster                                                            |
| logging_format             | 6.40 us                                                | 6.13 us: 1.04x faster                                                            |
| float                      | 79.2 ms                                                | 76.1 ms: 1.04x faster                                                            |
| scimark_monte_carlo        | 67.4 ms                                                | 64.8 ms: 1.04x faster                                                            |
| scimark_sor                | 124 ms                                                 | 119 ms: 1.04x faster                                                             |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                           |
| regex_v8                   | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                            |
| thrift                     | 809 us                                                 | 784 us: 1.03x faster                                                             |
| pyflate                    | 471 ms                                                 | 458 ms: 1.03x faster                                                             |
| connected_components       | 444 ms                                                 | 437 ms: 1.02x faster                                                             |
| json_loads                 | 27.2 us                                                | 26.8 us: 1.02x faster                                                            |
| logging_simple             | 5.72 us                                                | 5.64 us: 1.01x faster                                                            |
| pprint_pformat             | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                           |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                             |
| pprint_safe_repr           | 728 ms                                                 | 721 ms: 1.01x faster                                                             |
| xml_etree_iterparse        | 101 ms                                                 | 100 ms: 1.01x faster                                                             |
| logging_silent             | 102 ns                                                 | 101 ns: 1.01x faster                                                             |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                             |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                             |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.01x slower                                                             |
| regex_dna                  | 218 ms                                                 | 220 ms: 1.01x slower                                                             |
| coverage                   | 84.0 ms                                                | 84.8 ms: 1.01x slower                                                            |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.01x slower                                                             |
| typing_runtime_protocols   | 165 us                                                 | 167 us: 1.02x slower                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 555 ms: 1.02x slower                                                             |
| regex_effbot               | 3.73 ms                                                | 3.81 ms: 1.02x slower                                                            |
| python_startup_no_site     | 6.96 ms                                                | 7.11 ms: 1.02x slower                                                            |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                            |
| deltablue                  | 3.23 ms                                                | 3.30 ms: 1.02x slower                                                            |
| async_tree_io              | 842 ms                                                 | 863 ms: 1.02x slower                                                             |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                            |
| tornado_http               | 92.4 ms                                                | 94.9 ms: 1.03x slower                                                            |
| async_generators           | 436 ms                                                 | 448 ms: 1.03x slower                                                             |
| chaos                      | 58.1 ms                                                | 59.7 ms: 1.03x slower                                                            |
| django_template            | 35.2 ms                                                | 36.2 ms: 1.03x slower                                                            |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.6 ms: 1.03x slower                                                            |
| html5lib                   | 64.2 ms                                                | 67.0 ms: 1.04x slower                                                            |
| pickle_pure_python         | 310 us                                                 | 325 us: 1.05x slower                                                             |
| gc_traversal               | 4.37 ms                                                | 4.57 ms: 1.05x slower                                                            |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                            |
| 2to3                       | 267 ms                                                 | 280 ms: 1.05x slower                                                             |
| genshi_text                | 23.5 ms                                                | 24.7 ms: 1.05x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.05x slower                                                            |
| raytrace                   | 267 ms                                                 | 280 ms: 1.05x slower                                                             |
| comprehensions             | 16.5 us                                                | 17.3 us: 1.05x slower                                                            |
| dulwich_log                | 64.3 ms                                                | 67.7 ms: 1.05x slower                                                            |
| regex_compile              | 132 ms                                                 | 140 ms: 1.06x slower                                                             |
| sqlglot_normalize          | 108 ms                                                 | 115 ms: 1.07x slower                                                             |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.07x slower                                                            |
| bench_thread_pool          | 822 us                                                 | 888 us: 1.08x slower                                                             |
| sympy_expand               | 463 ms                                                 | 504 ms: 1.09x slower                                                             |
| sqlalchemy_declarative     | 133 ms                                                 | 147 ms: 1.10x slower                                                             |
| sympy_str                  | 275 ms                                                 | 303 ms: 1.10x slower                                                             |
| create_gc_cycles           | 2.41 ms                                                | 2.67 ms: 1.11x slower                                                            |
| sqlglot_optimize           | 53.7 ms                                                | 59.7 ms: 1.11x slower                                                            |
| nqueens                    | 78.4 ms                                                | 87.9 ms: 1.12x slower                                                            |
| sphinx                     | 1.03 sec                                               | 1.17 sec: 1.13x slower                                                           |
| docutils                   | 2.59 sec                                               | 2.95 sec: 1.14x slower                                                           |
| hexiom                     | 6.16 ms                                                | 7.06 ms: 1.15x slower                                                            |
| async_tree_io_tg           | 857 ms                                                 | 983 ms: 1.15x slower                                                             |
| genshi_xml                 | 50.9 ms                                                | 58.6 ms: 1.15x slower                                                            |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.17x slower                                                             |
| sympy_integrate            | 19.9 ms                                                | 23.5 ms: 1.18x slower                                                            |
| pylint                     | 313 ms                                                 | 379 ms: 1.21x slower                                                             |
| generators                 | 29.0 ms                                                | 35.4 ms: 1.22x slower                                                            |
| k_core                     | 2.35 sec                                               | 3.58 sec: 1.52x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 84.4 ms: 3.52x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, spectral_norm, shortest_path, fannkuch, async_tree_none_tg
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2
Ignored benchmarks (1) of results/bm-20241104-3.14.0a1+-6d6263c-JIT/bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c.json: sqlite_synth

- Geometric mean (including insignificant results): 1.006x slower
# HPT report

- Reliability score: 84.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x