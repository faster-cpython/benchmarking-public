# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_nops
- machine: windows-amd64
- commit hash: 75922b6
- commit date: 2025-06-27
- overall geometric mean: 1.113x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                       | 1.01x slower                                                         |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 387 ms: 1.99x faster                                                 |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                 |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                 |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                 |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                 |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 54.3 ms: 1.32x faster                                                |
| float          | 56.8 ms                                                     | 45.5 ms: 1.25x faster                                                |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                       | 1.20x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                |
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                       | 1.07x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 107 us: 1.24x faster                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                               |
| xml_etree_generate   | 55.8 ms                                                     | 50.4 ms: 1.11x faster                                                |
| xml_etree_parse      | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                |
| xml_etree_process    | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                 |
| json_dumps           | 5.70 ms                                                     | 6.55 ms: 1.15x slower                                                |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                |
| python_startup         | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.38 ms: 1.32x faster                                                |
| django_template | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.0 ms: 2.52x faster                                                |
| async_tree_io_tg           | 771 ms                                                      | 387 ms: 1.99x faster                                                 |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                 |
| mdp                        | 1.37 sec                                                    | 804 ms: 1.71x faster                                                 |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                 |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                 |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                 |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                 |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.34x faster                                                |
| nbody                      | 71.9 ms                                                     | 54.3 ms: 1.32x faster                                                |
| mako                       | 7.09 ms                                                     | 5.38 ms: 1.32x faster                                                |
| deepcopy_memo              | 23.7 us                                                     | 18.2 us: 1.30x faster                                                |
| float                      | 56.8 ms                                                     | 45.5 ms: 1.25x faster                                                |
| unpickle_pure_python       | 133 us                                                      | 107 us: 1.24x faster                                                 |
| scimark_fft                | 184 ms                                                      | 152 ms: 1.21x faster                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                               |
| go                         | 91.6 ms                                                     | 78.6 ms: 1.17x faster                                                |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.15x faster                                                |
| pyflate                    | 295 ms                                                      | 258 ms: 1.14x faster                                                 |
| pprint_safe_repr           | 513 ms                                                      | 459 ms: 1.12x faster                                                 |
| pprint_pformat             | 1.05 sec                                                    | 936 ms: 1.12x faster                                                 |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.29 ms: 1.12x faster                                                |
| regex_compile              | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                |
| xml_etree_generate         | 55.8 ms                                                     | 50.4 ms: 1.11x faster                                                |
| logging_silent             | 60.5 ns                                                     | 55.0 ns: 1.10x faster                                                |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                 |
| fannkuch                   | 247 ms                                                      | 227 ms: 1.09x faster                                                 |
| dulwich_log                | 44.3 ms                                                     | 41.1 ms: 1.08x faster                                                |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                 |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.5 ms: 1.05x faster                                                |
| xml_etree_parse            | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                |
| xml_etree_process          | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                                |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                 |
| richards                   | 28.4 ms                                                     | 27.1 ms: 1.05x faster                                                |
| nqueens                    | 62.8 ms                                                     | 60.0 ms: 1.05x faster                                                |
| crypto_pyaes               | 48.5 ms                                                     | 46.4 ms: 1.04x faster                                                |
| sympy_sum                  | 91.5 ms                                                     | 87.9 ms: 1.04x faster                                                |
| chaos                      | 43.3 ms                                                     | 41.6 ms: 1.04x faster                                                |
| richards_super             | 32.1 ms                                                     | 30.9 ms: 1.04x faster                                                |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                |
| meteor_contest             | 74.6 ms                                                     | 72.6 ms: 1.03x faster                                                |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.02x faster                                                 |
| spectral_norm              | 66.9 ms                                                     | 65.9 ms: 1.02x faster                                                |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.01x faster                                                |
| logging_simple             | 6.28 us                                                     | 6.21 us: 1.01x faster                                                |
| logging_format             | 6.72 us                                                     | 6.66 us: 1.01x faster                                                |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                 |
| scimark_sor                | 78.8 ms                                                     | 81.1 ms: 1.03x slower                                                |
| deltablue                  | 2.16 ms                                                     | 2.23 ms: 1.03x slower                                                |
| hexiom                     | 4.10 ms                                                     | 4.24 ms: 1.03x slower                                                |
| scimark_lu                 | 58.9 ms                                                     | 60.9 ms: 1.03x slower                                                |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                |
| telco                      | 4.13 ms                                                     | 4.29 ms: 1.04x slower                                                |
| sympy_expand               | 284 ms                                                      | 295 ms: 1.04x slower                                                 |
| async_generators           | 239 ms                                                      | 250 ms: 1.05x slower                                                 |
| django_template            | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                |
| coroutines                 | 14.3 ms                                                     | 15.2 ms: 1.07x slower                                                |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                 |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.09x slower                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.55 ms: 1.15x slower                                                |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                |
| coverage                   | 40.8 ms                                                     | 50.6 ms: 1.24x slower                                                |
| python_startup             | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                |
| gc_traversal               | 1.52 ms                                                     | 2.16 ms: 1.42x slower                                                |
| create_gc_cycles           | 752 us                                                      | 1.34 ms: 1.78x slower                                                |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                         |

Benchmark hidden because not significant (3): json, pycparser, docutils
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250627-3.15.0a0-75922b6-JIT/bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.113x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown