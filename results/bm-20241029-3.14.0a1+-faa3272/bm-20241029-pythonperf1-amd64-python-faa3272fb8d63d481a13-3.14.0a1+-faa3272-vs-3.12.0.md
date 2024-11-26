# Results vs. 3.12.0

- fork: python
- ref: faa3272fb8d63d481a13
- machine: windows-amd64
- commit hash: faa3272
- commit date: 2024-10-29
- overall geometric mean: 1.011x slower
- HPT reliability: 97.32%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 92.9 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                        |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.33x faster                                                        |
| async_tree_io              | 731 ms                                                      | 559 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 401 ms: 1.25x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 279 ms: 1.22x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 634 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| float          | 56.8 ms                                                     | 55.0 ms: 1.03x faster                                                       |
| nbody          | 71.9 ms                                                     | 76.9 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                       |
| regex_dna      | 126 ms                                                      | 123 ms: 1.03x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 90.6 ms: 1.04x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 15.2 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 57.1 ms: 1.02x slower                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 96.1 ms: 1.03x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.06x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 40.2 ms: 1.07x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 217 us: 1.11x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.13x slower                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.62 ms: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.0 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.64 ms: 1.07x faster                                                       |
| django_template | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                        |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.33x faster                                                        |
| async_tree_io              | 731 ms                                                      | 559 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                        |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 401 ms: 1.25x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 279 ms: 1.22x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 634 ms: 1.22x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 19.5 us: 1.21x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.19x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.94 us: 1.08x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.64 ms: 1.07x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 811 us: 1.06x faster                                                        |
| go                         | 91.6 ms                                                     | 86.7 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.5 ms: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 64.7 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| float                      | 56.8 ms                                                     | 55.0 ms: 1.03x faster                                                       |
| regex_dna                  | 126 ms                                                      | 123 ms: 1.03x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 89.2 ms: 1.03x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 78.6 ms: 1.02x faster                                                       |
| generators                 | 22.5 ms                                                     | 22.0 ms: 1.02x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.9 ms: 1.01x faster                                                       |
| async_generators           | 239 ms                                                      | 238 ms: 1.01x faster                                                        |
| nqueens                    | 62.8 ms                                                     | 62.4 ms: 1.01x faster                                                       |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.35 us: 1.01x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.82 us: 1.02x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 75.8 ms: 1.02x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 61.7 ns: 1.02x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 57.1 ms: 1.02x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.02x slower                                                       |
| raytrace                   | 192 ms                                                      | 198 ms: 1.03x slower                                                        |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| pycparser                  | 699 ms                                                      | 721 ms: 1.03x slower                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 96.1 ms: 1.03x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 90.6 ms: 1.04x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 92.9 ms: 1.04x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 61.3 ms: 1.04x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.04x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 535 ms: 1.04x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.06x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.35 ms: 1.06x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 199 ms: 1.06x slower                                                        |
| scimark_fft                | 184 ms                                                      | 196 ms: 1.06x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 15.2 ms: 1.06x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.2 ms: 1.07x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.31 ms: 1.07x slower                                                       |
| pyflate                    | 295 ms                                                      | 315 ms: 1.07x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 46.7 ms: 1.07x slower                                                       |
| nbody                      | 71.9 ms                                                     | 76.9 ms: 1.07x slower                                                       |
| sympy_expand               | 284 ms                                                      | 304 ms: 1.07x slower                                                        |
| fannkuch                   | 247 ms                                                      | 265 ms: 1.07x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 37.2 ms: 1.08x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.75 ms: 1.08x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 217 us: 1.11x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 88.0 ms: 1.12x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                       |
| coverage                   | 40.8 ms                                                     | 45.8 ms: 1.12x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 910 us: 1.13x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.13x slower                                                        |
| richards                   | 28.4 ms                                                     | 32.3 ms: 1.14x slower                                                       |
| richards_super             | 32.1 ms                                                     | 36.6 ms: 1.14x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.62 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.91 ms: 1.19x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 83.1 ms: 1.20x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.0 ms: 1.23x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.91 ms: 1.26x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.83x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (3): chaos, xml_etree_iterparse, json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241029-3.14.0a1+-faa3272/bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.011x slower
# HPT report

- Reliability score: 97.32% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown