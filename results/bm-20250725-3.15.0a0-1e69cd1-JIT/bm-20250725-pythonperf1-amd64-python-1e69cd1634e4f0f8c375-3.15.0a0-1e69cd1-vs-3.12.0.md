# Results vs. 3.12.0

- fork: python
- ref: 1e69cd1634e4f0f8c375
- machine: windows-amd64
- commit hash: 1e69cd1
- commit date: 2025-07-25
- overall geometric mean: 1.114x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 386 ms: 2.00x faster                                                       |
| async_tree_io              | 731 ms                                                      | 398 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                       |
| async_tree_none            | 291 ms                                                      | 177 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 351 ms: 1.43x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.67x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.4 ms: 1.28x faster                                                      |
| nbody          | 71.9 ms                                                     | 56.7 ms: 1.27x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 80.0 ms: 1.09x faster                                                      |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.64 ms: 1.01x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 105 us: 1.27x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.11 sec: 1.23x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 49.8 ms: 1.12x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.2 ms: 1.07x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 89.2 ms: 1.04x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 207 us: 1.06x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.31 ms: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.9 ms: 1.22x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.7 ms: 1.37x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.40 ms: 1.31x faster                                                      |
| django_template | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 33.5 ms: 2.40x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 386 ms: 2.00x faster                                                       |
| async_tree_io              | 731 ms                                                      | 398 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| mdp                        | 1.37 sec                                                    | 808 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                       |
| async_tree_none            | 291 ms                                                      | 177 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 351 ms: 1.43x faster                                                       |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.0 us: 1.32x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.40 ms: 1.31x faster                                                      |
| float                      | 56.8 ms                                                     | 44.4 ms: 1.28x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 105 us: 1.27x faster                                                       |
| nbody                      | 71.9 ms                                                     | 56.7 ms: 1.27x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.11 sec: 1.23x faster                                                     |
| go                         | 91.6 ms                                                     | 77.0 ms: 1.19x faster                                                      |
| fannkuch                   | 247 ms                                                      | 207 ms: 1.19x faster                                                       |
| scimark_fft                | 184 ms                                                      | 155 ms: 1.19x faster                                                       |
| pyflate                    | 295 ms                                                      | 249 ms: 1.18x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 906 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.84 us: 1.14x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 452 ms: 1.14x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.1 ms: 1.12x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 49.8 ms: 1.12x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 54.3 ns: 1.11x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.10x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.34 ms: 1.09x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 80.0 ms: 1.09x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.3 ms: 1.08x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.2 ms: 1.07x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.2 ms: 1.07x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.97 us: 1.05x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.2 ms: 1.05x faster                                                      |
| raytrace                   | 192 ms                                                      | 183 ms: 1.05x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.3 ms: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 89.2 ms: 1.04x faster                                                      |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.6 ms: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.7 ms: 1.03x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.52 us: 1.03x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.8 ms: 1.02x faster                                                      |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.6 ms: 1.02x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 73.4 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 4.05 ms: 1.01x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 58.2 ms: 1.01x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 77.9 ms: 1.01x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                     |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.01x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.64 ms: 1.01x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.6 ms: 1.02x slower                                                      |
| django_template            | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.32 ms: 1.05x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                      |
| async_generators           | 239 ms                                                      | 253 ms: 1.06x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                                       |
| sympy_expand               | 284 ms                                                      | 304 ms: 1.07x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.08x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.31 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.9 ms: 1.22x slower                                                      |
| coverage                   | 40.8 ms                                                     | 50.5 ms: 1.24x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.7 ms: 1.37x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.24 ms: 1.47x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.82x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (5): pycparser, xml_etree_iterparse, json, spectral_norm, sympy_integrate
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.114x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown