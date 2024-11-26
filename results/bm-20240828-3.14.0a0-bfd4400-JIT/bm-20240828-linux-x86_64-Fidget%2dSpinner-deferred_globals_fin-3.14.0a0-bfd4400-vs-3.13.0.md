# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.028x faster
- HPT reliability: 93.12%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 281 ms: 1.05x slower                                                            |
| docutils       | 2.59 sec                                               | 3.00 sec: 1.16x slower                                                          |
| html5lib       | 64.2 ms                                                | 65.9 ms: 1.03x slower                                                           |
| tornado_http   | 92.4 ms                                                | 93.0 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 396 ms: 1.17x faster                                                            |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                                            |
| async_tree_none_tg         | 321 ms                                                 | 302 ms: 1.06x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 429 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 530 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                                            |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                            |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                           |
| async_generators           | 436 ms                                                 | 452 ms: 1.04x slower                                                            |
| async_tree_io              | 842 ms                                                 | 904 ms: 1.07x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.5 ms: 1.12x faster                                                           |
| nbody          | 87.0 ms                                                | 80.0 ms: 1.09x faster                                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.4 ms: 1.08x faster                                                           |
| regex_effbot   | 3.73 ms                                                | 3.50 ms: 1.07x faster                                                           |
| regex_dna      | 218 ms                                                 | 217 ms: 1.01x faster                                                            |
| regex_compile  | 132 ms                                                 | 141 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.94 sec: 1.11x faster                                                          |
| xml_etree_generate   | 86.7 ms                                                | 81.9 ms: 1.06x faster                                                           |
| xml_etree_process    | 60.6 ms                                                | 57.7 ms: 1.05x faster                                                           |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                            |
| unpickle_pure_python | 216 us                                                 | 209 us: 1.03x faster                                                            |
| pickle_pure_python   | 310 us                                                 | 303 us: 1.03x faster                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.02x faster                                                           |
| json_dumps           | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                           |
| json_loads           | 27.2 us                                                | 28.7 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 7.15 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.85 ms: 1.12x faster                                                           |
| django_template | 35.2 ms                                                | 35.7 ms: 1.01x slower                                                           |
| genshi_text     | 23.5 ms                                                | 26.0 ms: 1.10x slower                                                           |
| genshi_xml      | 50.9 ms                                                | 59.7 ms: 1.17x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 26.5 us: 1.48x faster                                                           |
| create_gc_cycles           | 2.41 ms                                                | 1.76 ms: 1.37x faster                                                           |
| deepcopy                   | 358 us                                                 | 268 us: 1.34x faster                                                            |
| richards                   | 48.7 ms                                                | 39.0 ms: 1.25x faster                                                           |
| richards_super             | 54.9 ms                                                | 44.3 ms: 1.24x faster                                                           |
| scimark_fft                | 364 ms                                                 | 306 ms: 1.19x faster                                                            |
| gc_traversal               | 4.37 ms                                                | 3.69 ms: 1.18x faster                                                           |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                           |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.30 ms: 1.17x faster                                                           |
| async_tree_memoization_tg  | 464 ms                                                 | 396 ms: 1.17x faster                                                            |
| spectral_norm              | 115 ms                                                 | 98.6 ms: 1.17x faster                                                           |
| deepcopy_reduce            | 3.20 us                                                | 2.77 us: 1.16x faster                                                           |
| crypto_pyaes               | 75.3 ms                                                | 65.5 ms: 1.15x faster                                                           |
| mako                       | 11.1 ms                                                | 9.85 ms: 1.12x faster                                                           |
| float                      | 79.2 ms                                                | 70.5 ms: 1.12x faster                                                           |
| tomli_loads                | 2.14 sec                                               | 1.94 sec: 1.11x faster                                                          |
| telco                      | 8.54 ms                                                | 7.77 ms: 1.10x faster                                                           |
| scimark_sor                | 124 ms                                                 | 114 ms: 1.09x faster                                                            |
| nbody                      | 87.0 ms                                                | 80.0 ms: 1.09x faster                                                           |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                           |
| scimark_monte_carlo        | 67.4 ms                                                | 62.4 ms: 1.08x faster                                                           |
| regex_v8                   | 26.2 ms                                                | 24.4 ms: 1.08x faster                                                           |
| fannkuch                   | 404 ms                                                 | 377 ms: 1.07x faster                                                            |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                                            |
| regex_effbot               | 3.73 ms                                                | 3.50 ms: 1.07x faster                                                           |
| logging_format             | 6.40 us                                                | 6.02 us: 1.06x faster                                                           |
| async_tree_none_tg         | 321 ms                                                 | 302 ms: 1.06x faster                                                            |
| xml_etree_generate         | 86.7 ms                                                | 81.9 ms: 1.06x faster                                                           |
| xml_etree_process          | 60.6 ms                                                | 57.7 ms: 1.05x faster                                                           |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.05x faster                                                          |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                            |
| bpe_tokeniser              | 4.75 sec                                               | 4.57 sec: 1.04x faster                                                          |
| logging_simple             | 5.72 us                                                | 5.51 us: 1.04x faster                                                           |
| deltablue                  | 3.23 ms                                                | 3.12 ms: 1.03x faster                                                           |
| pyflate                    | 471 ms                                                 | 456 ms: 1.03x faster                                                            |
| unpickle_pure_python       | 216 us                                                 | 209 us: 1.03x faster                                                            |
| logging_silent             | 102 ns                                                 | 98.7 ns: 1.03x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 429 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 530 ms: 1.03x faster                                                            |
| pickle_pure_python         | 310 us                                                 | 303 us: 1.03x faster                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 98.8 ms: 1.02x faster                                                           |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.02x faster                                                            |
| mdp                        | 2.72 sec                                               | 2.66 sec: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                                            |
| thrift                     | 809 us                                                 | 794 us: 1.02x faster                                                            |
| json_dumps                 | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                           |
| raytrace                   | 267 ms                                                 | 263 ms: 1.01x faster                                                            |
| regex_dna                  | 218 ms                                                 | 217 ms: 1.01x faster                                                            |
| bench_thread_pool          | 822 us                                                 | 816 us: 1.01x faster                                                            |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| tornado_http               | 92.4 ms                                                | 93.0 ms: 1.01x slower                                                           |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                                           |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                            |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                           |
| coverage                   | 84.0 ms                                                | 84.9 ms: 1.01x slower                                                           |
| go                         | 144 ms                                                 | 145 ms: 1.01x slower                                                            |
| django_template            | 35.2 ms                                                | 35.7 ms: 1.01x slower                                                           |
| html5lib                   | 64.2 ms                                                | 65.9 ms: 1.03x slower                                                           |
| python_startup_no_site     | 6.96 ms                                                | 7.15 ms: 1.03x slower                                                           |
| pprint_pformat             | 1.49 sec                                               | 1.55 sec: 1.04x slower                                                          |
| async_generators           | 436 ms                                                 | 452 ms: 1.04x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                           |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                                            |
| 2to3                       | 267 ms                                                 | 281 ms: 1.05x slower                                                            |
| json_loads                 | 27.2 us                                                | 28.7 us: 1.05x slower                                                           |
| sqlglot_transpile          | 1.58 ms                                                | 1.68 ms: 1.06x slower                                                           |
| typing_runtime_protocols   | 165 us                                                 | 174 us: 1.06x slower                                                            |
| regex_compile              | 132 ms                                                 | 141 ms: 1.07x slower                                                            |
| async_tree_io              | 842 ms                                                 | 904 ms: 1.07x slower                                                            |
| sqlglot_optimize           | 53.7 ms                                                | 57.9 ms: 1.08x slower                                                           |
| hexiom                     | 6.16 ms                                                | 6.76 ms: 1.10x slower                                                           |
| genshi_text                | 23.5 ms                                                | 26.0 ms: 1.10x slower                                                           |
| nqueens                    | 78.4 ms                                                | 86.6 ms: 1.10x slower                                                           |
| sympy_expand               | 463 ms                                                 | 513 ms: 1.11x slower                                                            |
| sympy_str                  | 275 ms                                                 | 305 ms: 1.11x slower                                                            |
| generators                 | 29.0 ms                                                | 32.8 ms: 1.13x slower                                                           |
| sympy_integrate            | 19.9 ms                                                | 23.0 ms: 1.15x slower                                                           |
| docutils                   | 2.59 sec                                               | 3.00 sec: 1.16x slower                                                          |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.17x slower                                                            |
| genshi_xml                 | 50.9 ms                                                | 59.7 ms: 1.17x slower                                                           |
| pylint                     | 313 ms                                                 | 368 ms: 1.18x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (6): scimark_lu, bench_mp_pool, json, chaos, pprint_safe_repr, async_tree_io_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240828-3.14.0a0-bfd4400-JIT/bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 93.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x