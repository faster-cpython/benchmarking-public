# Results vs. 3.12.0

- fork: python
- ref: 8dd8b5c2f0785675b928
- machine: windows-amd64
- commit hash: 8dd8b5c
- commit date: 2025-06-17
- overall geometric mean: 1.094x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 395 ms: 1.95x faster                                                       |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.1 ms: 1.29x faster                                                      |
| nbody          | 71.9 ms                                                     | 61.8 ms: 1.16x faster                                                      |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.9 ms: 1.11x faster                                                      |
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|---------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse     | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                      |
| xml_etree_iterparse | 65.2 ms                                                     | 64.4 ms: 1.01x faster                                                      |
| json_loads          | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_process   | 37.7 ms                                                     | 39.3 ms: 1.04x slower                                                      |
| pickle_pure_python  | 195 us                                                      | 207 us: 1.06x slower                                                       |
| json_dumps          | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                      |
| Geometric mean      | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (3): tomli_loads, unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.73 ms: 1.05x faster                                                      |
| django_template | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.1 ms: 2.51x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 395 ms: 1.95x faster                                                       |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| mdp                        | 1.37 sec                                                    | 800 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                       |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.6 us: 1.35x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.8 us: 1.31x faster                                                      |
| float                      | 56.8 ms                                                     | 44.1 ms: 1.29x faster                                                      |
| go                         | 91.6 ms                                                     | 74.9 ms: 1.22x faster                                                      |
| nbody                      | 71.9 ms                                                     | 61.8 ms: 1.16x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.13x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.9 ms: 1.11x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                      |
| raytrace                   | 192 ms                                                      | 177 ms: 1.09x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.9 ms: 1.09x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 62.1 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.6 ms: 1.08x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.3 ms: 1.07x faster                                                      |
| scimark_fft                | 184 ms                                                      | 172 ms: 1.07x faster                                                       |
| richards                   | 28.4 ms                                                     | 26.8 ms: 1.06x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.73 ms: 1.05x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.2 ms: 1.05x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 75.0 ms: 1.05x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.05x faster                                                      |
| sympy_str                  | 175 ms                                                      | 168 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| async_generators           | 239 ms                                                      | 231 ms: 1.04x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.9 ms: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.5 ms: 1.03x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.1 ms: 1.03x faster                                                      |
| json                       | 3.05 ms                                                     | 2.97 ms: 1.03x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.02x faster                                                     |
| pyflate                    | 295 ms                                                      | 289 ms: 1.02x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 4.02 ms: 1.02x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.52 ms: 1.01x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 58.0 ms: 1.01x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.4 ms: 1.01x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.77 us: 1.01x slower                                                      |
| sympy_expand               | 284 ms                                                      | 286 ms: 1.01x slower                                                       |
| pycparser                  | 699 ms                                                      | 710 ms: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 39.3 ms: 1.04x slower                                                      |
| fannkuch                   | 247 ms                                                      | 257 ms: 1.04x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.05x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 537 ms: 1.05x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.1 ms: 1.05x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 101 us: 1.06x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.55 ms: 1.10x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.20x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.0 ms: 1.20x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.17 ms: 1.42x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.34 ms: 1.78x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 342 ns: 5.66x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (5): tomli_loads, logging_simple, unpickle_pure_python, deltablue, xml_etree_generate
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-8dd8b5c/bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.094x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown