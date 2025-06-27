# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: windows-amd64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.108x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.02x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                       |
| async_tree_io              | 731 ms                                                      | 395 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                       |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                      |
| nbody          | 71.9 ms                                                     | 59.5 ms: 1.21x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.2 ms: 1.12x faster                                                      |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 13.6 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 112 us: 1.19x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 50.8 ms: 1.10x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 87.0 ms: 1.07x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 204 us: 1.04x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.38 ms: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.2 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.54 ms: 1.28x faster                                                      |
| django_template | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.0 ms: 2.51x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                       |
| async_tree_io              | 731 ms                                                      | 395 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                       |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.72x faster                                                       |
| mdp                        | 1.37 sec                                                    | 809 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                       |
| deepcopy                   | 238 us                                                      | 171 us: 1.40x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.54 ms: 1.28x faster                                                      |
| float                      | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.8 us: 1.26x faster                                                      |
| go                         | 91.6 ms                                                     | 75.7 ms: 1.21x faster                                                      |
| nbody                      | 71.9 ms                                                     | 59.5 ms: 1.21x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 112 us: 1.19x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| scimark_fft                | 184 ms                                                      | 158 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.82 us: 1.15x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.2 ms: 1.12x faster                                                      |
| pyflate                    | 295 ms                                                      | 264 ms: 1.12x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 60.3 ms: 1.11x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.2 ms: 1.11x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.7 ms: 1.10x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 50.8 ms: 1.10x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.10x faster                                                      |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.7 ms: 1.09x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.37 ms: 1.08x faster                                                      |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 87.0 ms: 1.07x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 74.8 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.3 ms: 1.05x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.7 ms: 1.05x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.2 ms: 1.04x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.6 ms: 1.04x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.3 ms: 1.04x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.7 ms: 1.04x faster                                                      |
| fannkuch                   | 247 ms                                                      | 238 ms: 1.04x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.8 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 521 ms: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 221 ms: 1.02x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.17 ms: 1.02x slower                                                      |
| pycparser                  | 699 ms                                                      | 711 ms: 1.02x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 60.3 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.03x slower                                                     |
| deltablue                  | 2.16 ms                                                     | 2.22 ms: 1.03x slower                                                      |
| async_generators           | 239 ms                                                      | 247 ms: 1.03x slower                                                       |
| sympy_expand               | 284 ms                                                      | 293 ms: 1.03x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| django_template            | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 204 us: 1.04x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.36 ms: 1.06x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.09x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.38 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| coverage                   | 40.8 ms                                                     | 50.7 ms: 1.24x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.2 ms: 1.34x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.19 ms: 1.44x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.35 ms: 1.79x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 325 ns: 5.37x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (3): logging_simple, json, logging_format
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown