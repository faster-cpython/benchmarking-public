# Results vs. 3.12.0

- fork: brandtbucher
- ref: msvc_musttail
- machine: windows-amd64
- commit hash: 06bc3bd
- commit date: 2025-03-07
- overall geometric mean: 1.039x faster
- HPT reliability: 51.21%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 229 ms: 1.05x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                     |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 417 ms: 1.85x faster                                                       |
| async_tree_io              | 731 ms                                                      | 426 ms: 1.72x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.68x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.60x faster                                                       |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 225 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.44x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 343 ms: 1.43x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.59x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.8 ms: 1.27x faster                                                      |
| nbody          | 71.9 ms                                                     | 67.9 ms: 1.06x faster                                                      |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                      |
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 63.4 ms: 1.03x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 56.7 ms: 1.01x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| xml_etree_process    | 37.7 ms                                                     | 39.9 ms: 1.06x slower                                                      |
| json_loads           | 13.9 us                                                     | 15.1 us: 1.09x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.13x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 230 us: 1.17x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.86 ms: 1.20x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.79 ms: 1.04x faster                                                      |
| django_template | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.9 ms: 2.52x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 417 ms: 1.85x faster                                                       |
| async_tree_io              | 731 ms                                                      | 426 ms: 1.72x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 218 ms: 1.68x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.60x faster                                                       |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 225 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.44x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 343 ms: 1.43x faster                                                       |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                                       |
| float                      | 56.8 ms                                                     | 44.8 ms: 1.27x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.5 us: 1.23x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 19.9 us: 1.19x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 57.8 ms: 1.16x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.1 ms: 1.12x faster                                                      |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.91 us: 1.09x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.1 ms: 1.09x faster                                                      |
| async_generators           | 239 ms                                                      | 221 ms: 1.09x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                      |
| nbody                      | 71.9 ms                                                     | 67.9 ms: 1.06x faster                                                      |
| go                         | 91.6 ms                                                     | 86.6 ms: 1.06x faster                                                      |
| chaos                      | 43.3 ms                                                     | 41.1 ms: 1.05x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.79 ms: 1.04x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.8 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.4 ms: 1.03x faster                                                      |
| scimark_fft                | 184 ms                                                      | 180 ms: 1.03x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 59.0 ns: 1.03x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 90.0 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 63.1 ms: 1.01x slower                                                      |
| raytrace                   | 192 ms                                                      | 193 ms: 1.01x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.1 ms: 1.01x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 56.7 ms: 1.01x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| logging_simple             | 6.28 us                                                     | 6.41 us: 1.02x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.88 us: 1.02x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                     |
| meteor_contest             | 74.6 ms                                                     | 76.9 ms: 1.03x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 45.2 ms: 1.03x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.08 sec: 1.04x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 533 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.66 ms: 1.04x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.28 ms: 1.04x slower                                                      |
| 2to3                       | 218 ms                                                      | 229 ms: 1.05x slower                                                       |
| sympy_expand               | 284 ms                                                      | 299 ms: 1.05x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.9 ms: 1.06x slower                                                      |
| pyflate                    | 295 ms                                                      | 312 ms: 1.06x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.30 ms: 1.06x slower                                                      |
| pycparser                  | 699 ms                                                      | 746 ms: 1.07x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 84.2 ms: 1.07x slower                                                      |
| json_loads                 | 13.9 us                                                     | 15.1 us: 1.09x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 64.1 ms: 1.09x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.13x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 108 us: 1.13x slower                                                       |
| fannkuch                   | 247 ms                                                      | 282 ms: 1.14x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.78 ms: 1.16x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                     |
| pickle_pure_python         | 195 us                                                      | 230 us: 1.17x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.1 ms: 1.20x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.86 ms: 1.20x slower                                                      |
| richards                   | 28.4 ms                                                     | 35.6 ms: 1.26x slower                                                      |
| richards_super             | 32.1 ms                                                     | 40.6 ms: 1.27x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 87.8 ms: 1.27x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.04 ms: 1.34x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.66x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (4): bench_thread_pool, regex_compile, json, sympy_str
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250307-3.14.0a5+-06bc3bd/bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 51.21% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown