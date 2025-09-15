# Results vs. 3.12.0

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.156x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 214 ms: 1.02x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 378 ms: 2.04x faster                                                       |
| async_tree_io              | 731 ms                                                      | 382 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.73x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 165 ms: 1.72x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 332 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.72x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                      |
| nbody          | 71.9 ms                                                     | 55.5 ms: 1.29x faster                                                      |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 76.8 ms: 1.14x faster                                                      |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 105 us: 1.27x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.08 sec: 1.26x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 84.7 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.8 ms: 1.05x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.51 ms: 1.03x faster                                                      |
| unpickle_list        | 2.75 us                                                     | 2.69 us: 1.02x faster                                                      |
| json_loads           | 13.9 us                                                     | 13.8 us: 1.01x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 198 us: 1.01x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.41 us: 1.03x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.0 us: 1.03x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.16 us: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.6 ms: 1.14x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.0 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.25 ms: 1.35x faster                                                      |
| django_template | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.9 ms: 2.79x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 378 ms: 2.04x faster                                                       |
| async_tree_io              | 731 ms                                                      | 382 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| mdp                        | 1.37 sec                                                    | 791 ms: 1.73x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.73x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 165 ms: 1.72x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.39 sec: 1.51x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 332 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| deepcopy                   | 238 us                                                      | 164 us: 1.45x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 16.9 us: 1.40x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.25 ms: 1.35x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.35x faster                                                      |
| float                      | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                      |
| nbody                      | 71.9 ms                                                     | 55.5 ms: 1.29x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 105 us: 1.27x faster                                                       |
| richards                   | 28.4 ms                                                     | 22.3 ms: 1.27x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.08 sec: 1.26x faster                                                     |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.25x faster                                                       |
| go                         | 91.6 ms                                                     | 74.3 ms: 1.23x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 422 ms: 1.22x faster                                                       |
| richards_super             | 32.1 ms                                                     | 26.5 ms: 1.21x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 867 ms: 1.21x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.77 us: 1.18x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                      |
| pyflate                    | 295 ms                                                      | 252 ms: 1.17x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.51 us: 1.16x faster                                                      |
| fannkuch                   | 247 ms                                                      | 212 ms: 1.16x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.1 ms: 1.15x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.23 ms: 1.15x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 76.8 ms: 1.14x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 53.2 ns: 1.14x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 39.5 ms: 1.12x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                      |
| raytrace                   | 192 ms                                                      | 174 ms: 1.10x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 84.7 ms: 1.10x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 61.2 ms: 1.09x faster                                                      |
| telco                      | 4.13 ms                                                     | 3.80 ms: 1.09x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 44.7 ms: 1.08x faster                                                      |
| json                       | 3.05 ms                                                     | 2.83 ms: 1.08x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 85.4 ms: 1.07x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 58.8 ms: 1.07x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.7 ms: 1.07x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 74.4 ms: 1.06x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.8 ms: 1.05x faster                                                      |
| sympy_str                  | 175 ms                                                      | 166 ms: 1.05x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.97 us: 1.05x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.41 us: 1.05x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.4 ms: 1.05x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 36.0 ns: 1.04x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 56.8 ms: 1.04x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.51 ms: 1.03x faster                                                      |
| unpickle_list              | 2.75 us                                                     | 2.69 us: 1.02x faster                                                      |
| pycparser                  | 699 ms                                                      | 685 ms: 1.02x faster                                                       |
| 2to3                       | 218 ms                                                      | 214 ms: 1.02x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 4.02 ms: 1.02x faster                                                      |
| json_loads                 | 13.9 us                                                     | 13.8 us: 1.01x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 198 us: 1.01x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.6 ms: 1.02x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.41 us: 1.03x slower                                                      |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.0 us: 1.03x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                      |
| async_generators           | 239 ms                                                      | 251 ms: 1.05x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 100 us: 1.05x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.16 us: 1.12x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.6 ms: 1.14x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.3 ms: 1.21x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 88.0 ms: 1.27x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.0 ms: 1.29x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.06 ms: 1.35x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.66x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (5): deltablue, regex_v8, pickle, bench_thread_pool, asyncio_tcp
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.156x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown