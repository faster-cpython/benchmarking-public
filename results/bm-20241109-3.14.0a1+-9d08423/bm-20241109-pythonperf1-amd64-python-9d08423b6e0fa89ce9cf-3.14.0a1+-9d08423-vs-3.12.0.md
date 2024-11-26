# Results vs. 3.12.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: windows-amd64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.024x slower
- HPT reliability: 99.58%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 261 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 212 ms: 1.34x faster                                                        |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.32x faster                                                        |
| async_tree_io              | 731 ms                                                      | 564 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 402 ms: 1.25x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 279 ms: 1.22x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 635 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| float          | 56.8 ms                                                     | 56.0 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 79.6 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 91.5 ms: 1.05x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 57.4 ms: 1.03x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 40.5 ms: 1.08x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 153 us: 1.15x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 229 us: 1.17x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.67 ms: 1.17x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.60 sec: 1.17x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.93 ms: 1.02x faster                                                       |
| django_template | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 261 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 212 ms: 1.34x faster                                                        |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.32x faster                                                        |
| async_tree_io              | 731 ms                                                      | 564 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 402 ms: 1.25x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 279 ms: 1.22x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 635 ms: 1.21x faster                                                        |
| deepcopy                   | 238 us                                                      | 196 us: 1.21x faster                                                        |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.18x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.2 us: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 813 us: 1.05x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                       |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| json                       | 3.05 ms                                                     | 2.92 ms: 1.04x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.00 us: 1.04x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.7 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| mako                       | 7.09 ms                                                     | 6.93 ms: 1.02x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.4 ms: 1.02x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 79.1 ms: 1.02x faster                                                       |
| float                      | 56.8 ms                                                     | 56.0 ms: 1.01x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.3 ms: 1.01x faster                                                       |
| go                         | 91.6 ms                                                     | 90.5 ms: 1.01x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 48.0 ms: 1.01x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 67.8 ms: 1.01x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.83 us: 1.02x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.39 us: 1.02x slower                                                       |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.4 ms: 1.03x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 60.6 ms: 1.03x slower                                                       |
| async_generators           | 239 ms                                                      | 248 ms: 1.03x slower                                                        |
| chaos                      | 43.3 ms                                                     | 44.8 ms: 1.03x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 65.0 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.04x slower                                                       |
| raytrace                   | 192 ms                                                      | 200 ms: 1.04x slower                                                        |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 78.0 ms: 1.05x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 91.5 ms: 1.05x slower                                                       |
| pycparser                  | 699 ms                                                      | 738 ms: 1.06x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 198 ms: 1.06x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                      |
| scimark_fft                | 184 ms                                                      | 196 ms: 1.06x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 545 ms: 1.06x slower                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.73 ms: 1.07x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 64.6 ns: 1.07x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 40.5 ms: 1.08x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 37.2 ms: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 307 ms: 1.08x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                       |
| pyflate                    | 295 ms                                                      | 322 ms: 1.09x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.49 ms: 1.10x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.0 ms: 1.10x slower                                                       |
| nbody                      | 71.9 ms                                                     | 79.6 ms: 1.11x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.14 ms: 1.11x slower                                                       |
| fannkuch                   | 247 ms                                                      | 280 ms: 1.13x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 922 us: 1.15x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 153 us: 1.15x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 91.0 ms: 1.15x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.2 ms: 1.16x slower                                                       |
| richards_super             | 32.1 ms                                                     | 37.2 ms: 1.16x slower                                                       |
| richards                   | 28.4 ms                                                     | 32.9 ms: 1.16x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.81 ms: 1.17x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 229 us: 1.17x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.67 ms: 1.17x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.60 sec: 1.17x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.18x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 83.0 ms: 1.20x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.93 ms: 1.27x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.38 ms: 1.84x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (3): regex_effbot, xml_etree_parse, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.024x slower
# HPT report

- Reliability score: 99.58% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown