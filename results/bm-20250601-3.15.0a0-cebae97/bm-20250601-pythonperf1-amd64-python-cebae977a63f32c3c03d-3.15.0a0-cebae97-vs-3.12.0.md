# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.104x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 395 ms: 1.95x faster                                                       |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.73x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.67x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                      |
| nbody          | 71.9 ms                                                     | 60.9 ms: 1.18x faster                                                      |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 79.6 ms: 1.10x faster                                                      |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.1 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.1 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.4 ms: 1.03x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.02x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 134 us: 1.01x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.08x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.23 ms: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.5 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.38 ms: 1.11x faster                                                      |
| django_template | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.9 ms: 2.52x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 395 ms: 1.95x faster                                                       |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.73x faster                                                       |
| mdp                        | 1.37 sec                                                    | 795 ms: 1.73x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.67x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.49x faster                                                       |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.3 us: 1.37x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                                      |
| float                      | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                      |
| go                         | 91.6 ms                                                     | 75.7 ms: 1.21x faster                                                      |
| nbody                      | 71.9 ms                                                     | 60.9 ms: 1.18x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 57.0 ms: 1.17x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.84 us: 1.14x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.38 ms: 1.11x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.5 ms: 1.11x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.3 ms: 1.10x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 79.6 ms: 1.10x faster                                                      |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.1 ms: 1.09x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 72.9 ms: 1.08x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.2 ms: 1.08x faster                                                      |
| scimark_fft                | 184 ms                                                      | 172 ms: 1.07x faster                                                       |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                       |
| pyflate                    | 295 ms                                                      | 278 ms: 1.06x faster                                                       |
| async_generators           | 239 ms                                                      | 227 ms: 1.06x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.1 ms: 1.06x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.2 ms: 1.05x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.6 ms: 1.04x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.7 ms: 1.04x faster                                                      |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.04x faster                                                       |
| richards_super             | 32.1 ms                                                     | 30.9 ms: 1.04x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.4 ms: 1.04x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.6 ms: 1.04x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 57.1 ms: 1.03x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.4 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.49 ms: 1.03x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| hexiom                     | 4.10 ms                                                     | 4.00 ms: 1.02x faster                                                      |
| json                       | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.02x faster                                                     |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 134 us: 1.01x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.02x slower                                                      |
| sympy_expand               | 284 ms                                                      | 289 ms: 1.02x slower                                                       |
| fannkuch                   | 247 ms                                                      | 255 ms: 1.03x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 533 ms: 1.04x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.04x slower                                                     |
| typing_runtime_protocols   | 95.1 us                                                     | 100 us: 1.05x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.08x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.23 ms: 1.09x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.65 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.4 ms: 1.21x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.5 ms: 1.31x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.41x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.76x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 320 ns: 5.29x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (4): logging_format, logging_simple, xml_etree_generate, pycparser
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.104x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown