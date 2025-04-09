# Results vs. 3.12.0

- fork: faster-cpython
- ref: tstate_in_dealloc
- machine: windows-amd64
- commit hash: 49ac4ce
- commit date: 2025-04-09
- overall geometric mean: 1.086x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                               |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                             |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 399 ms: 1.93x faster                                                               |
| async_tree_io              | 731 ms                                                      | 411 ms: 1.78x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                               |
| async_tree_none            | 291 ms                                                      | 183 ms: 1.59x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.47x faster                                                               |
| Geometric mean             | (ref)                                                       | 1.65x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.5 ms: 1.31x faster                                                              |
| nbody          | 71.9 ms                                                     | 65.5 ms: 1.10x faster                                                              |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                               |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                              |
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                               |
| regex_compile  | 87.5 ms                                                     | 80.5 ms: 1.09x faster                                                              |
| regex_v8       | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                              |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.0 ms: 1.02x faster                                                              |
| xml_etree_generate   | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                              |
| unpickle_pure_python | 133 us                                                      | 137 us: 1.03x slower                                                               |
| xml_etree_process    | 37.7 ms                                                     | 39.5 ms: 1.05x slower                                                              |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                             |
| json_loads           | 13.9 us                                                     | 15.2 us: 1.09x slower                                                              |
| pickle_pure_python   | 195 us                                                      | 215 us: 1.10x slower                                                               |
| json_dumps           | 5.70 ms                                                     | 6.80 ms: 1.19x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                              |
| python_startup         | 19.5 ms                                                     | 25.4 ms: 1.31x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.81 ms: 1.04x faster                                                              |
| django_template | 22.9 ms                                                     | 24.7 ms: 1.07x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.7 ms: 2.80x faster                                                              |
| async_tree_io_tg           | 771 ms                                                      | 399 ms: 1.93x faster                                                               |
| async_tree_io              | 731 ms                                                      | 411 ms: 1.78x faster                                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                               |
| mdp                        | 1.37 sec                                                    | 798 ms: 1.72x faster                                                               |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                               |
| async_tree_none            | 291 ms                                                      | 183 ms: 1.59x faster                                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.47x faster                                                               |
| deepcopy                   | 238 us                                                      | 174 us: 1.36x faster                                                               |
| float                      | 56.8 ms                                                     | 43.5 ms: 1.31x faster                                                              |
| deepcopy_memo              | 23.7 us                                                     | 18.3 us: 1.30x faster                                                              |
| comprehensions             | 14.1 us                                                     | 11.7 us: 1.21x faster                                                              |
| go                         | 91.6 ms                                                     | 78.5 ms: 1.17x faster                                                              |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                              |
| regex_effbot               | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                              |
| spectral_norm              | 66.9 ms                                                     | 58.6 ms: 1.14x faster                                                              |
| deepcopy_reduce            | 2.09 us                                                     | 1.84 us: 1.14x faster                                                              |
| chaos                      | 43.3 ms                                                     | 38.4 ms: 1.13x faster                                                              |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                               |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                              |
| nbody                      | 71.9 ms                                                     | 65.5 ms: 1.10x faster                                                              |
| dulwich_log                | 44.3 ms                                                     | 40.6 ms: 1.09x faster                                                              |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.2 ms: 1.09x faster                                                              |
| regex_compile              | 87.5 ms                                                     | 80.5 ms: 1.09x faster                                                              |
| logging_silent             | 60.5 ns                                                     | 55.9 ns: 1.08x faster                                                              |
| raytrace                   | 192 ms                                                      | 179 ms: 1.08x faster                                                               |
| scimark_fft                | 184 ms                                                      | 175 ms: 1.05x faster                                                               |
| xml_etree_parse            | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                              |
| mako                       | 7.09 ms                                                     | 6.81 ms: 1.04x faster                                                              |
| scimark_sor                | 78.8 ms                                                     | 75.8 ms: 1.04x faster                                                              |
| regex_v8                   | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                              |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                              |
| sympy_sum                  | 91.5 ms                                                     | 89.0 ms: 1.03x faster                                                              |
| async_generators           | 239 ms                                                      | 233 ms: 1.03x faster                                                               |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.03x faster                                                              |
| richards                   | 28.4 ms                                                     | 27.7 ms: 1.02x faster                                                              |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                               |
| meteor_contest             | 74.6 ms                                                     | 73.2 ms: 1.02x faster                                                              |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.0 ms: 1.02x faster                                                              |
| pprint_pformat             | 1.05 sec                                                    | 1.03 sec: 1.02x faster                                                             |
| logging_simple             | 6.28 us                                                     | 6.16 us: 1.02x faster                                                              |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                               |
| nqueens                    | 62.8 ms                                                     | 61.8 ms: 1.02x faster                                                              |
| richards_super             | 32.1 ms                                                     | 31.6 ms: 1.01x faster                                                              |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                             |
| pprint_safe_repr           | 513 ms                                                      | 506 ms: 1.01x faster                                                               |
| logging_format             | 6.72 us                                                     | 6.64 us: 1.01x faster                                                              |
| xml_etree_generate         | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                              |
| crypto_pyaes               | 48.5 ms                                                     | 48.8 ms: 1.01x slower                                                              |
| hexiom                     | 4.10 ms                                                     | 4.14 ms: 1.01x slower                                                              |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                               |
| pycparser                  | 699 ms                                                      | 715 ms: 1.02x slower                                                               |
| unpickle_pure_python       | 133 us                                                      | 137 us: 1.03x slower                                                               |
| fannkuch                   | 247 ms                                                      | 256 ms: 1.04x slower                                                               |
| sympy_expand               | 284 ms                                                      | 295 ms: 1.04x slower                                                               |
| xml_etree_process          | 37.7 ms                                                     | 39.5 ms: 1.05x slower                                                              |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                             |
| json                       | 3.05 ms                                                     | 3.25 ms: 1.06x slower                                                              |
| scimark_lu                 | 58.9 ms                                                     | 62.7 ms: 1.07x slower                                                              |
| django_template            | 22.9 ms                                                     | 24.7 ms: 1.07x slower                                                              |
| json_loads                 | 13.9 us                                                     | 15.2 us: 1.09x slower                                                              |
| pickle_pure_python         | 195 us                                                      | 215 us: 1.10x slower                                                               |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.12x slower                                                               |
| telco                      | 4.13 ms                                                     | 4.77 ms: 1.16x slower                                                              |
| json_dumps                 | 5.70 ms                                                     | 6.80 ms: 1.19x slower                                                              |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                              |
| bench_mp_pool              | 69.2 ms                                                     | 87.1 ms: 1.26x slower                                                              |
| coverage                   | 40.8 ms                                                     | 52.0 ms: 1.27x slower                                                              |
| python_startup             | 19.5 ms                                                     | 25.4 ms: 1.31x slower                                                              |
| gc_traversal               | 1.52 ms                                                     | 2.02 ms: 1.33x slower                                                              |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                       |

Benchmark hidden because not significant (4): bench_thread_pool, scimark_sparse_mat_mult, deltablue, pyflate
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250409-3.14.0a7+-49ac4ce/bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.086x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown