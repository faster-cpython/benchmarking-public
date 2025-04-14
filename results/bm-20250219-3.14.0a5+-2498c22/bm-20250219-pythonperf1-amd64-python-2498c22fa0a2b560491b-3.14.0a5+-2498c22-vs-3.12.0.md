# Results vs. 3.12.0

- fork: python
- ref: 2498c22fa0a2b560491b
- machine: windows-amd64
- commit hash: 2498c22
- commit date: 2025-02-19
- overall geometric mean: 1.045x faster
- HPT reliability: 56.35%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 403 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 416 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 214 ms: 1.72x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                        |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 218 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.4 ms: 1.25x faster                                                       |
| pidigits       | 152 ms                                                      | 153 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.46 ms: 1.11x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 85.2 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 62.6 ms: 1.04x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.6 ms: 1.01x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.8 ms: 1.06x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.0 us: 1.08x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.10x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 224 us: 1.15x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.75 ms: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.8 ms: 1.27x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.81 ms: 1.04x faster                                                       |
| django_template | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.5 ms: 2.73x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 403 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 416 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 214 ms: 1.72x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                        |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 218 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                        |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                                        |
| float                      | 56.8 ms                                                     | 45.4 ms: 1.25x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.3 us: 1.25x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.0 us: 1.19x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.46 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.90 us: 1.10x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 61.0 ms: 1.10x faster                                                       |
| go                         | 91.6 ms                                                     | 84.5 ms: 1.08x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                                       |
| async_generators           | 239 ms                                                      | 223 ms: 1.08x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 41.7 ms: 1.06x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.81 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.6 ms: 1.04x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 58.2 ns: 1.04x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 88.2 ms: 1.04x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.8 ms: 1.04x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 831 us: 1.03x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 85.2 ms: 1.03x faster                                                       |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.02x faster                                                       |
| sympy_str                  | 175 ms                                                      | 173 ms: 1.01x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 153 ms: 1.00x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 74.9 ms: 1.00x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 34.7 ms: 1.01x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 63.4 ms: 1.01x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.6 ms: 1.01x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 190 ms: 1.02x slower                                                        |
| raytrace                   | 192 ms                                                      | 196 ms: 1.02x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.42 us: 1.02x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.19 ms: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.88 us: 1.02x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.9 ms: 1.03x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.08 sec: 1.03x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 534 ms: 1.04x slower                                                        |
| richards                   | 28.4 ms                                                     | 29.7 ms: 1.05x slower                                                       |
| sympy_expand               | 284 ms                                                      | 297 ms: 1.05x slower                                                        |
| scimark_fft                | 184 ms                                                      | 194 ms: 1.05x slower                                                        |
| richards_super             | 32.1 ms                                                     | 33.8 ms: 1.05x slower                                                       |
| pyflate                    | 295 ms                                                      | 310 ms: 1.05x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 39.8 ms: 1.06x slower                                                       |
| pycparser                  | 699 ms                                                      | 739 ms: 1.06x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 46.3 ms: 1.06x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.76 ms: 1.08x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.0 us: 1.08x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 85.8 ms: 1.09x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 64.2 ms: 1.09x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 885 us: 1.10x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.10x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.10x slower                                                        |
| fannkuch                   | 247 ms                                                      | 273 ms: 1.11x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.54 sec: 1.12x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 224 us: 1.15x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.74 ms: 1.15x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.1 ms: 1.18x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.75 ms: 1.18x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 84.9 ms: 1.23x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.8 ms: 1.27x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.97 ms: 1.30x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_parse, nbody, regex_v8
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250219-3.14.0a5+-2498c22/bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 56.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown