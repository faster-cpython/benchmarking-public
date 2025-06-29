# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.623x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 216 ms: 1.01x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 402 ms: 1.92x faster                                                       |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.66x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.4 ms: 1.31x faster                                                      |
| nbody          | 71.9 ms                                                     | 59.7 ms: 1.21x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 70.6 ms: 1.24x faster                                                      |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.66 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 110 us: 1.21x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 52.0 ms: 1.07x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 88.0 ms: 1.06x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 207 us: 1.06x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.21 ms: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.6 ms: 1.21x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.43 ms: 1.31x faster                                                      |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pprint_pformat             | 1.05 sec                                                    | 995 ns: 1050741.53x faster                                                 |
| pprint_safe_repr           | 513 ms                                                      | 579 ns: 885549.39x faster                                                  |
| pathlib                    | 80.5 ms                                                     | 31.8 ms: 2.53x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 402 ms: 1.92x faster                                                       |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                       |
| mdp                        | 1.37 sec                                                    | 802 ms: 1.71x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 172 ms: 1.66x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                       |
| deepcopy                   | 238 us                                                      | 168 us: 1.41x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.7 us: 1.34x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.8 us: 1.31x faster                                                      |
| float                      | 56.8 ms                                                     | 43.4 ms: 1.31x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.43 ms: 1.31x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 70.6 ms: 1.24x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 110 us: 1.21x faster                                                       |
| nbody                      | 71.9 ms                                                     | 59.7 ms: 1.21x faster                                                      |
| go                         | 91.6 ms                                                     | 76.4 ms: 1.20x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                     |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.17x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                      |
| scimark_fft                | 184 ms                                                      | 161 ms: 1.15x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                      |
| pyflate                    | 295 ms                                                      | 263 ms: 1.12x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 60.8 ms: 1.10x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.4 ms: 1.10x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.6 ms: 1.09x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.37 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.7 ms: 1.07x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 52.0 ms: 1.07x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 58.9 ms: 1.07x faster                                                      |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.0 ms: 1.06x faster                                                      |
| raytrace                   | 192 ms                                                      | 183 ms: 1.05x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 75.0 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.6 ms: 1.04x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 56.8 ms: 1.04x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.03x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                       |
| json                       | 3.05 ms                                                     | 2.97 ms: 1.03x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.19 us: 1.01x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.06 ms: 1.01x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.66 us: 1.01x faster                                                      |
| 2to3                       | 218 ms                                                      | 216 ms: 1.01x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| fannkuch                   | 247 ms                                                      | 250 ms: 1.01x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.02x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.66 ms: 1.03x slower                                                      |
| async_generators           | 239 ms                                                      | 246 ms: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 722 ms: 1.03x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| sympy_expand               | 284 ms                                                      | 296 ms: 1.04x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.35 ms: 1.05x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.21 ms: 1.09x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.10x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.4 ms: 1.19x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.6 ms: 1.21x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.0 ms: 1.34x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.17 ms: 1.43x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.34 ms: 1.78x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 316 ns: 5.22x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.57x faster                                                               |

Benchmark hidden because not significant (1): meteor_contest
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.623x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown