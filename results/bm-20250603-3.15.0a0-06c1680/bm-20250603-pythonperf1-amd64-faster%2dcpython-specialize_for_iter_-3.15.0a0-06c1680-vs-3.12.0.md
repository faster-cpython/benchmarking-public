# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: 06c1680
- commit date: 2025-06-03
- overall geometric mean: 1.074x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 219 ms: 1.01x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                               |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 394 ms: 1.85x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.47x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                                |
| nbody          | 71.9 ms                                                     | 60.9 ms: 1.18x faster                                                                |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.6 ms: 1.10x faster                                                                |
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                                |
| regex_v8       | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.5 ms: 1.04x faster                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.3 ms: 1.03x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                               |
| xml_etree_generate   | 55.8 ms                                                     | 55.5 ms: 1.01x faster                                                                |
| unpickle_pure_python | 133 us                                                      | 132 us: 1.01x faster                                                                 |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                                |
| xml_etree_process    | 37.7 ms                                                     | 39.4 ms: 1.05x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.06x slower                                                                 |
| json_dumps           | 5.70 ms                                                     | 6.30 ms: 1.11x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                                |
| python_startup         | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.54 ms: 1.08x faster                                                                |
| django_template | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.4 ms: 2.56x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 394 ms: 1.85x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                                 |
| mdp                        | 1.37 sec                                                    | 806 ms: 1.70x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.47x faster                                                                 |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                                 |
| deepcopy_memo              | 23.7 us                                                     | 17.7 us: 1.34x faster                                                                |
| float                      | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                                |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.29x faster                                                                |
| go                         | 91.6 ms                                                     | 73.9 ms: 1.24x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 56.6 ms: 1.18x faster                                                                |
| nbody                      | 71.9 ms                                                     | 60.9 ms: 1.18x faster                                                                |
| generators                 | 22.5 ms                                                     | 19.3 ms: 1.17x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                                |
| chaos                      | 43.3 ms                                                     | 37.8 ms: 1.15x faster                                                                |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                                |
| regex_compile              | 87.5 ms                                                     | 79.6 ms: 1.10x faster                                                                |
| dulwich_log                | 44.3 ms                                                     | 40.8 ms: 1.08x faster                                                                |
| mako                       | 7.09 ms                                                     | 6.54 ms: 1.08x faster                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.6 ms: 1.08x faster                                                                |
| raytrace                   | 192 ms                                                      | 179 ms: 1.08x faster                                                                 |
| scimark_sor                | 78.8 ms                                                     | 73.2 ms: 1.08x faster                                                                |
| pyflate                    | 295 ms                                                      | 277 ms: 1.07x faster                                                                 |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                                 |
| scimark_fft                | 184 ms                                                      | 175 ms: 1.06x faster                                                                 |
| nqueens                    | 62.8 ms                                                     | 59.5 ms: 1.05x faster                                                                |
| sympy_sum                  | 91.5 ms                                                     | 87.2 ms: 1.05x faster                                                                |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.05x faster                                                                |
| sympy_str                  | 175 ms                                                      | 167 ms: 1.05x faster                                                                 |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                                |
| crypto_pyaes               | 48.5 ms                                                     | 46.5 ms: 1.04x faster                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 89.5 ms: 1.04x faster                                                                |
| richards_super             | 32.1 ms                                                     | 31.1 ms: 1.03x faster                                                                |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                                |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.3 ms: 1.03x faster                                                                |
| hexiom                     | 4.10 ms                                                     | 3.99 ms: 1.03x faster                                                                |
| async_generators           | 239 ms                                                      | 233 ms: 1.03x faster                                                                 |
| meteor_contest             | 74.6 ms                                                     | 72.7 ms: 1.03x faster                                                                |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                               |
| richards                   | 28.4 ms                                                     | 27.8 ms: 1.02x faster                                                                |
| regex_v8                   | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.51 ms: 1.02x faster                                                                |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                               |
| logging_simple             | 6.28 us                                                     | 6.22 us: 1.01x faster                                                                |
| deltablue                  | 2.16 ms                                                     | 2.14 ms: 1.01x faster                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 55.5 ms: 1.01x faster                                                                |
| unpickle_pure_python       | 133 us                                                      | 132 us: 1.01x faster                                                                 |
| 2to3                       | 218 ms                                                      | 219 ms: 1.01x slower                                                                 |
| json                       | 3.05 ms                                                     | 3.09 ms: 1.01x slower                                                                |
| fannkuch                   | 247 ms                                                      | 250 ms: 1.01x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                                |
| xml_etree_process          | 37.7 ms                                                     | 39.4 ms: 1.05x slower                                                                |
| pprint_pformat             | 1.05 sec                                                    | 1.10 sec: 1.05x slower                                                               |
| pprint_safe_repr           | 513 ms                                                      | 540 ms: 1.05x slower                                                                 |
| django_template            | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                                |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.06x slower                                                                 |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.09x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.30 ms: 1.11x slower                                                                |
| telco                      | 4.13 ms                                                     | 4.66 ms: 1.13x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                                |
| python_startup             | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.41x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                                |
| logging_silent             | 60.5 ns                                                     | 310 ns: 5.13x slower                                                                 |
| coverage                   | 40.8 ms                                                     | 289 ms: 7.09x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                         |

Benchmark hidden because not significant (4): logging_format, sympy_expand, scimark_lu, pycparser
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250603-3.15.0a0-06c1680/bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.074x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown