# Results vs. 3.12.0

- fork: python
- ref: 2228e92da31ca7344a16
- machine: windows-amd64
- commit hash: 2228e92
- commit date: 2025-01-05
- overall geometric mean: 1.034x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 239 ms: 1.10x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.79 sec: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                        |
| async_tree_io              | 731 ms                                                      | 401 ms: 1.82x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 205 ms: 1.79x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                        |
| async_tree_none            | 291 ms                                                      | 177 ms: 1.64x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 218 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 373 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 373 ms: 1.31x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.63x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 68.8 ms: 1.04x faster                                                       |
| float          | 56.8 ms                                                     | 55.1 ms: 1.03x faster                                                       |
| pidigits       | 152 ms                                                      | 155 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 91.0 ms: 1.04x slower                                                       |
| regex_dna      | 126 ms                                                      | 142 ms: 1.12x slower                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.98 ms: 1.22x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 26.6 ms: 1.87x slower                                                       |
| Geometric mean | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 71.0 ms: 1.09x slower                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 102 ms: 1.09x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 228 us: 1.16x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 159 us: 1.19x slower                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 67.6 ms: 1.21x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 47.3 ms: 1.26x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 7.79 ms: 1.37x slower                                                       |
| json_loads           | 13.9 us                                                     | 19.6 us: 1.41x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.19x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.6 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                       |
| mako            | 7.09 ms                                                     | 8.55 ms: 1.21x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.16x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                        |
| async_tree_io              | 731 ms                                                      | 401 ms: 1.82x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 205 ms: 1.79x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                        |
| async_tree_none            | 291 ms                                                      | 177 ms: 1.64x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 218 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 373 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 373 ms: 1.31x faster                                                        |
| generators                 | 22.5 ms                                                     | 17.3 ms: 1.31x faster                                                       |
| deepcopy                   | 238 us                                                      | 185 us: 1.29x faster                                                        |
| go                         | 91.6 ms                                                     | 82.7 ms: 1.11x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.9 us: 1.10x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.7 us: 1.09x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.07x faster                                                       |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 42.3 ms: 1.05x faster                                                       |
| nbody                      | 71.9 ms                                                     | 68.8 ms: 1.04x faster                                                       |
| float                      | 56.8 ms                                                     | 55.1 ms: 1.03x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.72 us: 1.02x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 79.8 ms: 1.01x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.15 ms: 1.01x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 92.0 ms: 1.01x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 75.4 ms: 1.01x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.82 us: 1.02x slower                                                       |
| pidigits                   | 152 ms                                                      | 155 ms: 1.02x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.41 us: 1.02x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.6 ms: 1.03x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.8 ms: 1.03x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 91.0 ms: 1.04x slower                                                       |
| sympy_str                  | 175 ms                                                      | 182 ms: 1.04x slower                                                        |
| chaos                      | 43.3 ms                                                     | 45.2 ms: 1.04x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 45.7 ms: 1.05x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 82.5 ms: 1.05x slower                                                       |
| scimark_fft                | 184 ms                                                      | 194 ms: 1.05x slower                                                        |
| async_generators           | 239 ms                                                      | 254 ms: 1.06x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.7 ms: 1.06x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 549 ms: 1.07x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 37.0 ms: 1.07x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 201 ms: 1.08x slower                                                        |
| pycparser                  | 699 ms                                                      | 753 ms: 1.08x slower                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.76 ms: 1.08x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.79 sec: 1.08x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 871 us: 1.08x slower                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 71.0 ms: 1.09x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 73.1 ms: 1.09x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 102 ms: 1.09x slower                                                        |
| richards                   | 28.4 ms                                                     | 31.1 ms: 1.10x slower                                                       |
| 2to3                       | 218 ms                                                      | 239 ms: 1.10x slower                                                        |
| richards_super             | 32.1 ms                                                     | 35.3 ms: 1.10x slower                                                       |
| sympy_expand               | 284 ms                                                      | 314 ms: 1.11x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.59 ms: 1.12x slower                                                       |
| regex_dna                  | 126 ms                                                      | 142 ms: 1.12x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                       |
| pyflate                    | 295 ms                                                      | 332 ms: 1.13x slower                                                        |
| logging_silent             | 60.5 ns                                                     | 70.2 ns: 1.16x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 228 us: 1.16x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                       |
| fannkuch                   | 247 ms                                                      | 291 ms: 1.18x slower                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 57.7 ms: 1.19x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 159 us: 1.19x slower                                                        |
| json                       | 3.05 ms                                                     | 3.67 ms: 1.20x slower                                                       |
| mako                       | 7.09 ms                                                     | 8.55 ms: 1.21x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 67.6 ms: 1.21x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.68 sec: 1.22x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.98 ms: 1.22x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 72.3 ms: 1.23x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.18 ms: 1.25x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 47.3 ms: 1.26x slower                                                       |
| coverage                   | 40.8 ms                                                     | 53.1 ms: 1.30x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.6 ms: 1.31x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 93.5 ms: 1.35x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.79 ms: 1.37x slower                                                       |
| json_loads                 | 13.9 us                                                     | 19.6 us: 1.41x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.54 ms: 1.67x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.36 ms: 1.81x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 26.6 ms: 1.87x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250105-3.14.0a3+-2228e92-CLANG/bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.034x slower

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown