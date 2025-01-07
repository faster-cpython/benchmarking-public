# Results vs. 3.12.0

- fork: python
- ref: 2228e92da31ca7344a16
- machine: windows-amd64
- commit hash: 2228e92
- commit date: 2025-01-05
- overall geometric mean: 1.016x faster
- HPT reliability: 90.70%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 401 ms: 1.92x faster                                                        |
| async_tree_io              | 731 ms                                                      | 404 ms: 1.81x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 182 ms: 1.60x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 350 ms: 1.40x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.63x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 53.0 ms: 1.07x faster                                                       |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| nbody          | 71.9 ms                                                     | 77.0 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 24.6 ms: 1.73x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x slower                                                                |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 87.5 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.4 ms: 1.03x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 40.2 ms: 1.07x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 221 us: 1.13x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.70 ms: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.2 ms: 1.06x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.1 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.87 ms: 1.03x faster                                                       |
| django_template | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 401 ms: 1.92x faster                                                        |
| async_tree_io              | 731 ms                                                      | 404 ms: 1.81x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 182 ms: 1.60x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 350 ms: 1.40x faster                                                        |
| deepcopy                   | 238 us                                                      | 184 us: 1.29x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.8 us: 1.14x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.10x faster                                                       |
| float                      | 56.8 ms                                                     | 53.0 ms: 1.07x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.1 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.06x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 87.5 ms: 1.06x faster                                                       |
| go                         | 91.6 ms                                                     | 87.2 ms: 1.05x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 76.6 ms: 1.05x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 818 us: 1.05x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 64.1 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.7 ms: 1.04x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.87 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.2 ms: 1.01x faster                                                       |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 62.2 ms: 1.01x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 48.2 ms: 1.01x faster                                                       |
| async_generators           | 239 ms                                                      | 238 ms: 1.00x faster                                                        |
| raytrace                   | 192 ms                                                      | 193 ms: 1.00x slower                                                        |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.60 ms: 1.01x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.38 us: 1.02x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 61.6 ns: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| logging_format             | 6.72 us                                                     | 6.89 us: 1.03x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.03x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.4 ms: 1.03x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 77.0 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.03x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 531 ms: 1.03x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 35.9 ms: 1.04x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.27 ms: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 61.5 ms: 1.04x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.04x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.7 ms: 1.05x slower                                                       |
| scimark_fft                | 184 ms                                                      | 193 ms: 1.05x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 196 ms: 1.05x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 17.2 ms: 1.06x slower                                                       |
| richards_super             | 32.1 ms                                                     | 34.1 ms: 1.06x slower                                                       |
| pycparser                  | 699 ms                                                      | 742 ms: 1.06x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 40.2 ms: 1.07x slower                                                       |
| nbody                      | 71.9 ms                                                     | 77.0 ms: 1.07x slower                                                       |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.07x slower                                                        |
| fannkuch                   | 247 ms                                                      | 266 ms: 1.08x slower                                                        |
| django_template            | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.08x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.8 ms: 1.09x slower                                                       |
| pyflate                    | 295 ms                                                      | 326 ms: 1.10x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 889 us: 1.11x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 221 us: 1.13x slower                                                        |
| coverage                   | 40.8 ms                                                     | 46.5 ms: 1.14x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 90.3 ms: 1.15x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.82 ms: 1.17x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.70 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| python_startup             | 19.5 ms                                                     | 23.1 ms: 1.19x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 82.5 ms: 1.19x slower                                                       |
| mypy2                      | 509 ms                                                      | 639 ms: 1.26x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.96 ms: 1.29x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 24.6 ms: 1.73x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (4): regex_compile, chaos, docutils, regex_dna
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250105-3.14.0a3+-2228e92/bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.016x faster

# HPT report

- Reliability score: 90.70% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown