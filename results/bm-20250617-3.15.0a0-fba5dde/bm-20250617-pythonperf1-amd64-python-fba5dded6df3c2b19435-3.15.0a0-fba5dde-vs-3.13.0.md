# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.259x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 295 ms: 1.37x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.08 sec: 1.36x slower                                                     |
| html5lib       | 38.2 ms                                                     | 51.5 ms: 1.35x slower                                                      |
| sphinx         | 617 ms                                                      | 838 ms: 1.36x slower                                                       |
| Geometric mean | (ref)                                                       | 1.36x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 292 ms: 1.04x slower                                                       |
| async_tree_io              | 513 ms                                                      | 546 ms: 1.06x slower                                                       |
| async_tree_none            | 219 ms                                                      | 242 ms: 1.11x slower                                                       |
| async_tree_memoization     | 265 ms                                                      | 295 ms: 1.11x slower                                                       |
| async_tree_io_tg           | 497 ms                                                      | 561 ms: 1.13x slower                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 438 ms: 1.15x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 440 ms: 1.16x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 235 ms: 1.17x slower                                                       |
| async_generators           | 223 ms                                                      | 332 ms: 1.49x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 24.7 ms: 1.97x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 76.0 ms: 1.49x slower                                                      |
| nbody          | 66.3 ms                                                     | 99.6 ms: 1.50x slower                                                      |
| Geometric mean | (ref)                                                       | 1.31x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 17.0 ms: 1.40x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.73 ms: 1.02x slower                                                      |
| regex_compile  | 80.7 ms                                                     | 122 ms: 1.51x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 108 ms: 1.17x slower                                                       |
| json_loads           | 15.1 us                                                     | 21.1 us: 1.40x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 8.83 ms: 1.43x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.02 sec: 1.47x slower                                                     |
| xml_etree_iterparse  | 60.5 ms                                                     | 89.5 ms: 1.48x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 89.3 ms: 1.67x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 64.0 ms: 1.75x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 358 us: 1.93x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 275 us: 2.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.58x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.2 ms: 1.11x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.0 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 48.3 ms: 1.42x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 23.3 ms: 1.53x slower                                                      |
| django_template | 20.3 ms                                                     | 36.3 ms: 1.79x slower                                                      |
| mako            | 6.56 ms                                                     | 12.4 ms: 1.88x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.65x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 692 us: 12.23x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 34.3 ms: 2.20x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 17.0 ms: 1.40x faster                                                      |
| mdp                        | 1.43 sec                                                    | 1.15 sec: 1.25x faster                                                     |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.01x slower                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.73 ms: 1.02x slower                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 292 ms: 1.04x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.81 sec: 1.06x slower                                                     |
| async_tree_io              | 513 ms                                                      | 546 ms: 1.06x slower                                                       |
| shortest_path              | 355 ms                                                      | 380 ms: 1.07x slower                                                       |
| connected_components       | 320 ms                                                      | 347 ms: 1.08x slower                                                       |
| async_tree_none            | 219 ms                                                      | 242 ms: 1.11x slower                                                       |
| async_tree_memoization     | 265 ms                                                      | 295 ms: 1.11x slower                                                       |
| python_startup             | 24.4 ms                                                     | 27.2 ms: 1.11x slower                                                      |
| async_tree_io_tg           | 497 ms                                                      | 561 ms: 1.13x slower                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 438 ms: 1.15x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 440 ms: 1.16x slower                                                       |
| deepcopy                   | 223 us                                                      | 262 us: 1.17x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.86 us: 1.17x slower                                                      |
| async_tree_none_tg         | 200 ms                                                      | 235 ms: 1.17x slower                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 108 ms: 1.17x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.0 ms: 1.18x slower                                                      |
| pylint                     | 205 ms                                                      | 247 ms: 1.20x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.48 ms: 1.21x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 987 us: 1.22x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 105 ms: 1.25x slower                                                       |
| json                       | 3.30 ms                                                     | 4.17 ms: 1.26x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 50.8 ms: 1.27x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 92.3 ms: 1.28x slower                                                      |
| telco                      | 4.85 ms                                                     | 6.25 ms: 1.29x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 16.4 ms: 1.33x slower                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 2.71 us: 1.34x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 115 ms: 1.34x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 51.5 ms: 1.35x slower                                                      |
| sphinx                     | 617 ms                                                      | 838 ms: 1.36x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.08 sec: 1.36x slower                                                     |
| 2to3                       | 215 ms                                                      | 295 ms: 1.37x slower                                                       |
| coverage                   | 45.3 ms                                                     | 62.3 ms: 1.37x slower                                                      |
| sympy_str                  | 167 ms                                                      | 231 ms: 1.38x slower                                                       |
| sympy_expand               | 286 ms                                                      | 396 ms: 1.39x slower                                                       |
| json_loads                 | 15.1 us                                                     | 21.1 us: 1.40x slower                                                      |
| pycparser                  | 695 ms                                                      | 974 ms: 1.40x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 48.3 ms: 1.42x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 8.83 ms: 1.43x slower                                                      |
| deepcopy_memo              | 23.1 us                                                     | 33.0 us: 1.43x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 2.02 sec: 1.47x slower                                                     |
| xml_etree_iterparse        | 60.5 ms                                                     | 89.5 ms: 1.48x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 153 us: 1.48x slower                                                       |
| async_generators           | 223 ms                                                      | 332 ms: 1.49x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 4.28 sec: 1.49x slower                                                     |
| float                      | 50.8 ms                                                     | 76.0 ms: 1.49x slower                                                      |
| nbody                      | 66.3 ms                                                     | 99.6 ms: 1.50x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 122 ms: 1.51x slower                                                       |
| many_optionals             | 361 us                                                      | 547 us: 1.52x slower                                                       |
| scimark_fft                | 175 ms                                                      | 265 ms: 1.52x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 23.3 ms: 1.53x slower                                                      |
| go                         | 84.7 ms                                                     | 131 ms: 1.55x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 3.05 ms: 1.55x slower                                                      |
| logging_format             | 6.18 us                                                     | 9.74 us: 1.58x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 4.16 ms: 1.60x slower                                                      |
| pyflate                    | 283 ms                                                      | 453 ms: 1.60x slower                                                       |
| logging_simple             | 5.77 us                                                     | 9.25 us: 1.60x slower                                                      |
| fannkuch                   | 252 ms                                                      | 406 ms: 1.61x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 91.5 ms: 1.63x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 89.3 ms: 1.67x slower                                                      |
| chaos                      | 37.9 ms                                                     | 64.0 ms: 1.69x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 130 ms: 1.70x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 79.7 ms: 1.75x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 111 ms: 1.75x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 64.0 ms: 1.75x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 854 ms: 1.76x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 71.9 ms: 1.77x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.74 sec: 1.78x slower                                                     |
| django_template            | 20.3 ms                                                     | 36.3 ms: 1.79x slower                                                      |
| comprehensions             | 10.4 us                                                     | 19.3 us: 1.86x slower                                                      |
| mako                       | 6.56 ms                                                     | 12.4 ms: 1.88x slower                                                      |
| richards_super             | 29.8 ms                                                     | 57.0 ms: 1.91x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 7.36 ms: 1.92x slower                                                      |
| richards                   | 26.3 ms                                                     | 50.5 ms: 1.92x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 358 us: 1.93x slower                                                       |
| generators                 | 19.0 ms                                                     | 36.6 ms: 1.93x slower                                                      |
| raytrace                   | 153 ms                                                      | 300 ms: 1.96x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 24.7 ms: 1.97x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 22.3 ms: 2.06x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 119 ms: 2.10x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 275 us: 2.11x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 4.29 ms: 2.27x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 494 ns: 9.05x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.38x slower                                                               |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.259x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.34x
- 95% likely to have a slowdown of 1.32x
- 99% likely to have a slowdown of 1.27x

# Memory
- memory change: unknown