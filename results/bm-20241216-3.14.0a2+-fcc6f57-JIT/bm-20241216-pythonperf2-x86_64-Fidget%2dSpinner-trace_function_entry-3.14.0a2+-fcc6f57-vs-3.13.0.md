# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-x86_64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.031x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 289 ms: 1.01x faster                                                                   |
| docutils       | 2.83 sec                                                     | 3.01 sec: 1.07x slower                                                                 |
| html5lib       | 73.5 ms                                                      | 68.9 ms: 1.07x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 335 ms: 1.39x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 662 ms: 1.27x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 654 ms: 1.27x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 296 ms: 1.27x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 274 ms: 1.26x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 362 ms: 1.25x faster                                                                   |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 527 ms: 1.15x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                                   |
| async_generators           | 457 ms                                                       | 429 ms: 1.06x faster                                                                   |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.18x faster                                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 79.3 ms: 1.03x faster                                                                  |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                                   |
| nbody          | 89.3 ms                                                      | 91.2 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.26 ms: 1.13x faster                                                                  |
| regex_compile  | 143 ms                                                       | 139 ms: 1.02x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                           |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.10 sec: 1.17x faster                                                                 |
| xml_etree_parse      | 150 ms                                                       | 135 ms: 1.12x faster                                                                   |
| unpickle_pure_python | 217 us                                                       | 198 us: 1.10x faster                                                                   |
| xml_etree_generate   | 86.5 ms                                                      | 79.3 ms: 1.09x faster                                                                  |
| xml_etree_process    | 61.2 ms                                                      | 56.4 ms: 1.08x faster                                                                  |
| xml_etree_iterparse  | 103 ms                                                       | 96.3 ms: 1.07x faster                                                                  |
| json_dumps           | 11.1 ms                                                      | 11.2 ms: 1.01x slower                                                                  |
| json_loads           | 24.7 us                                                      | 25.4 us: 1.03x slower                                                                  |
| pickle_pure_python   | 323 us                                                       | 339 us: 1.05x slower                                                                   |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.08 ms: 1.01x slower                                                                  |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.02x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.47 ms: 1.10x faster                                                                  |
| genshi_text     | 26.2 ms                                                      | 25.5 ms: 1.03x faster                                                                  |
| genshi_xml      | 57.1 ms                                                      | 57.7 ms: 1.01x slower                                                                  |
| django_template | 36.4 ms                                                      | 38.5 ms: 1.06x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 335 ms: 1.39x faster                                                                   |
| deepcopy                   | 392 us                                                       | 291 us: 1.35x faster                                                                   |
| deepcopy_memo              | 38.6 us                                                      | 29.9 us: 1.29x faster                                                                  |
| async_tree_io              | 843 ms                                                       | 662 ms: 1.27x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 654 ms: 1.27x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 296 ms: 1.27x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 274 ms: 1.26x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 362 ms: 1.25x faster                                                                   |
| deepcopy_reduce            | 3.54 us                                                      | 2.95 us: 1.20x faster                                                                  |
| tomli_loads                | 2.46 sec                                                     | 2.10 sec: 1.17x faster                                                                 |
| telco                      | 8.79 ms                                                      | 7.63 ms: 1.15x faster                                                                  |
| go                         | 162 ms                                                       | 141 ms: 1.15x faster                                                                   |
| pyflate                    | 503 ms                                                       | 437 ms: 1.15x faster                                                                   |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 527 ms: 1.15x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                                   |
| regex_effbot               | 3.67 ms                                                      | 3.26 ms: 1.13x faster                                                                  |
| xml_etree_parse            | 150 ms                                                       | 135 ms: 1.12x faster                                                                   |
| generators                 | 33.6 ms                                                      | 30.4 ms: 1.10x faster                                                                  |
| unpickle_pure_python       | 217 us                                                       | 198 us: 1.10x faster                                                                   |
| mako                       | 10.4 ms                                                      | 9.47 ms: 1.10x faster                                                                  |
| scimark_fft                | 328 ms                                                       | 300 ms: 1.09x faster                                                                   |
| xml_etree_generate         | 86.5 ms                                                      | 79.3 ms: 1.09x faster                                                                  |
| spectral_norm              | 97.0 ms                                                      | 88.9 ms: 1.09x faster                                                                  |
| dulwich_log                | 68.2 ms                                                      | 62.9 ms: 1.08x faster                                                                  |
| xml_etree_process          | 61.2 ms                                                      | 56.4 ms: 1.08x faster                                                                  |
| bpe_tokeniser              | 5.09 sec                                                     | 4.69 sec: 1.08x faster                                                                 |
| json                       | 5.69 ms                                                      | 5.27 ms: 1.08x faster                                                                  |
| connected_components       | 432 ms                                                       | 401 ms: 1.08x faster                                                                   |
| scimark_sor                | 123 ms                                                       | 115 ms: 1.07x faster                                                                   |
| xml_etree_iterparse        | 103 ms                                                       | 96.3 ms: 1.07x faster                                                                  |
| html5lib                   | 73.5 ms                                                      | 68.9 ms: 1.07x faster                                                                  |
| async_generators           | 457 ms                                                       | 429 ms: 1.06x faster                                                                   |
| k_core                     | 2.17 sec                                                     | 2.04 sec: 1.06x faster                                                                 |
| pylint                     | 347 ms                                                       | 326 ms: 1.06x faster                                                                   |
| pathlib                    | 17.5 ms                                                      | 16.6 ms: 1.05x faster                                                                  |
| shortest_path              | 460 ms                                                       | 439 ms: 1.05x faster                                                                   |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.3 ms: 1.04x faster                                                                  |
| pprint_safe_repr           | 843 ms                                                       | 808 ms: 1.04x faster                                                                   |
| pprint_pformat             | 1.72 sec                                                     | 1.65 sec: 1.04x faster                                                                 |
| sqlalchemy_declarative     | 148 ms                                                       | 144 ms: 1.03x faster                                                                   |
| sqlite_synth               | 2.91 us                                                      | 2.81 us: 1.03x faster                                                                  |
| genshi_text                | 26.2 ms                                                      | 25.5 ms: 1.03x faster                                                                  |
| float                      | 81.3 ms                                                      | 79.3 ms: 1.03x faster                                                                  |
| regex_compile              | 143 ms                                                       | 139 ms: 1.02x faster                                                                   |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                                  |
| 2to3                       | 293 ms                                                       | 289 ms: 1.01x faster                                                                   |
| mdp                        | 2.54 sec                                                     | 2.51 sec: 1.01x faster                                                                 |
| nqueens                    | 90.7 ms                                                      | 89.7 ms: 1.01x faster                                                                  |
| scimark_lu                 | 98.7 ms                                                      | 97.9 ms: 1.01x faster                                                                  |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.2 ms: 1.01x faster                                                                  |
| richards                   | 52.9 ms                                                      | 52.6 ms: 1.01x faster                                                                  |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                                   |
| json_dumps                 | 11.1 ms                                                      | 11.2 ms: 1.01x slower                                                                  |
| sympy_sum                  | 155 ms                                                       | 156 ms: 1.01x slower                                                                   |
| genshi_xml                 | 57.1 ms                                                      | 57.7 ms: 1.01x slower                                                                  |
| sympy_integrate            | 23.6 ms                                                      | 23.8 ms: 1.01x slower                                                                  |
| python_startup_no_site     | 8.96 ms                                                      | 9.08 ms: 1.01x slower                                                                  |
| coverage                   | 80.0 ms                                                      | 81.1 ms: 1.01x slower                                                                  |
| sympy_str                  | 298 ms                                                       | 302 ms: 1.01x slower                                                                   |
| create_gc_cycles           | 2.68 ms                                                      | 2.72 ms: 1.01x slower                                                                  |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.02x slower                                                                  |
| meteor_contest             | 130 ms                                                       | 132 ms: 1.02x slower                                                                   |
| nbody                      | 89.3 ms                                                      | 91.2 ms: 1.02x slower                                                                  |
| sympy_expand               | 509 ms                                                       | 520 ms: 1.02x slower                                                                   |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.89 ms: 1.02x slower                                                                  |
| crypto_pyaes               | 73.3 ms                                                      | 75.2 ms: 1.03x slower                                                                  |
| fannkuch                   | 363 ms                                                       | 373 ms: 1.03x slower                                                                   |
| json_loads                 | 24.7 us                                                      | 25.4 us: 1.03x slower                                                                  |
| hexiom                     | 6.55 ms                                                      | 6.77 ms: 1.03x slower                                                                  |
| logging_silent             | 97.9 ns                                                      | 101 ns: 1.03x slower                                                                   |
| sqlglot_normalize          | 119 ms                                                       | 125 ms: 1.04x slower                                                                   |
| pycparser                  | 1.24 sec                                                     | 1.30 sec: 1.05x slower                                                                 |
| pickle_pure_python         | 323 us                                                       | 339 us: 1.05x slower                                                                   |
| sqlglot_optimize           | 59.3 ms                                                      | 62.5 ms: 1.05x slower                                                                  |
| django_template            | 36.4 ms                                                      | 38.5 ms: 1.06x slower                                                                  |
| sqlglot_transpile          | 1.79 ms                                                      | 1.90 ms: 1.06x slower                                                                  |
| docutils                   | 2.83 sec                                                     | 3.01 sec: 1.07x slower                                                                 |
| sqlglot_parse              | 1.40 ms                                                      | 1.49 ms: 1.07x slower                                                                  |
| deltablue                  | 3.42 ms                                                      | 3.70 ms: 1.08x slower                                                                  |
| typing_runtime_protocols   | 169 us                                                       | 186 us: 1.10x slower                                                                   |
| chaos                      | 60.2 ms                                                      | 67.8 ms: 1.13x slower                                                                  |
| comprehensions             | 17.0 us                                                      | 19.3 us: 1.13x slower                                                                  |
| many_optionals             | 930 us                                                       | 1.07 ms: 1.15x slower                                                                  |
| raytrace                   | 273 ms                                                       | 315 ms: 1.15x slower                                                                   |
| subparsers                 | 17.5 ms                                                      | 23.9 ms: 1.37x slower                                                                  |
| gc_traversal               | 4.74 ms                                                      | 6.53 ms: 1.38x slower                                                                  |
| bench_mp_pool              | 5.12 ms                                                      | 938 ms: 183.23x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                           |

Benchmark hidden because not significant (10): regex_v8, thrift, djangocms, richards_super, regex_dna, logging_simple, asyncio_websockets, logging_format, sphinx, bench_thread_pool
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: mypy2

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x