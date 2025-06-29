# Results vs. 3.12.0

- fork: python
- ref: 3.14
- machine: windows-amd64
- commit hash: 964c29d
- commit date: 2025-06-16
- overall geometric mean: 1.091x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 399 ms: 1.93x faster                                        |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                        |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.67x faster                                        |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.66x faster                                        |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                        |
| Geometric mean             | (ref)                                                       | 1.67x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.4 ms: 1.31x faster                                       |
| nbody          | 71.9 ms                                                     | 62.4 ms: 1.15x faster                                       |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.3 ms: 1.10x faster                                       |
| regex_v8       | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                       |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                        |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.6 ms: 1.05x faster                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.4 ms: 1.03x faster                                       |
| unpickle_pure_python | 133 us                                                      | 132 us: 1.01x faster                                        |
| xml_etree_process    | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                       |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                        |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                       |
| json_dumps           | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                |

Benchmark hidden because not significant (2): xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                       |
| python_startup         | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.76 ms: 1.05x faster                                       |
| django_template | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                       |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.4 ms: 2.48x faster                                       |
| async_tree_io_tg           | 771 ms                                                      | 399 ms: 1.93x faster                                        |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                        |
| mdp                        | 1.37 sec                                                    | 819 ms: 1.68x faster                                        |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.67x faster                                        |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.66x faster                                        |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                        |
| deepcopy                   | 238 us                                                      | 172 us: 1.38x faster                                        |
| float                      | 56.8 ms                                                     | 43.4 ms: 1.31x faster                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.3 us: 1.29x faster                                       |
| comprehensions             | 14.1 us                                                     | 11.2 us: 1.26x faster                                       |
| go                         | 91.6 ms                                                     | 77.0 ms: 1.19x faster                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.78 us: 1.18x faster                                       |
| spectral_norm              | 66.9 ms                                                     | 57.8 ms: 1.16x faster                                       |
| nbody                      | 71.9 ms                                                     | 62.4 ms: 1.15x faster                                       |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.14x faster                                       |
| regex_compile              | 87.5 ms                                                     | 79.3 ms: 1.10x faster                                       |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.10x faster                                       |
| chaos                      | 43.3 ms                                                     | 39.6 ms: 1.09x faster                                       |
| regex_v8                   | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                       |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                        |
| scimark_fft                | 184 ms                                                      | 173 ms: 1.07x faster                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.0 ms: 1.07x faster                                       |
| dulwich_log                | 44.3 ms                                                     | 41.7 ms: 1.06x faster                                       |
| richards                   | 28.4 ms                                                     | 26.8 ms: 1.06x faster                                       |
| raytrace                   | 192 ms                                                      | 183 ms: 1.05x faster                                        |
| xml_etree_parse            | 93.0 ms                                                     | 88.6 ms: 1.05x faster                                       |
| mako                       | 7.09 ms                                                     | 6.76 ms: 1.05x faster                                       |
| richards_super             | 32.1 ms                                                     | 30.7 ms: 1.05x faster                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.00 sec: 1.04x faster                                      |
| pprint_safe_repr           | 513 ms                                                      | 492 ms: 1.04x faster                                        |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                       |
| scimark_sor                | 78.8 ms                                                     | 76.1 ms: 1.04x faster                                       |
| sympy_sum                  | 91.5 ms                                                     | 88.5 ms: 1.03x faster                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.03x faster                                       |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                       |
| nqueens                    | 62.8 ms                                                     | 60.9 ms: 1.03x faster                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.4 ms: 1.03x faster                                       |
| scimark_lu                 | 58.9 ms                                                     | 57.3 ms: 1.03x faster                                       |
| deltablue                  | 2.16 ms                                                     | 2.11 ms: 1.03x faster                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.3 ms: 1.03x faster                                       |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.03x faster                                        |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                        |
| async_generators           | 239 ms                                                      | 235 ms: 1.02x faster                                        |
| pyflate                    | 295 ms                                                      | 290 ms: 1.02x faster                                        |
| meteor_contest             | 74.6 ms                                                     | 73.7 ms: 1.01x faster                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.53 ms: 1.01x faster                                       |
| unpickle_pure_python       | 133 us                                                      | 132 us: 1.01x faster                                        |
| pycparser                  | 699 ms                                                      | 710 ms: 1.02x slower                                        |
| fannkuch                   | 247 ms                                                      | 253 ms: 1.02x slower                                        |
| logging_format             | 6.72 us                                                     | 6.88 us: 1.02x slower                                       |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                        |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                        |
| json                       | 3.05 ms                                                     | 3.14 ms: 1.03x slower                                       |
| logging_simple             | 6.28 us                                                     | 6.48 us: 1.03x slower                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                       |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                        |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                       |
| django_template            | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                       |
| json_dumps                 | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.11x slower                                        |
| telco                      | 4.13 ms                                                     | 4.60 ms: 1.11x slower                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                       |
| coverage                   | 40.8 ms                                                     | 49.0 ms: 1.20x slower                                       |
| python_startup             | 19.5 ms                                                     | 26.5 ms: 1.36x slower                                       |
| gc_traversal               | 1.52 ms                                                     | 2.15 ms: 1.41x slower                                       |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                       |
| logging_silent             | 60.5 ns                                                     | 317 ns: 5.24x slower                                        |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                |

Benchmark hidden because not significant (4): hexiom, xml_etree_generate, docutils, tomli_loads
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250616-3.14.0b2+-964c29d/bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.091x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown