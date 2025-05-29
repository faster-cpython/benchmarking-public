# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: linux-x86_64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.064x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 307 ms: 1.05x slower                                                               |
| docutils       | 2.83 sec                                                     | 2.98 sec: 1.06x slower                                                             |
| html5lib       | 73.5 ms                                                      | 73.0 ms: 1.01x faster                                                              |
| sphinx         | 1.12 sec                                                     | 1.16 sec: 1.03x slower                                                             |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 372 ms: 1.25x faster                                                               |
| async_tree_io              | 843 ms                                                       | 713 ms: 1.18x faster                                                               |
| async_tree_none            | 376 ms                                                       | 319 ms: 1.18x faster                                                               |
| async_tree_io_tg           | 831 ms                                                       | 713 ms: 1.17x faster                                                               |
| async_tree_memoization     | 453 ms                                                       | 390 ms: 1.16x faster                                                               |
| async_tree_none_tg         | 346 ms                                                       | 307 ms: 1.13x faster                                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 586 ms: 1.03x faster                                                               |
| async_generators           | 457 ms                                                       | 445 ms: 1.03x faster                                                               |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 568 ms: 1.02x faster                                                               |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                               |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 84.7 ms: 1.04x slower                                                              |
| pidigits       | 252 ms                                                       | 293 ms: 1.16x slower                                                               |
| nbody          | 89.3 ms                                                      | 123 ms: 1.38x slower                                                               |
| Geometric mean | (ref)                                                        | 1.19x slower                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.01 ms: 1.22x faster                                                              |
| regex_dna      | 247 ms                                                       | 226 ms: 1.09x faster                                                               |
| regex_compile  | 143 ms                                                       | 165 ms: 1.15x slower                                                               |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.5 ms                                                      | 92.0 ms: 1.06x slower                                                              |
| xml_etree_parse      | 150 ms                                                       | 163 ms: 1.08x slower                                                               |
| json_loads           | 24.7 us                                                      | 26.7 us: 1.08x slower                                                              |
| json_dumps           | 11.1 ms                                                      | 12.3 ms: 1.10x slower                                                              |
| xml_etree_iterparse  | 103 ms                                                       | 114 ms: 1.11x slower                                                               |
| xml_etree_process    | 61.2 ms                                                      | 67.8 ms: 1.11x slower                                                              |
| tomli_loads          | 2.46 sec                                                     | 2.75 sec: 1.12x slower                                                             |
| pickle_pure_python   | 323 us                                                       | 404 us: 1.25x slower                                                               |
| unpickle_pure_python | 217 us                                                       | 275 us: 1.27x slower                                                               |
| Geometric mean       | (ref)                                                        | 1.13x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                              |
| python_startup_no_site | 8.96 ms                                                      | 9.26 ms: 1.03x slower                                                              |
| Geometric mean         | (ref)                                                        | 1.03x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 28.5 ms: 1.09x slower                                                              |
| genshi_xml      | 57.1 ms                                                      | 62.7 ms: 1.10x slower                                                              |
| django_template | 36.4 ms                                                      | 42.4 ms: 1.17x slower                                                              |
| mako            | 10.4 ms                                                      | 12.9 ms: 1.24x slower                                                              |
| Geometric mean  | (ref)                                                        | 1.15x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 372 ms: 1.25x faster                                                               |
| deepcopy                   | 392 us                                                       | 320 us: 1.22x faster                                                               |
| regex_effbot               | 3.67 ms                                                      | 3.01 ms: 1.22x faster                                                              |
| async_tree_io              | 843 ms                                                       | 713 ms: 1.18x faster                                                               |
| async_tree_none            | 376 ms                                                       | 319 ms: 1.18x faster                                                               |
| async_tree_io_tg           | 831 ms                                                       | 713 ms: 1.17x faster                                                               |
| async_tree_memoization     | 453 ms                                                       | 390 ms: 1.16x faster                                                               |
| async_tree_none_tg         | 346 ms                                                       | 307 ms: 1.13x faster                                                               |
| regex_dna                  | 247 ms                                                       | 226 ms: 1.09x faster                                                               |
| telco                      | 8.79 ms                                                      | 8.17 ms: 1.08x faster                                                              |
| deepcopy_reduce            | 3.54 us                                                      | 3.33 us: 1.06x faster                                                              |
| json                       | 5.69 ms                                                      | 5.40 ms: 1.05x faster                                                              |
| k_core                     | 2.17 sec                                                     | 2.10 sec: 1.03x faster                                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 586 ms: 1.03x faster                                                               |
| async_generators           | 457 ms                                                       | 445 ms: 1.03x faster                                                               |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 568 ms: 1.02x faster                                                               |
| deepcopy_memo              | 38.6 us                                                      | 37.9 us: 1.02x faster                                                              |
| pathlib                    | 17.5 ms                                                      | 17.4 ms: 1.01x faster                                                              |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                               |
| html5lib                   | 73.5 ms                                                      | 73.0 ms: 1.01x faster                                                              |
| shortest_path              | 460 ms                                                       | 459 ms: 1.00x faster                                                               |
| bpe_tokeniser              | 5.09 sec                                                     | 5.12 sec: 1.01x slower                                                             |
| connected_components       | 432 ms                                                       | 436 ms: 1.01x slower                                                               |
| spectral_norm              | 97.0 ms                                                      | 99.0 ms: 1.02x slower                                                              |
| pyflate                    | 503 ms                                                       | 517 ms: 1.03x slower                                                               |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                              |
| create_gc_cycles           | 2.68 ms                                                      | 2.77 ms: 1.03x slower                                                              |
| sphinx                     | 1.12 sec                                                     | 1.16 sec: 1.03x slower                                                             |
| python_startup_no_site     | 8.96 ms                                                      | 9.26 ms: 1.03x slower                                                              |
| sqlalchemy_declarative     | 148 ms                                                       | 154 ms: 1.04x slower                                                               |
| float                      | 81.3 ms                                                      | 84.7 ms: 1.04x slower                                                              |
| sympy_expand               | 509 ms                                                       | 532 ms: 1.04x slower                                                               |
| sympy_integrate            | 23.6 ms                                                      | 24.7 ms: 1.05x slower                                                              |
| 2to3                       | 293 ms                                                       | 307 ms: 1.05x slower                                                               |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                              |
| dulwich_log                | 68.2 ms                                                      | 71.5 ms: 1.05x slower                                                              |
| docutils                   | 2.83 sec                                                     | 2.98 sec: 1.06x slower                                                             |
| sqlalchemy_imperative      | 18.3 ms                                                      | 19.3 ms: 1.06x slower                                                              |
| sympy_str                  | 298 ms                                                       | 316 ms: 1.06x slower                                                               |
| sympy_sum                  | 155 ms                                                       | 164 ms: 1.06x slower                                                               |
| xml_etree_generate         | 86.5 ms                                                      | 92.0 ms: 1.06x slower                                                              |
| scimark_fft                | 328 ms                                                       | 351 ms: 1.07x slower                                                               |
| go                         | 162 ms                                                       | 175 ms: 1.08x slower                                                               |
| sqlglot_optimize           | 59.3 ms                                                      | 63.9 ms: 1.08x slower                                                              |
| typing_runtime_protocols   | 169 us                                                       | 182 us: 1.08x slower                                                               |
| xml_etree_parse            | 150 ms                                                       | 163 ms: 1.08x slower                                                               |
| json_loads                 | 24.7 us                                                      | 26.7 us: 1.08x slower                                                              |
| genshi_text                | 26.2 ms                                                      | 28.5 ms: 1.09x slower                                                              |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.21 ms: 1.09x slower                                                              |
| bench_thread_pool          | 942 us                                                       | 1.03 ms: 1.09x slower                                                              |
| sqlglot_normalize          | 119 ms                                                       | 131 ms: 1.10x slower                                                               |
| generators                 | 33.6 ms                                                      | 37.0 ms: 1.10x slower                                                              |
| genshi_xml                 | 57.1 ms                                                      | 62.7 ms: 1.10x slower                                                              |
| json_dumps                 | 11.1 ms                                                      | 12.3 ms: 1.10x slower                                                              |
| meteor_contest             | 130 ms                                                       | 143 ms: 1.10x slower                                                               |
| pycparser                  | 1.24 sec                                                     | 1.37 sec: 1.11x slower                                                             |
| xml_etree_iterparse        | 103 ms                                                       | 114 ms: 1.11x slower                                                               |
| xml_etree_process          | 61.2 ms                                                      | 67.8 ms: 1.11x slower                                                              |
| mdp                        | 2.54 sec                                                     | 2.83 sec: 1.11x slower                                                             |
| richards_super             | 59.6 ms                                                      | 66.4 ms: 1.12x slower                                                              |
| tomli_loads                | 2.46 sec                                                     | 2.75 sec: 1.12x slower                                                             |
| gc_traversal               | 4.74 ms                                                      | 5.31 ms: 1.12x slower                                                              |
| richards                   | 52.9 ms                                                      | 59.9 ms: 1.13x slower                                                              |
| many_optionals             | 930 us                                                       | 1.06 ms: 1.14x slower                                                              |
| pprint_pformat             | 1.72 sec                                                     | 1.97 sec: 1.14x slower                                                             |
| pprint_safe_repr           | 843 ms                                                       | 967 ms: 1.15x slower                                                               |
| logging_simple             | 6.39 us                                                      | 7.34 us: 1.15x slower                                                              |
| regex_compile              | 143 ms                                                       | 165 ms: 1.15x slower                                                               |
| sqlglot_transpile          | 1.79 ms                                                      | 2.07 ms: 1.16x slower                                                              |
| pidigits                   | 252 ms                                                       | 293 ms: 1.16x slower                                                               |
| logging_format             | 6.94 us                                                      | 8.07 us: 1.16x slower                                                              |
| logging_silent             | 97.9 ns                                                      | 114 ns: 1.16x slower                                                               |
| django_template            | 36.4 ms                                                      | 42.4 ms: 1.17x slower                                                              |
| crypto_pyaes               | 73.3 ms                                                      | 86.4 ms: 1.18x slower                                                              |
| comprehensions             | 17.0 us                                                      | 20.3 us: 1.19x slower                                                              |
| scimark_lu                 | 98.7 ms                                                      | 118 ms: 1.19x slower                                                               |
| scimark_sor                | 123 ms                                                       | 147 ms: 1.19x slower                                                               |
| sqlglot_parse              | 1.40 ms                                                      | 1.68 ms: 1.20x slower                                                              |
| chaos                      | 60.2 ms                                                      | 72.6 ms: 1.21x slower                                                              |
| nqueens                    | 90.7 ms                                                      | 110 ms: 1.21x slower                                                               |
| raytrace                   | 273 ms                                                       | 333 ms: 1.22x slower                                                               |
| hexiom                     | 6.55 ms                                                      | 8.11 ms: 1.24x slower                                                              |
| mako                       | 10.4 ms                                                      | 12.9 ms: 1.24x slower                                                              |
| scimark_monte_carlo        | 66.1 ms                                                      | 82.3 ms: 1.24x slower                                                              |
| pickle_pure_python         | 323 us                                                       | 404 us: 1.25x slower                                                               |
| unpickle_pure_python       | 217 us                                                       | 275 us: 1.27x slower                                                               |
| deltablue                  | 3.42 ms                                                      | 4.36 ms: 1.28x slower                                                              |
| fannkuch                   | 363 ms                                                       | 496 ms: 1.37x slower                                                               |
| nbody                      | 89.3 ms                                                      | 123 ms: 1.38x slower                                                               |
| subparsers                 | 17.5 ms                                                      | 24.9 ms: 1.42x slower                                                              |
| bench_mp_pool              | 5.12 ms                                                      | 1.09 sec: 212.43x slower                                                           |
| Geometric mean             | (ref)                                                        | 1.13x slower                                                                       |

Benchmark hidden because not significant (5): pylint, sqlite_synth, thrift, coverage, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.064x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.08x