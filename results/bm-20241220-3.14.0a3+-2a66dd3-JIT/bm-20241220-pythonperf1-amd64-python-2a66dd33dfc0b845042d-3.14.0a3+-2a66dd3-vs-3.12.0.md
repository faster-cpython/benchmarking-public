# Results vs. 3.12.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: windows-amd64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.063x faster
- HPT reliability: 97.72%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 401 ms: 1.92x faster                                                        |
| async_tree_io              | 731 ms                                                      | 403 ms: 1.81x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                        |
| async_tree_none            | 291 ms                                                      | 184 ms: 1.59x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.52x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 353 ms: 1.42x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 354 ms: 1.38x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.61x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.0 ms: 1.36x faster                                                       |
| float          | 56.8 ms                                                     | 45.9 ms: 1.24x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                       |
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 80.4 ms: 1.09x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 20.2 ms: 1.42x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 110 us: 1.21x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.20 sec: 1.14x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 58.8 ms: 1.11x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 50.5 ms: 1.11x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 85.9 ms: 1.08x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.05x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.09x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.41 ms: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.5 ms: 1.08x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.3 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.13 ms: 1.38x faster                                                       |
| django_template | 22.9 ms                                                     | 27.1 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 401 ms: 1.92x faster                                                        |
| async_tree_io              | 731 ms                                                      | 403 ms: 1.81x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                        |
| async_tree_none            | 291 ms                                                      | 184 ms: 1.59x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.52x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 353 ms: 1.42x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 16.8 us: 1.41x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.13 ms: 1.38x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 354 ms: 1.38x faster                                                        |
| nbody                      | 71.9 ms                                                     | 53.0 ms: 1.36x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 49.4 ms: 1.35x faster                                                       |
| scimark_fft                | 184 ms                                                      | 143 ms: 1.29x faster                                                        |
| deepcopy                   | 238 us                                                      | 191 us: 1.25x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.05 ms: 1.25x faster                                                       |
| float                      | 56.8 ms                                                     | 45.9 ms: 1.24x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 63.9 ms: 1.23x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 110 us: 1.21x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 40.8 ms: 1.19x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.18x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.4 ms: 1.17x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.20 sec: 1.14x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 58.8 ms: 1.11x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.5 ms: 1.11x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 80.4 ms: 1.09x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 85.9 ms: 1.08x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.0 ms: 1.08x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 54.7 ms: 1.08x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 56.3 ns: 1.07x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.07x faster                                                       |
| json                       | 3.05 ms                                                     | 2.87 ms: 1.06x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 996 ms: 1.05x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.3 ms: 1.05x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 77.4 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 830 us: 1.03x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 497 ms: 1.03x faster                                                        |
| pyflate                    | 295 ms                                                      | 288 ms: 1.02x faster                                                        |
| go                         | 91.6 ms                                                     | 89.9 ms: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 74.1 ms: 1.01x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 91.1 ms: 1.01x faster                                                       |
| fannkuch                   | 247 ms                                                      | 246 ms: 1.00x faster                                                        |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                        |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                        |
| pycparser                  | 699 ms                                                      | 714 ms: 1.02x slower                                                        |
| logging_format             | 6.72 us                                                     | 6.88 us: 1.02x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.43 us: 1.03x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.27 ms: 1.03x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                      |
| generators                 | 22.5 ms                                                     | 23.6 ms: 1.05x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 844 us: 1.05x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.05x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.28 ms: 1.06x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 66.6 ms: 1.06x slower                                                       |
| sympy_expand               | 284 ms                                                      | 303 ms: 1.07x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.09 ms: 1.07x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.5 ms: 1.08x slower                                                       |
| async_generators           | 239 ms                                                      | 260 ms: 1.08x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.09x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 37.8 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 206 ms: 1.10x slower                                                        |
| raytrace                   | 192 ms                                                      | 212 ms: 1.10x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.41 ms: 1.12x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.1 ms: 1.15x slower                                                       |
| django_template            | 22.9 ms                                                     | 27.1 ms: 1.18x slower                                                       |
| richards                   | 28.4 ms                                                     | 33.7 ms: 1.19x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 82.7 ms: 1.19x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.3 ms: 1.20x slower                                                       |
| richards_super             | 32.1 ms                                                     | 38.4 ms: 1.20x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 5.06 ms: 1.23x slower                                                       |
| mypy2                      | 509 ms                                                      | 636 ms: 1.25x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.96 ms: 1.29x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 20.2 ms: 1.42x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 97.72% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown