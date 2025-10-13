# Results vs. 3.12.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.103x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 216 ms: 1.01x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.59 sec: 1.05x faster                                                     |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 385 ms: 2.01x faster                                                       |
| async_tree_io              | 731 ms                                                      | 384 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 206 ms: 1.78x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.71x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.2 ms: 1.26x faster                                                      |
| nbody          | 71.9 ms                                                     | 67.4 ms: 1.07x faster                                                      |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 80.4 ms: 1.09x faster                                                      |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 87.5 ms: 1.06x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.51 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 135 us: 1.02x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| unpickle_list        | 2.75 us                                                     | 2.83 us: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.2 ms: 1.04x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.54 us: 1.04x slower                                                      |
| pickle               | 7.43 us                                                     | 7.95 us: 1.07x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 214 us: 1.09x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 20.5 us: 1.12x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.29 us: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.8 ms: 1.16x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.3 ms: 1.30x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.67 ms: 1.06x faster                                                      |
| django_template | 22.9 ms                                                     | 23.8 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.1 ms: 2.76x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 385 ms: 2.01x faster                                                       |
| async_tree_io              | 731 ms                                                      | 384 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 206 ms: 1.78x faster                                                       |
| mdp                        | 1.37 sec                                                    | 790 ms: 1.74x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 167 ms: 1.70x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.24 sec: 1.69x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| deepcopy                   | 238 us                                                      | 164 us: 1.45x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.4 us: 1.36x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 372 ms: 1.31x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.1 us: 1.27x faster                                                      |
| float                      | 56.8 ms                                                     | 45.2 ms: 1.26x faster                                                      |
| go                         | 91.6 ms                                                     | 76.8 ms: 1.19x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.79 us: 1.17x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.15x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 38.5 ms: 1.15x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.14x faster                                                      |
| raytrace                   | 192 ms                                                      | 176 ms: 1.09x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 80.4 ms: 1.09x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 56.1 ns: 1.08x faster                                                      |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 85.2 ms: 1.07x faster                                                      |
| nbody                      | 71.9 ms                                                     | 67.4 ms: 1.07x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.1 ms: 1.06x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 87.5 ms: 1.06x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.67 ms: 1.06x faster                                                      |
| scimark_fft                | 184 ms                                                      | 174 ms: 1.06x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.2 ms: 1.06x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.96 us: 1.05x faster                                                      |
| sympy_str                  | 175 ms                                                      | 166 ms: 1.05x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 35.7 ns: 1.05x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.59 sec: 1.05x faster                                                     |
| pprint_safe_repr           | 513 ms                                                      | 490 ms: 1.05x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.42 us: 1.05x faster                                                      |
| chaos                      | 43.3 ms                                                     | 41.5 ms: 1.05x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.00 sec: 1.04x faster                                                     |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                      |
| pyflate                    | 295 ms                                                      | 283 ms: 1.04x faster                                                       |
| async_generators           | 239 ms                                                      | 230 ms: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.51 ms: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.3 ms: 1.03x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.49 ms: 1.03x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.7 ms: 1.02x faster                                                      |
| richards_super             | 32.1 ms                                                     | 31.3 ms: 1.02x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 77.1 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| pycparser                  | 699 ms                                                      | 687 ms: 1.02x faster                                                       |
| sympy_expand               | 284 ms                                                      | 281 ms: 1.01x faster                                                       |
| 2to3                       | 218 ms                                                      | 216 ms: 1.01x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 66.6 ms: 1.01x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 63.4 ms: 1.01x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.14 ms: 1.01x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 135 us: 1.02x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.20 ms: 1.02x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| unpickle_list              | 2.75 us                                                     | 2.83 us: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| django_template            | 22.9 ms                                                     | 23.8 ms: 1.04x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 39.2 ms: 1.04x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.54 us: 1.04x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.07x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.95 us: 1.07x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 214 us: 1.09x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.5 us: 1.12x slower                                                      |
| fannkuch                   | 247 ms                                                      | 277 ms: 1.12x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.8 ms: 1.16x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.29 us: 1.16x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.4 ms: 1.21x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 88.8 ms: 1.28x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.3 ms: 1.30x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.07 ms: 1.36x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.67x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (3): bench_thread_pool, crypto_pyaes, scimark_lu
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.103x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown