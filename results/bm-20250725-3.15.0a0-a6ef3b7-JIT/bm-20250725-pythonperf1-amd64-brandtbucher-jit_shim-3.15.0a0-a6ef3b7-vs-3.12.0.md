# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_shim
- machine: windows-amd64
- commit hash: a6ef3b7
- commit date: 2025-07-25
- overall geometric mean: 1.107x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                       | 1.01x slower                                                         |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 395 ms: 1.95x faster                                                 |
| async_tree_io              | 731 ms                                                      | 389 ms: 1.88x faster                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.69x faster                                                 |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.66x faster                                                 |
| async_tree_none            | 291 ms                                                      | 176 ms: 1.65x faster                                                 |
| async_tree_memoization     | 339 ms                                                      | 216 ms: 1.57x faster                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 350 ms: 1.43x faster                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 344 ms: 1.42x faster                                                 |
| Geometric mean             | (ref)                                                       | 1.65x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                |
| nbody          | 71.9 ms                                                     | 57.0 ms: 1.26x faster                                                |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                       | 1.18x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 82.5 ms: 1.06x faster                                                |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.67 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                       | 1.02x faster                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                               |
| unpickle_pure_python | 133 us                                                      | 109 us: 1.22x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                                |
| xml_etree_process    | 37.7 ms                                                     | 36.0 ms: 1.05x faster                                                |
| xml_etree_parse      | 93.0 ms                                                     | 89.8 ms: 1.04x faster                                                |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                |
| pickle_pure_python   | 195 us                                                      | 211 us: 1.08x slower                                                 |
| json_dumps           | 5.70 ms                                                     | 6.30 ms: 1.11x slower                                                |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.1 ms: 1.24x slower                                                |
| python_startup         | 19.5 ms                                                     | 27.1 ms: 1.39x slower                                                |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.33 ms: 1.33x faster                                                |
| django_template | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 33.1 ms: 2.43x faster                                                |
| async_tree_io_tg           | 771 ms                                                      | 395 ms: 1.95x faster                                                 |
| async_tree_io              | 731 ms                                                      | 389 ms: 1.88x faster                                                 |
| mdp                        | 1.37 sec                                                    | 802 ms: 1.71x faster                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.69x faster                                                 |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.66x faster                                                 |
| async_tree_none            | 291 ms                                                      | 176 ms: 1.65x faster                                                 |
| async_tree_memoization     | 339 ms                                                      | 216 ms: 1.57x faster                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 350 ms: 1.43x faster                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 344 ms: 1.42x faster                                                 |
| deepcopy                   | 238 us                                                      | 168 us: 1.42x faster                                                 |
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.35x faster                                                |
| deepcopy_memo              | 23.7 us                                                     | 17.8 us: 1.33x faster                                                |
| mako                       | 7.09 ms                                                     | 5.33 ms: 1.33x faster                                                |
| float                      | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                |
| nbody                      | 71.9 ms                                                     | 57.0 ms: 1.26x faster                                                |
| tomli_loads                | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                               |
| unpickle_pure_python       | 133 us                                                      | 109 us: 1.22x faster                                                 |
| scimark_fft                | 184 ms                                                      | 154 ms: 1.19x faster                                                 |
| pyflate                    | 295 ms                                                      | 252 ms: 1.17x faster                                                 |
| go                         | 91.6 ms                                                     | 78.8 ms: 1.16x faster                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                |
| pprint_pformat             | 1.05 sec                                                    | 911 ms: 1.15x faster                                                 |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.14x faster                                                |
| pprint_safe_repr           | 513 ms                                                      | 451 ms: 1.14x faster                                                 |
| fannkuch                   | 247 ms                                                      | 217 ms: 1.13x faster                                                 |
| generators                 | 22.5 ms                                                     | 20.0 ms: 1.13x faster                                                |
| xml_etree_generate         | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                                |
| chaos                      | 43.3 ms                                                     | 40.1 ms: 1.08x faster                                                |
| logging_silent             | 60.5 ns                                                     | 56.1 ns: 1.08x faster                                                |
| dulwich_log                | 44.3 ms                                                     | 41.4 ms: 1.07x faster                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.40 ms: 1.07x faster                                                |
| raytrace                   | 192 ms                                                      | 181 ms: 1.06x faster                                                 |
| crypto_pyaes               | 48.5 ms                                                     | 45.7 ms: 1.06x faster                                                |
| regex_compile              | 87.5 ms                                                     | 82.5 ms: 1.06x faster                                                |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                 |
| xml_etree_process          | 37.7 ms                                                     | 36.0 ms: 1.05x faster                                                |
| nqueens                    | 62.8 ms                                                     | 60.2 ms: 1.04x faster                                                |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.2 ms: 1.04x faster                                                |
| logging_simple             | 6.28 us                                                     | 6.06 us: 1.04x faster                                                |
| richards_super             | 32.1 ms                                                     | 31.0 ms: 1.04x faster                                                |
| xml_etree_parse            | 93.0 ms                                                     | 89.8 ms: 1.04x faster                                                |
| richards                   | 28.4 ms                                                     | 27.7 ms: 1.02x faster                                                |
| spectral_norm              | 66.9 ms                                                     | 65.5 ms: 1.02x faster                                                |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                 |
| scimark_sor                | 78.8 ms                                                     | 77.7 ms: 1.01x faster                                                |
| meteor_contest             | 74.6 ms                                                     | 73.8 ms: 1.01x faster                                                |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.02x slower                                                |
| scimark_lu                 | 58.9 ms                                                     | 59.9 ms: 1.02x slower                                                |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                 |
| regex_effbot               | 1.62 ms                                                     | 1.67 ms: 1.03x slower                                                |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.03x slower                                                |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                                 |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                |
| coroutines                 | 14.3 ms                                                     | 14.9 ms: 1.04x slower                                                |
| telco                      | 4.13 ms                                                     | 4.33 ms: 1.05x slower                                                |
| sympy_expand               | 284 ms                                                      | 300 ms: 1.06x slower                                                 |
| pickle_pure_python         | 195 us                                                      | 211 us: 1.08x slower                                                 |
| django_template            | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                |
| json_dumps                 | 5.70 ms                                                     | 6.30 ms: 1.11x slower                                                |
| typing_runtime_protocols   | 95.1 us                                                     | 108 us: 1.13x slower                                                 |
| python_startup_no_site     | 16.2 ms                                                     | 20.1 ms: 1.24x slower                                                |
| coverage                   | 40.8 ms                                                     | 51.2 ms: 1.25x slower                                                |
| python_startup             | 19.5 ms                                                     | 27.1 ms: 1.39x slower                                                |
| gc_traversal               | 1.52 ms                                                     | 2.24 ms: 1.47x slower                                                |
| create_gc_cycles           | 752 us                                                      | 1.39 ms: 1.85x slower                                                |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                         |

Benchmark hidden because not significant (8): sympy_str, xml_etree_iterparse, docutils, sympy_sum, logging_format, hexiom, pycparser, regex_v8
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.107x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown