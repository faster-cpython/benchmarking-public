# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: be0ebdc
- commit date: 2025-06-20
- overall geometric mean: 1.089x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                               |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 389 ms: 1.98x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.69x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.7 ms: 1.27x faster                                                                |
| nbody          | 71.9 ms                                                     | 62.5 ms: 1.15x faster                                                                |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 81.1 ms: 1.08x faster                                                                |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                                |
| regex_v8       | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                                |
| regex_dna      | 126 ms                                                      | 122 ms: 1.03x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 87.5 ms: 1.06x faster                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                                |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.00x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 135 us: 1.01x slower                                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.03x slower                                                               |
| xml_etree_process    | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 216 us: 1.10x slower                                                                 |
| json_dumps           | 5.70 ms                                                     | 6.39 ms: 1.12x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                                |
| python_startup         | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.88 ms: 1.03x faster                                                                |
| django_template | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.9 ms: 2.52x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 389 ms: 1.98x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.69x faster                                                                 |
| mdp                        | 1.37 sec                                                    | 811 ms: 1.69x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                                 |
| deepcopy                   | 238 us                                                      | 173 us: 1.38x faster                                                                 |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 18.4 us: 1.29x faster                                                                |
| float                      | 56.8 ms                                                     | 44.7 ms: 1.27x faster                                                                |
| go                         | 91.6 ms                                                     | 76.2 ms: 1.20x faster                                                                |
| generators                 | 22.5 ms                                                     | 19.3 ms: 1.16x faster                                                                |
| nbody                      | 71.9 ms                                                     | 62.5 ms: 1.15x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.14x faster                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.3 ms: 1.11x faster                                                                |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                                |
| regex_compile              | 87.5 ms                                                     | 81.1 ms: 1.08x faster                                                                |
| dulwich_log                | 44.3 ms                                                     | 41.4 ms: 1.07x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 62.6 ms: 1.07x faster                                                                |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                                 |
| chaos                      | 43.3 ms                                                     | 40.6 ms: 1.07x faster                                                                |
| scimark_sor                | 78.8 ms                                                     | 73.9 ms: 1.07x faster                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 87.5 ms: 1.06x faster                                                                |
| scimark_fft                | 184 ms                                                      | 175 ms: 1.06x faster                                                                 |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                                |
| nqueens                    | 62.8 ms                                                     | 60.3 ms: 1.04x faster                                                                |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                                 |
| richards                   | 28.4 ms                                                     | 27.3 ms: 1.04x faster                                                                |
| pyflate                    | 295 ms                                                      | 284 ms: 1.04x faster                                                                 |
| regex_v8                   | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                                |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                                |
| sympy_sum                  | 91.5 ms                                                     | 88.3 ms: 1.04x faster                                                                |
| richards_super             | 32.1 ms                                                     | 31.0 ms: 1.04x faster                                                                |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.03x faster                                                                 |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.03x faster                                                                |
| mako                       | 7.09 ms                                                     | 6.88 ms: 1.03x faster                                                                |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                                 |
| async_generators           | 239 ms                                                      | 233 ms: 1.03x faster                                                                 |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                               |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.51 ms: 1.02x faster                                                                |
| crypto_pyaes               | 48.5 ms                                                     | 47.5 ms: 1.02x faster                                                                |
| hexiom                     | 4.10 ms                                                     | 4.04 ms: 1.01x faster                                                                |
| json                       | 3.05 ms                                                     | 3.02 ms: 1.01x faster                                                                |
| meteor_contest             | 74.6 ms                                                     | 73.9 ms: 1.01x faster                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                                |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.00x slower                                                                |
| deltablue                  | 2.16 ms                                                     | 2.18 ms: 1.01x slower                                                                |
| unpickle_pure_python       | 133 us                                                      | 135 us: 1.01x slower                                                                 |
| logging_simple             | 6.28 us                                                     | 6.36 us: 1.01x slower                                                                |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                                 |
| pycparser                  | 699 ms                                                      | 715 ms: 1.02x slower                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.03x slower                                                               |
| sympy_expand               | 284 ms                                                      | 293 ms: 1.03x slower                                                                 |
| xml_etree_process          | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                                |
| django_template            | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                                |
| fannkuch                   | 247 ms                                                      | 260 ms: 1.05x slower                                                                 |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                               |
| pprint_safe_repr           | 513 ms                                                      | 552 ms: 1.08x slower                                                                 |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.09x slower                                                                 |
| telco                      | 4.13 ms                                                     | 4.52 ms: 1.09x slower                                                                |
| pickle_pure_python         | 195 us                                                      | 216 us: 1.10x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.39 ms: 1.12x slower                                                                |
| coverage                   | 40.8 ms                                                     | 48.2 ms: 1.18x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                                |
| python_startup             | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 2.15 ms: 1.41x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.75x slower                                                                |
| logging_silent             | 60.5 ns                                                     | 323 ns: 5.34x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                         |

Benchmark hidden because not significant (3): scimark_lu, coroutines, logging_format
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250620-3.15.0a0-be0ebdc/bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.089x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown