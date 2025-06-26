# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.091x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.02x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                               |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 388 ms: 1.99x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 398 ms: 1.84x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.71x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 326 ms: 1.50x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 335 ms: 1.50x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.4 ms: 1.31x faster                                                                |
| nbody          | 71.9 ms                                                     | 65.3 ms: 1.10x faster                                                                |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.8 ms: 1.10x faster                                                                |
| regex_effbot   | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                                |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                                 |
| regex_v8       | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                                |
| unpickle_pure_python | 133 us                                                      | 132 us: 1.01x faster                                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                               |
| xml_etree_process    | 37.7 ms                                                     | 38.7 ms: 1.03x slower                                                                |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 210 us: 1.07x slower                                                                 |
| json_dumps           | 5.70 ms                                                     | 6.26 ms: 1.10x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                                |
| python_startup         | 19.5 ms                                                     | 26.3 ms: 1.35x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.80 ms: 1.04x faster                                                                |
| django_template | 22.9 ms                                                     | 23.8 ms: 1.04x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.1 ms: 2.51x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 388 ms: 1.99x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 398 ms: 1.84x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.71x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                                 |
| mdp                        | 1.37 sec                                                    | 811 ms: 1.69x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 326 ms: 1.50x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 335 ms: 1.50x faster                                                                 |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                                 |
| deepcopy_memo              | 23.7 us                                                     | 17.9 us: 1.32x faster                                                                |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                                |
| float                      | 56.8 ms                                                     | 43.4 ms: 1.31x faster                                                                |
| go                         | 91.6 ms                                                     | 76.5 ms: 1.20x faster                                                                |
| generators                 | 22.5 ms                                                     | 19.3 ms: 1.17x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.82 us: 1.15x faster                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.7 ms: 1.10x faster                                                                |
| nbody                      | 71.9 ms                                                     | 65.3 ms: 1.10x faster                                                                |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                                |
| regex_compile              | 87.5 ms                                                     | 79.8 ms: 1.10x faster                                                                |
| raytrace                   | 192 ms                                                      | 178 ms: 1.08x faster                                                                 |
| dulwich_log                | 44.3 ms                                                     | 41.3 ms: 1.07x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                                |
| async_generators           | 239 ms                                                      | 226 ms: 1.06x faster                                                                 |
| meteor_contest             | 74.6 ms                                                     | 70.7 ms: 1.06x faster                                                                |
| chaos                      | 43.3 ms                                                     | 41.3 ms: 1.05x faster                                                                |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                                 |
| mako                       | 7.09 ms                                                     | 6.80 ms: 1.04x faster                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                                                |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                                 |
| richards                   | 28.4 ms                                                     | 27.3 ms: 1.04x faster                                                                |
| sympy_sum                  | 91.5 ms                                                     | 88.1 ms: 1.04x faster                                                                |
| crypto_pyaes               | 48.5 ms                                                     | 46.8 ms: 1.04x faster                                                                |
| richards_super             | 32.1 ms                                                     | 31.0 ms: 1.04x faster                                                                |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                                |
| scimark_sor                | 78.8 ms                                                     | 76.7 ms: 1.03x faster                                                                |
| pyflate                    | 295 ms                                                      | 287 ms: 1.03x faster                                                                 |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.03x faster                                                                 |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                                |
| nqueens                    | 62.8 ms                                                     | 61.3 ms: 1.02x faster                                                                |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                               |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.51 ms: 1.02x faster                                                                |
| scimark_lu                 | 58.9 ms                                                     | 57.8 ms: 1.02x faster                                                                |
| regex_v8                   | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                                |
| hexiom                     | 4.10 ms                                                     | 4.04 ms: 1.01x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 66.2 ms: 1.01x faster                                                                |
| unpickle_pure_python       | 133 us                                                      | 132 us: 1.01x faster                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                               |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.01x slower                                                                |
| 2to3                       | 218 ms                                                      | 221 ms: 1.02x slower                                                                 |
| pycparser                  | 699 ms                                                      | 713 ms: 1.02x slower                                                                 |
| json                       | 3.05 ms                                                     | 3.11 ms: 1.02x slower                                                                |
| xml_etree_process          | 37.7 ms                                                     | 38.7 ms: 1.03x slower                                                                |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                                 |
| coroutines                 | 14.3 ms                                                     | 14.7 ms: 1.03x slower                                                                |
| pprint_safe_repr           | 513 ms                                                      | 532 ms: 1.04x slower                                                                 |
| django_template            | 22.9 ms                                                     | 23.8 ms: 1.04x slower                                                                |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.04x slower                                                               |
| fannkuch                   | 247 ms                                                      | 258 ms: 1.04x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                                |
| pickle_pure_python         | 195 us                                                      | 210 us: 1.07x slower                                                                 |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.07x slower                                                                 |
| telco                      | 4.13 ms                                                     | 4.53 ms: 1.10x slower                                                                |
| json_dumps                 | 5.70 ms                                                     | 6.26 ms: 1.10x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                                |
| coverage                   | 40.8 ms                                                     | 49.3 ms: 1.21x slower                                                                |
| python_startup             | 19.5 ms                                                     | 26.3 ms: 1.35x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.41x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.31 ms: 1.75x slower                                                                |
| logging_silent             | 60.5 ns                                                     | 319 ns: 5.27x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                         |

Benchmark hidden because not significant (4): logging_simple, logging_format, scimark_fft, xml_etree_generate
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250626-3.15.0a0-892a89d/bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.091x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown