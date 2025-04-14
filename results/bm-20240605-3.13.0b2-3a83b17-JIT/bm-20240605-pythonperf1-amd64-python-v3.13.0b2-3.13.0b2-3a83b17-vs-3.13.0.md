# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: windows-amd64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.006x faster
- HPT reliability: 90.83%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 229 ms: 1.04x slower                                            |
| chameleon      | 4.82 ms                                                     | 5.00 ms: 1.04x slower                                           |
| docutils       | 1.57 sec                                                    | 1.77 sec: 1.13x slower                                          |
| html5lib       | 38.9 ms                                                     | 37.9 ms: 1.03x faster                                           |
| tornado_http   | 93.0 ms                                                     | 86.1 ms: 1.08x faster                                           |
| Geometric mean | (ref)                                                       | 1.02x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg | 288 ms                                                      | 273 ms: 1.06x faster                                            |
| async_tree_cpu_io_mixed   | 383 ms                                                      | 392 ms: 1.02x slower                                            |
| async_tree_none_tg        | 209 ms                                                      | 215 ms: 1.03x slower                                            |
| coroutines                | 12.8 ms                                                     | 13.2 ms: 1.04x slower                                           |
| async_tree_io             | 521 ms                                                      | 579 ms: 1.11x slower                                            |
| async_generators          | 223 ms                                                      | 252 ms: 1.13x slower                                            |
| async_tree_io_tg          | 518 ms                                                      | 624 ms: 1.20x slower                                            |
| Geometric mean            | (ref)                                                       | 1.05x slower                                                    |

Benchmark hidden because not significant (3): async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 53.1 ms: 1.29x faster                                           |
| float          | 49.9 ms                                                     | 44.3 ms: 1.13x faster                                           |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                       | 1.13x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.2 ms: 1.41x faster                                           |
| regex_effbot   | 1.58 ms                                                     | 1.55 ms: 1.01x faster                                           |
| regex_compile  | 80.5 ms                                                     | 88.9 ms: 1.10x slower                                           |
| Geometric mean | (ref)                                                       | 1.07x faster                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.24 sec: 1.13x faster                                          |
| pickle_pure_python   | 190 us                                                      | 175 us: 1.08x faster                                            |
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                           |
| xml_etree_generate   | 54.0 ms                                                     | 51.4 ms: 1.05x faster                                           |
| json_dumps           | 5.92 ms                                                     | 5.70 ms: 1.04x faster                                           |
| xml_etree_parse      | 93.6 ms                                                     | 90.3 ms: 1.04x faster                                           |
| unpickle_pure_python | 133 us                                                      | 130 us: 1.02x faster                                            |
| xml_etree_iterparse  | 61.8 ms                                                     | 61.2 ms: 1.01x faster                                           |
| xml_etree_process    | 37.0 ms                                                     | 36.8 ms: 1.01x faster                                           |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 22.7 ms: 1.12x faster                                           |
| python_startup_no_site | 18.1 ms                                                     | 18.6 ms: 1.03x slower                                           |
| Geometric mean         | (ref)                                                       | 1.04x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.13 ms: 1.24x faster                                           |
| django_template | 22.4 ms                                                     | 25.4 ms: 1.14x slower                                           |
| genshi_text     | 15.6 ms                                                     | 17.9 ms: 1.15x slower                                           |
| genshi_xml      | 35.5 ms                                                     | 44.2 ms: 1.25x slower                                           |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8                  | 21.4 ms                                                     | 15.2 ms: 1.41x faster                                           |
| mypy2                     | 679 ms                                                      | 486 ms: 1.40x faster                                            |
| spectral_norm             | 62.8 ms                                                     | 45.3 ms: 1.39x faster                                           |
| create_gc_cycles          | 1.26 ms                                                     | 912 us: 1.38x faster                                            |
| nbody                     | 68.4 ms                                                     | 53.1 ms: 1.29x faster                                           |
| gc_traversal              | 1.97 ms                                                     | 1.55 ms: 1.27x faster                                           |
| mako                      | 6.35 ms                                                     | 5.13 ms: 1.24x faster                                           |
| bench_mp_pool             | 86.4 ms                                                     | 72.0 ms: 1.20x faster                                           |
| fannkuch                  | 253 ms                                                      | 215 ms: 1.18x faster                                            |
| scimark_fft               | 172 ms                                                      | 150 ms: 1.15x faster                                            |
| tomli_loads               | 1.39 sec                                                    | 1.24 sec: 1.13x faster                                          |
| float                     | 49.9 ms                                                     | 44.3 ms: 1.13x faster                                           |
| scimark_sparse_mat_mult   | 2.46 ms                                                     | 2.19 ms: 1.12x faster                                           |
| python_startup            | 25.4 ms                                                     | 22.7 ms: 1.12x faster                                           |
| deepcopy_memo             | 23.3 us                                                     | 20.9 us: 1.11x faster                                           |
| json                      | 3.19 ms                                                     | 2.88 ms: 1.11x faster                                           |
| pyflate                   | 283 ms                                                      | 257 ms: 1.10x faster                                            |
| crypto_pyaes              | 45.4 ms                                                     | 41.5 ms: 1.10x faster                                           |
| scimark_monte_carlo       | 40.8 ms                                                     | 37.7 ms: 1.08x faster                                           |
| pickle_pure_python        | 190 us                                                      | 175 us: 1.08x faster                                            |
| tornado_http              | 93.0 ms                                                     | 86.1 ms: 1.08x faster                                           |
| telco                     | 4.79 ms                                                     | 4.46 ms: 1.07x faster                                           |
| json_loads                | 15.1 us                                                     | 14.1 us: 1.07x faster                                           |
| pprint_safe_repr          | 494 ms                                                      | 461 ms: 1.07x faster                                            |
| bench_thread_pool         | 847 us                                                      | 793 us: 1.07x faster                                            |
| pathlib                   | 80.9 ms                                                     | 76.3 ms: 1.06x faster                                           |
| async_tree_memoization_tg | 288 ms                                                      | 273 ms: 1.06x faster                                            |
| pprint_pformat            | 999 ms                                                      | 946 ms: 1.06x faster                                            |
| xml_etree_generate        | 54.0 ms                                                     | 51.4 ms: 1.05x faster                                           |
| json_dumps                | 5.92 ms                                                     | 5.70 ms: 1.04x faster                                           |
| xml_etree_parse           | 93.6 ms                                                     | 90.3 ms: 1.04x faster                                           |
| html5lib                  | 38.9 ms                                                     | 37.9 ms: 1.03x faster                                           |
| unpickle_pure_python      | 133 us                                                      | 130 us: 1.02x faster                                            |
| meteor_contest            | 73.5 ms                                                     | 72.0 ms: 1.02x faster                                           |
| dulwich_log               | 40.8 ms                                                     | 40.2 ms: 1.02x faster                                           |
| regex_effbot              | 1.58 ms                                                     | 1.55 ms: 1.01x faster                                           |
| xml_etree_iterparse       | 61.8 ms                                                     | 61.2 ms: 1.01x faster                                           |
| logging_simple            | 5.96 us                                                     | 5.91 us: 1.01x faster                                           |
| xml_etree_process         | 37.0 ms                                                     | 36.8 ms: 1.01x faster                                           |
| comprehensions            | 10.3 us                                                     | 10.4 us: 1.01x slower                                           |
| logging_silent            | 54.6 ns                                                     | 55.3 ns: 1.01x slower                                           |
| pidigits                  | 148 ms                                                      | 150 ms: 1.01x slower                                            |
| chaos                     | 38.5 ms                                                     | 39.2 ms: 1.02x slower                                           |
| async_tree_cpu_io_mixed   | 383 ms                                                      | 392 ms: 1.02x slower                                            |
| logging_format            | 6.26 us                                                     | 6.42 us: 1.03x slower                                           |
| python_startup_no_site    | 18.1 ms                                                     | 18.6 ms: 1.03x slower                                           |
| async_tree_none_tg        | 209 ms                                                      | 215 ms: 1.03x slower                                            |
| deepcopy_reduce           | 2.06 us                                                     | 2.13 us: 1.04x slower                                           |
| chameleon                 | 4.82 ms                                                     | 5.00 ms: 1.04x slower                                           |
| coroutines                | 12.8 ms                                                     | 13.2 ms: 1.04x slower                                           |
| 2to3                      | 221 ms                                                      | 229 ms: 1.04x slower                                            |
| sqlglot_parse             | 771 us                                                      | 801 us: 1.04x slower                                            |
| thrift                    | 8.80 ms                                                     | 9.21 ms: 1.05x slower                                           |
| deepcopy                  | 226 us                                                      | 241 us: 1.06x slower                                            |
| typing_runtime_protocols  | 105 us                                                      | 113 us: 1.07x slower                                            |
| sympy_str                 | 169 ms                                                      | 181 ms: 1.07x slower                                            |
| go                        | 87.0 ms                                                     | 93.8 ms: 1.08x slower                                           |
| sympy_sum                 | 86.9 ms                                                     | 93.9 ms: 1.08x slower                                           |
| nqueens                   | 56.7 ms                                                     | 61.4 ms: 1.08x slower                                           |
| sqlglot_transpile         | 956 us                                                      | 1.04 ms: 1.08x slower                                           |
| pycparser                 | 683 ms                                                      | 741 ms: 1.09x slower                                            |
| richards                  | 27.3 ms                                                     | 29.7 ms: 1.09x slower                                           |
| richards_super            | 30.9 ms                                                     | 33.5 ms: 1.09x slower                                           |
| mdp                       | 1.39 sec                                                    | 1.51 sec: 1.09x slower                                          |
| generators                | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                           |
| sympy_expand              | 291 ms                                                      | 317 ms: 1.09x slower                                            |
| scimark_sor               | 76.2 ms                                                     | 83.5 ms: 1.10x slower                                           |
| raytrace                  | 160 ms                                                      | 176 ms: 1.10x slower                                            |
| regex_compile             | 80.5 ms                                                     | 88.9 ms: 1.10x slower                                           |
| async_tree_io             | 521 ms                                                      | 579 ms: 1.11x slower                                            |
| pylint                    | 211 ms                                                      | 235 ms: 1.12x slower                                            |
| sqlglot_optimize          | 32.9 ms                                                     | 37.0 ms: 1.12x slower                                           |
| sympy_integrate           | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                           |
| async_generators          | 223 ms                                                      | 252 ms: 1.13x slower                                            |
| docutils                  | 1.57 sec                                                    | 1.77 sec: 1.13x slower                                          |
| django_template           | 22.4 ms                                                     | 25.4 ms: 1.14x slower                                           |
| genshi_text               | 15.6 ms                                                     | 17.9 ms: 1.15x slower                                           |
| async_tree_io_tg          | 518 ms                                                      | 624 ms: 1.20x slower                                            |
| hexiom                    | 3.89 ms                                                     | 4.72 ms: 1.21x slower                                           |
| deltablue                 | 1.92 ms                                                     | 2.37 ms: 1.23x slower                                           |
| genshi_xml                | 35.5 ms                                                     | 44.2 ms: 1.25x slower                                           |
| scimark_lu                | 53.0 ms                                                     | 69.4 ms: 1.31x slower                                           |
| Geometric mean            | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (5): coverage, regex_dna, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.006x faster
# HPT report

- Reliability score: 90.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown