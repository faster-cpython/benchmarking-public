# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_hot
- machine: windows-amd64
- commit hash: a987be7
- commit date: 2025-06-23
- overall geometric mean: 1.119x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 219 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                       | 1.00x slower                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                                   |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                   |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.73x faster                                                   |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                   |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                   |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                   |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.47x faster                                                   |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 55.3 ms: 1.30x faster                                                  |
| float          | 56.8 ms                                                     | 44.7 ms: 1.27x faster                                                  |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                       | 1.19x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.3 ms: 1.12x faster                                                  |
| regex_dna      | 126 ms                                                      | 119 ms: 1.07x faster                                                   |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.02x faster                                                  |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                       | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 109 us: 1.22x faster                                                   |
| tomli_loads          | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                                  |
| xml_etree_process    | 37.7 ms                                                     | 35.5 ms: 1.06x faster                                                  |
| xml_etree_parse      | 93.0 ms                                                     | 88.3 ms: 1.05x faster                                                  |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                  |
| pickle_pure_python   | 195 us                                                      | 202 us: 1.03x slower                                                   |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                  |
| json_dumps           | 5.70 ms                                                     | 6.16 ms: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                  |
| python_startup         | 19.5 ms                                                     | 26.0 ms: 1.33x slower                                                  |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.40 ms: 1.31x faster                                                  |
| django_template | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                  |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.8 ms: 2.53x faster                                                  |
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                                   |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.75x faster                                                   |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.73x faster                                                   |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                   |
| mdp                        | 1.37 sec                                                    | 807 ms: 1.70x faster                                                   |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                   |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                   |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.47x faster                                                   |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                   |
| deepcopy_memo              | 23.7 us                                                     | 17.8 us: 1.33x faster                                                  |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                                  |
| mako                       | 7.09 ms                                                     | 5.40 ms: 1.31x faster                                                  |
| nbody                      | 71.9 ms                                                     | 55.3 ms: 1.30x faster                                                  |
| float                      | 56.8 ms                                                     | 44.7 ms: 1.27x faster                                                  |
| unpickle_pure_python       | 133 us                                                      | 109 us: 1.22x faster                                                   |
| go                         | 91.6 ms                                                     | 75.5 ms: 1.21x faster                                                  |
| tomli_loads                | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                 |
| scimark_fft                | 184 ms                                                      | 157 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 2.09 us                                                     | 1.78 us: 1.17x faster                                                  |
| pyflate                    | 295 ms                                                      | 256 ms: 1.15x faster                                                   |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.23 ms: 1.15x faster                                                  |
| fannkuch                   | 247 ms                                                      | 215 ms: 1.15x faster                                                   |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                                  |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.14x faster                                                  |
| spectral_norm              | 66.9 ms                                                     | 59.9 ms: 1.12x faster                                                  |
| regex_compile              | 87.5 ms                                                     | 78.3 ms: 1.12x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                                  |
| dulwich_log                | 44.3 ms                                                     | 40.9 ms: 1.08x faster                                                  |
| chaos                      | 43.3 ms                                                     | 40.4 ms: 1.07x faster                                                  |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.07x faster                                                   |
| xml_etree_process          | 37.7 ms                                                     | 35.5 ms: 1.06x faster                                                  |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.2 ms: 1.06x faster                                                  |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                   |
| crypto_pyaes               | 48.5 ms                                                     | 45.9 ms: 1.06x faster                                                  |
| xml_etree_parse            | 93.0 ms                                                     | 88.3 ms: 1.05x faster                                                  |
| richards                   | 28.4 ms                                                     | 26.9 ms: 1.05x faster                                                  |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                  |
| sympy_sum                  | 91.5 ms                                                     | 87.1 ms: 1.05x faster                                                  |
| nqueens                    | 62.8 ms                                                     | 60.1 ms: 1.05x faster                                                  |
| scimark_sor                | 78.8 ms                                                     | 75.9 ms: 1.04x faster                                                  |
| meteor_contest             | 74.6 ms                                                     | 72.1 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.03x faster                                                 |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                  |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                   |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.03x faster                                                  |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.02x faster                                                  |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                   |
| logging_format             | 6.72 us                                                     | 6.59 us: 1.02x faster                                                  |
| coroutines                 | 14.3 ms                                                     | 14.0 ms: 1.02x faster                                                  |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                  |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                  |
| hexiom                     | 4.10 ms                                                     | 4.05 ms: 1.01x faster                                                  |
| logging_simple             | 6.28 us                                                     | 6.21 us: 1.01x faster                                                  |
| 2to3                       | 218 ms                                                      | 219 ms: 1.01x slower                                                   |
| deltablue                  | 2.16 ms                                                     | 2.22 ms: 1.03x slower                                                  |
| pickle_pure_python         | 195 us                                                      | 202 us: 1.03x slower                                                   |
| async_generators           | 239 ms                                                      | 247 ms: 1.03x slower                                                   |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                  |
| telco                      | 4.13 ms                                                     | 4.27 ms: 1.03x slower                                                  |
| sympy_expand               | 284 ms                                                      | 294 ms: 1.04x slower                                                   |
| django_template            | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                  |
| scimark_lu                 | 58.9 ms                                                     | 62.8 ms: 1.07x slower                                                  |
| json_dumps                 | 5.70 ms                                                     | 6.16 ms: 1.08x slower                                                  |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.11x slower                                                   |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                  |
| coverage                   | 40.8 ms                                                     | 48.3 ms: 1.18x slower                                                  |
| python_startup             | 19.5 ms                                                     | 26.0 ms: 1.33x slower                                                  |
| gc_traversal               | 1.52 ms                                                     | 2.12 ms: 1.40x slower                                                  |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                  |
| logging_silent             | 60.5 ns                                                     | 316 ns: 5.22x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                           |

Benchmark hidden because not significant (3): docutils, pprint_safe_repr, pycparser
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250623-3.15.0a0-a987be7-JIT/bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.119x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown