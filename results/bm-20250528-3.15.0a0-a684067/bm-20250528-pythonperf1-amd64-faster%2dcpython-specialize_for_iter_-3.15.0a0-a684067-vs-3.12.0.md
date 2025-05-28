# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: a684067
- commit date: 2025-05-28
- overall geometric mean: 1.059x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                               |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 401 ms: 1.92x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 402 ms: 1.82x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.70x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.67x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.8 ms: 1.24x faster                                                                |
| nbody          | 71.9 ms                                                     | 64.1 ms: 1.12x faster                                                                |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 81.6 ms: 1.07x faster                                                                |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                                |
| regex_v8       | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 87.6 ms: 1.06x faster                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.3 ms: 1.03x faster                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 55.2 ms: 1.01x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                               |
| xml_etree_process    | 37.7 ms                                                     | 38.7 ms: 1.03x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 139 us: 1.04x slower                                                                 |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 214 us: 1.09x slower                                                                 |
| json_dumps           | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                                |
| python_startup         | 19.5 ms                                                     | 25.2 ms: 1.30x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.64 ms: 1.07x faster                                                                |
| django_template | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.6 ms: 2.71x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 401 ms: 1.92x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 402 ms: 1.82x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.70x faster                                                                 |
| mdp                        | 1.37 sec                                                    | 817 ms: 1.68x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.67x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                                 |
| deepcopy                   | 238 us                                                      | 172 us: 1.38x faster                                                                 |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.28x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 18.5 us: 1.28x faster                                                                |
| float                      | 56.8 ms                                                     | 45.8 ms: 1.24x faster                                                                |
| go                         | 91.6 ms                                                     | 77.2 ms: 1.19x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 58.5 ms: 1.14x faster                                                                |
| chaos                      | 43.3 ms                                                     | 38.5 ms: 1.12x faster                                                                |
| generators                 | 22.5 ms                                                     | 20.0 ms: 1.12x faster                                                                |
| nbody                      | 71.9 ms                                                     | 64.1 ms: 1.12x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.88 us: 1.11x faster                                                                |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.10x faster                                                                |
| dulwich_log                | 44.3 ms                                                     | 40.9 ms: 1.08x faster                                                                |
| regex_compile              | 87.5 ms                                                     | 81.6 ms: 1.07x faster                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.9 ms: 1.07x faster                                                                |
| mako                       | 7.09 ms                                                     | 6.64 ms: 1.07x faster                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 87.6 ms: 1.06x faster                                                                |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                                 |
| pyflate                    | 295 ms                                                      | 279 ms: 1.06x faster                                                                 |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                                 |
| sympy_sum                  | 91.5 ms                                                     | 88.0 ms: 1.04x faster                                                                |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                                |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.03x faster                                                                 |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                                 |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.3 ms: 1.03x faster                                                                |
| richards                   | 28.4 ms                                                     | 27.6 ms: 1.03x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                                |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                               |
| async_generators           | 239 ms                                                      | 233 ms: 1.03x faster                                                                 |
| crypto_pyaes               | 48.5 ms                                                     | 47.3 ms: 1.03x faster                                                                |
| scimark_sor                | 78.8 ms                                                     | 76.8 ms: 1.02x faster                                                                |
| meteor_contest             | 74.6 ms                                                     | 72.9 ms: 1.02x faster                                                                |
| scimark_fft                | 184 ms                                                      | 181 ms: 1.02x faster                                                                 |
| richards_super             | 32.1 ms                                                     | 31.6 ms: 1.01x faster                                                                |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 55.2 ms: 1.01x faster                                                                |
| regex_v8                   | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                                |
| logging_simple             | 6.28 us                                                     | 6.33 us: 1.01x slower                                                                |
| logging_format             | 6.72 us                                                     | 6.79 us: 1.01x slower                                                                |
| hexiom                     | 4.10 ms                                                     | 4.15 ms: 1.01x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                               |
| deltablue                  | 2.16 ms                                                     | 2.20 ms: 1.02x slower                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.61 ms: 1.02x slower                                                                |
| sympy_expand               | 284 ms                                                      | 290 ms: 1.02x slower                                                                 |
| pycparser                  | 699 ms                                                      | 716 ms: 1.02x slower                                                                 |
| xml_etree_process          | 37.7 ms                                                     | 38.7 ms: 1.03x slower                                                                |
| json                       | 3.05 ms                                                     | 3.15 ms: 1.03x slower                                                                |
| fannkuch                   | 247 ms                                                      | 256 ms: 1.04x slower                                                                 |
| unpickle_pure_python       | 133 us                                                      | 139 us: 1.04x slower                                                                 |
| django_template            | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                                |
| typing_runtime_protocols   | 95.1 us                                                     | 101 us: 1.07x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                                |
| pprint_pformat             | 1.05 sec                                                    | 1.14 sec: 1.09x slower                                                               |
| pprint_safe_repr           | 513 ms                                                      | 558 ms: 1.09x slower                                                                 |
| pickle_pure_python         | 195 us                                                      | 214 us: 1.09x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                                |
| telco                      | 4.13 ms                                                     | 4.67 ms: 1.13x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                                |
| python_startup             | 19.5 ms                                                     | 25.2 ms: 1.30x slower                                                                |
| bench_mp_pool              | 69.2 ms                                                     | 92.7 ms: 1.34x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 2.19 ms: 1.44x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.31 ms: 1.74x slower                                                                |
| logging_silent             | 60.5 ns                                                     | 318 ns: 5.27x slower                                                                 |
| coverage                   | 40.8 ms                                                     | 291 ms: 7.14x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                         |

Benchmark hidden because not significant (4): bench_thread_pool, scimark_lu, nqueens, 2to3
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250528-3.15.0a0-a684067/bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown