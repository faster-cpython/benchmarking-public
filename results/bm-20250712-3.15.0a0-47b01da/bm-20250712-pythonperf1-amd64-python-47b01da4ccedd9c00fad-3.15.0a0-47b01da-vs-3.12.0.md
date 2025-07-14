# Results vs. 3.12.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.101x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 396 ms: 1.95x faster                                                       |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.78x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.73x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 42.9 ms: 1.32x faster                                                      |
| nbody          | 71.9 ms                                                     | 64.2 ms: 1.12x faster                                                      |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.5 ms: 1.11x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.50 ms: 1.08x faster                                                      |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 87.8 ms: 1.06x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 132 us: 1.01x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 38.4 ms: 1.02x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.41 us: 1.03x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.84 us: 1.03x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 206 us: 1.05x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.18 ms: 1.08x slower                                                      |
| pickle               | 7.43 us                                                     | 8.08 us: 1.09x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.5 us: 1.11x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.33 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.0 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.57 ms: 1.08x faster                                                      |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.2 ms: 2.67x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 396 ms: 1.95x faster                                                       |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.78x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.73x faster                                                       |
| mdp                        | 1.37 sec                                                    | 802 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.40 sec: 1.49x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                       |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                       |
| float                      | 56.8 ms                                                     | 42.9 ms: 1.32x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 19.3 us: 1.23x faster                                                      |
| go                         | 91.6 ms                                                     | 74.6 ms: 1.23x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                      |
| nbody                      | 71.9 ms                                                     | 64.2 ms: 1.12x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.5 ms: 1.11x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.3 ms: 1.10x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.5 ns: 1.09x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.57 ms: 1.08x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.50 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.7 ms: 1.08x faster                                                      |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 87.8 ms: 1.06x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 86.3 ms: 1.06x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.9 ms: 1.06x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 74.9 ms: 1.05x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                                      |
| chaos                      | 43.3 ms                                                     | 41.3 ms: 1.05x faster                                                      |
| sympy_str                  | 175 ms                                                      | 167 ms: 1.05x faster                                                       |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 492 ms: 1.04x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.3 ms: 1.04x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.04x faster                                                     |
| spectral_norm              | 66.9 ms                                                     | 64.5 ms: 1.04x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                     |
| async_generators           | 239 ms                                                      | 231 ms: 1.04x faster                                                       |
| json                       | 3.05 ms                                                     | 2.95 ms: 1.03x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 57.0 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.48 ms: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.4 ms: 1.03x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.2 ms: 1.03x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.0 ms: 1.02x faster                                                      |
| scimark_fft                | 184 ms                                                      | 181 ms: 1.02x faster                                                       |
| pyflate                    | 295 ms                                                      | 290 ms: 1.02x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 4.03 ms: 1.02x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 36.9 ns: 1.02x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                     |
| logging_simple             | 6.28 us                                                     | 6.21 us: 1.01x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 2.14 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 132 us: 1.01x faster                                                       |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| pycparser                  | 699 ms                                                      | 709 ms: 1.01x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 38.4 ms: 1.02x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.41 us: 1.03x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.84 us: 1.03x slower                                                      |
| fannkuch                   | 247 ms                                                      | 258 ms: 1.05x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 206 us: 1.05x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 101 us: 1.06x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.48 ms: 1.08x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.18 ms: 1.08x slower                                                      |
| pickle                     | 7.43 us                                                     | 8.08 us: 1.09x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 20.5 us: 1.11x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.33 us: 1.18x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| coverage                   | 40.8 ms                                                     | 50.4 ms: 1.23x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.0 ms: 1.33x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 93.9 ms: 1.36x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.10 ms: 1.38x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.31 ms: 1.74x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (8): regex_v8, xml_etree_iterparse, xml_etree_generate, logging_format, 2to3, sympy_expand, bench_thread_pool, asyncio_tcp
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.101x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown