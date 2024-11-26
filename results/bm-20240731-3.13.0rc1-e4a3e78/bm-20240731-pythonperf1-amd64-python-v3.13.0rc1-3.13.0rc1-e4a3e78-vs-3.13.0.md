# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc1
- machine: windows-amd64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.012x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 226 ms: 1.02x slower                                              |
| chameleon      | 4.82 ms                                                     | 5.10 ms: 1.06x slower                                             |
| docutils       | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                            |
| tornado_http   | 93.0 ms                                                     | 92.0 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                       | 1.03x slower                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg | 288 ms                                                      | 272 ms: 1.06x faster                                              |
| coroutines                | 12.8 ms                                                     | 13.0 ms: 1.02x slower                                             |
| async_generators          | 223 ms                                                      | 231 ms: 1.03x slower                                              |
| async_tree_cpu_io_mixed   | 383 ms                                                      | 396 ms: 1.03x slower                                              |
| async_tree_io             | 521 ms                                                      | 603 ms: 1.16x slower                                              |
| async_tree_io_tg          | 518 ms                                                      | 627 ms: 1.21x slower                                              |
| Geometric mean            | (ref)                                                       | 1.04x slower                                                      |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                              |
| nbody          | 68.4 ms                                                     | 76.8 ms: 1.12x slower                                             |
| Geometric mean | (ref)                                                       | 1.05x slower                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 16.4 ms: 1.30x faster                                             |
| regex_effbot   | 1.58 ms                                                     | 1.62 ms: 1.03x slower                                             |
| regex_compile  | 80.5 ms                                                     | 83.9 ms: 1.04x slower                                             |
| regex_dna      | 115 ms                                                      | 123 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                       | 1.03x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.2 us: 1.07x faster                                             |
| xml_etree_parse      | 93.6 ms                                                     | 91.5 ms: 1.02x faster                                             |
| tomli_loads          | 1.39 sec                                                    | 1.42 sec: 1.02x slower                                            |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.0 ms: 1.02x slower                                             |
| pickle_pure_python   | 190 us                                                      | 194 us: 1.02x slower                                              |
| xml_etree_generate   | 54.0 ms                                                     | 55.4 ms: 1.03x slower                                             |
| unpickle_pure_python | 133 us                                                      | 138 us: 1.03x slower                                              |
| xml_etree_process    | 37.0 ms                                                     | 38.4 ms: 1.04x slower                                             |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                      |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 22.5 ms: 1.13x faster                                             |
| python_startup_no_site | 18.1 ms                                                     | 18.4 ms: 1.02x slower                                             |
| Geometric mean         | (ref)                                                       | 1.06x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 33.2 ms: 1.07x faster                                             |
| genshi_text     | 15.6 ms                                                     | 15.3 ms: 1.02x faster                                             |
| django_template | 22.4 ms                                                     | 22.7 ms: 1.02x slower                                             |
| mako            | 6.35 ms                                                     | 6.66 ms: 1.05x slower                                             |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                      |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mypy2                     | 679 ms                                                      | 439 ms: 1.55x faster                                              |
| create_gc_cycles          | 1.26 ms                                                     | 917 us: 1.37x faster                                              |
| regex_v8                  | 21.4 ms                                                     | 16.4 ms: 1.30x faster                                             |
| gc_traversal              | 1.97 ms                                                     | 1.58 ms: 1.24x faster                                             |
| bench_mp_pool             | 86.4 ms                                                     | 71.1 ms: 1.22x faster                                             |
| python_startup            | 25.4 ms                                                     | 22.5 ms: 1.13x faster                                             |
| genshi_xml                | 35.5 ms                                                     | 33.2 ms: 1.07x faster                                             |
| json_loads                | 15.1 us                                                     | 14.2 us: 1.07x faster                                             |
| async_tree_memoization_tg | 288 ms                                                      | 272 ms: 1.06x faster                                              |
| bench_thread_pool         | 847 us                                                      | 813 us: 1.04x faster                                              |
| xml_etree_parse           | 93.6 ms                                                     | 91.5 ms: 1.02x faster                                             |
| logging_simple            | 5.96 us                                                     | 5.85 us: 1.02x faster                                             |
| genshi_text               | 15.6 ms                                                     | 15.3 ms: 1.02x faster                                             |
| tornado_http              | 93.0 ms                                                     | 92.0 ms: 1.01x faster                                             |
| sympy_expand              | 291 ms                                                      | 289 ms: 1.01x faster                                              |
| logging_format            | 6.26 us                                                     | 6.29 us: 1.01x slower                                             |
| sympy_sum                 | 86.9 ms                                                     | 87.6 ms: 1.01x slower                                             |
| tomli_loads               | 1.39 sec                                                    | 1.42 sec: 1.02x slower                                            |
| python_startup_no_site    | 18.1 ms                                                     | 18.4 ms: 1.02x slower                                             |
| django_template           | 22.4 ms                                                     | 22.7 ms: 1.02x slower                                             |
| sympy_integrate           | 12.5 ms                                                     | 12.7 ms: 1.02x slower                                             |
| pathlib                   | 80.9 ms                                                     | 82.3 ms: 1.02x slower                                             |
| go                        | 87.0 ms                                                     | 88.6 ms: 1.02x slower                                             |
| coroutines                | 12.8 ms                                                     | 13.0 ms: 1.02x slower                                             |
| xml_etree_iterparse       | 61.8 ms                                                     | 63.0 ms: 1.02x slower                                             |
| pidigits                  | 148 ms                                                      | 151 ms: 1.02x slower                                              |
| raytrace                  | 160 ms                                                      | 164 ms: 1.02x slower                                              |
| 2to3                      | 221 ms                                                      | 226 ms: 1.02x slower                                              |
| pickle_pure_python        | 190 us                                                      | 194 us: 1.02x slower                                              |
| spectral_norm             | 62.8 ms                                                     | 64.3 ms: 1.02x slower                                             |
| xml_etree_generate        | 54.0 ms                                                     | 55.4 ms: 1.03x slower                                             |
| regex_effbot              | 1.58 ms                                                     | 1.62 ms: 1.03x slower                                             |
| logging_silent            | 54.6 ns                                                     | 56.1 ns: 1.03x slower                                             |
| deepcopy_reduce           | 2.06 us                                                     | 2.11 us: 1.03x slower                                             |
| sqlglot_normalize         | 175 ms                                                      | 180 ms: 1.03x slower                                              |
| sqlglot_optimize          | 32.9 ms                                                     | 33.9 ms: 1.03x slower                                             |
| async_generators          | 223 ms                                                      | 231 ms: 1.03x slower                                              |
| async_tree_cpu_io_mixed   | 383 ms                                                      | 396 ms: 1.03x slower                                              |
| unpickle_pure_python      | 133 us                                                      | 138 us: 1.03x slower                                              |
| xml_etree_process         | 37.0 ms                                                     | 38.4 ms: 1.04x slower                                             |
| pprint_safe_repr          | 494 ms                                                      | 512 ms: 1.04x slower                                              |
| richards                  | 27.3 ms                                                     | 28.3 ms: 1.04x slower                                             |
| richards_super            | 30.9 ms                                                     | 32.1 ms: 1.04x slower                                             |
| mdp                       | 1.39 sec                                                    | 1.44 sec: 1.04x slower                                            |
| regex_compile             | 80.5 ms                                                     | 83.9 ms: 1.04x slower                                             |
| sqlglot_parse             | 771 us                                                      | 803 us: 1.04x slower                                              |
| crypto_pyaes              | 45.4 ms                                                     | 47.4 ms: 1.04x slower                                             |
| chaos                     | 38.5 ms                                                     | 40.4 ms: 1.05x slower                                             |
| deepcopy                  | 226 us                                                      | 237 us: 1.05x slower                                              |
| hexiom                    | 3.89 ms                                                     | 4.08 ms: 1.05x slower                                             |
| mako                      | 6.35 ms                                                     | 6.66 ms: 1.05x slower                                             |
| pprint_pformat            | 999 ms                                                      | 1.05 sec: 1.05x slower                                            |
| deltablue                 | 1.92 ms                                                     | 2.01 ms: 1.05x slower                                             |
| pyflate                   | 283 ms                                                      | 298 ms: 1.05x slower                                              |
| generators                | 19.5 ms                                                     | 20.6 ms: 1.06x slower                                             |
| nqueens                   | 56.7 ms                                                     | 59.8 ms: 1.06x slower                                             |
| sqlglot_transpile         | 956 us                                                      | 1.01 ms: 1.06x slower                                             |
| chameleon                 | 4.82 ms                                                     | 5.10 ms: 1.06x slower                                             |
| comprehensions            | 10.3 us                                                     | 10.9 us: 1.07x slower                                             |
| docutils                  | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                            |
| fannkuch                  | 253 ms                                                      | 271 ms: 1.07x slower                                              |
| deepcopy_memo             | 23.3 us                                                     | 24.9 us: 1.07x slower                                             |
| regex_dna                 | 115 ms                                                      | 123 ms: 1.07x slower                                              |
| scimark_sor               | 76.2 ms                                                     | 81.9 ms: 1.08x slower                                             |
| scimark_monte_carlo       | 40.8 ms                                                     | 44.4 ms: 1.09x slower                                             |
| scimark_sparse_mat_mult   | 2.46 ms                                                     | 2.68 ms: 1.09x slower                                             |
| pycparser                 | 683 ms                                                      | 754 ms: 1.10x slower                                              |
| scimark_fft               | 172 ms                                                      | 192 ms: 1.11x slower                                              |
| nbody                     | 68.4 ms                                                     | 76.8 ms: 1.12x slower                                             |
| async_tree_io             | 521 ms                                                      | 603 ms: 1.16x slower                                              |
| scimark_lu                | 53.0 ms                                                     | 61.4 ms: 1.16x slower                                             |
| async_tree_io_tg          | 518 ms                                                      | 627 ms: 1.21x slower                                              |
| Geometric mean            | (ref)                                                       | 1.01x slower                                                      |

Benchmark hidden because not significant (16): json, json_dumps, meteor_contest, telco, sympy_str, float, coverage, html5lib, dulwich_log, thrift, typing_runtime_protocols, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.012x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown