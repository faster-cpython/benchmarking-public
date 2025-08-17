# Results vs. 3.12.0

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.139x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 380 ms: 2.03x faster                                                       |
| async_tree_io              | 731 ms                                                      | 382 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                       |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 201 ms: 1.69x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.71x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                      |
| nbody          | 71.9 ms                                                     | 57.5 ms: 1.25x faster                                                      |
| pidigits       | 152 ms                                                      | 143 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.0 ms: 1.12x faster                                                      |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 104 us: 1.28x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 50.0 ms: 1.12x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 85.3 ms: 1.09x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.3 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.8 ms: 1.05x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.42 ms: 1.05x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| pickle               | 7.43 us                                                     | 7.60 us: 1.02x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 200 us: 1.02x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.43 us: 1.03x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.2 us: 1.04x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.23 us: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.1 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.28 ms: 1.34x faster                                                      |
| django_template | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.2 ms: 2.75x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 380 ms: 2.03x faster                                                       |
| async_tree_io              | 731 ms                                                      | 382 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                       |
| mdp                        | 1.37 sec                                                    | 809 ms: 1.70x faster                                                       |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 201 ms: 1.69x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.39 sec: 1.51x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.28 ms: 1.34x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.34x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.0 us: 1.32x faster                                                      |
| float                      | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 104 us: 1.28x faster                                                       |
| nbody                      | 71.9 ms                                                     | 57.5 ms: 1.25x faster                                                      |
| scimark_fft                | 184 ms                                                      | 149 ms: 1.24x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                                     |
| go                         | 91.6 ms                                                     | 76.7 ms: 1.19x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 884 ms: 1.18x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 435 ms: 1.18x faster                                                       |
| fannkuch                   | 247 ms                                                      | 211 ms: 1.17x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.52 us: 1.16x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.82 us: 1.15x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 32.7 ns: 1.15x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.24 ms: 1.14x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 39.0 ms: 1.13x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.0 ms: 1.12x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 50.0 ms: 1.12x faster                                                      |
| pyflate                    | 295 ms                                                      | 265 ms: 1.11x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 54.9 ns: 1.10x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.7 ms: 1.09x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 85.3 ms: 1.09x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.3 ms: 1.09x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 69.1 ms: 1.08x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 44.9 ms: 1.08x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| raytrace                   | 192 ms                                                      | 179 ms: 1.07x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 85.6 ms: 1.07x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.3 ms: 1.07x faster                                                      |
| pidigits                   | 152 ms                                                      | 143 ms: 1.06x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 63.1 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.8 ms: 1.05x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.42 ms: 1.05x faster                                                      |
| json                       | 3.05 ms                                                     | 2.90 ms: 1.05x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.6 ms: 1.05x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                                      |
| telco                      | 4.13 ms                                                     | 3.96 ms: 1.04x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.45 us: 1.04x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 829 us: 1.03x faster                                                       |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.9 ms: 1.03x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.99 ms: 1.03x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| logging_simple             | 6.28 us                                                     | 6.15 us: 1.02x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 57.7 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 79.6 ms: 1.01x slower                                                      |
| sympy_expand               | 284 ms                                                      | 288 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.60 us: 1.02x slower                                                      |
| async_generators           | 239 ms                                                      | 245 ms: 1.02x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 200 us: 1.02x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.43 us: 1.03x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.2 us: 1.04x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.23 us: 1.14x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                      |
| coverage                   | 40.8 ms                                                     | 48.4 ms: 1.19x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.1 ms: 1.29x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 92.4 ms: 1.34x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.17 ms: 1.42x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.29 ms: 1.72x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (5): pycparser, 2to3, coroutines, unpickle_list, asyncio_tcp
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.139x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown