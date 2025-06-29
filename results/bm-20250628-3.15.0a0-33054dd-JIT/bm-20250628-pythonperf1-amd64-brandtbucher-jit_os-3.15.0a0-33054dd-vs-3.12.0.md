# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_os
- machine: windows-amd64
- commit hash: 33054dd
- commit date: 2025-06-28
- overall geometric mean: 1.112x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 219 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                       | 1.00x slower                                                       |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 394 ms: 1.96x faster                                               |
| async_tree_io              | 731 ms                                                      | 399 ms: 1.83x faster                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                               |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                               |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                               |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.62x faster                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.47x faster                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                               |
| Geometric mean             | (ref)                                                       | 1.67x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                              |
| nbody          | 71.9 ms                                                     | 59.7 ms: 1.20x faster                                              |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                       | 1.16x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 80.3 ms: 1.09x faster                                              |
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                               |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                       | 1.04x faster                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 108 us: 1.24x faster                                               |
| tomli_loads          | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                             |
| xml_etree_process    | 37.7 ms                                                     | 35.8 ms: 1.05x faster                                              |
| xml_etree_parse      | 93.0 ms                                                     | 89.0 ms: 1.05x faster                                              |
| xml_etree_generate   | 55.8 ms                                                     | 54.1 ms: 1.03x faster                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.4 ms: 1.01x faster                                              |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                              |
| pickle_pure_python   | 195 us                                                      | 205 us: 1.05x slower                                               |
| json_dumps           | 5.70 ms                                                     | 6.29 ms: 1.10x slower                                              |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                              |
| python_startup         | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                              |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.31 ms: 1.33x faster                                              |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                              |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.7 ms: 2.53x faster                                              |
| async_tree_io_tg           | 771 ms                                                      | 394 ms: 1.96x faster                                               |
| async_tree_io              | 731 ms                                                      | 399 ms: 1.83x faster                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                               |
| mdp                        | 1.37 sec                                                    | 803 ms: 1.71x faster                                               |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                               |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                               |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.62x faster                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.47x faster                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                               |
| deepcopy                   | 238 us                                                      | 171 us: 1.40x faster                                               |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.34x faster                                              |
| mako                       | 7.09 ms                                                     | 5.31 ms: 1.33x faster                                              |
| deepcopy_memo              | 23.7 us                                                     | 18.5 us: 1.28x faster                                              |
| float                      | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                              |
| unpickle_pure_python       | 133 us                                                      | 108 us: 1.24x faster                                               |
| scimark_fft                | 184 ms                                                      | 151 ms: 1.22x faster                                               |
| nbody                      | 71.9 ms                                                     | 59.7 ms: 1.20x faster                                              |
| tomli_loads                | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                             |
| go                         | 91.6 ms                                                     | 77.9 ms: 1.18x faster                                              |
| pyflate                    | 295 ms                                                      | 255 ms: 1.16x faster                                               |
| fannkuch                   | 247 ms                                                      | 216 ms: 1.14x faster                                               |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                              |
| pprint_pformat             | 1.05 sec                                                    | 918 ms: 1.14x faster                                               |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                              |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                              |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.29 ms: 1.12x faster                                              |
| pprint_safe_repr           | 513 ms                                                      | 460 ms: 1.12x faster                                               |
| logging_silent             | 60.5 ns                                                     | 55.3 ns: 1.09x faster                                              |
| regex_compile              | 87.5 ms                                                     | 80.3 ms: 1.09x faster                                              |
| dulwich_log                | 44.3 ms                                                     | 40.9 ms: 1.08x faster                                              |
| raytrace                   | 192 ms                                                      | 179 ms: 1.08x faster                                               |
| meteor_contest             | 74.6 ms                                                     | 70.4 ms: 1.06x faster                                              |
| crypto_pyaes               | 48.5 ms                                                     | 46.0 ms: 1.05x faster                                              |
| xml_etree_process          | 37.7 ms                                                     | 35.8 ms: 1.05x faster                                              |
| chaos                      | 43.3 ms                                                     | 41.2 ms: 1.05x faster                                              |
| xml_etree_parse            | 93.0 ms                                                     | 89.0 ms: 1.05x faster                                              |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                               |
| richards                   | 28.4 ms                                                     | 27.2 ms: 1.04x faster                                              |
| spectral_norm              | 66.9 ms                                                     | 64.3 ms: 1.04x faster                                              |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                               |
| richards_super             | 32.1 ms                                                     | 30.9 ms: 1.04x faster                                              |
| sympy_sum                  | 91.5 ms                                                     | 88.3 ms: 1.04x faster                                              |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                              |
| nqueens                    | 62.8 ms                                                     | 60.8 ms: 1.03x faster                                              |
| xml_etree_generate         | 55.8 ms                                                     | 54.1 ms: 1.03x faster                                              |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.6 ms: 1.03x faster                                              |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.02x faster                                               |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.01x faster                                              |
| logging_simple             | 6.28 us                                                     | 6.19 us: 1.01x faster                                              |
| logging_format             | 6.72 us                                                     | 6.63 us: 1.01x faster                                              |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.4 ms: 1.01x faster                                              |
| 2to3                       | 218 ms                                                      | 219 ms: 1.01x slower                                               |
| hexiom                     | 4.10 ms                                                     | 4.13 ms: 1.01x slower                                              |
| scimark_lu                 | 58.9 ms                                                     | 60.2 ms: 1.02x slower                                              |
| deltablue                  | 2.16 ms                                                     | 2.22 ms: 1.03x slower                                              |
| json                       | 3.05 ms                                                     | 3.17 ms: 1.04x slower                                              |
| telco                      | 4.13 ms                                                     | 4.29 ms: 1.04x slower                                              |
| async_generators           | 239 ms                                                      | 250 ms: 1.04x slower                                               |
| sympy_expand               | 284 ms                                                      | 296 ms: 1.04x slower                                               |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                              |
| pickle_pure_python         | 195 us                                                      | 205 us: 1.05x slower                                               |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                              |
| json_dumps                 | 5.70 ms                                                     | 6.29 ms: 1.10x slower                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.11x slower                                               |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                              |
| coverage                   | 40.8 ms                                                     | 50.3 ms: 1.23x slower                                              |
| python_startup             | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                              |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.41x slower                                              |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                              |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                       |

Benchmark hidden because not significant (5): docutils, regex_v8, coroutines, pycparser, scimark_sor
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250628-3.15.0a0-33054dd-JIT/bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.112x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown