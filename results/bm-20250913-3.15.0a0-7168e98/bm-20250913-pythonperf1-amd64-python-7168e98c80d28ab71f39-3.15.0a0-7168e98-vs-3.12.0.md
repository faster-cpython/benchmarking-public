# Results vs. 3.12.0

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.114x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 215 ms: 1.02x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 382 ms: 2.02x faster                                                       |
| async_tree_io              | 731 ms                                                      | 390 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 201 ms: 1.69x faster                                                       |
| async_tree_none            | 291 ms                                                      | 176 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 42.5 ms: 1.34x faster                                                      |
| nbody          | 71.9 ms                                                     | 65.5 ms: 1.10x faster                                                      |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.3 ms: 1.13x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                      |
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 86.3 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.44 ms: 1.05x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 55.1 ms: 1.01x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 134 us: 1.00x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.78 us: 1.01x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.48 us: 1.04x slower                                                      |
| pickle               | 7.43 us                                                     | 7.80 us: 1.05x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.4 us: 1.05x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.27 us: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.5 ms: 1.14x slower                                                      |
| python_startup         | 19.5 ms                                                     | 24.9 ms: 1.28x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.67 ms: 1.06x faster                                                      |
| django_template | 22.9 ms                                                     | 25.2 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.8 ms: 2.80x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 382 ms: 2.02x faster                                                       |
| async_tree_io              | 731 ms                                                      | 390 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                       |
| mdp                        | 1.37 sec                                                    | 800 ms: 1.72x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 201 ms: 1.69x faster                                                       |
| async_tree_none            | 291 ms                                                      | 176 ms: 1.66x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.39 sec: 1.51x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| deepcopy                   | 238 us                                                      | 166 us: 1.43x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 16.6 us: 1.43x faster                                                      |
| float                      | 56.8 ms                                                     | 42.5 ms: 1.34x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.9 us: 1.30x faster                                                      |
| go                         | 91.6 ms                                                     | 75.5 ms: 1.21x faster                                                      |
| generators                 | 22.5 ms                                                     | 18.9 ms: 1.19x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.77 us: 1.18x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.14x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 77.3 ms: 1.13x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 39.3 ms: 1.13x faster                                                      |
| nbody                      | 71.9 ms                                                     | 65.5 ms: 1.10x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.2 ns: 1.10x faster                                                      |
| raytrace                   | 192 ms                                                      | 177 ms: 1.09x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.5 ms: 1.08x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 86.3 ms: 1.08x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 975 ms: 1.07x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 62.5 ms: 1.07x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 480 ms: 1.07x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.67 ms: 1.06x faster                                                      |
| sympy_str                  | 175 ms                                                      | 165 ms: 1.06x faster                                                       |
| chaos                      | 43.3 ms                                                     | 40.9 ms: 1.06x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.8 ms: 1.06x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 74.5 ms: 1.06x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.06x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                      |
| json                       | 3.05 ms                                                     | 2.89 ms: 1.05x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.98 us: 1.05x faster                                                      |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.44 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| pyflate                    | 295 ms                                                      | 282 ms: 1.05x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.46 us: 1.04x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 36.1 ns: 1.04x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.1 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.6 ms: 1.03x faster                                                      |
| scimark_fft                | 184 ms                                                      | 180 ms: 1.03x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 836 us: 1.02x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| async_generators           | 239 ms                                                      | 234 ms: 1.02x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 61.5 ms: 1.02x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.51 ms: 1.02x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                     |
| hexiom                     | 4.10 ms                                                     | 4.04 ms: 1.02x faster                                                      |
| 2to3                       | 218 ms                                                      | 215 ms: 1.02x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 55.1 ms: 1.01x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 58.3 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 134 us: 1.00x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.78 us: 1.01x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.20 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.48 us: 1.04x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.80 us: 1.05x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.4 us: 1.05x slower                                                      |
| fannkuch                   | 247 ms                                                      | 261 ms: 1.06x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 101 us: 1.06x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.2 ms: 1.10x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.5 ms: 1.14x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.27 us: 1.16x slower                                                      |
| coverage                   | 40.8 ms                                                     | 48.8 ms: 1.20x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 87.8 ms: 1.27x slower                                                      |
| python_startup             | 19.5 ms                                                     | 24.9 ms: 1.28x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.13 ms: 1.40x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.24 ms: 1.65x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (4): sympy_expand, telco, pycparser, asyncio_tcp
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.114x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown