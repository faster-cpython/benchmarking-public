# Results vs. 3.12.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.017x slower
- HPT reliability: 98.57%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 229 ms: 1.05x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.87 sec: 1.73x slower                                                     |
| Geometric mean | (ref)                                                       | 1.35x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 331 ms: 2.33x faster                                                       |
| async_tree_io              | 731 ms                                                      | 354 ms: 2.07x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 147 ms: 1.94x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 192 ms: 1.91x faster                                                       |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.69x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 309 ms: 1.62x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 211 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.81x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.9 ms: 1.24x faster                                                      |
| pidigits       | 152 ms                                                      | 137 ms: 1.11x faster                                                       |
| nbody          | 71.9 ms                                                     | 84.0 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.5 ms: 1.05x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 94.7 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 59.2 ms: 1.10x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                      |
| pickle               | 7.43 us                                                     | 7.72 us: 1.04x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.05 us: 1.08x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.0 us: 1.09x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.06 us: 1.11x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 62.4 ms: 1.12x slower                                                      |
| json_loads           | 13.9 us                                                     | 15.7 us: 1.13x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.70 ms: 1.18x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 44.7 ms: 1.19x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 160 us: 1.20x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 237 us: 1.21x slower                                                       |
| unpickle             | 8.18 us                                                     | 10.1 us: 1.24x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.69 sec: 1.97x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.6 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                      |
| mako            | 7.09 ms                                                     | 9.84 ms: 1.39x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.29x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.6 ms: 2.63x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 331 ms: 2.33x faster                                                       |
| async_tree_io              | 731 ms                                                      | 354 ms: 2.07x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 147 ms: 1.94x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 192 ms: 1.91x faster                                                       |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.69x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 309 ms: 1.62x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 211 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.15 ms: 1.33x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.33 us: 1.32x faster                                                      |
| float                      | 56.8 ms                                                     | 45.9 ms: 1.24x faster                                                      |
| deepcopy                   | 238 us                                                      | 199 us: 1.19x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 411 ms: 1.19x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.17 sec: 1.18x faster                                                     |
| comprehensions             | 14.1 us                                                     | 12.2 us: 1.15x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.9 us: 1.13x faster                                                      |
| pidigits                   | 152 ms                                                      | 137 ms: 1.11x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.2 ms: 1.10x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.5 ms: 1.05x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.1 ms: 1.05x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                      |
| go                         | 91.6 ms                                                     | 92.5 ms: 1.01x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.13 us: 1.02x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 38.3 ns: 1.02x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 62.0 ns: 1.02x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.72 us: 1.04x slower                                                      |
| pycparser                  | 699 ms                                                      | 731 ms: 1.05x slower                                                       |
| 2to3                       | 218 ms                                                      | 229 ms: 1.05x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 15.1 ms: 1.06x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.05 us: 1.08x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 99.0 ms: 1.08x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 94.7 ms: 1.08x slower                                                      |
| chaos                      | 43.3 ms                                                     | 47.0 ms: 1.08x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 20.0 us: 1.09x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.2 ms: 1.10x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.38 us: 1.10x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.91 us: 1.10x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 568 ms: 1.11x slower                                                       |
| pyflate                    | 295 ms                                                      | 327 ms: 1.11x slower                                                       |
| raytrace                   | 192 ms                                                      | 213 ms: 1.11x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 3.06 us: 1.11x slower                                                      |
| async_generators           | 239 ms                                                      | 267 ms: 1.11x slower                                                       |
| sympy_str                  | 175 ms                                                      | 195 ms: 1.12x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 62.4 ms: 1.12x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.63 ms: 1.13x slower                                                      |
| json_loads                 | 13.9 us                                                     | 15.7 us: 1.13x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 76.3 ms: 1.14x slower                                                      |
| sympy_expand               | 284 ms                                                      | 324 ms: 1.14x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 78.9 ms: 1.14x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 72.1 ms: 1.15x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.50 ms: 1.16x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 68.3 ms: 1.16x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 91.6 ms: 1.16x slower                                                      |
| nbody                      | 71.9 ms                                                     | 84.0 ms: 1.17x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 87.3 ms: 1.17x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.70 ms: 1.18x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 44.7 ms: 1.19x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 57.7 ms: 1.19x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                      |
| django_template            | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 160 us: 1.20x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 237 us: 1.21x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.11 ms: 1.21x slower                                                      |
| scimark_fft                | 184 ms                                                      | 226 ms: 1.22x slower                                                       |
| richards                   | 28.4 ms                                                     | 34.8 ms: 1.23x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 54.1 ms: 1.24x slower                                                      |
| unpickle                   | 8.18 us                                                     | 10.1 us: 1.24x slower                                                      |
| fannkuch                   | 247 ms                                                      | 309 ms: 1.25x slower                                                       |
| richards_super             | 32.1 ms                                                     | 41.1 ms: 1.28x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.10 ms: 1.28x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 977 us: 1.30x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.6 ms: 1.31x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.59 ms: 1.35x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 129 us: 1.36x slower                                                       |
| mako                       | 7.09 ms                                                     | 9.84 ms: 1.39x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.70 sec: 1.62x slower                                                     |
| coverage                   | 40.8 ms                                                     | 66.9 ms: 1.64x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.87 sec: 1.73x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.69 sec: 1.97x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (3): generators, json, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.017x slower

# HPT report

- Reliability score: 98.57% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown