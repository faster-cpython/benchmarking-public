# Results vs. 3.12.0

- fork: python
- ref: 9c7b2af73dee2b997936
- machine: windows-amd64
- commit hash: 9c7b2af
- commit date: 2025-07-21
- overall geometric mean: 1.123x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 396 ms: 1.95x faster                                                       |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 213 ms: 1.73x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 339 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 54.4 ms: 1.32x faster                                                      |
| float          | 56.8 ms                                                     | 43.8 ms: 1.30x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.4 ms: 1.10x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.49 ms: 1.09x faster                                                      |
| regex_dna      | 126 ms                                                      | 116 ms: 1.08x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.4 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 105 us: 1.27x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.10 sec: 1.24x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 49.5 ms: 1.13x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 86.3 ms: 1.08x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.1 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 202 us: 1.04x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.21 ms: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.27 ms: 1.34x faster                                                      |
| django_template | 22.9 ms                                                     | 24.7 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.1 ms: 2.67x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 396 ms: 1.95x faster                                                       |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 213 ms: 1.73x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                       |
| mdp                        | 1.37 sec                                                    | 806 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 339 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.47x faster                                                       |
| deepcopy                   | 238 us                                                      | 172 us: 1.39x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.35x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.27 ms: 1.34x faster                                                      |
| nbody                      | 71.9 ms                                                     | 54.4 ms: 1.32x faster                                                      |
| float                      | 56.8 ms                                                     | 43.8 ms: 1.30x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.4 us: 1.29x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 105 us: 1.27x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.10 sec: 1.24x faster                                                     |
| scimark_fft                | 184 ms                                                      | 150 ms: 1.23x faster                                                       |
| fannkuch                   | 247 ms                                                      | 209 ms: 1.18x faster                                                       |
| go                         | 91.6 ms                                                     | 77.8 ms: 1.18x faster                                                      |
| pyflate                    | 295 ms                                                      | 254 ms: 1.16x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 902 ms: 1.16x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 445 ms: 1.15x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.14x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.26 ms: 1.13x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 49.5 ms: 1.13x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 54.7 ns: 1.11x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 79.4 ms: 1.10x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.7 ms: 1.09x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.49 ms: 1.09x faster                                                      |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.08x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 86.3 ms: 1.08x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.1 ms: 1.08x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 58.5 ms: 1.07x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 69.7 ms: 1.07x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 45.6 ms: 1.06x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.4 ms: 1.06x faster                                                      |
| raytrace                   | 192 ms                                                      | 181 ms: 1.06x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.0 ms: 1.06x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.0 ms: 1.05x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.1 ms: 1.05x faster                                                      |
| pidigits                   | 152 ms                                                      | 146 ms: 1.05x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.0 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.6 ms: 1.02x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.19 us: 1.01x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                     |
| pycparser                  | 699 ms                                                      | 692 ms: 1.01x faster                                                       |
| json                       | 3.05 ms                                                     | 3.07 ms: 1.01x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 79.5 ms: 1.01x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 68.1 ms: 1.02x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                       |
| async_generators           | 239 ms                                                      | 247 ms: 1.03x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 202 us: 1.04x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 61.2 ms: 1.04x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.31 ms: 1.04x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.7 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.09x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.21 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| coverage                   | 40.8 ms                                                     | 51.8 ms: 1.27x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.12 ms: 1.39x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.30 ms: 1.73x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (4): logging_format, hexiom, scimark_monte_carlo, 2to3
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250721-3.15.0a0-9c7b2af-JIT/bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.123x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown