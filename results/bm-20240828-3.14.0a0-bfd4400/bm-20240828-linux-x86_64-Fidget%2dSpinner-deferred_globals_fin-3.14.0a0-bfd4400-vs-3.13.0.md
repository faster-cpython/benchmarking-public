# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.030x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 261 ms: 1.02x faster                                                            |
| docutils       | 2.59 sec                                               | 2.70 sec: 1.04x slower                                                          |
| html5lib       | 64.2 ms                                                | 64.8 ms: 1.01x slower                                                           |
| tornado_http   | 92.4 ms                                                | 90.2 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 393 ms: 1.18x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 406 ms: 1.09x faster                                                            |
| async_tree_none            | 351 ms                                                 | 325 ms: 1.08x faster                                                            |
| async_tree_none_tg         | 321 ms                                                 | 300 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 560 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 531 ms: 1.03x faster                                                            |
| async_generators           | 436 ms                                                 | 434 ms: 1.01x faster                                                            |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                            |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 857 ms                                                 | 885 ms: 1.03x slower                                                            |
| async_tree_io              | 842 ms                                                 | 907 ms: 1.08x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 77.9 ms: 1.02x faster                                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                           |
| regex_effbot   | 3.73 ms                                                | 3.60 ms: 1.04x faster                                                           |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                            |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 300 us: 1.04x faster                                                            |
| tomli_loads          | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                          |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                           |
| xml_etree_process    | 60.6 ms                                                | 59.8 ms: 1.01x faster                                                           |
| unpickle_pure_python | 216 us                                                 | 214 us: 1.01x faster                                                            |
| xml_etree_generate   | 86.7 ms                                                | 86.4 ms: 1.00x faster                                                           |
| xml_etree_parse      | 156 ms                                                 | 159 ms: 1.02x slower                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 105 ms: 1.04x slower                                                            |
| json_loads           | 27.2 us                                                | 28.3 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 34.3 ms: 1.03x faster                                                           |
| genshi_text     | 23.5 ms                                                | 23.0 ms: 1.02x faster                                                           |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 259 us: 1.38x faster                                                            |
| create_gc_cycles           | 2.41 ms                                                | 1.75 ms: 1.38x faster                                                           |
| deepcopy_memo              | 39.1 us                                                | 29.8 us: 1.31x faster                                                           |
| deepcopy_reduce            | 3.20 us                                                | 2.68 us: 1.19x faster                                                           |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                           |
| async_tree_memoization_tg  | 464 ms                                                 | 393 ms: 1.18x faster                                                            |
| gc_traversal               | 4.37 ms                                                | 3.85 ms: 1.13x faster                                                           |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 406 ms: 1.09x faster                                                            |
| async_tree_none            | 351 ms                                                 | 325 ms: 1.08x faster                                                            |
| richards                   | 48.7 ms                                                | 45.4 ms: 1.07x faster                                                           |
| regex_v8                   | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                           |
| async_tree_none_tg         | 321 ms                                                 | 300 ms: 1.07x faster                                                            |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                          |
| richards_super             | 54.9 ms                                                | 51.9 ms: 1.06x faster                                                           |
| logging_format             | 6.40 us                                                | 6.07 us: 1.05x faster                                                           |
| telco                      | 8.54 ms                                                | 8.14 ms: 1.05x faster                                                           |
| logging_simple             | 5.72 us                                                | 5.45 us: 1.05x faster                                                           |
| bench_thread_pool          | 822 us                                                 | 786 us: 1.05x faster                                                            |
| raytrace                   | 267 ms                                                 | 256 ms: 1.04x faster                                                            |
| regex_effbot               | 3.73 ms                                                | 3.60 ms: 1.04x faster                                                           |
| pickle_pure_python         | 310 us                                                 | 300 us: 1.04x faster                                                            |
| go                         | 144 ms                                                 | 139 ms: 1.03x faster                                                            |
| tomli_loads                | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                          |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 560 ms: 1.03x faster                                                            |
| generators                 | 29.0 ms                                                | 28.1 ms: 1.03x faster                                                           |
| thrift                     | 809 us                                                 | 787 us: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 531 ms: 1.03x faster                                                            |
| deltablue                  | 3.23 ms                                                | 3.14 ms: 1.03x faster                                                           |
| django_template            | 35.2 ms                                                | 34.3 ms: 1.03x faster                                                           |
| crypto_pyaes               | 75.3 ms                                                | 73.5 ms: 1.03x faster                                                           |
| tornado_http               | 92.4 ms                                                | 90.2 ms: 1.02x faster                                                           |
| json_dumps                 | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                           |
| 2to3                       | 267 ms                                                 | 261 ms: 1.02x faster                                                            |
| genshi_text                | 23.5 ms                                                | 23.0 ms: 1.02x faster                                                           |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                            |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                            |
| mdp                        | 2.72 sec                                               | 2.67 sec: 1.02x faster                                                          |
| fannkuch                   | 404 ms                                                 | 396 ms: 1.02x faster                                                            |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.96 ms: 1.02x faster                                                           |
| float                      | 79.2 ms                                                | 77.9 ms: 1.02x faster                                                           |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.02x faster                                                            |
| typing_runtime_protocols   | 165 us                                                 | 162 us: 1.02x faster                                                            |
| xml_etree_process          | 60.6 ms                                                | 59.8 ms: 1.01x faster                                                           |
| sympy_expand               | 463 ms                                                 | 457 ms: 1.01x faster                                                            |
| pyflate                    | 471 ms                                                 | 464 ms: 1.01x faster                                                            |
| sympy_str                  | 275 ms                                                 | 271 ms: 1.01x faster                                                            |
| scimark_monte_carlo        | 67.4 ms                                                | 66.6 ms: 1.01x faster                                                           |
| sqlglot_optimize           | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                           |
| hexiom                     | 6.16 ms                                                | 6.10 ms: 1.01x faster                                                           |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                            |
| unpickle_pure_python       | 216 us                                                 | 214 us: 1.01x faster                                                            |
| scimark_fft                | 364 ms                                                 | 361 ms: 1.01x faster                                                            |
| sympy_integrate            | 19.9 ms                                                | 19.7 ms: 1.01x faster                                                           |
| sqlglot_transpile          | 1.58 ms                                                | 1.58 ms: 1.01x faster                                                           |
| async_generators           | 436 ms                                                 | 434 ms: 1.01x faster                                                            |
| xml_etree_generate         | 86.7 ms                                                | 86.4 ms: 1.00x faster                                                           |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                            |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.00x slower                                                            |
| nqueens                    | 78.4 ms                                                | 78.8 ms: 1.01x slower                                                           |
| bpe_tokeniser              | 4.75 sec                                               | 4.78 sec: 1.01x slower                                                          |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                           |
| html5lib                   | 64.2 ms                                                | 64.8 ms: 1.01x slower                                                           |
| regex_dna                  | 218 ms                                                 | 221 ms: 1.01x slower                                                            |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                            |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                           |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                            |
| pprint_pformat             | 1.49 sec                                               | 1.52 sec: 1.02x slower                                                          |
| xml_etree_parse            | 156 ms                                                 | 159 ms: 1.02x slower                                                            |
| scimark_sor                | 124 ms                                                 | 126 ms: 1.02x slower                                                            |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| pprint_safe_repr           | 728 ms                                                 | 746 ms: 1.03x slower                                                            |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 857 ms                                                 | 885 ms: 1.03x slower                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 105 ms: 1.04x slower                                                            |
| json_loads                 | 27.2 us                                                | 28.3 us: 1.04x slower                                                           |
| docutils                   | 2.59 sec                                               | 2.70 sec: 1.04x slower                                                          |
| async_tree_io              | 842 ms                                                 | 907 ms: 1.08x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (9): json, coverage, bench_mp_pool, comprehensions, chaos, scimark_lu, genshi_xml, nbody, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x