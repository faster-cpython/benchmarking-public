# Results vs. 3.12.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.59 sec: 1.05x faster                                                     |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 379 ms: 2.03x faster                                                       |
| async_tree_io              | 731 ms                                                      | 382 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 164 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 200 ms: 1.69x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 327 ms: 1.50x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.72x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.1 ms: 1.32x faster                                                      |
| nbody          | 71.9 ms                                                     | 65.2 ms: 1.10x faster                                                      |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.4 ms: 1.12x faster                                                      |
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 5.70 ms                                                     | 5.27 ms: 1.08x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 86.8 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.5 ms: 1.01x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 132 us: 1.01x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.01x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.81 us: 1.02x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 38.8 ms: 1.03x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.5 ms: 1.03x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.60 us: 1.05x slower                                                      |
| pickle               | 7.43 us                                                     | 7.82 us: 1.05x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.06x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.6 us: 1.07x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.33 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.53 ms: 1.09x faster                                                      |
| django_template | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.1 ms: 2.50x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 379 ms: 2.03x faster                                                       |
| async_tree_io              | 731 ms                                                      | 382 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 164 ms: 1.74x faster                                                       |
| mdp                        | 1.37 sec                                                    | 790 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 200 ms: 1.69x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.39 sec: 1.51x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 327 ms: 1.50x faster                                                       |
| deepcopy                   | 238 us                                                      | 167 us: 1.43x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.8 us: 1.33x faster                                                      |
| float                      | 56.8 ms                                                     | 43.1 ms: 1.32x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.8 us: 1.31x faster                                                      |
| go                         | 91.6 ms                                                     | 75.6 ms: 1.21x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.77 us: 1.18x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.14x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.14x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 39.1 ms: 1.13x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.9 ms: 1.12x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.4 ms: 1.12x faster                                                      |
| nbody                      | 71.9 ms                                                     | 65.2 ms: 1.10x faster                                                      |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.7 ms: 1.09x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.53 ms: 1.09x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.1 ms: 1.09x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.27 ms: 1.08x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 56.0 ns: 1.08x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 85.2 ms: 1.07x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 86.8 ms: 1.07x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.1 ms: 1.07x faster                                                      |
| sympy_str                  | 175 ms                                                      | 165 ms: 1.06x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.2 ms: 1.06x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 988 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 487 ms: 1.05x faster                                                       |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 55.9 ms: 1.05x faster                                                      |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.99 us: 1.05x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.59 sec: 1.05x faster                                                     |
| logging_format             | 6.72 us                                                     | 6.41 us: 1.05x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.5 ms: 1.04x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 75.7 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.46 ms: 1.04x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.97 ms: 1.03x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.9 ms: 1.03x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.8 ms: 1.03x faster                                                      |
| json                       | 3.05 ms                                                     | 2.96 ms: 1.03x faster                                                      |
| pyflate                    | 295 ms                                                      | 289 ms: 1.02x faster                                                       |
| sympy_expand               | 284 ms                                                      | 279 ms: 1.02x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 66.0 ms: 1.01x faster                                                      |
| pycparser                  | 699 ms                                                      | 689 ms: 1.01x faster                                                       |
| scimark_fft                | 184 ms                                                      | 182 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.5 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 132 us: 1.01x faster                                                       |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.01x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.01x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.20 ms: 1.02x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.81 us: 1.02x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 38.8 ms: 1.03x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.5 ms: 1.03x slower                                                      |
| django_template            | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 509 ms: 1.04x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.60 us: 1.05x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.82 us: 1.05x slower                                                      |
| fannkuch                   | 247 ms                                                      | 262 ms: 1.06x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.06x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.6 us: 1.07x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.07x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.47 ms: 1.08x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.33 us: 1.18x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.5 ms: 1.21x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 94.9 ms: 1.37x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.11 ms: 1.38x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.30 ms: 1.73x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (5): unpack_sequence, tomli_loads, raytrace, 2to3, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown