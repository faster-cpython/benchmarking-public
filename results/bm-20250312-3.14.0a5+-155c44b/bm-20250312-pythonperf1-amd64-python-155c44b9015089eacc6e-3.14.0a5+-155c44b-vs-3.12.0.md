# Results vs. 3.12.0

- fork: python
- ref: 155c44b9015089eacc6e
- machine: windows-amd64
- commit hash: 155c44b
- commit date: 2025-03-12
- overall geometric mean: 1.035x faster
- HPT reliability: 55.57%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.04x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 420 ms: 1.84x faster                                                        |
| async_tree_io              | 731 ms                                                      | 424 ms: 1.73x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.59x faster                                                        |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.54x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.44x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.1 ms: 1.23x faster                                                       |
| nbody          | 71.9 ms                                                     | 67.8 ms: 1.06x faster                                                       |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 86.4 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 90.8 ms: 1.02x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.06x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 60.0 ms: 1.08x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.12x slower                                                        |
| xml_etree_process    | 37.7 ms                                                     | 42.6 ms: 1.13x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 227 us: 1.16x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.92 ms: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.6 ms: 1.27x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.87 ms: 1.03x faster                                                       |
| django_template | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.1 ms: 2.51x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 420 ms: 1.84x faster                                                        |
| async_tree_io              | 731 ms                                                      | 424 ms: 1.73x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.59x faster                                                        |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.54x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.44x faster                                                        |
| deepcopy                   | 238 us                                                      | 181 us: 1.31x faster                                                        |
| float                      | 56.8 ms                                                     | 46.1 ms: 1.23x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.4 us: 1.22x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.19x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.18x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 59.3 ms: 1.13x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| nbody                      | 71.9 ms                                                     | 67.8 ms: 1.06x faster                                                       |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.4 ms: 1.05x faster                                                       |
| go                         | 91.6 ms                                                     | 88.2 ms: 1.04x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.87 ms: 1.03x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.8 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.4 ms: 1.02x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 59.1 ns: 1.02x faster                                                       |
| scimark_fft                | 184 ms                                                      | 181 ms: 1.02x faster                                                        |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 86.4 ms: 1.01x faster                                                       |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.54 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.1 ms: 1.01x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                      |
| chaos                      | 43.3 ms                                                     | 43.9 ms: 1.01x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 60.0 ms: 1.02x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.8 ms: 1.03x slower                                                       |
| raytrace                   | 192 ms                                                      | 199 ms: 1.04x slower                                                        |
| 2to3                       | 218 ms                                                      | 226 ms: 1.04x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.04x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 78.3 ms: 1.05x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.8 ms: 1.05x slower                                                       |
| richards_super             | 32.1 ms                                                     | 33.8 ms: 1.05x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.62 us: 1.05x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 51.3 ms: 1.06x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 83.3 ms: 1.06x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.34 ms: 1.06x slower                                                       |
| pycparser                  | 699 ms                                                      | 740 ms: 1.06x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.06x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.16 us: 1.07x slower                                                       |
| pyflate                    | 295 ms                                                      | 314 ms: 1.07x slower                                                        |
| sympy_expand               | 284 ms                                                      | 303 ms: 1.07x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 60.0 ms: 1.08x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 558 ms: 1.09x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.12x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 42.6 ms: 1.13x slower                                                       |
| fannkuch                   | 247 ms                                                      | 283 ms: 1.15x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 227 us: 1.16x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.16x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.91 ms: 1.19x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.7 ms: 1.19x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.92 ms: 1.22x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.6 ms: 1.27x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.5 ms: 1.28x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.03 ms: 1.33x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.26 ms: 1.67x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (4): xml_etree_iterparse, regex_v8, sympy_str, bench_thread_pool
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250312-3.14.0a5+-155c44b/bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 55.57% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown