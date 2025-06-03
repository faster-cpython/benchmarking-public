# Results vs. 3.12.0

- fork: python
- ref: ec12559ebafca01ded22
- machine: windows-amd64
- commit hash: ec12559
- commit date: 2025-06-03
- overall geometric mean: 1.064x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 399 ms: 1.93x faster                                                       |
| async_tree_io              | 731 ms                                                      | 395 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.71x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.66x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.7 ms: 1.27x faster                                                      |
| nbody          | 71.9 ms                                                     | 62.6 ms: 1.15x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.4 ms: 1.10x faster                                                      |
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|---------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse     | 93.0 ms                                                     | 88.3 ms: 1.05x faster                                                      |
| xml_etree_iterparse | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                      |
| json_loads          | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_process   | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                      |
| pickle_pure_python  | 195 us                                                      | 211 us: 1.08x slower                                                       |
| json_dumps          | 5.70 ms                                                     | 6.29 ms: 1.11x slower                                                      |
| Geometric mean      | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (3): xml_etree_generate, tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.45 ms: 1.10x faster                                                      |
| django_template | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.8 ms: 2.53x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 399 ms: 1.93x faster                                                       |
| async_tree_io              | 731 ms                                                      | 395 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.71x faster                                                       |
| mdp                        | 1.37 sec                                                    | 810 ms: 1.69x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.66x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.47x faster                                                       |
| deepcopy                   | 238 us                                                      | 173 us: 1.38x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.35x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.2 us: 1.31x faster                                                      |
| float                      | 56.8 ms                                                     | 44.7 ms: 1.27x faster                                                      |
| go                         | 91.6 ms                                                     | 75.3 ms: 1.22x faster                                                      |
| nbody                      | 71.9 ms                                                     | 62.6 ms: 1.15x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 58.5 ms: 1.14x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.12x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 79.4 ms: 1.10x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.45 ms: 1.10x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.8 ms: 1.09x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.2 ms: 1.09x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.8 ms: 1.08x faster                                                      |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.3 ms: 1.05x faster                                                      |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.4 ms: 1.04x faster                                                      |
| pyflate                    | 295 ms                                                      | 282 ms: 1.04x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.2 ms: 1.04x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.8 ms: 1.04x faster                                                      |
| sympy_str                  | 175 ms                                                      | 168 ms: 1.04x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 46.7 ms: 1.04x faster                                                      |
| scimark_fft                | 184 ms                                                      | 178 ms: 1.03x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.8 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.49 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 77.0 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| async_generators           | 239 ms                                                      | 235 ms: 1.02x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 4.06 ms: 1.01x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 58.6 ms: 1.00x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.76 us: 1.01x slower                                                      |
| sympy_expand               | 284 ms                                                      | 288 ms: 1.01x slower                                                       |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                       |
| fannkuch                   | 247 ms                                                      | 251 ms: 1.02x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.20 ms: 1.02x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.6 ms: 1.02x slower                                                      |
| pycparser                  | 699 ms                                                      | 719 ms: 1.03x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 546 ms: 1.06x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 211 us: 1.08x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.29 ms: 1.11x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.11x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.59 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.41x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.76x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 315 ns: 5.21x slower                                                       |
| coverage                   | 40.8 ms                                                     | 294 ms: 7.19x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (6): xml_etree_generate, tomli_loads, unpickle_pure_python, logging_simple, json, regex_v8
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250603-3.15.0a0-ec12559/bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown