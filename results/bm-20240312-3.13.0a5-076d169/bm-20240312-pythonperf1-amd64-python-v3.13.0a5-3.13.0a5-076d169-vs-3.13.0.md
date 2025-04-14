# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a5
- machine: windows-amd64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.013x faster
- HPT reliability: 94.73%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 216 ms: 1.02x faster                                            |
| docutils       | 1.57 sec                                                    | 1.54 sec: 1.02x faster                                          |
| html5lib       | 38.9 ms                                                     | 36.5 ms: 1.07x faster                                           |
| tornado_http   | 93.0 ms                                                     | 84.8 ms: 1.10x faster                                           |
| Geometric mean | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_generators           | 223 ms                                                      | 224 ms: 1.01x slower                                            |
| coroutines                 | 12.8 ms                                                     | 13.2 ms: 1.03x slower                                           |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 454 ms: 1.19x slower                                            |
| async_tree_none            | 226 ms                                                      | 270 ms: 1.20x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 349 ms: 1.21x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 340 ms: 1.23x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 474 ms: 1.26x slower                                            |
| async_tree_none_tg         | 209 ms                                                      | 274 ms: 1.31x slower                                            |
| async_tree_io              | 521 ms                                                      | 738 ms: 1.42x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 758 ms: 1.46x slower                                            |
| Geometric mean             | (ref)                                                       | 1.22x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 50.8 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                       | 1.00x slower                                                    |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.5 ms: 1.38x faster                                           |
| regex_compile  | 80.5 ms                                                     | 78.2 ms: 1.03x faster                                           |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                       | 1.09x faster                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 13.9 us: 1.09x faster                                           |
| unpickle_pure_python | 133 us                                                      | 125 us: 1.07x faster                                            |
| pickle_pure_python   | 190 us                                                      | 180 us: 1.05x faster                                            |
| json_dumps           | 5.92 ms                                                     | 5.63 ms: 1.05x faster                                           |
| xml_etree_process    | 37.0 ms                                                     | 36.7 ms: 1.01x faster                                           |
| xml_etree_iterparse  | 61.8 ms                                                     | 62.9 ms: 1.02x slower                                           |
| tomli_loads          | 1.39 sec                                                    | 1.43 sec: 1.03x slower                                          |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                    |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 20.3 ms: 1.25x faster                                           |
| Geometric mean | (ref)                                                       | 1.12x faster                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 6.21 ms: 1.02x faster                                           |
| django_template | 22.4 ms                                                     | 22.1 ms: 1.01x faster                                           |
| genshi_text     | 15.6 ms                                                     | 15.8 ms: 1.02x slower                                           |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| create_gc_cycles           | 1.26 ms                                                     | 745 us: 1.69x faster                                            |
| mypy2                      | 679 ms                                                      | 413 ms: 1.64x faster                                            |
| typing_runtime_protocols   | 105 us                                                      | 75.1 us: 1.40x faster                                           |
| regex_v8                   | 21.4 ms                                                     | 15.5 ms: 1.38x faster                                           |
| gc_traversal               | 1.97 ms                                                     | 1.50 ms: 1.31x faster                                           |
| bench_mp_pool              | 86.4 ms                                                     | 66.6 ms: 1.30x faster                                           |
| python_startup             | 25.4 ms                                                     | 20.3 ms: 1.25x faster                                           |
| tornado_http               | 93.0 ms                                                     | 84.8 ms: 1.10x faster                                           |
| json_loads                 | 15.1 us                                                     | 13.9 us: 1.09x faster                                           |
| sympy_expand               | 291 ms                                                      | 270 ms: 1.08x faster                                            |
| thrift                     | 8.80 ms                                                     | 8.19 ms: 1.07x faster                                           |
| unpickle_pure_python       | 133 us                                                      | 125 us: 1.07x faster                                            |
| sympy_str                  | 169 ms                                                      | 158 ms: 1.07x faster                                            |
| crypto_pyaes               | 45.4 ms                                                     | 42.6 ms: 1.07x faster                                           |
| html5lib                   | 38.9 ms                                                     | 36.5 ms: 1.07x faster                                           |
| deepcopy_reduce            | 2.06 us                                                     | 1.95 us: 1.06x faster                                           |
| pickle_pure_python         | 190 us                                                      | 180 us: 1.05x faster                                            |
| spectral_norm              | 62.8 ms                                                     | 59.7 ms: 1.05x faster                                           |
| json_dumps                 | 5.92 ms                                                     | 5.63 ms: 1.05x faster                                           |
| sympy_sum                  | 86.9 ms                                                     | 82.9 ms: 1.05x faster                                           |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.35 ms: 1.04x faster                                           |
| deepcopy_memo              | 23.3 us                                                     | 22.3 us: 1.04x faster                                           |
| scimark_monte_carlo        | 40.8 ms                                                     | 39.2 ms: 1.04x faster                                           |
| fannkuch                   | 253 ms                                                      | 243 ms: 1.04x faster                                            |
| regex_compile              | 80.5 ms                                                     | 78.2 ms: 1.03x faster                                           |
| deepcopy                   | 226 us                                                      | 220 us: 1.03x faster                                            |
| mako                       | 6.35 ms                                                     | 6.21 ms: 1.02x faster                                           |
| 2to3                       | 221 ms                                                      | 216 ms: 1.02x faster                                            |
| docutils                   | 1.57 sec                                                    | 1.54 sec: 1.02x faster                                          |
| logging_silent             | 54.6 ns                                                     | 53.5 ns: 1.02x faster                                           |
| sqlglot_normalize          | 175 ms                                                      | 172 ms: 1.01x faster                                            |
| sympy_integrate            | 12.5 ms                                                     | 12.3 ms: 1.01x faster                                           |
| pprint_safe_repr           | 494 ms                                                      | 487 ms: 1.01x faster                                            |
| mdp                        | 1.39 sec                                                    | 1.37 sec: 1.01x faster                                          |
| django_template            | 22.4 ms                                                     | 22.1 ms: 1.01x faster                                           |
| dulwich_log                | 40.8 ms                                                     | 40.4 ms: 1.01x faster                                           |
| sqlglot_parse              | 771 us                                                      | 762 us: 1.01x faster                                            |
| go                         | 87.0 ms                                                     | 86.1 ms: 1.01x faster                                           |
| scimark_sor                | 76.2 ms                                                     | 75.4 ms: 1.01x faster                                           |
| meteor_contest             | 73.5 ms                                                     | 72.8 ms: 1.01x faster                                           |
| telco                      | 4.79 ms                                                     | 4.75 ms: 1.01x faster                                           |
| sqlglot_optimize           | 32.9 ms                                                     | 32.6 ms: 1.01x faster                                           |
| xml_etree_process          | 37.0 ms                                                     | 36.7 ms: 1.01x faster                                           |
| richards_super             | 30.9 ms                                                     | 30.6 ms: 1.01x faster                                           |
| pathlib                    | 80.9 ms                                                     | 80.3 ms: 1.01x faster                                           |
| pprint_pformat             | 999 ms                                                      | 992 ms: 1.01x faster                                            |
| pyflate                    | 283 ms                                                      | 281 ms: 1.01x faster                                            |
| hexiom                     | 3.89 ms                                                     | 3.91 ms: 1.00x slower                                           |
| richards                   | 27.3 ms                                                     | 27.5 ms: 1.00x slower                                           |
| async_generators           | 223 ms                                                      | 224 ms: 1.01x slower                                            |
| genshi_text                | 15.6 ms                                                     | 15.8 ms: 1.02x slower                                           |
| float                      | 49.9 ms                                                     | 50.8 ms: 1.02x slower                                           |
| xml_etree_iterparse        | 61.8 ms                                                     | 62.9 ms: 1.02x slower                                           |
| logging_format             | 6.26 us                                                     | 6.41 us: 1.02x slower                                           |
| sqlglot_transpile          | 956 us                                                      | 980 us: 1.02x slower                                            |
| tomli_loads                | 1.39 sec                                                    | 1.43 sec: 1.03x slower                                          |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                            |
| coroutines                 | 12.8 ms                                                     | 13.2 ms: 1.03x slower                                           |
| deltablue                  | 1.92 ms                                                     | 1.98 ms: 1.03x slower                                           |
| coverage                   | 45.6 ms                                                     | 47.1 ms: 1.03x slower                                           |
| scimark_lu                 | 53.0 ms                                                     | 55.5 ms: 1.05x slower                                           |
| generators                 | 19.5 ms                                                     | 20.6 ms: 1.05x slower                                           |
| nqueens                    | 56.7 ms                                                     | 59.9 ms: 1.06x slower                                           |
| comprehensions             | 10.3 us                                                     | 11.0 us: 1.08x slower                                           |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 454 ms: 1.19x slower                                            |
| async_tree_none            | 226 ms                                                      | 270 ms: 1.20x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 349 ms: 1.21x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 340 ms: 1.23x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 474 ms: 1.26x slower                                            |
| async_tree_none_tg         | 209 ms                                                      | 274 ms: 1.31x slower                                            |
| async_tree_io              | 521 ms                                                      | 738 ms: 1.42x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 758 ms: 1.46x slower                                            |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (16): genshi_xml, pylint, bench_thread_pool, xml_etree_generate, regex_effbot, chaos, nbody, pidigits, xml_etree_parse, python_startup_no_site, scimark_fft, raytrace, chameleon, logging_simple, json, pycparser
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.013x faster
# HPT report

- Reliability score: 94.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown