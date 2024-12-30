# Results vs. 3.12.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: windows-amd64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.003x faster
- HPT reliability: 96.68%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 403 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 410 ms: 1.78x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                        |
| async_tree_none            | 291 ms                                                      | 183 ms: 1.59x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 225 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 348 ms: 1.41x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| float          | 56.8 ms                                                     | 55.4 ms: 1.03x faster                                                       |
| nbody          | 71.9 ms                                                     | 83.2 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 88.2 ms: 1.01x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 21.5 ms: 1.51x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 87.5 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 57.7 ms: 1.03x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.8 ms: 1.08x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.13x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 227 us: 1.16x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.66 ms: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.2 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 403 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 410 ms: 1.78x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                        |
| async_tree_none            | 291 ms                                                      | 183 ms: 1.59x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 225 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 348 ms: 1.41x faster                                                        |
| deepcopy                   | 238 us                                                      | 186 us: 1.28x faster                                                        |
| comprehensions             | 14.1 us                                                     | 12.5 us: 1.13x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.3 us: 1.11x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.90 us: 1.10x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.09x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 62.8 ms: 1.07x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 87.5 ms: 1.06x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.7 ms: 1.06x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.2 ms: 1.06x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 816 us: 1.05x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                       |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.7 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| float                      | 56.8 ms                                                     | 55.4 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.4 ms: 1.01x faster                                                       |
| go                         | 91.6 ms                                                     | 90.9 ms: 1.01x faster                                                       |
| async_generators           | 239 ms                                                      | 238 ms: 1.01x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 88.2 ms: 1.01x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.83 us: 1.02x slower                                                       |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 49.5 ms: 1.02x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.44 us: 1.03x slower                                                       |
| raytrace                   | 192 ms                                                      | 198 ms: 1.03x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 57.7 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 35.8 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.66 ms: 1.04x slower                                                       |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 77.8 ms: 1.04x slower                                                       |
| scimark_fft                | 184 ms                                                      | 193 ms: 1.05x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 196 ms: 1.05x slower                                                        |
| pycparser                  | 699 ms                                                      | 738 ms: 1.06x slower                                                        |
| nqueens                    | 62.8 ms                                                     | 66.3 ms: 1.06x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.30 ms: 1.06x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                      |
| pyflate                    | 295 ms                                                      | 316 ms: 1.07x slower                                                        |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.07x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 63.3 ms: 1.08x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 553 ms: 1.08x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.48 sec: 1.08x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 40.8 ms: 1.08x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 65.8 ns: 1.09x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.7 ms: 1.09x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.13 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.59 ms: 1.12x slower                                                       |
| richards_super             | 32.1 ms                                                     | 36.2 ms: 1.13x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 88.8 ms: 1.13x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 909 us: 1.13x slower                                                        |
| richards                   | 28.4 ms                                                     | 32.1 ms: 1.13x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.13x slower                                                        |
| coverage                   | 40.8 ms                                                     | 46.9 ms: 1.15x slower                                                       |
| nbody                      | 71.9 ms                                                     | 83.2 ms: 1.16x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 227 us: 1.16x slower                                                        |
| fannkuch                   | 247 ms                                                      | 287 ms: 1.16x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.66 ms: 1.17x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.89 ms: 1.18x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.2 ms: 1.24x slower                                                       |
| mypy2                      | 509 ms                                                      | 633 ms: 1.24x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 88.0 ms: 1.27x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.97 ms: 1.29x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 21.5 ms: 1.51x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.20 ms: 1.59x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (2): mako, chaos
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 96.68% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown