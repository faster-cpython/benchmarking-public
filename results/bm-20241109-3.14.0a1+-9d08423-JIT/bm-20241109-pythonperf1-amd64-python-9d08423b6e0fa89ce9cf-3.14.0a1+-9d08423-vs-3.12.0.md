# Results vs. 3.12.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: windows-amd64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.019x faster
- HPT reliability: 87.60%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 251 ms: 1.15x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.88 sec: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 261 ms: 1.41x faster                                                        |
| async_tree_none            | 291 ms                                                      | 210 ms: 1.39x faster                                                        |
| async_tree_io              | 731 ms                                                      | 546 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 218 ms: 1.31x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 262 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 403 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 627 ms: 1.23x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.2 ms: 1.35x faster                                                       |
| float          | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 90.9 ms: 1.04x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 51.0 ms: 1.09x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.27 sec: 1.08x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.0 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 94.4 ms: 1.01x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 207 us: 1.06x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 144 us: 1.08x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.42 ms: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.8 ms: 1.16x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.9 ms: 1.28x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.04 ms: 1.41x faster                                                       |
| django_template | 22.9 ms                                                     | 26.7 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 16.6 us: 1.43x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 261 ms: 1.41x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.04 ms: 1.41x faster                                                       |
| async_tree_none            | 291 ms                                                      | 210 ms: 1.39x faster                                                        |
| nbody                      | 71.9 ms                                                     | 53.2 ms: 1.35x faster                                                       |
| async_tree_io              | 731 ms                                                      | 546 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 218 ms: 1.31x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 262 ms: 1.29x faster                                                        |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 403 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 627 ms: 1.23x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 64.3 ms: 1.23x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 54.9 ms: 1.22x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 39.9 ms: 1.22x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.7 us: 1.21x faster                                                       |
| scimark_fft                | 184 ms                                                      | 153 ms: 1.21x faster                                                        |
| float                      | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.4 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.15x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 918 ms: 1.14x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.25 ms: 1.13x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 453 ms: 1.13x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 39.6 ms: 1.12x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 51.0 ms: 1.09x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.27 sec: 1.08x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 54.7 ms: 1.08x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 56.3 ns: 1.07x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.2 ms: 1.05x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.0 ms: 1.05x faster                                                       |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                       |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 827 us: 1.04x faster                                                        |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                       |
| fannkuch                   | 247 ms                                                      | 242 ms: 1.02x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 79.0 ms: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 73.5 ms: 1.02x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.22 us: 1.01x faster                                                       |
| go                         | 91.6 ms                                                     | 90.7 ms: 1.01x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.66 us: 1.01x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 94.4 ms: 1.01x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.3 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 721 ms: 1.03x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 90.9 ms: 1.04x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.29 ms: 1.04x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 144 us: 1.08x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.33 ms: 1.08x slower                                                       |
| async_generators           | 239 ms                                                      | 259 ms: 1.08x slower                                                        |
| sympy_str                  | 175 ms                                                      | 190 ms: 1.08x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 880 us: 1.09x slower                                                        |
| sympy_sum                  | 91.5 ms                                                     | 101 ms: 1.10x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 208 ms: 1.11x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.53 sec: 1.12x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.42 ms: 1.13x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.88 sec: 1.13x slower                                                      |
| sympy_expand               | 284 ms                                                      | 321 ms: 1.13x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.17 ms: 1.14x slower                                                       |
| 2to3                       | 218 ms                                                      | 251 ms: 1.15x slower                                                        |
| raytrace                   | 192 ms                                                      | 222 ms: 1.15x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 18.8 ms: 1.16x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.4 ms: 1.16x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.7 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 15.6 ms: 1.20x slower                                                       |
| richards_super             | 32.1 ms                                                     | 39.0 ms: 1.22x slower                                                       |
| richards                   | 28.4 ms                                                     | 34.9 ms: 1.23x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 42.6 ms: 1.23x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.16 ms: 1.26x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.93 ms: 1.27x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.9 ms: 1.28x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 93.3 ms: 1.35x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.83x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (2): generators, pyflate
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.019x faster
# HPT report

- Reliability score: 87.60% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown