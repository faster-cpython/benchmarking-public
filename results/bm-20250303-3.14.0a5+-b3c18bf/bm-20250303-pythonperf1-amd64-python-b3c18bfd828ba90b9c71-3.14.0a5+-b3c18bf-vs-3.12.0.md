# Results vs. 3.12.0

- fork: python
- ref: b3c18bfd828ba90b9c71
- machine: windows-amd64
- commit hash: b3c18bf
- commit date: 2025-03-03
- overall geometric mean: 1.021x faster
- HPT reliability: 91.83%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 230 ms: 1.05x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 411 ms: 1.88x faster                                                        |
| async_tree_io              | 731 ms                                                      | 418 ms: 1.75x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.61x faster                                                        |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 219 ms: 1.55x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 343 ms: 1.43x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.61x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                       |
| pidigits       | 152 ms                                                      | 154 ms: 1.01x slower                                                        |
| nbody          | 71.9 ms                                                     | 73.5 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.50 ms: 1.08x faster                                                       |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 58.6 ms: 1.05x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.07x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.3 ms: 1.09x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 154 us: 1.16x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 234 us: 1.20x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.90 ms: 1.21x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.0 ms: 1.23x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 25.6 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.0 ms: 2.51x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 411 ms: 1.88x faster                                                        |
| async_tree_io              | 731 ms                                                      | 418 ms: 1.75x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.61x faster                                                        |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 219 ms: 1.55x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 343 ms: 1.43x faster                                                        |
| deepcopy                   | 238 us                                                      | 191 us: 1.25x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                       |
| float                      | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.0 us: 1.13x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 60.0 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.50 ms: 1.08x faster                                                       |
| async_generators           | 239 ms                                                      | 224 ms: 1.07x faster                                                        |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.99 us: 1.05x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.7 ms: 1.04x faster                                                       |
| go                         | 91.6 ms                                                     | 88.9 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.5 ms: 1.02x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.4 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 154 ms: 1.01x slower                                                        |
| raytrace                   | 192 ms                                                      | 195 ms: 1.01x slower                                                        |
| json                       | 3.05 ms                                                     | 3.10 ms: 1.02x slower                                                       |
| nbody                      | 71.9 ms                                                     | 73.5 ms: 1.02x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 35.4 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 77.6 ms: 1.04x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.54 us: 1.04x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 63.0 ns: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.67 ms: 1.04x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 50.6 ms: 1.04x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 196 ms: 1.05x slower                                                        |
| sympy_expand               | 284 ms                                                      | 297 ms: 1.05x slower                                                        |
| scimark_fft                | 184 ms                                                      | 193 ms: 1.05x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 58.6 ms: 1.05x slower                                                       |
| 2to3                       | 218 ms                                                      | 230 ms: 1.05x slower                                                        |
| logging_format             | 6.72 us                                                     | 7.09 us: 1.06x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.31 ms: 1.07x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.07x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.40 ms: 1.07x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.07x slower                                                       |
| pyflate                    | 295 ms                                                      | 317 ms: 1.07x slower                                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.13 sec: 1.08x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.2 ms: 1.08x slower                                                       |
| pycparser                  | 699 ms                                                      | 755 ms: 1.08x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 561 ms: 1.09x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 41.3 ms: 1.09x slower                                                       |
| richards                   | 28.4 ms                                                     | 31.3 ms: 1.10x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 887 us: 1.10x slower                                                        |
| richards_super             | 32.1 ms                                                     | 35.5 ms: 1.11x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.12x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 67.2 ms: 1.14x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 89.9 ms: 1.14x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.57 sec: 1.15x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 109 us: 1.15x slower                                                        |
| coverage                   | 40.8 ms                                                     | 47.0 ms: 1.15x slower                                                       |
| fannkuch                   | 247 ms                                                      | 285 ms: 1.15x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 154 us: 1.16x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.90 ms: 1.19x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 234 us: 1.20x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.90 ms: 1.21x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.0 ms: 1.23x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 87.5 ms: 1.27x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.07 ms: 1.36x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.24 ms: 1.64x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (6): xml_etree_iterparse, regex_compile, nqueens, sympy_str, bench_thread_pool, mako
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250303-3.14.0a5+-b3c18bf/bm-20250303-pythonperf1-amd64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.021x faster

# HPT report

- Reliability score: 91.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown