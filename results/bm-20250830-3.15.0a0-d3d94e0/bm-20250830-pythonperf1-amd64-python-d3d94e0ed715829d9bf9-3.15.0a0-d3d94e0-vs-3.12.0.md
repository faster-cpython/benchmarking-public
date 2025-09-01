# Results vs. 3.12.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.102x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.58 sec: 1.05x faster                                                     |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 397 ms: 1.94x faster                                                       |
| async_tree_io              | 731 ms                                                      | 392 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.68x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 332 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 326 ms: 1.50x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                      |
| nbody          | 71.9 ms                                                     | 65.3 ms: 1.10x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.11x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 78.9 ms: 1.11x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 13.1 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 85.4 ms: 1.09x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.41 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 135 us: 1.01x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.31 us: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.02x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| xml_etree_process    | 37.7 ms                                                     | 38.9 ms: 1.03x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.1 us: 1.04x slower                                                      |
| pickle               | 7.43 us                                                     | 7.73 us: 1.04x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.96 us: 1.08x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.08x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.26 us: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.6 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.6 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.79 ms: 1.04x faster                                                      |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.7 ms: 2.71x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 397 ms: 1.94x faster                                                       |
| async_tree_io              | 731 ms                                                      | 392 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| mdp                        | 1.37 sec                                                    | 793 ms: 1.73x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.68x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.65x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.28 sec: 1.63x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 332 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 326 ms: 1.50x faster                                                       |
| deepcopy                   | 238 us                                                      | 168 us: 1.41x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.3 us: 1.30x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.29x faster                                                      |
| float                      | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                      |
| go                         | 91.6 ms                                                     | 77.1 ms: 1.19x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 420 ms: 1.16x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 38.5 ms: 1.15x faster                                                      |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.11x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.9 ms: 1.11x faster                                                      |
| nbody                      | 71.9 ms                                                     | 65.3 ms: 1.10x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 85.4 ms: 1.09x faster                                                      |
| raytrace                   | 192 ms                                                      | 177 ms: 1.09x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.1 ms: 1.09x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.7 ms: 1.07x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 85.2 ms: 1.07x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 56.4 ns: 1.07x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.2 ms: 1.06x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.41 ms: 1.05x faster                                                      |
| chaos                      | 43.3 ms                                                     | 41.2 ms: 1.05x faster                                                      |
| sympy_str                  | 175 ms                                                      | 166 ms: 1.05x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.58 sec: 1.05x faster                                                     |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.43 us: 1.04x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.79 ms: 1.04x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.8 ms: 1.04x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.00 sec: 1.04x faster                                                     |
| async_generators           | 239 ms                                                      | 230 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 495 ms: 1.04x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.07 us: 1.03x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 64.8 ms: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.3 ms: 1.03x faster                                                      |
| pyflate                    | 295 ms                                                      | 287 ms: 1.03x faster                                                       |
| json                       | 3.05 ms                                                     | 2.97 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.5 ms: 1.02x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.8 ms: 1.02x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 62.1 ms: 1.01x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 58.4 ms: 1.01x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 37.8 ns: 1.01x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.18 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 135 us: 1.01x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.31 us: 1.01x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.02x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| coroutines                 | 14.3 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 38.9 ms: 1.03x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.1 us: 1.04x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.73 us: 1.04x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.96 us: 1.08x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.08x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.09x slower                                                       |
| fannkuch                   | 247 ms                                                      | 269 ms: 1.09x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.26 us: 1.15x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.6 ms: 1.20x slower                                                      |
| coverage                   | 40.8 ms                                                     | 50.6 ms: 1.24x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.6 ms: 1.31x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 93.1 ms: 1.35x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.15 ms: 1.41x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.28 ms: 1.70x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (9): bench_thread_pool, pycparser, telco, scimark_fft, sympy_expand, scimark_sor, scimark_sparse_mat_mult, hexiom, 2to3
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.102x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown