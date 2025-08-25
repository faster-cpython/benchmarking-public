# Results vs. 3.12.0

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.113x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                                       |
| async_tree_io              | 731 ms                                                      | 384 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 204 ms: 1.80x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 201 ms: 1.69x faster                                                       |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.68x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.71x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.5 ms: 1.31x faster                                                      |
| nbody          | 71.9 ms                                                     | 62.8 ms: 1.14x faster                                                      |
| pidigits       | 152 ms                                                      | 143 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.1 ms: 1.12x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.52 ms: 1.06x faster                                                      |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 5.70 ms                                                     | 5.36 ms: 1.06x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 87.6 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 133 us: 1.00x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 38.4 ms: 1.02x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.80 us: 1.02x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.37 us: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 20.0 us: 1.08x slower                                                      |
| pickle               | 7.43 us                                                     | 8.21 us: 1.10x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.35 us: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.5 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.59 ms: 1.08x faster                                                      |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.4 ms: 2.64x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                                       |
| async_tree_io              | 731 ms                                                      | 384 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 204 ms: 1.80x faster                                                       |
| mdp                        | 1.37 sec                                                    | 800 ms: 1.71x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.24 sec: 1.69x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 201 ms: 1.69x faster                                                       |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.68x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| deepcopy                   | 238 us                                                      | 171 us: 1.40x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.9 us: 1.32x faster                                                      |
| float                      | 56.8 ms                                                     | 43.5 ms: 1.31x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.28x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 381 ms: 1.28x faster                                                       |
| go                         | 91.6 ms                                                     | 76.5 ms: 1.20x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.14x faster                                                      |
| nbody                      | 71.9 ms                                                     | 62.8 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.13x faster                                                      |
| raytrace                   | 192 ms                                                      | 172 ms: 1.12x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 78.1 ms: 1.12x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.1 ms: 1.12x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.0 ms: 1.11x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 53.6 ms: 1.10x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.2 ns: 1.10x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 34.5 ns: 1.09x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.4 ms: 1.08x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.59 ms: 1.08x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 73.5 ms: 1.07x faster                                                      |
| async_generators           | 239 ms                                                      | 224 ms: 1.07x faster                                                       |
| chaos                      | 43.3 ms                                                     | 40.6 ms: 1.07x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 62.7 ms: 1.07x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.1 ms: 1.07x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.36 ms: 1.06x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 87.6 ms: 1.06x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.52 ms: 1.06x faster                                                      |
| pidigits                   | 152 ms                                                      | 143 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 485 ms: 1.06x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 991 ms: 1.06x faster                                                       |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                                      |
| scimark_fft                | 184 ms                                                      | 176 ms: 1.05x faster                                                       |
| sympy_str                  | 175 ms                                                      | 167 ms: 1.05x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 87.2 ms: 1.05x faster                                                      |
| json                       | 3.05 ms                                                     | 2.91 ms: 1.05x faster                                                      |
| pyflate                    | 295 ms                                                      | 282 ms: 1.04x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.9 ms: 1.04x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.06 us: 1.04x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.48 ms: 1.03x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.53 us: 1.03x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.0 ms: 1.03x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.1 ms: 1.03x faster                                                      |
| sympy_expand               | 284 ms                                                      | 278 ms: 1.02x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 840 us: 1.02x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| hexiom                     | 4.10 ms                                                     | 4.04 ms: 1.02x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 133 us: 1.00x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.18 ms: 1.01x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 38.4 ms: 1.02x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.80 us: 1.02x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.37 us: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| fannkuch                   | 247 ms                                                      | 256 ms: 1.04x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.0 us: 1.08x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.09x slower                                                       |
| pickle                     | 7.43 us                                                     | 8.21 us: 1.10x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.35 us: 1.19x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| coverage                   | 40.8 ms                                                     | 50.5 ms: 1.24x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.5 ms: 1.31x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 94.3 ms: 1.36x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.10 ms: 1.38x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.29 ms: 1.72x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (6): xml_etree_generate, 2to3, tomli_loads, coroutines, telco, pycparser
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.113x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown