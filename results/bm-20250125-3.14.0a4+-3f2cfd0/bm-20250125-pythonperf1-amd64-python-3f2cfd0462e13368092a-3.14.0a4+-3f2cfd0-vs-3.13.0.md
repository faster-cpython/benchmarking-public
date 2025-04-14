# Results vs. 3.13.0

- fork: python
- ref: 3f2cfd0462e13368092a
- machine: windows-amd64
- commit hash: 3f2cfd0
- commit date: 2025-01-25
- overall geometric mean: 1.039x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 232 ms: 1.08x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.5 ms: 1.03x slower                                                       |
| sphinx         | 617 ms                                                      | 659 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 224 ms: 1.26x faster                                                        |
| async_tree_io              | 513 ms                                                      | 434 ms: 1.18x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 435 ms: 1.14x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 233 ms: 1.14x faster                                                        |
| async_tree_none            | 219 ms                                                      | 199 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 353 ms: 1.09x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 185 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 356 ms: 1.07x faster                                                        |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 307 ms: 1.02x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 147 ms: 1.01x slower                                                        |
| float          | 50.8 ms                                                     | 51.8 ms: 1.02x slower                                                       |
| nbody          | 66.3 ms                                                     | 77.7 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.8 ms: 1.51x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                       |
| regex_dna      | 115 ms                                                      | 123 ms: 1.07x slower                                                        |
| regex_compile  | 80.7 ms                                                     | 89.2 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 89.0 ms: 1.04x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.9 us: 1.01x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 65.6 ms: 1.08x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 59.1 ms: 1.11x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.85 ms: 1.11x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 41.9 ms: 1.15x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 165 us: 1.27x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 242 us: 1.30x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.9 ms                                                     | 17.9 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 36.2 ms: 1.07x slower                                                       |
| mako            | 6.56 ms                                                     | 7.13 ms: 1.09x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.7 ms: 1.10x slower                                                       |
| django_template | 20.3 ms                                                     | 26.4 ms: 1.30x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 520 us: 16.27x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 15.8 ms: 1.51x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 224 ms: 1.26x faster                                                        |
| async_tree_io              | 513 ms                                                      | 434 ms: 1.18x faster                                                        |
| deepcopy                   | 223 us                                                      | 189 us: 1.18x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 435 ms: 1.14x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 233 ms: 1.14x faster                                                        |
| async_tree_none            | 219 ms                                                      | 199 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 353 ms: 1.09x faster                                                        |
| json                       | 3.30 ms                                                     | 3.05 ms: 1.08x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 185 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 356 ms: 1.07x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 21.6 us: 1.07x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.04x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.0 ms: 1.04x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.9 us: 1.01x faster                                                       |
| shortest_path              | 355 ms                                                      | 354 ms: 1.00x faster                                                        |
| pidigits                   | 146 ms                                                      | 147 ms: 1.01x slower                                                        |
| telco                      | 4.85 ms                                                     | 4.90 ms: 1.01x slower                                                       |
| float                      | 50.8 ms                                                     | 51.8 ms: 1.02x slower                                                       |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.62 us: 1.02x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 307 ms: 1.02x slower                                                        |
| spectral_norm              | 63.4 ms                                                     | 65.0 ms: 1.03x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 834 us: 1.03x slower                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.68 ms: 1.03x slower                                                       |
| pathlib                    | 75.3 ms                                                     | 77.7 ms: 1.03x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.5 ms: 1.03x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 87.7 ms: 1.04x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 17.9 ms: 1.06x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.6 ms: 1.06x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 3.06 sec: 1.06x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 36.2 ms: 1.07x slower                                                       |
| sphinx                     | 617 ms                                                      | 659 ms: 1.07x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 91.0 ms: 1.07x slower                                                       |
| regex_dna                  | 115 ms                                                      | 123 ms: 1.07x slower                                                        |
| coverage                   | 45.3 ms                                                     | 48.5 ms: 1.07x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 111 us: 1.07x slower                                                        |
| sympy_expand               | 286 ms                                                      | 308 ms: 1.08x slower                                                        |
| 2to3                       | 215 ms                                                      | 232 ms: 1.08x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 49.2 ms: 1.08x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 77.6 ms: 1.08x slower                                                       |
| sympy_str                  | 167 ms                                                      | 180 ms: 1.08x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 65.6 ms: 1.08x slower                                                       |
| mako                       | 6.56 ms                                                     | 7.13 ms: 1.09x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 16.7 ms: 1.10x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                      |
| go                         | 84.7 ms                                                     | 93.4 ms: 1.10x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.58 sec: 1.10x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 89.2 ms: 1.10x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 59.1 ms: 1.11x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.85 ms: 1.11x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.87 us: 1.11x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.45 us: 1.12x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.8 ms: 1.12x slower                                                       |
| pyflate                    | 283 ms                                                      | 318 ms: 1.12x slower                                                        |
| pycparser                  | 695 ms                                                      | 785 ms: 1.13x slower                                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 36.8 ms: 1.13x slower                                                       |
| fannkuch                   | 252 ms                                                      | 286 ms: 1.14x slower                                                        |
| chaos                      | 37.9 ms                                                     | 43.1 ms: 1.14x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 41.9 ms: 1.15x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.13 sec: 1.16x slower                                                      |
| generators                 | 19.0 ms                                                     | 22.0 ms: 1.16x slower                                                       |
| scimark_fft                | 175 ms                                                      | 203 ms: 1.16x slower                                                        |
| pprint_safe_repr           | 485 ms                                                      | 563 ms: 1.16x slower                                                        |
| nbody                      | 66.3 ms                                                     | 77.7 ms: 1.17x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 201 ms: 1.17x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 66.8 ms: 1.19x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.14 ms: 1.19x slower                                                       |
| many_optionals             | 361 us                                                      | 433 us: 1.20x slower                                                        |
| sqlglot_parse              | 764 us                                                      | 921 us: 1.21x slower                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 49.7 ms: 1.22x slower                                                       |
| comprehensions             | 10.4 us                                                     | 12.7 us: 1.22x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 94.0 ms: 1.23x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 70.3 ms: 1.24x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.76 ms: 1.24x slower                                                       |
| richards                   | 26.3 ms                                                     | 32.7 ms: 1.25x slower                                                       |
| richards_super             | 29.8 ms                                                     | 37.2 ms: 1.25x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 165 us: 1.27x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.41 ms: 1.27x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 242 us: 1.30x slower                                                        |
| django_template            | 20.3 ms                                                     | 26.4 ms: 1.30x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 71.2 ns: 1.31x slower                                                       |
| raytrace                   | 153 ms                                                      | 207 ms: 1.35x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.0 ms: 1.48x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (6): pylint, create_gc_cycles, python_startup, connected_components, k_core, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250125-3.14.0a4+-3f2cfd0/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.039x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown