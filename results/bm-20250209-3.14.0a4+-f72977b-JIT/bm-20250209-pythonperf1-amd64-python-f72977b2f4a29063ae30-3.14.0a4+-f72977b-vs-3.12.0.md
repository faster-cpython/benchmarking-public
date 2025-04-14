# Results vs. 3.12.0

- fork: python
- ref: f72977b2f4a29063ae30
- machine: windows-amd64
- commit hash: f72977b
- commit date: 2025-02-09
- overall geometric mean: 1.070x faster
- HPT reliability: 99.39%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.72 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 403 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 408 ms: 1.79x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 183 ms: 1.60x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.63x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.0 ms: 1.23x faster                                                       |
| nbody          | 71.9 ms                                                     | 59.4 ms: 1.21x faster                                                       |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                       |
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 81.8 ms: 1.07x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 113 us: 1.18x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 49.7 ms: 1.12x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.2 ms: 1.08x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 35.8 ms: 1.05x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 88.7 ms: 1.05x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.06x slower                                                        |
| json_loads           | 13.9 us                                                     | 15.2 us: 1.10x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.57 ms: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.3 ms: 1.30x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.25 ms: 1.35x faster                                                       |
| django_template | 22.9 ms                                                     | 25.3 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 403 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 408 ms: 1.79x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 183 ms: 1.60x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 58.1 ms: 1.38x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.25 ms: 1.35x faster                                                       |
| deepcopy                   | 238 us                                                      | 184 us: 1.30x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.1 us: 1.27x faster                                                       |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.26x faster                                                        |
| float                      | 56.8 ms                                                     | 46.0 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.10 ms: 1.22x faster                                                       |
| nbody                      | 71.9 ms                                                     | 59.4 ms: 1.21x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 113 us: 1.18x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 20.2 us: 1.18x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.53 us: 1.15x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 58.4 ms: 1.15x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.13x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 49.7 ms: 1.12x faster                                                       |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.1 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.2 ms: 1.08x faster                                                       |
| fannkuch                   | 247 ms                                                      | 228 ms: 1.08x faster                                                        |
| pyflate                    | 295 ms                                                      | 273 ms: 1.08x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 81.8 ms: 1.07x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.5 ms: 1.07x faster                                                       |
| go                         | 91.6 ms                                                     | 85.9 ms: 1.07x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 45.6 ms: 1.06x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.97 us: 1.06x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 987 ms: 1.06x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 35.8 ms: 1.05x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.7 ms: 1.05x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.4 ms: 1.05x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 58.0 ns: 1.04x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 61.1 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.5 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 505 ms: 1.02x faster                                                        |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| logging_format             | 6.72 us                                                     | 6.68 us: 1.01x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 74.9 ms: 1.00x slower                                                       |
| raytrace                   | 192 ms                                                      | 196 ms: 1.02x slower                                                        |
| richards_super             | 32.1 ms                                                     | 32.7 ms: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| json                       | 3.05 ms                                                     | 3.14 ms: 1.03x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 60.6 ms: 1.03x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.72 sec: 1.03x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.04x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.06 ms: 1.04x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 838 us: 1.04x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 83.6 ms: 1.06x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.06x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.38 ms: 1.07x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 200 ms: 1.07x slower                                                        |
| sympy_expand               | 284 ms                                                      | 304 ms: 1.07x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 37.0 ms: 1.07x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.49 ms: 1.09x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.2 us: 1.10x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.3 ms: 1.10x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.57 ms: 1.15x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.4 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.16x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 87.7 ms: 1.27x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.97 ms: 1.30x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.3 ms: 1.30x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (7): bench_thread_pool, async_generators, logging_simple, sympy_str, richards, scimark_monte_carlo, pycparser
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250209-3.14.0a4+-f72977b-JIT/bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.070x faster

# HPT report

- Reliability score: 99.39% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown