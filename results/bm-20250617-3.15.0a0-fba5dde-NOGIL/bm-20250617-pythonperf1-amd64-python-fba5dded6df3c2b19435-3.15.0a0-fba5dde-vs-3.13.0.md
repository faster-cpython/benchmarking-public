# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.418x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.66x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 337 ms: 1.57x slower                                                       |
| docutils       | 1.53 sec                                                    | 4.24 sec: 2.77x slower                                                     |
| html5lib       | 38.2 ms                                                     | 63.3 ms: 1.66x slower                                                      |
| sphinx         | 617 ms                                                      | 1.30 sec: 2.10x slower                                                     |
| Geometric mean | (ref)                                                       | 1.97x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 143 ms: 2.10x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 311 ms: 1.11x slower                                                       |
| async_tree_io_tg           | 497 ms                                                      | 558 ms: 1.12x slower                                                       |
| async_tree_io              | 513 ms                                                      | 583 ms: 1.14x slower                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 460 ms: 1.20x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 249 ms: 1.24x slower                                                       |
| async_tree_none            | 219 ms                                                      | 275 ms: 1.25x slower                                                       |
| async_tree_memoization     | 265 ms                                                      | 336 ms: 1.27x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 486 ms: 1.28x slower                                                       |
| async_generators           | 223 ms                                                      | 415 ms: 1.86x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 33.9 ms: 2.71x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 140 ms: 1.04x faster                                                       |
| float          | 50.8 ms                                                     | 97.6 ms: 1.92x slower                                                      |
| nbody          | 66.3 ms                                                     | 183 ms: 2.77x slower                                                       |
| Geometric mean | (ref)                                                       | 1.72x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.8 ms: 1.42x faster                                                      |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.81 ms: 1.07x slower                                                      |
| regex_compile  | 80.7 ms                                                     | 161 ms: 1.99x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 113 ms: 1.22x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 92.7 ms: 1.53x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 9.51 ms: 1.54x slower                                                      |
| json_loads           | 15.1 us                                                     | 23.2 us: 1.54x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 108 ms: 2.02x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 80.0 ms: 2.19x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 452 us: 2.43x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 358 us: 2.75x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 5.05 sec: 3.68x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.99x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.7 ms: 1.13x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.3 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 66.3 ms: 1.96x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 33.7 ms: 2.22x slower                                                      |
| django_template | 20.3 ms                                                     | 45.6 ms: 2.25x slower                                                      |
| mako            | 6.56 ms                                                     | 16.4 ms: 2.51x slower                                                      |
| Geometric mean  | (ref)                                                       | 2.22x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 848 us: 9.98x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 35.4 ms: 2.12x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 143 ms: 2.10x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 16.8 ms: 1.42x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.72 ms: 1.14x faster                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.11 ms: 1.10x faster                                                      |
| pidigits                   | 146 ms                                                      | 140 ms: 1.04x faster                                                       |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 89.8 ms: 1.07x slower                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.81 ms: 1.07x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.70 us: 1.07x slower                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 311 ms: 1.11x slower                                                       |
| async_tree_io_tg           | 497 ms                                                      | 558 ms: 1.12x slower                                                       |
| python_startup             | 24.4 ms                                                     | 27.7 ms: 1.13x slower                                                      |
| async_tree_io              | 513 ms                                                      | 583 ms: 1.14x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.3 ms: 1.20x slower                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 460 ms: 1.20x slower                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 113 ms: 1.22x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 249 ms: 1.24x slower                                                       |
| async_tree_none            | 219 ms                                                      | 275 ms: 1.25x slower                                                       |
| async_tree_memoization     | 265 ms                                                      | 336 ms: 1.27x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 486 ms: 1.28x slower                                                       |
| json                       | 3.30 ms                                                     | 4.23 ms: 1.28x slower                                                      |
| pylint                     | 205 ms                                                      | 283 ms: 1.38x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 56.5 ms: 1.41x slower                                                      |
| deepcopy                   | 223 us                                                      | 336 us: 1.50x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 92.7 ms: 1.53x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.24 ms: 1.53x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 9.51 ms: 1.54x slower                                                      |
| json_loads                 | 15.1 us                                                     | 23.2 us: 1.54x slower                                                      |
| mdp                        | 1.43 sec                                                    | 2.22 sec: 1.55x slower                                                     |
| 2to3                       | 215 ms                                                      | 337 ms: 1.57x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 118 ms: 1.63x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 63.3 ms: 1.66x slower                                                      |
| telco                      | 4.85 ms                                                     | 8.06 ms: 1.66x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 143 ms: 1.68x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 21.0 ms: 1.70x slower                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 3.47 us: 1.72x slower                                                      |
| sympy_str                  | 167 ms                                                      | 291 ms: 1.75x slower                                                       |
| sympy_expand               | 286 ms                                                      | 499 ms: 1.75x slower                                                       |
| many_optionals             | 361 us                                                      | 641 us: 1.77x slower                                                       |
| k_core                     | 1.70 sec                                                    | 3.06 sec: 1.80x slower                                                     |
| coverage                   | 45.3 ms                                                     | 83.9 ms: 1.85x slower                                                      |
| async_generators           | 223 ms                                                      | 415 ms: 1.86x slower                                                       |
| logging_format             | 6.18 us                                                     | 11.6 us: 1.88x slower                                                      |
| deepcopy_memo              | 23.1 us                                                     | 43.6 us: 1.89x slower                                                      |
| float                      | 50.8 ms                                                     | 97.6 ms: 1.92x slower                                                      |
| logging_simple             | 5.77 us                                                     | 11.1 us: 1.92x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 199 us: 1.93x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 66.3 ms: 1.96x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 161 ms: 1.99x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 108 ms: 2.02x slower                                                       |
| shortest_path              | 355 ms                                                      | 734 ms: 2.07x slower                                                       |
| sphinx                     | 617 ms                                                      | 1.30 sec: 2.10x slower                                                     |
| connected_components       | 320 ms                                                      | 691 ms: 2.16x slower                                                       |
| pyflate                    | 283 ms                                                      | 614 ms: 2.17x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 80.0 ms: 2.19x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 124 ms: 2.21x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 33.7 ms: 2.22x slower                                                      |
| generators                 | 19.0 ms                                                     | 42.4 ms: 2.23x slower                                                      |
| django_template            | 20.3 ms                                                     | 45.6 ms: 2.25x slower                                                      |
| go                         | 84.7 ms                                                     | 192 ms: 2.27x slower                                                       |
| fannkuch                   | 252 ms                                                      | 573 ms: 2.28x slower                                                       |
| scimark_fft                | 175 ms                                                      | 424 ms: 2.43x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 452 us: 2.43x slower                                                       |
| pycparser                  | 695 ms                                                      | 1.70 sec: 2.44x slower                                                     |
| comprehensions             | 10.4 us                                                     | 25.5 us: 2.46x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 189 ms: 2.48x slower                                                       |
| mako                       | 6.56 ms                                                     | 16.4 ms: 2.51x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 27.3 ms: 2.52x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 6.58 ms: 2.53x slower                                                      |
| chaos                      | 37.9 ms                                                     | 96.8 ms: 2.55x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 164 ms: 2.58x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 118 ms: 2.59x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 107 ms: 2.63x slower                                                       |
| richards_super             | 29.8 ms                                                     | 79.1 ms: 2.66x slower                                                      |
| richards                   | 26.3 ms                                                     | 70.3 ms: 2.68x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 33.9 ms: 2.71x slower                                                      |
| raytrace                   | 153 ms                                                      | 419 ms: 2.73x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 10.6 ms: 2.75x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 358 us: 2.75x slower                                                       |
| docutils                   | 1.53 sec                                                    | 4.24 sec: 2.77x slower                                                     |
| nbody                      | 66.3 ms                                                     | 183 ms: 2.77x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 164 ms: 2.90x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 8.39 sec: 2.92x slower                                                     |
| pprint_safe_repr           | 485 ms                                                      | 1.47 sec: 3.04x slower                                                     |
| deltablue                  | 1.89 ms                                                     | 5.93 ms: 3.13x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 5.05 sec: 3.68x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 4.23 sec: 4.34x slower                                                     |
| logging_silent             | 54.6 ns                                                     | 586 ns: 10.74x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.76x slower                                                               |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.418x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.75x
- 95% likely to have a slowdown of 1.73x
- 99% likely to have a slowdown of 1.66x

# Memory
- memory change: unknown