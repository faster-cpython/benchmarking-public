# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_oz
- machine: windows-amd64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.116x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                             |
| Geometric mean | (ref)                                                       | 1.01x faster                                                       |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                               |
| async_tree_io              | 731 ms                                                      | 391 ms: 1.87x faster                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                               |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                               |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                               |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.47x faster                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                               |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 56.2 ms: 1.28x faster                                              |
| float          | 56.8 ms                                                     | 44.9 ms: 1.27x faster                                              |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                       | 1.19x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.5 ms: 1.11x faster                                              |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                               |
| regex_v8       | 14.2 ms                                                     | 13.4 ms: 1.06x faster                                              |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                       | 1.08x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 110 us: 1.21x faster                                               |
| xml_etree_generate   | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                              |
| tomli_loads          | 1.37 sec                                                    | 1.24 sec: 1.11x faster                                             |
| xml_etree_parse      | 93.0 ms                                                     | 86.5 ms: 1.08x faster                                              |
| xml_etree_process    | 37.7 ms                                                     | 35.5 ms: 1.06x faster                                              |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.3 ms: 1.05x faster                                              |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.06x slower                                              |
| pickle_pure_python   | 195 us                                                      | 207 us: 1.06x slower                                               |
| json_dumps           | 5.70 ms                                                     | 6.19 ms: 1.09x slower                                              |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.1 ms: 1.18x slower                                              |
| python_startup         | 19.5 ms                                                     | 26.0 ms: 1.33x slower                                              |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.57 ms: 1.27x faster                                              |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                              |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.7 ms: 2.80x faster                                              |
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                               |
| async_tree_io              | 731 ms                                                      | 391 ms: 1.87x faster                                               |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                               |
| mdp                        | 1.37 sec                                                    | 795 ms: 1.73x faster                                               |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                               |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                               |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                               |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.47x faster                                               |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                               |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                               |
| deepcopy_memo              | 23.7 us                                                     | 17.6 us: 1.35x faster                                              |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.28x faster                                              |
| nbody                      | 71.9 ms                                                     | 56.2 ms: 1.28x faster                                              |
| mako                       | 7.09 ms                                                     | 5.57 ms: 1.27x faster                                              |
| float                      | 56.8 ms                                                     | 44.9 ms: 1.27x faster                                              |
| unpickle_pure_python       | 133 us                                                      | 110 us: 1.21x faster                                               |
| go                         | 91.6 ms                                                     | 77.8 ms: 1.18x faster                                              |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.15x faster                                              |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.23 ms: 1.15x faster                                              |
| scimark_fft                | 184 ms                                                      | 161 ms: 1.14x faster                                               |
| pyflate                    | 295 ms                                                      | 258 ms: 1.14x faster                                               |
| deepcopy_reduce            | 2.09 us                                                     | 1.84 us: 1.14x faster                                              |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                              |
| pprint_safe_repr           | 513 ms                                                      | 460 ms: 1.12x faster                                               |
| regex_compile              | 87.5 ms                                                     | 78.5 ms: 1.11x faster                                              |
| pprint_pformat             | 1.05 sec                                                    | 941 ms: 1.11x faster                                               |
| xml_etree_generate         | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                              |
| tomli_loads                | 1.37 sec                                                    | 1.24 sec: 1.11x faster                                             |
| logging_silent             | 60.5 ns                                                     | 54.8 ns: 1.10x faster                                              |
| dulwich_log                | 44.3 ms                                                     | 40.3 ms: 1.10x faster                                              |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                               |
| raytrace                   | 192 ms                                                      | 178 ms: 1.08x faster                                               |
| xml_etree_parse            | 93.0 ms                                                     | 86.5 ms: 1.08x faster                                              |
| regex_v8                   | 14.2 ms                                                     | 13.4 ms: 1.06x faster                                              |
| xml_etree_process          | 37.7 ms                                                     | 35.5 ms: 1.06x faster                                              |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                              |
| sympy_sum                  | 91.5 ms                                                     | 86.9 ms: 1.05x faster                                              |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                              |
| chaos                      | 43.3 ms                                                     | 41.2 ms: 1.05x faster                                              |
| meteor_contest             | 74.6 ms                                                     | 71.0 ms: 1.05x faster                                              |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.7 ms: 1.05x faster                                              |
| richards_super             | 32.1 ms                                                     | 30.7 ms: 1.05x faster                                              |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.3 ms: 1.05x faster                                              |
| spectral_norm              | 66.9 ms                                                     | 64.5 ms: 1.04x faster                                              |
| crypto_pyaes               | 48.5 ms                                                     | 46.7 ms: 1.04x faster                                              |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                               |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.03x faster                                               |
| nqueens                    | 62.8 ms                                                     | 60.8 ms: 1.03x faster                                              |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.02x faster                                              |
| fannkuch                   | 247 ms                                                      | 242 ms: 1.02x faster                                               |
| pycparser                  | 699 ms                                                      | 691 ms: 1.01x faster                                               |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                             |
| logging_simple             | 6.28 us                                                     | 6.23 us: 1.01x faster                                              |
| scimark_lu                 | 58.9 ms                                                     | 58.6 ms: 1.01x faster                                              |
| scimark_sor                | 78.8 ms                                                     | 79.2 ms: 1.01x slower                                              |
| hexiom                     | 4.10 ms                                                     | 4.17 ms: 1.02x slower                                              |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                              |
| deltablue                  | 2.16 ms                                                     | 2.21 ms: 1.02x slower                                              |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                               |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                               |
| telco                      | 4.13 ms                                                     | 4.36 ms: 1.06x slower                                              |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.06x slower                                              |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                               |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                              |
| json                       | 3.05 ms                                                     | 3.26 ms: 1.07x slower                                              |
| json_dumps                 | 5.70 ms                                                     | 6.19 ms: 1.09x slower                                              |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.10x slower                                               |
| python_startup_no_site     | 16.2 ms                                                     | 19.1 ms: 1.18x slower                                              |
| coverage                   | 40.8 ms                                                     | 49.7 ms: 1.22x slower                                              |
| python_startup             | 19.5 ms                                                     | 26.0 ms: 1.33x slower                                              |
| gc_traversal               | 1.52 ms                                                     | 2.09 ms: 1.37x slower                                              |
| create_gc_cycles           | 752 us                                                      | 1.30 ms: 1.73x slower                                              |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                       |

Benchmark hidden because not significant (2): logging_format, 2to3
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.116x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown