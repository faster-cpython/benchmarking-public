# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_compa
- machine: windows-amd64
- commit hash: e27d994
- commit date: 2025-06-18
- overall geometric mean: 1.080x faster
- HPT reliability: 99.45%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                               |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.71x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                                |
| nbody          | 71.9 ms                                                     | 64.7 ms: 1.11x faster                                                                |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 80.8 ms: 1.08x faster                                                                |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                                |
| regex_v8       | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.2 ms: 1.04x faster                                                                |
| unpickle_pure_python | 133 us                                                      | 134 us: 1.01x slower                                                                 |
| xml_etree_generate   | 55.8 ms                                                     | 56.6 ms: 1.01x slower                                                                |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                               |
| xml_etree_process    | 37.7 ms                                                     | 39.6 ms: 1.05x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 213 us: 1.09x slower                                                                 |
| json_dumps           | 5.70 ms                                                     | 6.23 ms: 1.09x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                                |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.59 ms: 1.07x faster                                                                |
| django_template | 22.9 ms                                                     | 24.0 ms: 1.04x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.7 ms: 2.54x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.71x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                                 |
| mdp                        | 1.37 sec                                                    | 813 ms: 1.69x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                                 |
| deepcopy                   | 238 us                                                      | 168 us: 1.41x faster                                                                 |
| deepcopy_memo              | 23.7 us                                                     | 18.1 us: 1.31x faster                                                                |
| comprehensions             | 14.1 us                                                     | 10.9 us: 1.30x faster                                                                |
| float                      | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                                |
| go                         | 91.6 ms                                                     | 77.4 ms: 1.18x faster                                                                |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.16x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.82 us: 1.15x faster                                                                |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                                |
| nbody                      | 71.9 ms                                                     | 64.7 ms: 1.11x faster                                                                |
| regex_compile              | 87.5 ms                                                     | 80.8 ms: 1.08x faster                                                                |
| dulwich_log                | 44.3 ms                                                     | 40.9 ms: 1.08x faster                                                                |
| mako                       | 7.09 ms                                                     | 6.59 ms: 1.07x faster                                                                |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                                 |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                                 |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                                |
| sympy_sum                  | 91.5 ms                                                     | 87.5 ms: 1.05x faster                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 89.2 ms: 1.04x faster                                                                |
| chaos                      | 43.3 ms                                                     | 41.6 ms: 1.04x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 64.3 ms: 1.04x faster                                                                |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                                 |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.03x faster                                                                |
| meteor_contest             | 74.6 ms                                                     | 72.5 ms: 1.03x faster                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.49 ms: 1.03x faster                                                                |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                                 |
| async_generators           | 239 ms                                                      | 233 ms: 1.03x faster                                                                 |
| crypto_pyaes               | 48.5 ms                                                     | 47.3 ms: 1.02x faster                                                                |
| richards                   | 28.4 ms                                                     | 27.7 ms: 1.02x faster                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.8 ms: 1.02x faster                                                                |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                               |
| nqueens                    | 62.8 ms                                                     | 61.7 ms: 1.02x faster                                                                |
| richards_super             | 32.1 ms                                                     | 31.6 ms: 1.02x faster                                                                |
| regex_v8                   | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                                |
| scimark_sor                | 78.8 ms                                                     | 78.4 ms: 1.00x faster                                                                |
| unpickle_pure_python       | 133 us                                                      | 134 us: 1.01x slower                                                                 |
| scimark_lu                 | 58.9 ms                                                     | 59.6 ms: 1.01x slower                                                                |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                                 |
| xml_etree_generate         | 55.8 ms                                                     | 56.6 ms: 1.01x slower                                                                |
| json                       | 3.05 ms                                                     | 3.10 ms: 1.02x slower                                                                |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                                |
| scimark_fft                | 184 ms                                                      | 188 ms: 1.02x slower                                                                 |
| hexiom                     | 4.10 ms                                                     | 4.19 ms: 1.02x slower                                                                |
| pycparser                  | 699 ms                                                      | 715 ms: 1.02x slower                                                                 |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                                 |
| deltablue                  | 2.16 ms                                                     | 2.23 ms: 1.03x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                               |
| django_template            | 22.9 ms                                                     | 24.0 ms: 1.04x slower                                                                |
| logging_simple             | 6.28 us                                                     | 6.56 us: 1.05x slower                                                                |
| xml_etree_process          | 37.7 ms                                                     | 39.6 ms: 1.05x slower                                                                |
| logging_format             | 6.72 us                                                     | 7.06 us: 1.05x slower                                                                |
| pprint_safe_repr           | 513 ms                                                      | 541 ms: 1.05x slower                                                                 |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                               |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                                 |
| pickle_pure_python         | 195 us                                                      | 213 us: 1.09x slower                                                                 |
| fannkuch                   | 247 ms                                                      | 269 ms: 1.09x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.23 ms: 1.09x slower                                                                |
| telco                      | 4.13 ms                                                     | 4.63 ms: 1.12x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                                |
| coverage                   | 40.8 ms                                                     | 51.5 ms: 1.26x slower                                                                |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 2.12 ms: 1.39x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.76x slower                                                                |
| logging_silent             | 60.5 ns                                                     | 329 ns: 5.44x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                         |

Benchmark hidden because not significant (3): xml_etree_iterparse, coroutines, pyflate
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250618-3.15.0a0-e27d994/bm-20250618-pythonperf1-amd64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.080x faster

# HPT report

- Reliability score: 99.45% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown