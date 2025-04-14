# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: clang_hot
- machine: linux-x86_64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.099x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 273 ms: 1.07x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.82 sec: 1.00x faster                                                      |
| html5lib       | 73.5 ms                                                      | 66.5 ms: 1.10x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.07 sec: 1.05x faster                                                      |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 316 ms: 1.47x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 327 ms: 1.39x faster                                                        |
| async_tree_none            | 376 ms                                                       | 273 ms: 1.38x faster                                                        |
| async_tree_io              | 843 ms                                                       | 614 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 607 ms: 1.37x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 258 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 539 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 520 ms: 1.12x faster                                                        |
| async_generators           | 457 ms                                                       | 412 ms: 1.11x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.4 ms: 1.06x faster                                                       |
| Geometric mean             | (ref)                                                        | 1.24x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 67.5 ms: 1.21x faster                                                       |
| nbody          | 89.3 ms                                                      | 83.5 ms: 1.07x faster                                                       |
| pidigits       | 252 ms                                                       | 292 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 2.96 ms: 1.24x faster                                                       |
| regex_dna      | 247 ms                                                       | 218 ms: 1.13x faster                                                        |
| regex_compile  | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 25.5 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.03 sec: 1.21x faster                                                      |
| xml_etree_process    | 61.2 ms                                                      | 54.1 ms: 1.13x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 76.9 ms: 1.12x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 201 us: 1.08x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 307 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                       |
| json_loads           | 24.7 us                                                      | 25.7 us: 1.04x slower                                                       |
| xml_etree_parse      | 150 ms                                                       | 164 ms: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 9.14 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 21.9 ms: 1.20x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 51.6 ms: 1.10x faster                                                       |
| django_template | 36.4 ms                                                      | 33.1 ms: 1.10x faster                                                       |
| mako            | 10.4 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf2-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 258 us: 1.52x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 316 ms: 1.47x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 26.7 us: 1.45x faster                                                       |
| async_tree_memoization     | 453 ms                                                       | 327 ms: 1.39x faster                                                        |
| async_tree_none            | 376 ms                                                       | 273 ms: 1.38x faster                                                        |
| async_tree_io              | 843 ms                                                       | 614 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 607 ms: 1.37x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 72.0 ms: 1.35x faster                                                       |
| async_tree_none_tg         | 346 ms                                                       | 258 ms: 1.34x faster                                                        |
| scimark_sor                | 123 ms                                                       | 92.0 ms: 1.34x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.65 us: 1.34x faster                                                       |
| go                         | 162 ms                                                       | 125 ms: 1.30x faster                                                        |
| pyflate                    | 503 ms                                                       | 403 ms: 1.25x faster                                                        |
| richards                   | 52.9 ms                                                      | 42.5 ms: 1.25x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 2.96 ms: 1.24x faster                                                       |
| richards_super             | 59.6 ms                                                      | 48.2 ms: 1.23x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.03 sec: 1.21x faster                                                      |
| float                      | 81.3 ms                                                      | 67.5 ms: 1.21x faster                                                       |
| genshi_text                | 26.2 ms                                                      | 21.9 ms: 1.20x faster                                                       |
| scimark_fft                | 328 ms                                                       | 274 ms: 1.20x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 82.5 ns: 1.19x faster                                                       |
| generators                 | 33.6 ms                                                      | 29.2 ms: 1.15x faster                                                       |
| coverage                   | 80.0 ms                                                      | 70.2 ms: 1.14x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 5.76 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.20 ms: 1.14x faster                                                       |
| regex_dna                  | 247 ms                                                       | 218 ms: 1.13x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 58.4 ms: 1.13x faster                                                       |
| xml_etree_process          | 61.2 ms                                                      | 54.1 ms: 1.13x faster                                                       |
| telco                      | 8.79 ms                                                      | 7.79 ms: 1.13x faster                                                       |
| pylint                     | 347 ms                                                       | 308 ms: 1.13x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.52 sec: 1.13x faster                                                      |
| xml_etree_generate         | 86.5 ms                                                      | 76.9 ms: 1.12x faster                                                       |
| thrift                     | 901 us                                                       | 804 us: 1.12x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.54 sec: 1.12x faster                                                      |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 539 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 520 ms: 1.12x faster                                                        |
| comprehensions             | 17.0 us                                                      | 15.3 us: 1.11x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 88.8 ms: 1.11x faster                                                       |
| async_generators           | 457 ms                                                       | 412 ms: 1.11x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 66.5 ms: 1.10x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 51.6 ms: 1.10x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 766 ms: 1.10x faster                                                        |
| django_template            | 36.4 ms                                                      | 33.1 ms: 1.10x faster                                                       |
| json                       | 5.69 ms                                                      | 5.20 ms: 1.09x faster                                                       |
| deltablue                  | 3.42 ms                                                      | 3.15 ms: 1.08x faster                                                       |
| sqlglot_transpile          | 1.79 ms                                                      | 1.65 ms: 1.08x faster                                                       |
| unpickle_pure_python       | 217 us                                                       | 201 us: 1.08x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 16.3 ms: 1.08x faster                                                       |
| chaos                      | 60.2 ms                                                      | 55.9 ms: 1.08x faster                                                       |
| typing_runtime_protocols   | 169 us                                                       | 157 us: 1.08x faster                                                        |
| regex_compile              | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| sqlglot_parse              | 1.40 ms                                                      | 1.30 ms: 1.08x faster                                                       |
| sqlglot_optimize           | 59.3 ms                                                      | 55.1 ms: 1.08x faster                                                       |
| 2to3                       | 293 ms                                                       | 273 ms: 1.07x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 84.7 ms: 1.07x faster                                                       |
| nbody                      | 89.3 ms                                                      | 83.5 ms: 1.07x faster                                                       |
| sqlglot_normalize          | 119 ms                                                       | 112 ms: 1.07x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 139 ms: 1.07x faster                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.2 ms: 1.06x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 22.2 ms: 1.06x faster                                                       |
| sympy_expand               | 509 ms                                                       | 481 ms: 1.06x faster                                                        |
| sympy_str                  | 298 ms                                                       | 282 ms: 1.06x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.4 ms: 1.06x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.06 sec: 1.05x faster                                                      |
| pickle_pure_python         | 323 us                                                       | 307 us: 1.05x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.07 sec: 1.05x faster                                                      |
| raytrace                   | 273 ms                                                       | 259 ms: 1.05x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.76 us: 1.05x faster                                                       |
| sympy_sum                  | 155 ms                                                       | 147 ms: 1.05x faster                                                        |
| bench_thread_pool          | 942 us                                                       | 902 us: 1.04x faster                                                        |
| logging_simple             | 6.39 us                                                      | 6.13 us: 1.04x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 65.5 ms: 1.04x faster                                                       |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                                        |
| pycparser                  | 1.24 sec                                                     | 1.21 sec: 1.03x faster                                                      |
| regex_v8                   | 26.1 ms                                                      | 25.5 ms: 1.03x faster                                                       |
| connected_components       | 432 ms                                                       | 424 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.89 us: 1.01x faster                                                       |
| docutils                   | 2.83 sec                                                     | 2.82 sec: 1.00x faster                                                      |
| meteor_contest             | 130 ms                                                       | 131 ms: 1.01x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                       |
| fannkuch                   | 363 ms                                                       | 370 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 9.14 ms: 1.02x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 75.3 ms: 1.03x slower                                                       |
| mdp                        | 2.54 sec                                                     | 2.62 sec: 1.03x slower                                                      |
| mako                       | 10.4 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.7 us: 1.04x slower                                                       |
| many_optionals             | 930 us                                                       | 990 us: 1.06x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.86 ms: 1.07x slower                                                       |
| xml_etree_parse            | 150 ms                                                       | 164 ms: 1.09x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 5.33 ms: 1.12x slower                                                       |
| pidigits                   | 252 ms                                                       | 292 ms: 1.16x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 22.2 ms: 1.27x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 925 ms: 180.67x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.099x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.06x