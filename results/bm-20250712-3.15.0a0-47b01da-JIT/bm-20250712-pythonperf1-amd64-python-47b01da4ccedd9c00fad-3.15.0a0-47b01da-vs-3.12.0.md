# Results vs. 3.12.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.113x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 384 ms: 2.01x faster                                                       |
| async_tree_io              | 731 ms                                                      | 391 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.77x faster                                                       |
| async_tree_none            | 291 ms                                                      | 167 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.71x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 54.7 ms: 1.32x faster                                                      |
| float          | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.1 ms: 1.11x faster                                                      |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 107 us: 1.24x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.7 ms: 1.06x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.1 ms: 1.04x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 204 us: 1.04x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.61 us: 1.05x slower                                                      |
| pickle               | 7.43 us                                                     | 7.88 us: 1.06x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.1 us: 1.09x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.39 us: 1.20x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.5 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.35 ms: 1.32x faster                                                      |
| django_template | 22.9 ms                                                     | 25.0 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.1 ms: 2.67x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 384 ms: 2.01x faster                                                       |
| async_tree_io              | 731 ms                                                      | 391 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.77x faster                                                       |
| async_tree_none            | 291 ms                                                      | 167 ms: 1.75x faster                                                       |
| mdp                        | 1.37 sec                                                    | 800 ms: 1.71x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 334 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.42 sec: 1.47x faster                                                     |
| deepcopy                   | 238 us                                                      | 173 us: 1.37x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.35 ms: 1.32x faster                                                      |
| nbody                      | 71.9 ms                                                     | 54.7 ms: 1.32x faster                                                      |
| float                      | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.7 us: 1.27x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 107 us: 1.24x faster                                                       |
| scimark_fft                | 184 ms                                                      | 153 ms: 1.21x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                                     |
| go                         | 91.6 ms                                                     | 78.2 ms: 1.17x faster                                                      |
| pyflate                    | 295 ms                                                      | 252 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.14x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.25 ms: 1.14x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                      |
| fannkuch                   | 247 ms                                                      | 220 ms: 1.12x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 458 ms: 1.12x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.3 ms: 1.11x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 944 ms: 1.11x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 79.1 ms: 1.11x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.5 ms: 1.09x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.7 ns: 1.09x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 45.4 ms: 1.07x faster                                                      |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                      |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.7 ms: 1.06x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 70.9 ms: 1.05x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.7 ms: 1.05x faster                                                      |
| chaos                      | 43.3 ms                                                     | 41.3 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.6 ms: 1.04x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.1 ms: 1.04x faster                                                      |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.4 ms: 1.04x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.02x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.57 us: 1.02x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                                      |
| richards_super             | 32.1 ms                                                     | 31.4 ms: 1.02x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.16 us: 1.02x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 43.3 ms: 1.01x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 67.3 ms: 1.01x slower                                                      |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 80.6 ms: 1.02x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.24 ms: 1.04x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 204 us: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                      |
| sympy_expand               | 284 ms                                                      | 298 ms: 1.05x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.61 us: 1.05x slower                                                      |
| async_generators           | 239 ms                                                      | 252 ms: 1.05x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.88 us: 1.06x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 62.4 ms: 1.06x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.41 ms: 1.07x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 521 ms: 1.07x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.1 us: 1.09x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.0 ms: 1.09x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.10x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.39 us: 1.20x slower                                                      |
| coverage                   | 40.8 ms                                                     | 50.9 ms: 1.25x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.5 ms: 1.31x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 94.4 ms: 1.36x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.13 ms: 1.40x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.31 ms: 1.74x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (8): pycparser, regex_effbot, json, docutils, hexiom, bench_thread_pool, unpickle_list, unpack_sequence
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.113x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown