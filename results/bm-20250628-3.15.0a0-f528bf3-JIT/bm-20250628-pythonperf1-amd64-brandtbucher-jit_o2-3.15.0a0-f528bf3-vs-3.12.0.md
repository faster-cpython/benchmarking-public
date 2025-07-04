# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_o2
- machine: windows-amd64
- commit hash: f528bf3
- commit date: 2025-06-28
- overall geometric mean: 1.115x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                       | 1.01x slower                                                       |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 388 ms: 1.99x faster                                               |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 213 ms: 1.72x faster                                               |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.72x faster                                               |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                               |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.47x faster                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                               |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 55.1 ms: 1.30x faster                                              |
| float          | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                              |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                       | 1.20x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.5 ms: 1.12x faster                                              |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                               |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                       | 1.05x faster                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 108 us: 1.23x faster                                               |
| tomli_loads          | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                             |
| xml_etree_generate   | 55.8 ms                                                     | 50.4 ms: 1.11x faster                                              |
| xml_etree_parse      | 93.0 ms                                                     | 88.2 ms: 1.06x faster                                              |
| xml_etree_process    | 37.7 ms                                                     | 36.1 ms: 1.04x faster                                              |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                              |
| pickle_pure_python   | 195 us                                                      | 205 us: 1.05x slower                                               |
| json_dumps           | 5.70 ms                                                     | 6.19 ms: 1.09x slower                                              |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                       |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                              |
| python_startup         | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                              |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.46 ms: 1.30x faster                                              |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                              |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.1 ms: 2.51x faster                                              |
| async_tree_io_tg           | 771 ms                                                      | 388 ms: 1.99x faster                                               |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 213 ms: 1.72x faster                                               |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.72x faster                                               |
| mdp                        | 1.37 sec                                                    | 802 ms: 1.71x faster                                               |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                               |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.47x faster                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                               |
| deepcopy                   | 238 us                                                      | 172 us: 1.39x faster                                               |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.33x faster                                              |
| deepcopy_memo              | 23.7 us                                                     | 18.1 us: 1.31x faster                                              |
| nbody                      | 71.9 ms                                                     | 55.1 ms: 1.30x faster                                              |
| mako                       | 7.09 ms                                                     | 5.46 ms: 1.30x faster                                              |
| float                      | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                              |
| unpickle_pure_python       | 133 us                                                      | 108 us: 1.23x faster                                               |
| scimark_fft                | 184 ms                                                      | 151 ms: 1.22x faster                                               |
| go                         | 91.6 ms                                                     | 77.7 ms: 1.18x faster                                              |
| tomli_loads                | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                             |
| fannkuch                   | 247 ms                                                      | 214 ms: 1.15x faster                                               |
| pprint_safe_repr           | 513 ms                                                      | 447 ms: 1.15x faster                                               |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                              |
| pyflate                    | 295 ms                                                      | 259 ms: 1.14x faster                                               |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.26 ms: 1.13x faster                                              |
| pprint_pformat             | 1.05 sec                                                    | 925 ms: 1.13x faster                                               |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                              |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.12x faster                                              |
| logging_silent             | 60.5 ns                                                     | 54.1 ns: 1.12x faster                                              |
| regex_compile              | 87.5 ms                                                     | 78.5 ms: 1.12x faster                                              |
| xml_etree_generate         | 55.8 ms                                                     | 50.4 ms: 1.11x faster                                              |
| dulwich_log                | 44.3 ms                                                     | 41.5 ms: 1.07x faster                                              |
| crypto_pyaes               | 48.5 ms                                                     | 45.5 ms: 1.06x faster                                              |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.2 ms: 1.06x faster                                              |
| raytrace                   | 192 ms                                                      | 181 ms: 1.06x faster                                               |
| chaos                      | 43.3 ms                                                     | 41.0 ms: 1.06x faster                                              |
| xml_etree_parse            | 93.0 ms                                                     | 88.2 ms: 1.06x faster                                              |
| nqueens                    | 62.8 ms                                                     | 59.5 ms: 1.05x faster                                              |
| spectral_norm              | 66.9 ms                                                     | 64.1 ms: 1.04x faster                                              |
| xml_etree_process          | 37.7 ms                                                     | 36.1 ms: 1.04x faster                                              |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                               |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                               |
| sympy_sum                  | 91.5 ms                                                     | 87.9 ms: 1.04x faster                                              |
| meteor_contest             | 74.6 ms                                                     | 71.7 ms: 1.04x faster                                              |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                              |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                               |
| richards                   | 28.4 ms                                                     | 27.6 ms: 1.03x faster                                              |
| logging_simple             | 6.28 us                                                     | 6.11 us: 1.03x faster                                              |
| logging_format             | 6.72 us                                                     | 6.57 us: 1.02x faster                                              |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                              |
| richards_super             | 32.1 ms                                                     | 31.7 ms: 1.01x faster                                              |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                              |
| scimark_sor                | 78.8 ms                                                     | 79.9 ms: 1.01x slower                                              |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.01x slower                                              |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                               |
| hexiom                     | 4.10 ms                                                     | 4.19 ms: 1.02x slower                                              |
| async_generators           | 239 ms                                                      | 245 ms: 1.02x slower                                               |
| scimark_lu                 | 58.9 ms                                                     | 60.4 ms: 1.03x slower                                              |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                               |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                              |
| telco                      | 4.13 ms                                                     | 4.29 ms: 1.04x slower                                              |
| pickle_pure_python         | 195 us                                                      | 205 us: 1.05x slower                                               |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                              |
| json                       | 3.05 ms                                                     | 3.25 ms: 1.07x slower                                              |
| json_dumps                 | 5.70 ms                                                     | 6.19 ms: 1.09x slower                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.09x slower                                               |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                              |
| coverage                   | 40.8 ms                                                     | 50.1 ms: 1.23x slower                                              |
| python_startup             | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                              |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.41x slower                                              |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.75x slower                                              |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                       |

Benchmark hidden because not significant (4): xml_etree_iterparse, pycparser, docutils, regex_v8
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250628-3.15.0a0-f528bf3-JIT/bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.115x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown