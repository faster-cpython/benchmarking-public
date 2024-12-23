# Results vs. 3.12.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: windows-amd64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.006x faster
- HPT reliability: 93.66%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.04x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 409 ms: 1.88x faster                                                        |
| async_tree_io              | 731 ms                                                      | 412 ms: 1.77x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.69x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                        |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.57x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 229 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 355 ms: 1.41x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 354 ms: 1.38x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.59x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| float          | 56.8 ms                                                     | 55.3 ms: 1.03x faster                                                       |
| nbody          | 71.9 ms                                                     | 82.0 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                                       |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 88.7 ms: 1.01x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 21.2 ms: 1.49x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.3 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 58.3 ms: 1.04x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.06x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.4 ms: 1.07x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.14x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 228 us: 1.17x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.74 ms: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.78 ms: 1.04x faster                                                       |
| django_template | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 409 ms: 1.88x faster                                                        |
| async_tree_io              | 731 ms                                                      | 412 ms: 1.77x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.69x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                        |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.57x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 229 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 355 ms: 1.41x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 354 ms: 1.38x faster                                                        |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 20.8 us: 1.14x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.4 us: 1.14x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.91 us: 1.10x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.6 ms: 1.09x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 75.5 ms: 1.07x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 62.9 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.05x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.3 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.1 ms: 1.05x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.78 ms: 1.04x faster                                                       |
| go                         | 91.6 ms                                                     | 88.3 ms: 1.04x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 830 us: 1.03x faster                                                        |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| float                      | 56.8 ms                                                     | 55.3 ms: 1.03x faster                                                       |
| async_generators           | 239 ms                                                      | 235 ms: 1.02x faster                                                        |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.2 ms: 1.01x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.9 ms: 1.01x faster                                                       |
| chaos                      | 43.3 ms                                                     | 43.6 ms: 1.01x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 88.7 ms: 1.01x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.81 us: 1.01x slower                                                       |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                        |
| raytrace                   | 192 ms                                                      | 196 ms: 1.02x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.42 us: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.62 ms: 1.03x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 62.3 ns: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 226 ms: 1.04x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 77.8 ms: 1.04x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 58.3 ms: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                                       |
| scimark_fft                | 184 ms                                                      | 194 ms: 1.05x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 36.4 ms: 1.05x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 66.3 ms: 1.06x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.06x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 62.6 ms: 1.06x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 200 ms: 1.07x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 40.4 ms: 1.07x slower                                                       |
| pyflate                    | 295 ms                                                      | 316 ms: 1.07x slower                                                        |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.08x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 558 ms: 1.09x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.6 ms: 1.09x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.09x slower                                                       |
| pycparser                  | 699 ms                                                      | 764 ms: 1.09x slower                                                        |
| richards                   | 28.4 ms                                                     | 31.2 ms: 1.10x slower                                                       |
| richards_super             | 32.1 ms                                                     | 35.6 ms: 1.11x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.52 sec: 1.11x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.55 ms: 1.11x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 903 us: 1.12x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.14x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 89.5 ms: 1.14x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.6 ms: 1.14x slower                                                       |
| nbody                      | 71.9 ms                                                     | 82.0 ms: 1.14x slower                                                       |
| fannkuch                   | 247 ms                                                      | 282 ms: 1.14x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 228 us: 1.17x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.86 ms: 1.18x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.74 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.19x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 82.2 ms: 1.19x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                       |
| mypy2                      | 509 ms                                                      | 637 ms: 1.25x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.98 ms: 1.30x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 21.2 ms: 1.49x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.60x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                                |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 93.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown