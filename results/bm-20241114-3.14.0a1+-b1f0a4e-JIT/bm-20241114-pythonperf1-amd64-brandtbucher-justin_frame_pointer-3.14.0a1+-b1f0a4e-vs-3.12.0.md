# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: windows-amd64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.000x faster
- HPT reliability: 65.86%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 248 ms: 1.14x slower                                                              |
| docutils       | 1.66 sec                                                    | 1.90 sec: 1.14x slower                                                            |
| Geometric mean | (ref)                                                       | 1.14x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 251 ms: 1.46x faster                                                              |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.38x faster                                                              |
| async_tree_io              | 731 ms                                                      | 532 ms: 1.37x faster                                                              |
| async_tree_none_tg         | 285 ms                                                      | 209 ms: 1.37x faster                                                              |
| async_tree_io_tg           | 771 ms                                                      | 587 ms: 1.31x faster                                                              |
| async_tree_memoization     | 339 ms                                                      | 262 ms: 1.30x faster                                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 395 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                              |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 56.5 ms: 1.27x faster                                                             |
| float          | 56.8 ms                                                     | 48.4 ms: 1.17x faster                                                             |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                              |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                              |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                             |
| regex_compile  | 87.5 ms                                                     | 93.3 ms: 1.07x slower                                                             |
| regex_v8       | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 51.8 ms: 1.08x faster                                                             |
| tomli_loads          | 1.37 sec                                                    | 1.30 sec: 1.06x faster                                                            |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                             |
| xml_etree_process    | 37.7 ms                                                     | 37.1 ms: 1.02x faster                                                             |
| xml_etree_parse      | 93.0 ms                                                     | 93.9 ms: 1.01x slower                                                             |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                             |
| json_dumps           | 5.70 ms                                                     | 6.11 ms: 1.07x slower                                                             |
| pickle_pure_python   | 195 us                                                      | 214 us: 1.10x slower                                                              |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                             |
| python_startup         | 19.5 ms                                                     | 23.5 ms: 1.21x slower                                                             |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.44 ms: 1.30x faster                                                             |
| django_template | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                             |
| Geometric mean  | (ref)                                                       | 1.05x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 251 ms: 1.46x faster                                                              |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.38x faster                                                              |
| async_tree_io              | 731 ms                                                      | 532 ms: 1.37x faster                                                              |
| async_tree_none_tg         | 285 ms                                                      | 209 ms: 1.37x faster                                                              |
| deepcopy_memo              | 23.7 us                                                     | 17.6 us: 1.35x faster                                                             |
| async_tree_io_tg           | 771 ms                                                      | 587 ms: 1.31x faster                                                              |
| mako                       | 7.09 ms                                                     | 5.44 ms: 1.30x faster                                                             |
| async_tree_memoization     | 339 ms                                                      | 262 ms: 1.30x faster                                                              |
| nbody                      | 71.9 ms                                                     | 56.5 ms: 1.27x faster                                                             |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 395 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 394 ms: 1.24x faster                                                              |
| deepcopy                   | 238 us                                                      | 197 us: 1.21x faster                                                              |
| spectral_norm              | 66.9 ms                                                     | 55.7 ms: 1.20x faster                                                             |
| float                      | 56.8 ms                                                     | 48.4 ms: 1.17x faster                                                             |
| crypto_pyaes               | 48.5 ms                                                     | 42.3 ms: 1.15x faster                                                             |
| scimark_sor                | 78.8 ms                                                     | 68.9 ms: 1.14x faster                                                             |
| dulwich_log                | 44.3 ms                                                     | 39.7 ms: 1.12x faster                                                             |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.2 ms: 1.12x faster                                                             |
| scimark_fft                | 184 ms                                                      | 166 ms: 1.11x faster                                                              |
| comprehensions             | 14.1 us                                                     | 12.7 us: 1.11x faster                                                             |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.31 ms: 1.11x faster                                                             |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                             |
| xml_etree_generate         | 55.8 ms                                                     | 51.8 ms: 1.08x faster                                                             |
| pprint_safe_repr           | 513 ms                                                      | 478 ms: 1.07x faster                                                              |
| pathlib                    | 80.5 ms                                                     | 75.2 ms: 1.07x faster                                                             |
| pprint_pformat             | 1.05 sec                                                    | 979 ms: 1.07x faster                                                              |
| deepcopy_reduce            | 2.09 us                                                     | 1.98 us: 1.06x faster                                                             |
| tomli_loads                | 1.37 sec                                                    | 1.30 sec: 1.06x faster                                                            |
| bench_thread_pool          | 857 us                                                      | 821 us: 1.04x faster                                                              |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                              |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                             |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                             |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                              |
| scimark_lu                 | 58.9 ms                                                     | 57.4 ms: 1.02x faster                                                             |
| logging_silent             | 60.5 ns                                                     | 59.2 ns: 1.02x faster                                                             |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                             |
| chaos                      | 43.3 ms                                                     | 42.6 ms: 1.02x faster                                                             |
| xml_etree_process          | 37.7 ms                                                     | 37.1 ms: 1.02x faster                                                             |
| fannkuch                   | 247 ms                                                      | 243 ms: 1.01x faster                                                              |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                             |
| logging_format             | 6.72 us                                                     | 6.68 us: 1.01x faster                                                             |
| logging_simple             | 6.28 us                                                     | 6.25 us: 1.00x faster                                                             |
| xml_etree_parse            | 93.0 ms                                                     | 93.9 ms: 1.01x slower                                                             |
| meteor_contest             | 74.6 ms                                                     | 75.8 ms: 1.02x slower                                                             |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                             |
| go                         | 91.6 ms                                                     | 95.9 ms: 1.05x slower                                                             |
| pycparser                  | 699 ms                                                      | 734 ms: 1.05x slower                                                              |
| regex_compile              | 87.5 ms                                                     | 93.3 ms: 1.07x slower                                                             |
| nqueens                    | 62.8 ms                                                     | 67.0 ms: 1.07x slower                                                             |
| json_dumps                 | 5.70 ms                                                     | 6.11 ms: 1.07x slower                                                             |
| pyflate                    | 295 ms                                                      | 317 ms: 1.08x slower                                                              |
| regex_v8                   | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                             |
| pickle_pure_python         | 195 us                                                      | 214 us: 1.10x slower                                                              |
| async_generators           | 239 ms                                                      | 263 ms: 1.10x slower                                                              |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                             |
| mdp                        | 1.37 sec                                                    | 1.53 sec: 1.12x slower                                                            |
| sympy_str                  | 175 ms                                                      | 196 ms: 1.12x slower                                                              |
| telco                      | 4.13 ms                                                     | 4.62 ms: 1.12x slower                                                             |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.12x slower                                                              |
| generators                 | 22.5 ms                                                     | 25.3 ms: 1.12x slower                                                             |
| deltablue                  | 2.16 ms                                                     | 2.43 ms: 1.13x slower                                                             |
| 2to3                       | 218 ms                                                      | 248 ms: 1.14x slower                                                              |
| sympy_sum                  | 91.5 ms                                                     | 104 ms: 1.14x slower                                                              |
| sqlglot_parse              | 804 us                                                      | 915 us: 1.14x slower                                                              |
| coverage                   | 40.8 ms                                                     | 46.5 ms: 1.14x slower                                                             |
| docutils                   | 1.66 sec                                                    | 1.90 sec: 1.14x slower                                                            |
| sqlglot_normalize          | 187 ms                                                      | 214 ms: 1.15x slower                                                              |
| sympy_expand               | 284 ms                                                      | 331 ms: 1.17x slower                                                              |
| raytrace                   | 192 ms                                                      | 225 ms: 1.17x slower                                                              |
| sqlglot_transpile          | 1.02 ms                                                     | 1.20 ms: 1.17x slower                                                             |
| django_template            | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                             |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                              |
| python_startup             | 19.5 ms                                                     | 23.5 ms: 1.21x slower                                                             |
| richards_super             | 32.1 ms                                                     | 39.0 ms: 1.21x slower                                                             |
| richards                   | 28.4 ms                                                     | 35.0 ms: 1.23x slower                                                             |
| sympy_integrate            | 13.0 ms                                                     | 16.0 ms: 1.24x slower                                                             |
| gc_traversal               | 1.52 ms                                                     | 1.92 ms: 1.26x slower                                                             |
| sqlglot_optimize           | 34.5 ms                                                     | 43.6 ms: 1.26x slower                                                             |
| bench_mp_pool              | 69.2 ms                                                     | 87.6 ms: 1.27x slower                                                             |
| hexiom                     | 4.10 ms                                                     | 5.53 ms: 1.35x slower                                                             |
| create_gc_cycles           | 752 us                                                      | 1.36 ms: 1.81x slower                                                             |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                                      |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.000x faster
# HPT report

- Reliability score: 65.86% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown