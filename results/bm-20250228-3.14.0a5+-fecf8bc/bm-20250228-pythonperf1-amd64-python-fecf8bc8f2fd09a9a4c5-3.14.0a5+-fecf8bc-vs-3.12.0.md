# Results vs. 3.12.0

- fork: python
- ref: fecf8bc8f2fd09a9a4c5
- machine: windows-amd64
- commit hash: fecf8bc
- commit date: 2025-02-28
- overall geometric mean: 1.040x faster
- HPT reliability: 58.94%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 417 ms: 1.75x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.57x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 217 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 339 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 340 ms: 1.44x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.63x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.2 ms: 1.23x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| nbody          | 71.9 ms                                                     | 72.7 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.48 ms: 1.10x faster                                                       |
| regex_dna      | 126 ms                                                      | 119 ms: 1.07x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 86.9 ms: 1.01x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 62.0 ms: 1.05x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 89.1 ms: 1.04x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 57.2 ms: 1.03x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 40.3 ms: 1.07x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.13x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 227 us: 1.16x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.76 ms: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.0 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.68 ms: 1.06x faster                                                       |
| django_template | 22.9 ms                                                     | 25.2 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.8 ms: 2.53x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 417 ms: 1.75x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.57x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 217 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 339 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 340 ms: 1.44x faster                                                        |
| deepcopy                   | 238 us                                                      | 184 us: 1.30x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                       |
| float                      | 56.8 ms                                                     | 46.2 ms: 1.23x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.3 us: 1.17x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.48 ms: 1.10x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 61.3 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                       |
| async_generators           | 239 ms                                                      | 221 ms: 1.08x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.07x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.07x faster                                                        |
| mako                       | 7.09 ms                                                     | 6.68 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.0 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.3 ms: 1.05x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.5 ms: 1.05x faster                                                       |
| go                         | 91.6 ms                                                     | 87.6 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.1 ms: 1.04x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 88.9 ms: 1.03x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 59.6 ns: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| sympy_str                  | 175 ms                                                      | 174 ms: 1.01x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 86.9 ms: 1.01x faster                                                       |
| raytrace                   | 192 ms                                                      | 193 ms: 1.01x slower                                                        |
| nbody                      | 71.9 ms                                                     | 72.7 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 35.1 ms: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.85 us: 1.02x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.40 us: 1.02x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 191 ms: 1.02x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 57.2 ms: 1.03x slower                                                       |
| json                       | 3.05 ms                                                     | 3.13 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.22 ms: 1.03x slower                                                       |
| scimark_fft                | 184 ms                                                      | 190 ms: 1.03x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 45.2 ms: 1.03x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 50.2 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.65 ms: 1.04x slower                                                       |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 77.9 ms: 1.04x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| sympy_expand               | 284 ms                                                      | 298 ms: 1.05x slower                                                        |
| richards                   | 28.4 ms                                                     | 29.8 ms: 1.05x slower                                                       |
| pyflate                    | 295 ms                                                      | 311 ms: 1.06x slower                                                        |
| richards_super             | 32.1 ms                                                     | 34.0 ms: 1.06x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.36 ms: 1.06x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.09 ms: 1.07x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.3 ms: 1.07x slower                                                       |
| pycparser                  | 699 ms                                                      | 752 ms: 1.08x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 63.6 ms: 1.08x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 555 ms: 1.08x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 85.4 ms: 1.08x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 883 us: 1.10x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.2 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.11x slower                                                        |
| fannkuch                   | 247 ms                                                      | 276 ms: 1.12x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.13x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.77 ms: 1.16x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 227 us: 1.16x slower                                                        |
| coverage                   | 40.8 ms                                                     | 47.5 ms: 1.16x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.76 ms: 1.19x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 86.5 ms: 1.25x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.0 ms: 1.29x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.04 ms: 1.34x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (3): docutils, nqueens, bench_thread_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250228-3.14.0a5+-fecf8bc/bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 58.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown