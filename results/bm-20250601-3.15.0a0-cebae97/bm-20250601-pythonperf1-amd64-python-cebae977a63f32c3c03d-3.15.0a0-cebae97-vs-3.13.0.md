# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.319x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 292 ms: 1.36x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.06 sec: 1.35x slower                                                     |
| html5lib       | 38.2 ms                                                     | 50.8 ms: 1.33x slower                                                      |
| sphinx         | 617 ms                                                      | 836 ms: 1.35x slower                                                       |
| Geometric mean | (ref)                                                       | 1.35x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 286 ms: 1.02x slower                                                       |
| async_tree_io              | 513 ms                                                      | 548 ms: 1.07x slower                                                       |
| async_tree_none            | 219 ms                                                      | 242 ms: 1.11x slower                                                       |
| async_tree_io_tg           | 497 ms                                                      | 554 ms: 1.11x slower                                                       |
| async_tree_memoization     | 265 ms                                                      | 296 ms: 1.12x slower                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 439 ms: 1.15x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 443 ms: 1.16x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 234 ms: 1.17x slower                                                       |
| async_generators           | 223 ms                                                      | 343 ms: 1.54x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 25.6 ms: 2.05x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                       |
| float          | 50.8 ms                                                     | 77.0 ms: 1.51x slower                                                      |
| nbody          | 66.3 ms                                                     | 105 ms: 1.58x slower                                                       |
| Geometric mean | (ref)                                                       | 1.34x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.6 ms: 1.43x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.80 ms: 1.06x slower                                                      |
| regex_compile  | 80.7 ms                                                     | 124 ms: 1.54x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 108 ms: 1.17x slower                                                       |
| json_loads           | 15.1 us                                                     | 20.5 us: 1.36x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 8.73 ms: 1.41x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 90.2 ms: 1.49x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.10 sec: 1.53x slower                                                     |
| xml_etree_generate   | 53.5 ms                                                     | 89.7 ms: 1.68x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 64.8 ms: 1.77x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 359 us: 1.93x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 275 us: 2.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.58x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.4 ms: 1.12x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.2 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 49.1 ms: 1.45x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 23.8 ms: 1.57x slower                                                      |
| django_template | 20.3 ms                                                     | 37.2 ms: 1.83x slower                                                      |
| mako            | 6.56 ms                                                     | 12.5 ms: 1.91x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.68x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 34.2 ms: 2.20x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.88x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 16.6 ms: 1.43x faster                                                      |
| mdp                        | 1.43 sec                                                    | 1.18 sec: 1.21x faster                                                     |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 286 ms: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.80 ms: 1.06x slower                                                      |
| async_tree_io              | 513 ms                                                      | 548 ms: 1.07x slower                                                       |
| shortest_path              | 355 ms                                                      | 381 ms: 1.07x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.83 sec: 1.08x slower                                                     |
| connected_components       | 320 ms                                                      | 350 ms: 1.09x slower                                                       |
| async_tree_none            | 219 ms                                                      | 242 ms: 1.11x slower                                                       |
| async_tree_io_tg           | 497 ms                                                      | 554 ms: 1.11x slower                                                       |
| async_tree_memoization     | 265 ms                                                      | 296 ms: 1.12x slower                                                       |
| python_startup             | 24.4 ms                                                     | 27.4 ms: 1.12x slower                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 439 ms: 1.15x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 443 ms: 1.16x slower                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 108 ms: 1.17x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 234 ms: 1.17x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.87 us: 1.18x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.45 ms: 1.18x slower                                                      |
| deepcopy                   | 223 us                                                      | 265 us: 1.19x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.2 ms: 1.19x slower                                                      |
| pylint                     | 205 ms                                                      | 245 ms: 1.19x slower                                                       |
| json                       | 3.30 ms                                                     | 3.94 ms: 1.20x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 103 ms: 1.23x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 1.00 ms: 1.24x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 51.1 ms: 1.27x slower                                                      |
| telco                      | 4.85 ms                                                     | 6.25 ms: 1.29x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 94.4 ms: 1.31x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 50.8 ms: 1.33x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 16.6 ms: 1.34x slower                                                      |
| docutils                   | 1.53 sec                                                    | 2.06 sec: 1.35x slower                                                     |
| sympy_sum                  | 85.2 ms                                                     | 115 ms: 1.35x slower                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 2.74 us: 1.35x slower                                                      |
| sphinx                     | 617 ms                                                      | 836 ms: 1.35x slower                                                       |
| json_loads                 | 15.1 us                                                     | 20.5 us: 1.36x slower                                                      |
| 2to3                       | 215 ms                                                      | 292 ms: 1.36x slower                                                       |
| sympy_str                  | 167 ms                                                      | 234 ms: 1.40x slower                                                       |
| sympy_expand               | 286 ms                                                      | 400 ms: 1.40x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 8.73 ms: 1.41x slower                                                      |
| pycparser                  | 695 ms                                                      | 985 ms: 1.42x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.82 ms: 1.44x slower                                                      |
| deepcopy_memo              | 23.1 us                                                     | 33.3 us: 1.44x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 49.1 ms: 1.45x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 90.2 ms: 1.49x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 155 us: 1.50x slower                                                       |
| many_optionals             | 361 us                                                      | 546 us: 1.51x slower                                                       |
| float                      | 50.8 ms                                                     | 77.0 ms: 1.51x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 4.40 sec: 1.53x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.10 sec: 1.53x slower                                                     |
| regex_compile              | 80.7 ms                                                     | 124 ms: 1.54x slower                                                       |
| async_generators           | 223 ms                                                      | 343 ms: 1.54x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 23.8 ms: 1.57x slower                                                      |
| scimark_fft                | 175 ms                                                      | 274 ms: 1.57x slower                                                       |
| go                         | 84.7 ms                                                     | 133 ms: 1.58x slower                                                       |
| nbody                      | 66.3 ms                                                     | 105 ms: 1.58x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 4.14 ms: 1.59x slower                                                      |
| logging_format             | 6.18 us                                                     | 9.89 us: 1.60x slower                                                      |
| pyflate                    | 283 ms                                                      | 455 ms: 1.61x slower                                                       |
| logging_simple             | 5.77 us                                                     | 9.36 us: 1.62x slower                                                      |
| fannkuch                   | 252 ms                                                      | 420 ms: 1.67x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 94.2 ms: 1.68x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 89.7 ms: 1.68x slower                                                      |
| chaos                      | 37.9 ms                                                     | 65.8 ms: 1.74x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 79.3 ms: 1.74x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 133 ms: 1.74x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 848 ms: 1.75x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 64.8 ms: 1.77x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 72.5 ms: 1.78x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.74 sec: 1.78x slower                                                     |
| generators                 | 19.0 ms                                                     | 34.3 ms: 1.81x slower                                                      |
| django_template            | 20.3 ms                                                     | 37.2 ms: 1.83x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 117 ms: 1.84x slower                                                       |
| comprehensions             | 10.4 us                                                     | 19.6 us: 1.89x slower                                                      |
| mako                       | 6.56 ms                                                     | 12.5 ms: 1.91x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 7.39 ms: 1.92x slower                                                      |
| richards_super             | 29.8 ms                                                     | 57.4 ms: 1.93x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 359 us: 1.93x slower                                                       |
| richards                   | 26.3 ms                                                     | 50.8 ms: 1.93x slower                                                      |
| raytrace                   | 153 ms                                                      | 302 ms: 1.97x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 25.6 ms: 2.05x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 117 ms: 2.07x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 22.7 ms: 2.09x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 275 us: 2.11x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 4.31 ms: 2.28x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 494 ns: 9.06x slower                                                       |
| coverage                   | 45.3 ms                                                     | 475 ms: 10.48x slower                                                      |
| thrift                     | 8.47 ms                                                     | 98.8 ms: 11.67x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.50x slower                                                               |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.319x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.35x
- 95% likely to have a slowdown of 1.34x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: unknown