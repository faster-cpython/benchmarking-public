# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.105x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 385 ms: 2.00x faster                                                       |
| async_tree_io              | 731 ms                                                      | 395 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                       |
| async_tree_none            | 291 ms                                                      | 167 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 339 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.2 ms: 1.32x faster                                                      |
| nbody          | 71.9 ms                                                     | 60.5 ms: 1.19x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.7 ms: 1.11x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                      |
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.3 ms: 1.05x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 131 us: 1.02x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 38.5 ms: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 206 us: 1.05x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.16 ms: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.6 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.57 ms: 1.08x faster                                                      |
| django_template | 22.9 ms                                                     | 23.6 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.8 ms: 2.53x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 385 ms: 2.00x faster                                                       |
| async_tree_io              | 731 ms                                                      | 395 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                       |
| async_tree_none            | 291 ms                                                      | 167 ms: 1.75x faster                                                       |
| mdp                        | 1.37 sec                                                    | 794 ms: 1.73x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 339 ms: 1.48x faster                                                       |
| deepcopy                   | 238 us                                                      | 168 us: 1.42x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.34x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 17.8 us: 1.33x faster                                                      |
| float                      | 56.8 ms                                                     | 43.2 ms: 1.32x faster                                                      |
| go                         | 91.6 ms                                                     | 74.0 ms: 1.24x faster                                                      |
| nbody                      | 71.9 ms                                                     | 60.5 ms: 1.19x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.15x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 59.7 ms: 1.12x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.7 ms: 1.11x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.3 ms: 1.10x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.0 ms: 1.09x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.57 ms: 1.08x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.2 ms: 1.07x faster                                                      |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                      |
| scimark_fft                | 184 ms                                                      | 173 ms: 1.07x faster                                                       |
| richards                   | 28.4 ms                                                     | 26.6 ms: 1.07x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.2 ms: 1.06x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 74.3 ms: 1.06x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 88.3 ms: 1.05x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.91 ms: 1.05x faster                                                      |
| pyflate                    | 295 ms                                                      | 281 ms: 1.05x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 87.6 ms: 1.04x faster                                                      |
| sympy_str                  | 175 ms                                                      | 168 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| async_generators           | 239 ms                                                      | 230 ms: 1.04x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 71.8 ms: 1.04x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.7 ms: 1.04x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.5 ms: 1.04x faster                                                      |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.48 ms: 1.03x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                     |
| scimark_lu                 | 58.9 ms                                                     | 57.7 ms: 1.02x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 131 us: 1.02x faster                                                       |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                     |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 2.14 ms: 1.01x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                      |
| fannkuch                   | 247 ms                                                      | 247 ms: 1.00x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.32 us: 1.01x slower                                                      |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| sympy_expand               | 284 ms                                                      | 287 ms: 1.01x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 38.5 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.02x slower                                                     |
| django_template            | 22.9 ms                                                     | 23.6 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 530 ms: 1.03x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 206 us: 1.05x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 101 us: 1.06x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.16 ms: 1.08x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.52 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| coverage                   | 40.8 ms                                                     | 50.6 ms: 1.24x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.6 ms: 1.32x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.16 ms: 1.42x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.31 ms: 1.75x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 318 ns: 5.26x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_iterparse, pycparser, logging_format
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.105x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown