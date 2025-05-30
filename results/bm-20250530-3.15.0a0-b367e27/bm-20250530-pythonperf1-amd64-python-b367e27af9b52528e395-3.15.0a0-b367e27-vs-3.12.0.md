# Results vs. 3.12.0

- fork: python
- ref: b367e27af9b52528e395
- machine: windows-amd64
- commit hash: b367e27
- commit date: 2025-05-30
- overall geometric mean: 1.068x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 402 ms: 1.92x faster                                                       |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 339 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                      |
| nbody          | 71.9 ms                                                     | 62.4 ms: 1.15x faster                                                      |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.7 ms: 1.10x faster                                                      |
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|---------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse     | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                      |
| xml_etree_iterparse | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| xml_etree_generate  | 55.8 ms                                                     | 54.8 ms: 1.02x faster                                                      |
| xml_etree_process   | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                      |
| pickle_pure_python  | 195 us                                                      | 209 us: 1.07x slower                                                       |
| json_loads          | 13.9 us                                                     | 14.9 us: 1.07x slower                                                      |
| json_dumps          | 5.70 ms                                                     | 6.11 ms: 1.07x slower                                                      |
| Geometric mean      | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.55 ms: 1.08x faster                                                      |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.6 ms: 2.55x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 402 ms: 1.92x faster                                                       |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                       |
| mdp                        | 1.37 sec                                                    | 795 ms: 1.73x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 339 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| deepcopy                   | 238 us                                                      | 168 us: 1.42x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.7 us: 1.34x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                                      |
| float                      | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                      |
| go                         | 91.6 ms                                                     | 75.1 ms: 1.22x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 57.7 ms: 1.16x faster                                                      |
| nbody                      | 71.9 ms                                                     | 62.4 ms: 1.15x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.84 us: 1.14x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.7 ms: 1.13x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.3 ms: 1.10x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 79.7 ms: 1.10x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.55 ms: 1.08x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.0 ms: 1.08x faster                                                      |
| raytrace                   | 192 ms                                                      | 179 ms: 1.08x faster                                                       |
| scimark_fft                | 184 ms                                                      | 173 ms: 1.06x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.2 ms: 1.06x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 70.5 ms: 1.06x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.1 ms: 1.05x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.1 ms: 1.05x faster                                                      |
| sympy_str                  | 175 ms                                                      | 167 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.46 ms: 1.04x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 56.6 ms: 1.04x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.9 ms: 1.04x faster                                                      |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 76.1 ms: 1.04x faster                                                      |
| async_generators           | 239 ms                                                      | 232 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                     |
| pyflate                    | 295 ms                                                      | 286 ms: 1.03x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.1 ms: 1.03x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.99 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.2 ms: 1.03x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 54.8 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.20 us: 1.01x faster                                                      |
| json                       | 3.05 ms                                                     | 3.02 ms: 1.01x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.67 us: 1.01x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 2.18 ms: 1.01x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                      |
| sympy_expand               | 284 ms                                                      | 288 ms: 1.01x slower                                                       |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 530 ms: 1.03x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.04x slower                                                     |
| fannkuch                   | 247 ms                                                      | 258 ms: 1.05x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.11 ms: 1.07x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.56 ms: 1.10x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 94.4 ms: 1.36x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.11 ms: 1.39x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.31 ms: 1.75x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 321 ns: 5.30x slower                                                       |
| coverage                   | 40.8 ms                                                     | 290 ms: 7.09x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (5): regex_v8, bench_thread_pool, tomli_loads, unpickle_pure_python, pycparser
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250530-3.15.0a0-b367e27/bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown