# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_side_4096
- machine: windows-amd64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.038x faster
- HPT reliability: 97.77%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                          |
| docutils       | 1.66 sec                                                    | 1.75 sec: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 257 ms: 1.43x faster                                                          |
| async_tree_none_tg         | 285 ms                                                      | 208 ms: 1.37x faster                                                          |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                          |
| async_tree_io_tg           | 771 ms                                                      | 579 ms: 1.33x faster                                                          |
| async_tree_io              | 731 ms                                                      | 575 ms: 1.27x faster                                                          |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                          |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 399 ms: 1.23x faster                                                          |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 410 ms: 1.22x faster                                                          |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 56.4 ms: 1.28x faster                                                         |
| float          | 56.8 ms                                                     | 48.3 ms: 1.18x faster                                                         |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                         |
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                          |
| regex_compile  | 87.5 ms                                                     | 82.2 ms: 1.06x faster                                                         |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 111 us: 1.20x faster                                                          |
| xml_etree_generate   | 55.8 ms                                                     | 50.8 ms: 1.10x faster                                                         |
| tomli_loads          | 1.37 sec                                                    | 1.29 sec: 1.06x faster                                                        |
| xml_etree_process    | 37.7 ms                                                     | 35.7 ms: 1.06x faster                                                         |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.3 ms: 1.05x faster                                                         |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.00x slower                                                         |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.06x slower                                                          |
| json_dumps           | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                         |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                                         |
| python_startup         | 19.5 ms                                                     | 23.7 ms: 1.22x slower                                                         |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.17 ms: 1.37x faster                                                         |
| django_template | 22.9 ms                                                     | 27.6 ms: 1.20x slower                                                         |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 257 ms: 1.43x faster                                                          |
| deepcopy_memo              | 23.7 us                                                     | 16.8 us: 1.41x faster                                                         |
| async_tree_none_tg         | 285 ms                                                      | 208 ms: 1.37x faster                                                          |
| mako                       | 7.09 ms                                                     | 5.17 ms: 1.37x faster                                                         |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                          |
| async_tree_io_tg           | 771 ms                                                      | 579 ms: 1.33x faster                                                          |
| nbody                      | 71.9 ms                                                     | 56.4 ms: 1.28x faster                                                         |
| spectral_norm              | 66.9 ms                                                     | 52.6 ms: 1.27x faster                                                         |
| async_tree_io              | 731 ms                                                      | 575 ms: 1.27x faster                                                          |
| scimark_sor                | 78.8 ms                                                     | 62.1 ms: 1.27x faster                                                         |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                          |
| deepcopy                   | 238 us                                                      | 193 us: 1.23x faster                                                          |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.08 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 399 ms: 1.23x faster                                                          |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 410 ms: 1.22x faster                                                          |
| crypto_pyaes               | 48.5 ms                                                     | 39.9 ms: 1.21x faster                                                         |
| scimark_fft                | 184 ms                                                      | 153 ms: 1.20x faster                                                          |
| unpickle_pure_python       | 133 us                                                      | 111 us: 1.20x faster                                                          |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.19x faster                                                         |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.1 ms: 1.18x faster                                                         |
| float                      | 56.8 ms                                                     | 48.3 ms: 1.18x faster                                                         |
| regex_effbot               | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                         |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                                         |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                         |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                          |
| scimark_lu                 | 58.9 ms                                                     | 53.0 ms: 1.11x faster                                                         |
| dulwich_log                | 44.3 ms                                                     | 40.0 ms: 1.11x faster                                                         |
| xml_etree_generate         | 55.8 ms                                                     | 50.8 ms: 1.10x faster                                                         |
| logging_silent             | 60.5 ns                                                     | 56.7 ns: 1.07x faster                                                         |
| regex_compile              | 87.5 ms                                                     | 82.2 ms: 1.06x faster                                                         |
| bench_thread_pool          | 857 us                                                      | 806 us: 1.06x faster                                                          |
| tomli_loads                | 1.37 sec                                                    | 1.29 sec: 1.06x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 988 ms: 1.06x faster                                                          |
| pathlib                    | 80.5 ms                                                     | 76.1 ms: 1.06x faster                                                         |
| xml_etree_process          | 37.7 ms                                                     | 35.7 ms: 1.06x faster                                                         |
| chaos                      | 43.3 ms                                                     | 41.1 ms: 1.05x faster                                                         |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                         |
| json                       | 3.05 ms                                                     | 2.91 ms: 1.05x faster                                                         |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.3 ms: 1.05x faster                                                         |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                          |
| pprint_safe_repr           | 513 ms                                                      | 497 ms: 1.03x faster                                                          |
| fannkuch                   | 247 ms                                                      | 240 ms: 1.03x faster                                                          |
| go                         | 91.6 ms                                                     | 89.7 ms: 1.02x faster                                                         |
| pyflate                    | 295 ms                                                      | 290 ms: 1.02x faster                                                          |
| meteor_contest             | 74.6 ms                                                     | 73.8 ms: 1.01x faster                                                         |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.00x slower                                                         |
| logging_simple             | 6.28 us                                                     | 6.32 us: 1.01x slower                                                         |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.01x slower                                                          |
| logging_format             | 6.72 us                                                     | 6.82 us: 1.02x slower                                                         |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                          |
| nqueens                    | 62.8 ms                                                     | 64.2 ms: 1.02x slower                                                         |
| pycparser                  | 699 ms                                                      | 717 ms: 1.03x slower                                                          |
| telco                      | 4.13 ms                                                     | 4.28 ms: 1.04x slower                                                         |
| generators                 | 22.5 ms                                                     | 23.4 ms: 1.04x slower                                                         |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                         |
| docutils                   | 1.66 sec                                                    | 1.75 sec: 1.05x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.7 ms: 1.05x slower                                                         |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.06x slower                                                          |
| sqlglot_parse              | 804 us                                                      | 863 us: 1.07x slower                                                          |
| sympy_expand               | 284 ms                                                      | 307 ms: 1.08x slower                                                          |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.08x slower                                                         |
| python_startup_no_site     | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                                         |
| deltablue                  | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                         |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.10x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                         |
| raytrace                   | 192 ms                                                      | 212 ms: 1.10x slower                                                          |
| sqlglot_normalize          | 187 ms                                                      | 208 ms: 1.11x slower                                                          |
| sqlglot_optimize           | 34.5 ms                                                     | 38.9 ms: 1.13x slower                                                         |
| async_generators           | 239 ms                                                      | 270 ms: 1.13x slower                                                          |
| coverage                   | 40.8 ms                                                     | 46.5 ms: 1.14x slower                                                         |
| bench_mp_pool              | 69.2 ms                                                     | 82.1 ms: 1.19x slower                                                         |
| django_template            | 22.9 ms                                                     | 27.6 ms: 1.20x slower                                                         |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                          |
| hexiom                     | 4.10 ms                                                     | 4.98 ms: 1.21x slower                                                         |
| python_startup             | 19.5 ms                                                     | 23.7 ms: 1.22x slower                                                         |
| gc_traversal               | 1.52 ms                                                     | 1.86 ms: 1.22x slower                                                         |
| richards_super             | 32.1 ms                                                     | 39.7 ms: 1.24x slower                                                         |
| richards                   | 28.4 ms                                                     | 35.1 ms: 1.24x slower                                                         |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                         |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                  |

Benchmark hidden because not significant (2): sympy_sum, xml_etree_parse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-pythonperf1-amd64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.038x faster
# HPT report

- Reliability score: 97.77% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown