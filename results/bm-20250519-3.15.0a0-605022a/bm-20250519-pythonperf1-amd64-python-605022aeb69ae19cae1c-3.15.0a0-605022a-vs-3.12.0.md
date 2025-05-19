# Results vs. 3.12.0

- fork: python
- ref: 605022aeb69ae19cae1c
- machine: windows-amd64
- commit hash: 605022a
- commit date: 2025-05-19
- overall geometric mean: 1.075x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 389 ms: 1.98x faster                                                       |
| async_tree_io              | 731 ms                                                      | 395 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.78x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 42.5 ms: 1.34x faster                                                      |
| nbody          | 71.9 ms                                                     | 61.6 ms: 1.17x faster                                                      |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.9 ms: 1.10x faster                                                      |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.2 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 56.2 ms: 1.01x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 136 us: 1.02x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.07x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.0 us: 1.08x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.17 ms: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.8 ms: 1.15x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.0 ms: 1.28x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.47 ms: 1.10x faster                                                      |
| django_template | 22.9 ms                                                     | 24.0 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.6 ms: 2.72x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 389 ms: 1.98x faster                                                       |
| async_tree_io              | 731 ms                                                      | 395 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.78x faster                                                       |
| mdp                        | 1.37 sec                                                    | 779 ms: 1.76x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| deepcopy                   | 238 us                                                      | 173 us: 1.37x faster                                                       |
| float                      | 56.8 ms                                                     | 42.5 ms: 1.34x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 19.2 us: 1.24x faster                                                      |
| go                         | 91.6 ms                                                     | 78.1 ms: 1.17x faster                                                      |
| nbody                      | 71.9 ms                                                     | 61.6 ms: 1.17x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 57.5 ms: 1.16x faster                                                      |
| chaos                      | 43.3 ms                                                     | 38.1 ms: 1.14x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 79.9 ms: 1.10x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.47 ms: 1.10x faster                                                      |
| raytrace                   | 192 ms                                                      | 178 ms: 1.08x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.9 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.4 ms: 1.08x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| scimark_fft                | 184 ms                                                      | 174 ms: 1.06x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.2 ms: 1.05x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 994 ms: 1.05x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                                      |
| pyflate                    | 295 ms                                                      | 280 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 489 ms: 1.05x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                      |
| async_generators           | 239 ms                                                      | 229 ms: 1.04x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.7 ms: 1.04x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.8 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.46 ms: 1.04x faster                                                      |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.04x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 76.0 ms: 1.04x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.6 ms: 1.04x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.9 ms: 1.03x faster                                                      |
| json                       | 3.05 ms                                                     | 2.95 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.99 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.02x faster                                                     |
| meteor_contest             | 74.6 ms                                                     | 73.0 ms: 1.02x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 840 us: 1.02x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.12 ms: 1.02x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 57.8 ms: 1.02x faster                                                      |
| fannkuch                   | 247 ms                                                      | 246 ms: 1.00x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.2 ms: 1.01x slower                                                      |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| pycparser                  | 699 ms                                                      | 707 ms: 1.01x slower                                                       |
| sympy_expand               | 284 ms                                                      | 289 ms: 1.02x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 136 us: 1.02x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.44 us: 1.03x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.91 us: 1.03x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.0 ms: 1.04x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.07x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.0 us: 1.08x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.17 ms: 1.08x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.61 ms: 1.12x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 108 us: 1.13x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.8 ms: 1.15x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.0 ms: 1.28x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 92.0 ms: 1.33x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.08 ms: 1.37x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.28 ms: 1.71x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 316 ns: 5.22x slower                                                       |
| coverage                   | 40.8 ms                                                     | 295 ms: 7.22x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): tomli_loads
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250519-3.15.0a0-605022a/bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.075x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown