# Results vs. 3.12.0

- fork: python
- ref: f33d21e24fdb05da7512
- machine: windows-amd64
- commit hash: f33d21e
- commit date: 2025-03-05
- overall geometric mean: 1.027x faster
- HPT reliability: 88.51%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 411 ms: 1.88x faster                                                        |
| async_tree_io              | 731 ms                                                      | 421 ms: 1.74x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.59x faster                                                        |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 348 ms: 1.44x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 345 ms: 1.42x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 47.2 ms: 1.20x faster                                                       |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| nbody          | 71.9 ms                                                     | 73.4 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                                       |
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 88.9 ms: 1.02x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 58.0 ms: 1.04x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.06x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.7 ms: 1.08x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 152 us: 1.14x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 229 us: 1.17x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.81 ms: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.1 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.96 ms: 1.02x faster                                                       |
| django_template | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.0 ms: 2.51x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 411 ms: 1.88x faster                                                        |
| async_tree_io              | 731 ms                                                      | 421 ms: 1.74x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.59x faster                                                        |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 348 ms: 1.44x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 345 ms: 1.42x faster                                                        |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.6 us: 1.22x faster                                                       |
| float                      | 56.8 ms                                                     | 47.2 ms: 1.20x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.15x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.0 us: 1.13x faster                                                       |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 61.5 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.93 us: 1.08x faster                                                       |
| async_generators           | 239 ms                                                      | 226 ms: 1.06x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 42.5 ms: 1.04x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                       |
| go                         | 91.6 ms                                                     | 88.6 ms: 1.03x faster                                                       |
| json                       | 3.05 ms                                                     | 2.95 ms: 1.03x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.96 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.1 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| chaos                      | 43.3 ms                                                     | 43.0 ms: 1.01x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 63.2 ms: 1.01x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 88.9 ms: 1.02x slower                                                       |
| raytrace                   | 192 ms                                                      | 195 ms: 1.02x slower                                                        |
| nbody                      | 71.9 ms                                                     | 73.4 ms: 1.02x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 61.9 ns: 1.02x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 76.5 ms: 1.02x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.9 ms: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.47 us: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.64 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 35.7 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.03x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 58.0 ms: 1.04x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 194 ms: 1.04x slower                                                        |
| logging_format             | 6.72 us                                                     | 6.98 us: 1.04x slower                                                       |
| scimark_fft                | 184 ms                                                      | 192 ms: 1.04x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.06x slower                                                      |
| sympy_expand               | 284 ms                                                      | 300 ms: 1.06x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                                       |
| pycparser                  | 699 ms                                                      | 746 ms: 1.07x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 40.7 ms: 1.08x slower                                                       |
| richards                   | 28.4 ms                                                     | 30.7 ms: 1.08x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.49 sec: 1.08x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.08x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                       |
| pyflate                    | 295 ms                                                      | 320 ms: 1.09x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.8 ms: 1.09x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.48 ms: 1.09x slower                                                       |
| richards_super             | 32.1 ms                                                     | 35.3 ms: 1.10x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.16 sec: 1.11x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 891 us: 1.11x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 577 ms: 1.13x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 108 us: 1.13x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 89.9 ms: 1.14x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 152 us: 1.14x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 67.7 ms: 1.15x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.78 ms: 1.16x slower                                                       |
| fannkuch                   | 247 ms                                                      | 286 ms: 1.16x slower                                                        |
| coverage                   | 40.8 ms                                                     | 47.7 ms: 1.17x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 229 us: 1.17x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.81 ms: 1.20x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 86.6 ms: 1.25x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.1 ms: 1.29x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.03 ms: 1.34x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.23 ms: 1.64x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (2): bench_thread_pool, sympy_str
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250305-3.14.0a5+-f33d21e/bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.027x faster

# HPT report

- Reliability score: 88.51% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown