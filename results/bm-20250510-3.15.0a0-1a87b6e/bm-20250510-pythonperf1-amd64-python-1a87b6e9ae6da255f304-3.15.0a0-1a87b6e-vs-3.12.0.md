# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-amd64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.067x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 394 ms: 1.96x faster                                                       |
| async_tree_io              | 731 ms                                                      | 398 ms: 1.83x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                       |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.68x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.3 ms: 1.31x faster                                                      |
| nbody          | 71.9 ms                                                     | 61.9 ms: 1.16x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 80.4 ms: 1.09x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                      |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 90.7 ms: 1.03x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 130 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.2 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 56.3 ms: 1.01x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.78 us: 1.01x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.54 us: 1.04x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.8 ms: 1.05x slower                                                      |
| pickle               | 7.43 us                                                     | 7.89 us: 1.06x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.06x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.4 us: 1.11x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.5 us: 1.12x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.64 ms: 1.17x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.59 us: 1.27x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.8 ms: 1.22x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.3 ms: 1.35x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.59 ms: 1.07x faster                                                      |
| django_template | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.6 ms: 2.47x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 394 ms: 1.96x faster                                                       |
| async_tree_io              | 731 ms                                                      | 398 ms: 1.83x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                       |
| mdp                        | 1.37 sec                                                    | 792 ms: 1.73x faster                                                       |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.68x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.46 sec: 1.44x faster                                                     |
| deepcopy                   | 238 us                                                      | 173 us: 1.38x faster                                                       |
| float                      | 56.8 ms                                                     | 43.3 ms: 1.31x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.9 us: 1.25x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.3 us: 1.25x faster                                                      |
| go                         | 91.6 ms                                                     | 77.2 ms: 1.19x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 57.0 ms: 1.17x faster                                                      |
| nbody                      | 71.9 ms                                                     | 61.9 ms: 1.16x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.15x faster                                                      |
| chaos                      | 43.3 ms                                                     | 38.0 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.13x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.3 ms: 1.11x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 80.4 ms: 1.09x faster                                                      |
| scimark_fft                | 184 ms                                                      | 170 ms: 1.08x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 72.7 ms: 1.08x faster                                                      |
| raytrace                   | 192 ms                                                      | 179 ms: 1.08x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.59 ms: 1.07x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.8 ms: 1.06x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.9 ms: 1.06x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 486 ms: 1.06x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 990 ms: 1.06x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.0 ms: 1.05x faster                                                      |
| pyflate                    | 295 ms                                                      | 282 ms: 1.05x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.9 ms: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.3 ms: 1.04x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.98 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 57.1 ms: 1.03x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 2.10 ms: 1.03x faster                                                      |
| async_generators           | 239 ms                                                      | 234 ms: 1.03x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.7 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 130 us: 1.02x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.5 ms: 1.02x faster                                                      |
| fannkuch                   | 247 ms                                                      | 242 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.2 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.53 ms: 1.01x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 56.3 ms: 1.01x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.78 us: 1.01x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 872 us: 1.02x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 38.2 ns: 1.02x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.44 us: 1.03x slower                                                      |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 718 ms: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.92 us: 1.03x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.54 us: 1.04x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 39.8 ms: 1.05x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.89 us: 1.06x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.06x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 522 ms: 1.07x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.4 us: 1.11x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.59 ms: 1.11x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 20.5 us: 1.12x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 107 us: 1.12x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.64 ms: 1.17x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.8 ms: 1.22x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.59 us: 1.27x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.3 ms: 1.35x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 97.2 ms: 1.41x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.17 ms: 1.43x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.31 ms: 1.74x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 318 ns: 5.26x slower                                                       |
| coverage                   | 40.8 ms                                                     | 290 ms: 7.10x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (4): meteor_contest, docutils, json, tomli_loads
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.067x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown