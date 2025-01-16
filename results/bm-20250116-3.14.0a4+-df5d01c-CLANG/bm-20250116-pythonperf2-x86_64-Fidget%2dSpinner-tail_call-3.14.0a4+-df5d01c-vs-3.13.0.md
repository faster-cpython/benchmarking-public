# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-x86_64
- commit hash: df5d01c
- commit date: 2025-01-16
- overall geometric mean: 1.093x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 274 ms: 1.07x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                      |
| html5lib       | 73.5 ms                                                      | 66.0 ms: 1.11x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 315 ms: 1.48x faster                                                        |
| async_tree_none            | 376 ms                                                       | 271 ms: 1.39x faster                                                        |
| async_tree_io              | 843 ms                                                       | 610 ms: 1.38x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 334 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 613 ms: 1.36x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 257 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 532 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 517 ms: 1.12x faster                                                        |
| async_generators           | 457 ms                                                       | 421 ms: 1.08x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.23x faster                                                                |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 66.9 ms: 1.22x faster                                                       |
| pidigits       | 252 ms                                                       | 285 ms: 1.13x slower                                                        |
| nbody          | 89.3 ms                                                      | 101 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 2.98 ms: 1.23x faster                                                       |
| regex_dna      | 247 ms                                                       | 226 ms: 1.09x faster                                                        |
| regex_compile  | 143 ms                                                       | 134 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.99 sec: 1.24x faster                                                      |
| xml_etree_process    | 61.2 ms                                                      | 55.6 ms: 1.10x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 79.0 ms: 1.09x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 202 us: 1.08x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 311 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| json_loads           | 24.7 us                                                      | 25.2 us: 1.02x slower                                                       |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                       |
| xml_etree_parse      | 150 ms                                                       | 162 ms: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 9.02 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 22.0 ms: 1.19x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 52.6 ms: 1.08x faster                                                       |
| django_template | 36.4 ms                                                      | 34.0 ms: 1.07x faster                                                       |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 263 us: 1.49x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 315 ms: 1.48x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 27.0 us: 1.43x faster                                                       |
| async_tree_none            | 376 ms                                                       | 271 ms: 1.39x faster                                                        |
| go                         | 162 ms                                                       | 117 ms: 1.39x faster                                                        |
| async_tree_io              | 843 ms                                                       | 610 ms: 1.38x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 334 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 613 ms: 1.36x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 257 ms: 1.35x faster                                                        |
| scimark_sor                | 123 ms                                                       | 95.1 ms: 1.30x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.75 us: 1.29x faster                                                       |
| scimark_fft                | 328 ms                                                       | 258 ms: 1.27x faster                                                        |
| richards                   | 52.9 ms                                                      | 42.1 ms: 1.26x faster                                                       |
| pyflate                    | 503 ms                                                       | 405 ms: 1.24x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.99 sec: 1.24x faster                                                      |
| regex_effbot               | 3.67 ms                                                      | 2.98 ms: 1.23x faster                                                       |
| richards_super             | 59.6 ms                                                      | 48.4 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 3.88 ms: 1.23x faster                                                       |
| float                      | 81.3 ms                                                      | 66.9 ms: 1.22x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 54.8 ms: 1.21x faster                                                       |
| spectral_norm              | 97.0 ms                                                      | 80.7 ms: 1.20x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 82.5 ms: 1.20x faster                                                       |
| genshi_text                | 26.2 ms                                                      | 22.0 ms: 1.19x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 82.8 ns: 1.18x faster                                                       |
| generators                 | 33.6 ms                                                      | 28.5 ms: 1.18x faster                                                       |
| telco                      | 8.79 ms                                                      | 7.54 ms: 1.17x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 5.65 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 532 ms: 1.14x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 15.6 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 517 ms: 1.12x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.56 sec: 1.12x faster                                                      |
| sqlglot_parse              | 1.40 ms                                                      | 1.26 ms: 1.11x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 66.0 ms: 1.11x faster                                                       |
| xml_etree_process          | 61.2 ms                                                      | 55.6 ms: 1.10x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 767 ms: 1.10x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.57 sec: 1.10x faster                                                      |
| deltablue                  | 3.42 ms                                                      | 3.12 ms: 1.10x faster                                                       |
| pylint                     | 347 ms                                                       | 317 ms: 1.10x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 79.0 ms: 1.09x faster                                                       |
| coverage                   | 80.0 ms                                                      | 73.2 ms: 1.09x faster                                                       |
| regex_dna                  | 247 ms                                                       | 226 ms: 1.09x faster                                                        |
| thrift                     | 901 us                                                       | 827 us: 1.09x faster                                                        |
| async_generators           | 457 ms                                                       | 421 ms: 1.08x faster                                                        |
| json                       | 5.69 ms                                                      | 5.24 ms: 1.08x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 52.6 ms: 1.08x faster                                                       |
| sqlglot_transpile          | 1.79 ms                                                      | 1.65 ms: 1.08x faster                                                       |
| comprehensions             | 17.0 us                                                      | 15.8 us: 1.08x faster                                                       |
| unpickle_pure_python       | 217 us                                                       | 202 us: 1.08x faster                                                        |
| raytrace                   | 273 ms                                                       | 254 ms: 1.07x faster                                                        |
| django_template            | 36.4 ms                                                      | 34.0 ms: 1.07x faster                                                       |
| 2to3                       | 293 ms                                                       | 274 ms: 1.07x faster                                                        |
| regex_compile              | 143 ms                                                       | 134 ms: 1.06x faster                                                        |
| sympy_str                  | 298 ms                                                       | 282 ms: 1.06x faster                                                        |
| logging_simple             | 6.39 us                                                      | 6.05 us: 1.06x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.05 sec: 1.06x faster                                                      |
| sympy_expand               | 509 ms                                                       | 483 ms: 1.06x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 64.9 ms: 1.05x faster                                                       |
| sympy_sum                  | 155 ms                                                       | 148 ms: 1.05x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 22.5 ms: 1.05x faster                                                       |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.5 ms: 1.05x faster                                                       |
| bench_thread_pool          | 942 us                                                       | 901 us: 1.05x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 86.9 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.79 us: 1.04x faster                                                       |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.04x faster                                                        |
| pickle_pure_python         | 323 us                                                       | 311 us: 1.04x faster                                                        |
| chaos                      | 60.2 ms                                                      | 58.1 ms: 1.04x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.71 us: 1.03x faster                                                       |
| sqlglot_optimize           | 59.3 ms                                                      | 57.3 ms: 1.03x faster                                                       |
| sqlglot_normalize          | 119 ms                                                       | 115 ms: 1.03x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| shortest_path              | 460 ms                                                       | 446 ms: 1.03x faster                                                        |
| typing_runtime_protocols   | 169 us                                                       | 165 us: 1.03x faster                                                        |
| pycparser                  | 1.24 sec                                                     | 1.21 sec: 1.02x faster                                                      |
| connected_components       | 432 ms                                                       | 426 ms: 1.02x faster                                                        |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.01x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| fannkuch                   | 363 ms                                                       | 359 ms: 1.01x faster                                                        |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.00x slower                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 9.02 ms: 1.01x slower                                                       |
| docutils                   | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                      |
| json_loads                 | 24.7 us                                                      | 25.2 us: 1.02x slower                                                       |
| mdp                        | 2.54 sec                                                     | 2.60 sec: 1.02x slower                                                      |
| crypto_pyaes               | 73.3 ms                                                      | 75.1 ms: 1.03x slower                                                       |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                       |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.87 ms: 1.07x slower                                                       |
| xml_etree_parse            | 150 ms                                                       | 162 ms: 1.07x slower                                                        |
| many_optionals             | 930 us                                                       | 1.02 ms: 1.10x slower                                                       |
| pidigits                   | 252 ms                                                       | 285 ms: 1.13x slower                                                        |
| nbody                      | 89.3 ms                                                      | 101 ms: 1.13x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 5.72 ms: 1.21x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 22.8 ms: 1.30x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 1.54 sec: 301.28x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (2): coroutines, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.093x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.07x