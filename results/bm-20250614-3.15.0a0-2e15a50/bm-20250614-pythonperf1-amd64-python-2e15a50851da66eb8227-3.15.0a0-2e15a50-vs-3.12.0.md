# Results vs. 3.12.0

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.094x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 389 ms: 1.98x faster                                                       |
| async_tree_io              | 731 ms                                                      | 396 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.4 ms: 1.31x faster                                                      |
| nbody          | 71.9 ms                                                     | 61.6 ms: 1.17x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 80.5 ms: 1.09x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.2 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.1 ms: 1.02x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 132 us: 1.01x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.7 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.07x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.20 ms: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.68 ms: 1.06x faster                                                      |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.0 ms: 2.52x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 389 ms: 1.98x faster                                                       |
| async_tree_io              | 731 ms                                                      | 396 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.72x faster                                                       |
| mdp                        | 1.37 sec                                                    | 804 ms: 1.71x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                       |
| deepcopy                   | 238 us                                                      | 171 us: 1.39x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.0 us: 1.31x faster                                                      |
| float                      | 56.8 ms                                                     | 43.4 ms: 1.31x faster                                                      |
| go                         | 91.6 ms                                                     | 74.7 ms: 1.23x faster                                                      |
| nbody                      | 71.9 ms                                                     | 61.6 ms: 1.17x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.14x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                      |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.9 ms: 1.10x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 80.5 ms: 1.09x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.9 ms: 1.09x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 61.8 ms: 1.08x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.5 ms: 1.07x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.68 ms: 1.06x faster                                                      |
| async_generators           | 239 ms                                                      | 227 ms: 1.06x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.2 ms: 1.06x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.9 ms: 1.05x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 74.8 ms: 1.05x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.6 ms: 1.05x faster                                                      |
| raytrace                   | 192 ms                                                      | 183 ms: 1.05x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 87.8 ms: 1.04x faster                                                      |
| sympy_str                  | 175 ms                                                      | 168 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.95 ms: 1.04x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.5 ms: 1.03x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.1 ms: 1.03x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.3 ms: 1.02x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.51 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.1 ms: 1.02x faster                                                      |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                      |
| pyflate                    | 295 ms                                                      | 291 ms: 1.01x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 58.1 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 132 us: 1.01x faster                                                       |
| scimark_fft                | 184 ms                                                      | 183 ms: 1.01x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.14 ms: 1.01x faster                                                      |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 56.7 ms: 1.01x slower                                                      |
| sympy_expand               | 284 ms                                                      | 289 ms: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.85 us: 1.02x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.41 us: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| fannkuch                   | 247 ms                                                      | 253 ms: 1.02x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.05x slower                                                     |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 544 ms: 1.06x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.07x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.20 ms: 1.09x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.61 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.20x slower                                                      |
| coverage                   | 40.8 ms                                                     | 52.5 ms: 1.29x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.15 ms: 1.42x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.34 ms: 1.78x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 320 ns: 5.29x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (2): tomli_loads, pycparser
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.094x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown