# Results vs. 3.13.0

- fork: python
- ref: a3990df6121880e8c678
- machine: windows-amd64
- commit hash: a3990df
- commit date: 2025-03-08
- overall geometric mean: 1.020x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 230 ms: 1.07x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.76 sec: 1.15x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.5 ms: 1.04x slower                                                       |
| sphinx         | 617 ms                                                      | 696 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                        |
| async_tree_io              | 513 ms                                                      | 404 ms: 1.27x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                        |
| async_tree_none            | 219 ms                                                      | 180 ms: 1.22x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 361 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 368 ms: 1.04x faster                                                        |
| async_generators           | 223 ms                                                      | 228 ms: 1.03x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 332 ms: 1.11x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 47.4 ms: 1.07x faster                                                       |
| nbody          | 66.3 ms                                                     | 64.4 ms: 1.03x faster                                                       |
| pidigits       | 146 ms                                                      | 156 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 17.0 ms: 1.40x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 86.7 ms: 1.07x slower                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.88 ms: 1.11x slower                                                       |
| regex_dna      | 115 ms                                                      | 130 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 103 ms: 1.12x slower                                                        |
| unpickle_pure_python | 130 us                                                      | 148 us: 1.14x slower                                                        |
| xml_etree_iterparse  | 60.5 ms                                                     | 70.6 ms: 1.17x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 219 us: 1.18x slower                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 66.7 ms: 1.25x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 7.80 ms: 1.26x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 46.4 ms: 1.27x slower                                                       |
| json_loads           | 15.1 us                                                     | 19.9 us: 1.32x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.19x slower                                                                |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.3 ms: 1.12x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 21.3 ms: 1.26x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 32.3 ms: 1.05x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 14.8 ms: 1.03x faster                                                       |
| django_template | 20.3 ms                                                     | 24.7 ms: 1.22x slower                                                       |
| mako            | 6.56 ms                                                     | 8.33 ms: 1.27x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 551 us: 15.36x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 31.9 ms: 2.36x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 17.0 ms: 1.40x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                        |
| async_tree_io              | 513 ms                                                      | 404 ms: 1.27x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                        |
| deepcopy                   | 223 us                                                      | 182 us: 1.23x faster                                                        |
| async_tree_none            | 219 ms                                                      | 180 ms: 1.22x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.17x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 20.1 us: 1.15x faster                                                       |
| generators                 | 19.0 ms                                                     | 16.9 ms: 1.12x faster                                                       |
| go                         | 84.7 ms                                                     | 76.7 ms: 1.10x faster                                                       |
| float                      | 50.8 ms                                                     | 47.4 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 361 ms: 1.05x faster                                                        |
| genshi_xml                 | 33.9 ms                                                     | 32.3 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 368 ms: 1.04x faster                                                        |
| genshi_text                | 15.2 ms                                                     | 14.8 ms: 1.03x faster                                                       |
| nbody                      | 66.3 ms                                                     | 64.4 ms: 1.03x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.0 ms: 1.01x slower                                                       |
| async_generators           | 223 ms                                                      | 228 ms: 1.03x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 1.94 ms: 1.03x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.63 us: 1.03x slower                                                       |
| connected_components       | 320 ms                                                      | 330 ms: 1.03x slower                                                        |
| spectral_norm              | 63.4 ms                                                     | 65.4 ms: 1.03x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.5 ms: 1.04x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 74.8 ms: 1.04x slower                                                       |
| pycparser                  | 695 ms                                                      | 725 ms: 1.04x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 42.4 ms: 1.06x slower                                                       |
| pidigits                   | 146 ms                                                      | 156 ms: 1.06x slower                                                        |
| 2to3                       | 215 ms                                                      | 230 ms: 1.07x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 111 us: 1.07x slower                                                        |
| regex_compile              | 80.7 ms                                                     | 86.7 ms: 1.07x slower                                                       |
| pyflate                    | 283 ms                                                      | 306 ms: 1.08x slower                                                        |
| sympy_expand               | 286 ms                                                      | 311 ms: 1.09x slower                                                        |
| sympy_str                  | 167 ms                                                      | 182 ms: 1.09x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.20 ms: 1.09x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 531 ms: 1.10x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 1.07 sec: 1.10x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.33 ms: 1.10x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 92.6 ms: 1.10x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 93.6 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                       |
| scimark_fft                | 175 ms                                                      | 192 ms: 1.10x slower                                                        |
| chaos                      | 37.9 ms                                                     | 41.8 ms: 1.10x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 844 us: 1.10x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 895 us: 1.10x slower                                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 36.0 ms: 1.11x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 332 ms: 1.11x slower                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.88 ms: 1.11x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.06 ms: 1.11x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.42 us: 1.11x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.88 us: 1.11x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.8 ms: 1.12x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.20 sec: 1.12x slower                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 103 ms: 1.12x slower                                                        |
| fannkuch                   | 252 ms                                                      | 281 ms: 1.12x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.37 ms: 1.12x slower                                                       |
| python_startup             | 24.4 ms                                                     | 27.3 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 193 ms: 1.13x slower                                                        |
| sphinx                     | 617 ms                                                      | 696 ms: 1.13x slower                                                        |
| comprehensions             | 10.4 us                                                     | 11.7 us: 1.13x slower                                                       |
| regex_dna                  | 115 ms                                                      | 130 ms: 1.13x slower                                                        |
| json                       | 3.30 ms                                                     | 3.73 ms: 1.13x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 148 us: 1.14x slower                                                        |
| mdp                        | 1.43 sec                                                    | 1.64 sec: 1.15x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 64.5 ms: 1.15x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.76 sec: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 177 ms: 1.15x slower                                                        |
| richards_super             | 29.8 ms                                                     | 34.4 ms: 1.15x slower                                                       |
| richards                   | 26.3 ms                                                     | 30.4 ms: 1.16x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 63.3 ns: 1.16x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 53.0 ms: 1.16x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 70.6 ms: 1.17x slower                                                       |
| coverage                   | 45.3 ms                                                     | 53.2 ms: 1.17x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 219 us: 1.18x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 67.8 ms: 1.20x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.7 ms: 1.22x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 66.7 ms: 1.25x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 21.3 ms: 1.26x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 7.80 ms: 1.26x slower                                                       |
| many_optionals             | 361 us                                                      | 456 us: 1.26x slower                                                        |
| mako                       | 6.56 ms                                                     | 8.33 ms: 1.27x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 46.4 ms: 1.27x slower                                                       |
| json_loads                 | 15.1 us                                                     | 19.9 us: 1.32x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.61 ms: 1.33x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.3 ms: 1.50x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (6): tomli_loads, shortest_path, scimark_sparse_mat_mult, scimark_sor, pylint, k_core
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.020x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown