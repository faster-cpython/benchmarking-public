# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: windows-amd64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.004x faster
- HPT reliability: 74.54%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 210 ms: 1.06x faster                                            |
| docutils       | 1.57 sec                                                    | 1.55 sec: 1.01x faster                                          |
| html5lib       | 38.9 ms                                                     | 36.6 ms: 1.06x faster                                           |
| tornado_http   | 93.0 ms                                                     | 86.1 ms: 1.08x faster                                           |
| Geometric mean | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                            |
| coroutines                 | 12.8 ms                                                     | 13.2 ms: 1.04x slower                                           |
| async_tree_none            | 226 ms                                                      | 264 ms: 1.17x slower                                            |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 453 ms: 1.18x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 341 ms: 1.23x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 361 ms: 1.25x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 482 ms: 1.28x slower                                            |
| async_tree_none_tg         | 209 ms                                                      | 281 ms: 1.35x slower                                            |
| async_tree_io              | 521 ms                                                      | 731 ms: 1.40x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 769 ms: 1.48x slower                                            |
| Geometric mean             | (ref)                                                       | 1.23x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 147 ms: 1.00x faster                                            |
| float          | 49.9 ms                                                     | 52.3 ms: 1.05x slower                                           |
| nbody          | 68.4 ms                                                     | 72.0 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                       | 1.03x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.3 ms: 1.40x faster                                           |
| regex_compile  | 80.5 ms                                                     | 78.9 ms: 1.02x faster                                           |
| regex_effbot   | 1.58 ms                                                     | 1.62 ms: 1.03x slower                                           |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                       | 1.07x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 13.4 us: 1.13x faster                                           |
| json_dumps           | 5.92 ms                                                     | 5.50 ms: 1.07x faster                                           |
| pickle_pure_python   | 190 us                                                      | 179 us: 1.06x faster                                            |
| unpickle_pure_python | 133 us                                                      | 128 us: 1.05x faster                                            |
| tomli_loads          | 1.39 sec                                                    | 1.37 sec: 1.02x faster                                          |
| xml_etree_process    | 37.0 ms                                                     | 36.4 ms: 1.02x faster                                           |
| xml_etree_generate   | 54.0 ms                                                     | 53.2 ms: 1.02x faster                                           |
| xml_etree_parse      | 93.6 ms                                                     | 92.3 ms: 1.01x faster                                           |
| xml_etree_iterparse  | 61.8 ms                                                     | 64.5 ms: 1.04x slower                                           |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 19.9 ms: 1.28x faster                                           |
| python_startup_no_site | 18.1 ms                                                     | 17.6 ms: 1.03x faster                                           |
| Geometric mean         | (ref)                                                       | 1.15x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 33.1 ms: 1.07x faster                                           |
| genshi_text     | 15.6 ms                                                     | 15.0 ms: 1.04x faster                                           |
| django_template | 22.4 ms                                                     | 21.9 ms: 1.02x faster                                           |
| mako            | 6.35 ms                                                     | 6.48 ms: 1.02x slower                                           |
| Geometric mean  | (ref)                                                       | 1.03x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| create_gc_cycles           | 1.26 ms                                                     | 746 us: 1.69x faster                                            |
| typing_runtime_protocols   | 105 us                                                      | 73.9 us: 1.43x faster                                           |
| regex_v8                   | 21.4 ms                                                     | 15.3 ms: 1.40x faster                                           |
| bench_mp_pool              | 86.4 ms                                                     | 64.0 ms: 1.35x faster                                           |
| gc_traversal               | 1.97 ms                                                     | 1.52 ms: 1.30x faster                                           |
| python_startup             | 25.4 ms                                                     | 19.9 ms: 1.28x faster                                           |
| json_loads                 | 15.1 us                                                     | 13.4 us: 1.13x faster                                           |
| json                       | 3.19 ms                                                     | 2.85 ms: 1.12x faster                                           |
| sympy_expand               | 291 ms                                                      | 269 ms: 1.08x faster                                            |
| tornado_http               | 93.0 ms                                                     | 86.1 ms: 1.08x faster                                           |
| sympy_str                  | 169 ms                                                      | 156 ms: 1.08x faster                                            |
| json_dumps                 | 5.92 ms                                                     | 5.50 ms: 1.07x faster                                           |
| genshi_xml                 | 35.5 ms                                                     | 33.1 ms: 1.07x faster                                           |
| html5lib                   | 38.9 ms                                                     | 36.6 ms: 1.06x faster                                           |
| pickle_pure_python         | 190 us                                                      | 179 us: 1.06x faster                                            |
| deepcopy_reduce            | 2.06 us                                                     | 1.95 us: 1.06x faster                                           |
| sympy_sum                  | 86.9 ms                                                     | 82.3 ms: 1.06x faster                                           |
| 2to3                       | 221 ms                                                      | 210 ms: 1.06x faster                                            |
| thrift                     | 8.80 ms                                                     | 8.35 ms: 1.05x faster                                           |
| fannkuch                   | 253 ms                                                      | 241 ms: 1.05x faster                                            |
| crypto_pyaes               | 45.4 ms                                                     | 43.3 ms: 1.05x faster                                           |
| telco                      | 4.79 ms                                                     | 4.57 ms: 1.05x faster                                           |
| unpickle_pure_python       | 133 us                                                      | 128 us: 1.05x faster                                            |
| genshi_text                | 15.6 ms                                                     | 15.0 ms: 1.04x faster                                           |
| deepcopy                   | 226 us                                                      | 218 us: 1.04x faster                                            |
| go                         | 87.0 ms                                                     | 84.3 ms: 1.03x faster                                           |
| pprint_safe_repr           | 494 ms                                                      | 479 ms: 1.03x faster                                            |
| python_startup_no_site     | 18.1 ms                                                     | 17.6 ms: 1.03x faster                                           |
| sympy_integrate            | 12.5 ms                                                     | 12.2 ms: 1.03x faster                                           |
| sqlglot_parse              | 771 us                                                      | 752 us: 1.03x faster                                            |
| mdp                        | 1.39 sec                                                    | 1.36 sec: 1.02x faster                                          |
| hexiom                     | 3.89 ms                                                     | 3.81 ms: 1.02x faster                                           |
| regex_compile              | 80.5 ms                                                     | 78.9 ms: 1.02x faster                                           |
| pprint_pformat             | 999 ms                                                      | 979 ms: 1.02x faster                                            |
| django_template            | 22.4 ms                                                     | 21.9 ms: 1.02x faster                                           |
| sqlglot_normalize          | 175 ms                                                      | 171 ms: 1.02x faster                                            |
| tomli_loads                | 1.39 sec                                                    | 1.37 sec: 1.02x faster                                          |
| xml_etree_process          | 37.0 ms                                                     | 36.4 ms: 1.02x faster                                           |
| xml_etree_generate         | 54.0 ms                                                     | 53.2 ms: 1.02x faster                                           |
| docutils                   | 1.57 sec                                                    | 1.55 sec: 1.01x faster                                          |
| sqlglot_optimize           | 32.9 ms                                                     | 32.5 ms: 1.01x faster                                           |
| xml_etree_parse            | 93.6 ms                                                     | 92.3 ms: 1.01x faster                                           |
| meteor_contest             | 73.5 ms                                                     | 72.6 ms: 1.01x faster                                           |
| pathlib                    | 80.9 ms                                                     | 79.9 ms: 1.01x faster                                           |
| logging_silent             | 54.6 ns                                                     | 54.1 ns: 1.01x faster                                           |
| pidigits                   | 148 ms                                                      | 147 ms: 1.00x faster                                            |
| coverage                   | 45.6 ms                                                     | 45.8 ms: 1.01x slower                                           |
| deepcopy_memo              | 23.3 us                                                     | 23.5 us: 1.01x slower                                           |
| sqlglot_transpile          | 956 us                                                      | 965 us: 1.01x slower                                            |
| dulwich_log                | 40.8 ms                                                     | 41.4 ms: 1.01x slower                                           |
| spectral_norm              | 62.8 ms                                                     | 63.6 ms: 1.01x slower                                           |
| raytrace                   | 160 ms                                                      | 163 ms: 1.02x slower                                            |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                            |
| chaos                      | 38.5 ms                                                     | 39.2 ms: 1.02x slower                                           |
| logging_simple             | 5.96 us                                                     | 6.07 us: 1.02x slower                                           |
| mako                       | 6.35 ms                                                     | 6.48 ms: 1.02x slower                                           |
| pyflate                    | 283 ms                                                      | 291 ms: 1.03x slower                                            |
| generators                 | 19.5 ms                                                     | 20.0 ms: 1.03x slower                                           |
| nqueens                    | 56.7 ms                                                     | 58.2 ms: 1.03x slower                                           |
| regex_effbot               | 1.58 ms                                                     | 1.62 ms: 1.03x slower                                           |
| coroutines                 | 12.8 ms                                                     | 13.2 ms: 1.04x slower                                           |
| logging_format             | 6.26 us                                                     | 6.51 us: 1.04x slower                                           |
| xml_etree_iterparse        | 61.8 ms                                                     | 64.5 ms: 1.04x slower                                           |
| float                      | 49.9 ms                                                     | 52.3 ms: 1.05x slower                                           |
| deltablue                  | 1.92 ms                                                     | 2.01 ms: 1.05x slower                                           |
| nbody                      | 68.4 ms                                                     | 72.0 ms: 1.05x slower                                           |
| pycparser                  | 683 ms                                                      | 723 ms: 1.06x slower                                            |
| regex_dna                  | 115 ms                                                      | 122 ms: 1.06x slower                                            |
| scimark_lu                 | 53.0 ms                                                     | 56.4 ms: 1.06x slower                                           |
| scimark_fft                | 172 ms                                                      | 184 ms: 1.07x slower                                            |
| scimark_sor                | 76.2 ms                                                     | 85.4 ms: 1.12x slower                                           |
| async_tree_none            | 226 ms                                                      | 264 ms: 1.17x slower                                            |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 453 ms: 1.18x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 341 ms: 1.23x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 361 ms: 1.25x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 482 ms: 1.28x slower                                            |
| async_tree_none_tg         | 209 ms                                                      | 281 ms: 1.35x slower                                            |
| async_tree_io              | 521 ms                                                      | 731 ms: 1.40x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 769 ms: 1.48x slower                                            |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (9): mypy2, pylint, richards_super, chameleon, richards, scimark_sparse_mat_mult, bench_thread_pool, scimark_monte_carlo, comprehensions
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 74.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown