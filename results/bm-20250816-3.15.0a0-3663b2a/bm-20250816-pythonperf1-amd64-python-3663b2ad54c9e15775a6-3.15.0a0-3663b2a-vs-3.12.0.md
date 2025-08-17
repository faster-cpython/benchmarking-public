# Results vs. 3.12.0

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.107x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 215 ms: 1.01x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 380 ms: 2.03x faster                                                       |
| async_tree_io              | 731 ms                                                      | 388 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.78x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 165 ms: 1.72x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 201 ms: 1.69x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 327 ms: 1.50x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.72x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.2 ms: 1.28x faster                                                      |
| nbody          | 71.9 ms                                                     | 63.6 ms: 1.13x faster                                                      |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 87.0 ms: 1.07x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.43 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 132 us: 1.01x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.3 ms: 1.01x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                     |
| unpickle_list        | 2.75 us                                                     | 2.82 us: 1.03x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.39 us: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.2 ms: 1.04x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.7 us: 1.07x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.09x slower                                                       |
| pickle               | 7.43 us                                                     | 8.25 us: 1.11x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.38 us: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.3 ms: 1.30x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.64 ms: 1.07x faster                                                      |
| django_template | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.7 ms: 2.80x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 380 ms: 2.03x faster                                                       |
| async_tree_io              | 731 ms                                                      | 388 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.78x faster                                                       |
| mdp                        | 1.37 sec                                                    | 794 ms: 1.73x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 165 ms: 1.72x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 201 ms: 1.69x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.25 sec: 1.68x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 327 ms: 1.50x faster                                                       |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.9 us: 1.30x faster                                                      |
| float                      | 56.8 ms                                                     | 44.2 ms: 1.28x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 380 ms: 1.28x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.7 us: 1.27x faster                                                      |
| go                         | 91.6 ms                                                     | 75.3 ms: 1.22x faster                                                      |
| generators                 | 22.5 ms                                                     | 18.9 ms: 1.19x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.14x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.14x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 39.0 ms: 1.13x faster                                                      |
| nbody                      | 71.9 ms                                                     | 63.6 ms: 1.13x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.5 ms: 1.11x faster                                                      |
| raytrace                   | 192 ms                                                      | 174 ms: 1.11x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 55.0 ns: 1.10x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.5 ms: 1.10x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 87.0 ms: 1.07x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.64 ms: 1.07x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 85.8 ms: 1.07x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.2 ms: 1.07x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.93 us: 1.06x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.8 ms: 1.06x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 55.8 ms: 1.06x faster                                                      |
| sympy_str                  | 175 ms                                                      | 166 ms: 1.06x faster                                                       |
| async_generators           | 239 ms                                                      | 227 ms: 1.05x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 70.8 ms: 1.05x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.37 us: 1.05x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 994 ms: 1.05x faster                                                       |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 489 ms: 1.05x faster                                                       |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.43 ms: 1.05x faster                                                      |
| scimark_fft                | 184 ms                                                      | 177 ms: 1.04x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| spectral_norm              | 66.9 ms                                                     | 64.5 ms: 1.04x faster                                                      |
| json                       | 3.05 ms                                                     | 2.95 ms: 1.03x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.99 ms: 1.03x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.1 ms: 1.03x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 835 us: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 77.0 ms: 1.02x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.7 ms: 1.02x faster                                                      |
| 2to3                       | 218 ms                                                      | 215 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.53 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 132 us: 1.01x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.18 ms: 1.01x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 56.3 ms: 1.01x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                     |
| unpickle_list              | 2.75 us                                                     | 2.82 us: 1.03x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.39 us: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| pycparser                  | 699 ms                                                      | 723 ms: 1.03x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.2 ms: 1.04x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.38 ms: 1.06x slower                                                      |
| fannkuch                   | 247 ms                                                      | 263 ms: 1.07x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.7 us: 1.07x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 40.5 ns: 1.08x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.09x slower                                                       |
| pickle                     | 7.43 us                                                     | 8.25 us: 1.11x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.11x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.38 us: 1.19x slower                                                      |
| coverage                   | 40.8 ms                                                     | 51.0 ms: 1.25x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.3 ms: 1.30x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 92.2 ms: 1.33x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.13 ms: 1.40x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.28 ms: 1.71x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (4): regex_dna, coroutines, pyflate, sympy_expand
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.107x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown