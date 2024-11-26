# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc2
- machine: windows-amd64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.018x faster
- HPT reliability: 58.13%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 216 ms: 1.02x faster                                              |
| chameleon      | 4.82 ms                                                     | 4.89 ms: 1.01x slower                                             |
| docutils       | 1.57 sec                                                    | 1.67 sec: 1.06x slower                                            |
| html5lib       | 38.9 ms                                                     | 39.8 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                       | 1.01x slower                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg | 288 ms                                                      | 266 ms: 1.09x faster                                              |
| async_tree_none           | 226 ms                                                      | 222 ms: 1.02x faster                                              |
| coroutines                | 12.8 ms                                                     | 12.9 ms: 1.01x slower                                             |
| async_tree_cpu_io_mixed   | 383 ms                                                      | 389 ms: 1.02x slower                                              |
| async_generators          | 223 ms                                                      | 232 ms: 1.04x slower                                              |
| async_tree_io             | 521 ms                                                      | 591 ms: 1.13x slower                                              |
| async_tree_io_tg          | 518 ms                                                      | 613 ms: 1.18x slower                                              |
| Geometric mean            | (ref)                                                       | 1.03x slower                                                      |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 68.0 ms: 1.01x faster                                             |
| pidigits       | 148 ms                                                      | 152 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                       | 1.01x slower                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.3 ms: 1.40x faster                                             |
| regex_compile  | 80.5 ms                                                     | 82.0 ms: 1.02x slower                                             |
| regex_effbot   | 1.58 ms                                                     | 1.62 ms: 1.03x slower                                             |
| regex_dna      | 115 ms                                                      | 126 ms: 1.09x slower                                              |
| Geometric mean | (ref)                                                       | 1.05x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                             |
| unpickle_pure_python | 133 us                                                      | 126 us: 1.06x faster                                              |
| pickle_pure_python   | 190 us                                                      | 185 us: 1.02x faster                                              |
| json_dumps           | 5.92 ms                                                     | 5.80 ms: 1.02x faster                                             |
| xml_etree_parse      | 93.6 ms                                                     | 92.9 ms: 1.01x faster                                             |
| tomli_loads          | 1.39 sec                                                    | 1.38 sec: 1.01x faster                                            |
| xml_etree_generate   | 54.0 ms                                                     | 54.4 ms: 1.01x slower                                             |
| xml_etree_process    | 37.0 ms                                                     | 37.8 ms: 1.02x slower                                             |
| xml_etree_iterparse  | 61.8 ms                                                     | 64.2 ms: 1.04x slower                                             |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 22.3 ms: 1.14x faster                                             |
| python_startup_no_site | 18.1 ms                                                     | 17.9 ms: 1.01x faster                                             |
| Geometric mean         | (ref)                                                       | 1.08x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 32.0 ms: 1.11x faster                                             |
| genshi_text     | 15.6 ms                                                     | 15.2 ms: 1.03x faster                                             |
| django_template | 22.4 ms                                                     | 22.1 ms: 1.01x faster                                             |
| mako            | 6.35 ms                                                     | 6.50 ms: 1.02x slower                                             |
| Geometric mean  | (ref)                                                       | 1.03x faster                                                      |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mypy2                     | 679 ms                                                      | 433 ms: 1.57x faster                                              |
| regex_v8                  | 21.4 ms                                                     | 15.3 ms: 1.40x faster                                             |
| create_gc_cycles          | 1.26 ms                                                     | 901 us: 1.40x faster                                              |
| bench_mp_pool             | 86.4 ms                                                     | 68.0 ms: 1.27x faster                                             |
| gc_traversal              | 1.97 ms                                                     | 1.55 ms: 1.27x faster                                             |
| python_startup            | 25.4 ms                                                     | 22.3 ms: 1.14x faster                                             |
| pylint                    | 211 ms                                                      | 186 ms: 1.13x faster                                              |
| genshi_xml                | 35.5 ms                                                     | 32.0 ms: 1.11x faster                                             |
| async_tree_memoization_tg | 288 ms                                                      | 266 ms: 1.09x faster                                              |
| json_loads                | 15.1 us                                                     | 14.1 us: 1.07x faster                                             |
| json                      | 3.19 ms                                                     | 2.98 ms: 1.07x faster                                             |
| unpickle_pure_python      | 133 us                                                      | 126 us: 1.06x faster                                              |
| logging_simple            | 5.96 us                                                     | 5.67 us: 1.05x faster                                             |
| richards_super            | 30.9 ms                                                     | 29.5 ms: 1.05x faster                                             |
| scimark_sparse_mat_mult   | 2.46 ms                                                     | 2.35 ms: 1.04x faster                                             |
| richards                  | 27.3 ms                                                     | 26.2 ms: 1.04x faster                                             |
| hexiom                    | 3.89 ms                                                     | 3.75 ms: 1.04x faster                                             |
| genshi_text               | 15.6 ms                                                     | 15.2 ms: 1.03x faster                                             |
| logging_format            | 6.26 us                                                     | 6.09 us: 1.03x faster                                             |
| deepcopy_memo             | 23.3 us                                                     | 22.7 us: 1.03x faster                                             |
| logging_silent            | 54.6 ns                                                     | 53.3 ns: 1.03x faster                                             |
| spectral_norm             | 62.8 ms                                                     | 61.2 ms: 1.03x faster                                             |
| pickle_pure_python        | 190 us                                                      | 185 us: 1.02x faster                                              |
| fannkuch                  | 253 ms                                                      | 248 ms: 1.02x faster                                              |
| deepcopy_reduce           | 2.06 us                                                     | 2.02 us: 1.02x faster                                             |
| 2to3                      | 221 ms                                                      | 216 ms: 1.02x faster                                              |
| json_dumps                | 5.92 ms                                                     | 5.80 ms: 1.02x faster                                             |
| thrift                    | 8.80 ms                                                     | 8.64 ms: 1.02x faster                                             |
| meteor_contest            | 73.5 ms                                                     | 72.2 ms: 1.02x faster                                             |
| crypto_pyaes              | 45.4 ms                                                     | 44.6 ms: 1.02x faster                                             |
| pathlib                   | 80.9 ms                                                     | 79.6 ms: 1.02x faster                                             |
| async_tree_none           | 226 ms                                                      | 222 ms: 1.02x faster                                              |
| go                        | 87.0 ms                                                     | 85.7 ms: 1.01x faster                                             |
| typing_runtime_protocols  | 105 us                                                      | 104 us: 1.01x faster                                              |
| django_template           | 22.4 ms                                                     | 22.1 ms: 1.01x faster                                             |
| deepcopy                  | 226 us                                                      | 223 us: 1.01x faster                                              |
| python_startup_no_site    | 18.1 ms                                                     | 17.9 ms: 1.01x faster                                             |
| scimark_sor               | 76.2 ms                                                     | 75.3 ms: 1.01x faster                                             |
| deltablue                 | 1.92 ms                                                     | 1.90 ms: 1.01x faster                                             |
| telco                     | 4.79 ms                                                     | 4.74 ms: 1.01x faster                                             |
| xml_etree_parse           | 93.6 ms                                                     | 92.9 ms: 1.01x faster                                             |
| tomli_loads               | 1.39 sec                                                    | 1.38 sec: 1.01x faster                                            |
| nbody                     | 68.4 ms                                                     | 68.0 ms: 1.01x faster                                             |
| chaos                     | 38.5 ms                                                     | 38.3 ms: 1.00x faster                                             |
| xml_etree_generate        | 54.0 ms                                                     | 54.4 ms: 1.01x slower                                             |
| pprint_pformat            | 999 ms                                                      | 1.01 sec: 1.01x slower                                            |
| coroutines                | 12.8 ms                                                     | 12.9 ms: 1.01x slower                                             |
| sqlglot_optimize          | 32.9 ms                                                     | 33.2 ms: 1.01x slower                                             |
| coverage                  | 45.6 ms                                                     | 46.0 ms: 1.01x slower                                             |
| nqueens                   | 56.7 ms                                                     | 57.3 ms: 1.01x slower                                             |
| raytrace                  | 160 ms                                                      | 162 ms: 1.01x slower                                              |
| comprehensions            | 10.3 us                                                     | 10.4 us: 1.01x slower                                             |
| chameleon                 | 4.82 ms                                                     | 4.89 ms: 1.01x slower                                             |
| async_tree_cpu_io_mixed   | 383 ms                                                      | 389 ms: 1.02x slower                                              |
| regex_compile             | 80.5 ms                                                     | 82.0 ms: 1.02x slower                                             |
| xml_etree_process         | 37.0 ms                                                     | 37.8 ms: 1.02x slower                                             |
| html5lib                  | 38.9 ms                                                     | 39.8 ms: 1.02x slower                                             |
| scimark_monte_carlo       | 40.8 ms                                                     | 41.8 ms: 1.02x slower                                             |
| mako                      | 6.35 ms                                                     | 6.50 ms: 1.02x slower                                             |
| pidigits                  | 148 ms                                                      | 152 ms: 1.03x slower                                              |
| dulwich_log               | 40.8 ms                                                     | 42.0 ms: 1.03x slower                                             |
| sqlglot_parse             | 771 us                                                      | 793 us: 1.03x slower                                              |
| sqlglot_transpile         | 956 us                                                      | 985 us: 1.03x slower                                              |
| regex_effbot              | 1.58 ms                                                     | 1.62 ms: 1.03x slower                                             |
| generators                | 19.5 ms                                                     | 20.2 ms: 1.04x slower                                             |
| xml_etree_iterparse       | 61.8 ms                                                     | 64.2 ms: 1.04x slower                                             |
| async_generators          | 223 ms                                                      | 232 ms: 1.04x slower                                              |
| docutils                  | 1.57 sec                                                    | 1.67 sec: 1.06x slower                                            |
| scimark_lu                | 53.0 ms                                                     | 56.5 ms: 1.07x slower                                             |
| mdp                       | 1.39 sec                                                    | 1.49 sec: 1.07x slower                                            |
| pycparser                 | 683 ms                                                      | 733 ms: 1.07x slower                                              |
| regex_dna                 | 115 ms                                                      | 126 ms: 1.09x slower                                              |
| async_tree_io             | 521 ms                                                      | 591 ms: 1.13x slower                                              |
| async_tree_io_tg          | 518 ms                                                      | 613 ms: 1.18x slower                                              |
| Geometric mean            | (ref)                                                       | 1.02x faster                                                      |

Benchmark hidden because not significant (14): bench_thread_pool, async_tree_memoization, tornado_http, pyflate, sympy_expand, sqlglot_normalize, scimark_fft, pprint_safe_repr, sympy_integrate, async_tree_none_tg, float, sympy_str, sympy_sum, async_tree_cpu_io_mixed_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.018x faster
# HPT report

- Reliability score: 58.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown