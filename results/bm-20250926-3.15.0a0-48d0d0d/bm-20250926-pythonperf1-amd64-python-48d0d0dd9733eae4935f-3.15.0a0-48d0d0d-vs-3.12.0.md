# Results vs. 3.12.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.119x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 215 ms: 1.01x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.58 sec: 1.05x faster                                                     |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 383 ms: 2.01x faster                                                       |
| async_tree_io              | 731 ms                                                      | 380 ms: 1.93x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 206 ms: 1.78x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 201 ms: 1.69x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.72x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                      |
| nbody          | 71.9 ms                                                     | 63.0 ms: 1.14x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.9 ms: 1.12x faster                                                      |
| regex_dna      | 126 ms                                                      | 119 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 5.70 ms                                                     | 5.36 ms: 1.06x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.0 ms: 1.05x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.01x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 136 us: 1.02x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.85 us: 1.04x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.55 us: 1.04x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.5 us: 1.06x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                       |
| pickle               | 7.43 us                                                     | 8.08 us: 1.09x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.21 us: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (2): tomli_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.9 ms: 1.16x slower                                                      |
| python_startup         | 19.5 ms                                                     | 24.9 ms: 1.28x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.41 ms: 1.11x faster                                                      |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.0 ms: 2.77x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 383 ms: 2.01x faster                                                       |
| async_tree_io              | 731 ms                                                      | 380 ms: 1.93x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 206 ms: 1.78x faster                                                       |
| mdp                        | 1.37 sec                                                    | 796 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 201 ms: 1.69x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.25 sec: 1.68x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| deepcopy                   | 238 us                                                      | 163 us: 1.46x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 16.4 us: 1.45x faster                                                      |
| float                      | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 377 ms: 1.29x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.28x faster                                                      |
| go                         | 91.6 ms                                                     | 75.2 ms: 1.22x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.77 us: 1.18x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 38.8 ms: 1.14x faster                                                      |
| nbody                      | 71.9 ms                                                     | 63.0 ms: 1.14x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 77.9 ms: 1.12x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.41 ms: 1.11x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 34.4 ns: 1.09x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.2 ms: 1.09x faster                                                      |
| scimark_fft                | 184 ms                                                      | 170 ms: 1.08x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 72.9 ms: 1.08x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 476 ms: 1.08x faster                                                       |
| pyflate                    | 295 ms                                                      | 274 ms: 1.08x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 62.2 ms: 1.08x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 85.1 ms: 1.08x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 972 ms: 1.08x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.84 us: 1.07x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.5 ms: 1.07x faster                                                      |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 56.5 ns: 1.07x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.0 ms: 1.07x faster                                                      |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.07x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.2 ms: 1.06x faster                                                      |
| sympy_str                  | 175 ms                                                      | 165 ms: 1.06x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.36 ms: 1.06x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.33 us: 1.06x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.9 ms: 1.06x faster                                                      |
| json                       | 3.05 ms                                                     | 2.89 ms: 1.06x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.0 ms: 1.05x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.58 sec: 1.05x faster                                                     |
| async_generators           | 239 ms                                                      | 229 ms: 1.05x faster                                                       |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 829 us: 1.03x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 57.1 ms: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.6 ms: 1.03x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.99 ms: 1.03x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.2 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.50 ms: 1.02x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 2.13 ms: 1.01x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 62.0 ms: 1.01x faster                                                      |
| 2to3                       | 218 ms                                                      | 215 ms: 1.01x faster                                                       |
| sympy_expand               | 284 ms                                                      | 282 ms: 1.01x faster                                                       |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.01x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 136 us: 1.02x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.85 us: 1.04x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.55 us: 1.04x slower                                                      |
| fannkuch                   | 247 ms                                                      | 259 ms: 1.05x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.5 us: 1.06x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                       |
| pickle                     | 7.43 us                                                     | 8.08 us: 1.09x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.10x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.21 us: 1.13x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.9 ms: 1.16x slower                                                      |
| coverage                   | 40.8 ms                                                     | 48.9 ms: 1.20x slower                                                      |
| python_startup             | 19.5 ms                                                     | 24.9 ms: 1.28x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 89.4 ms: 1.29x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.11 ms: 1.38x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.26 ms: 1.67x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (4): pycparser, telco, tomli_loads, xml_etree_generate
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.119x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown