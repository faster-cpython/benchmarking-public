# Results vs. 3.12.0

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.011x slower
- HPT reliability: 98.57%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 228 ms: 1.05x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.87 sec: 1.73x slower                                                     |
| Geometric mean | (ref)                                                       | 1.34x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 335 ms: 2.30x faster                                                       |
| async_tree_io              | 731 ms                                                      | 358 ms: 2.04x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 149 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 194 ms: 1.89x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 313 ms: 1.60x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 214 ms: 1.59x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.46x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.79x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.5 ms: 1.22x faster                                                      |
| pidigits       | 152 ms                                                      | 136 ms: 1.12x faster                                                       |
| nbody          | 71.9 ms                                                     | 82.5 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.5 ms: 1.05x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 95.2 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 58.4 ms: 1.12x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                      |
| pickle               | 7.43 us                                                     | 7.92 us: 1.07x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.05 us: 1.08x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.15 ms: 1.08x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.2 us: 1.10x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 62.9 ms: 1.13x slower                                                      |
| json_loads           | 13.9 us                                                     | 16.1 us: 1.16x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 44.9 ms: 1.19x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.30 us: 1.20x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 160 us: 1.20x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.94 us: 1.21x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 238 us: 1.22x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.40 sec: 1.75x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.2 ms: 1.30x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                      |
| mako            | 7.09 ms                                                     | 10.1 ms: 1.43x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.31x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.9 ms: 2.78x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 335 ms: 2.30x faster                                                       |
| async_tree_io              | 731 ms                                                      | 358 ms: 2.04x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 149 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 194 ms: 1.89x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 313 ms: 1.60x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 214 ms: 1.59x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 334 ms: 1.46x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.34 us: 1.31x faster                                                      |
| deepcopy                   | 238 us                                                      | 195 us: 1.22x faster                                                       |
| float                      | 56.8 ms                                                     | 46.5 ms: 1.22x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 19.9 us: 1.19x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 413 ms: 1.18x faster                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.30 ms: 1.17x faster                                                      |
| mdp                        | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                     |
| comprehensions             | 14.1 us                                                     | 12.2 us: 1.16x faster                                                      |
| pidigits                   | 152 ms                                                      | 136 ms: 1.12x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 58.4 ms: 1.12x faster                                                      |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.5 ms: 1.05x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.3 ms: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 37.9 ns: 1.01x slower                                                      |
| json                       | 3.05 ms                                                     | 3.08 ms: 1.01x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 62.3 ns: 1.03x slower                                                      |
| generators                 | 22.5 ms                                                     | 23.2 ms: 1.03x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| 2to3                       | 218 ms                                                      | 228 ms: 1.05x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 70.7 ms: 1.06x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 97.5 ms: 1.07x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.92 us: 1.07x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.69 us: 1.07x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.19 us: 1.07x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.05 us: 1.08x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.15 ms: 1.08x slower                                                      |
| pyflate                    | 295 ms                                                      | 319 ms: 1.08x slower                                                       |
| sympy_str                  | 175 ms                                                      | 190 ms: 1.09x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 95.2 ms: 1.09x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 75.3 ms: 1.09x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.1 ms: 1.09x slower                                                      |
| chaos                      | 43.3 ms                                                     | 47.6 ms: 1.10x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 20.2 us: 1.10x slower                                                      |
| async_generators           | 239 ms                                                      | 265 ms: 1.11x slower                                                       |
| pycparser                  | 699 ms                                                      | 775 ms: 1.11x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 65.6 ms: 1.11x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 88.4 ms: 1.12x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 577 ms: 1.12x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 62.9 ms: 1.13x slower                                                      |
| raytrace                   | 192 ms                                                      | 217 ms: 1.13x slower                                                       |
| sympy_expand               | 284 ms                                                      | 321 ms: 1.13x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.45 ms: 1.14x slower                                                      |
| nbody                      | 71.9 ms                                                     | 82.5 ms: 1.15x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.71 ms: 1.15x slower                                                      |
| scimark_fft                | 184 ms                                                      | 212 ms: 1.15x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.77 ms: 1.15x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 72.9 ms: 1.16x slower                                                      |
| json_loads                 | 13.9 us                                                     | 16.1 us: 1.16x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 51.3 ms: 1.17x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 44.9 ms: 1.19x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 89.0 ms: 1.19x slower                                                      |
| django_template            | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.30 us: 1.20x slower                                                      |
| richards                   | 28.4 ms                                                     | 34.1 ms: 1.20x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 160 us: 1.20x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 58.5 ms: 1.21x slower                                                      |
| unpickle                   | 8.18 us                                                     | 9.94 us: 1.21x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 238 us: 1.22x slower                                                       |
| fannkuch                   | 247 ms                                                      | 305 ms: 1.24x slower                                                       |
| richards_super             | 32.1 ms                                                     | 39.9 ms: 1.24x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.19 ms: 1.25x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.07 ms: 1.25x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.2 ms: 1.30x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 998 us: 1.33x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 134 us: 1.41x slower                                                       |
| mako                       | 7.09 ms                                                     | 10.1 ms: 1.43x slower                                                      |
| coverage                   | 40.8 ms                                                     | 67.7 ms: 1.66x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.76 sec: 1.68x slower                                                     |
| docutils                   | 1.66 sec                                                    | 2.87 sec: 1.73x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.40 sec: 1.75x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (3): deepcopy_reduce, go, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250913-3.15.0a0-7168e98-NOGIL/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 98.57% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown