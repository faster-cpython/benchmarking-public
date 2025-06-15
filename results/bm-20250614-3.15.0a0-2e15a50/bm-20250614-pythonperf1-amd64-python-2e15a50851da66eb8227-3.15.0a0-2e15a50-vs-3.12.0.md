# Results vs. 3.12.0

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.285x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 296 ms: 1.36x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.10 sec: 1.26x slower                                                     |
| Geometric mean | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 566 ms: 1.36x faster                                                       |
| async_tree_io              | 731 ms                                                      | 547 ms: 1.34x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 294 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 237 ms: 1.20x faster                                                       |
| async_tree_none            | 291 ms                                                      | 243 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 437 ms: 1.15x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 296 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 442 ms: 1.11x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| float          | 56.8 ms                                                     | 76.8 ms: 1.35x slower                                                      |
| nbody          | 71.9 ms                                                     | 107 ms: 1.49x slower                                                       |
| Geometric mean | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.73 ms: 1.07x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 17.0 ms: 1.20x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 124 ms: 1.41x slower                                                       |
| Geometric mean | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_list        | 2.75 us                                                     | 3.11 us: 1.13x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 108 ms: 1.16x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 22.6 us: 1.23x slower                                                      |
| pickle               | 7.43 us                                                     | 9.60 us: 1.29x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.86 us: 1.37x slower                                                      |
| unpickle             | 8.18 us                                                     | 11.3 us: 1.38x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 91.6 ms: 1.41x slower                                                      |
| json_loads           | 13.9 us                                                     | 20.5 us: 1.47x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 8.45 ms: 1.48x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.08 sec: 1.52x slower                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 91.2 ms: 1.63x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 65.7 ms: 1.74x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 363 us: 1.86x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 279 us: 2.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.46x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.0 ms: 1.23x slower                                                      |
| python_startup         | 19.5 ms                                                     | 27.0 ms: 1.39x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 37.3 ms: 1.63x slower                                                      |
| mako            | 7.09 ms                                                     | 13.1 ms: 1.84x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.73x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 34.3 ms: 2.34x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.39 sec: 1.51x faster                                                     |
| async_tree_io_tg           | 771 ms                                                      | 566 ms: 1.36x faster                                                       |
| async_tree_io              | 731 ms                                                      | 547 ms: 1.34x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 294 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 237 ms: 1.20x faster                                                       |
| async_tree_none            | 291 ms                                                      | 243 ms: 1.20x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.17 sec: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 437 ms: 1.15x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 296 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 442 ms: 1.11x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 459 ms: 1.06x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.85 us: 1.05x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.73 ms: 1.07x slower                                                      |
| deepcopy                   | 238 us                                                      | 267 us: 1.12x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 3.11 us: 1.13x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 108 ms: 1.16x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 1.01 ms: 1.17x slower                                                      |
| dulwich_log                | 44.3 ms                                                     | 52.1 ms: 1.18x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 17.0 ms: 1.20x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 22.6 us: 1.23x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 20.0 ms: 1.23x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 93.2 ms: 1.25x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.10 sec: 1.26x slower                                                     |
| sympy_sum                  | 91.5 ms                                                     | 116 ms: 1.27x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 16.7 ms: 1.29x slower                                                      |
| pickle                     | 7.43 us                                                     | 9.60 us: 1.29x slower                                                      |
| json                       | 3.05 ms                                                     | 4.01 ms: 1.32x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.78 us: 1.33x slower                                                      |
| sympy_str                  | 175 ms                                                      | 234 ms: 1.34x slower                                                       |
| float                      | 56.8 ms                                                     | 76.8 ms: 1.35x slower                                                      |
| 2to3                       | 218 ms                                                      | 296 ms: 1.36x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.86 us: 1.37x slower                                                      |
| unpickle                   | 8.18 us                                                     | 11.3 us: 1.38x slower                                                      |
| python_startup             | 19.5 ms                                                     | 27.0 ms: 1.39x slower                                                      |
| comprehensions             | 14.1 us                                                     | 19.8 us: 1.40x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 91.6 ms: 1.41x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 124 ms: 1.41x slower                                                       |
| pycparser                  | 699 ms                                                      | 988 ms: 1.41x slower                                                       |
| sympy_expand               | 284 ms                                                      | 402 ms: 1.42x slower                                                       |
| deepcopy_memo              | 23.7 us                                                     | 33.6 us: 1.42x slower                                                      |
| async_generators           | 239 ms                                                      | 341 ms: 1.43x slower                                                       |
| go                         | 91.6 ms                                                     | 134 ms: 1.46x slower                                                       |
| json_loads                 | 13.9 us                                                     | 20.5 us: 1.47x slower                                                      |
| logging_format             | 6.72 us                                                     | 9.91 us: 1.48x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 8.45 ms: 1.48x slower                                                      |
| nbody                      | 71.9 ms                                                     | 107 ms: 1.49x slower                                                       |
| logging_simple             | 6.28 us                                                     | 9.42 us: 1.50x slower                                                      |
| scimark_fft                | 184 ms                                                      | 277 ms: 1.50x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 94.5 ms: 1.51x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 104 ms: 1.51x slower                                                       |
| telco                      | 4.13 ms                                                     | 6.26 ms: 1.52x slower                                                      |
| chaos                      | 43.3 ms                                                     | 65.8 ms: 1.52x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 2.08 sec: 1.52x slower                                                     |
| pyflate                    | 295 ms                                                      | 462 ms: 1.57x slower                                                       |
| raytrace                   | 192 ms                                                      | 303 ms: 1.57x slower                                                       |
| generators                 | 22.5 ms                                                     | 36.4 ms: 1.62x slower                                                      |
| django_template            | 22.9 ms                                                     | 37.3 ms: 1.63x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 155 us: 1.63x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 91.2 ms: 1.63x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 79.8 ms: 1.65x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 111 ms: 1.66x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 856 ms: 1.67x slower                                                       |
| fannkuch                   | 247 ms                                                      | 413 ms: 1.67x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.76 sec: 1.68x slower                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 73.9 ms: 1.69x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 133 ms: 1.69x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 4.41 ms: 1.72x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 65.7 ms: 1.74x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 7.46 ms: 1.82x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 26.1 ms: 1.83x slower                                                      |
| richards_super             | 32.1 ms                                                     | 58.7 ms: 1.83x slower                                                      |
| mako                       | 7.09 ms                                                     | 13.1 ms: 1.84x slower                                                      |
| richards                   | 28.4 ms                                                     | 52.3 ms: 1.84x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 363 us: 1.86x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.93 ms: 1.92x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.45 ms: 1.93x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 4.38 ms: 2.03x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 120 ms: 2.04x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 279 us: 2.09x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 83.6 ns: 2.23x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 501 ns: 8.29x slower                                                       |
| coverage                   | 40.8 ms                                                     | 471 ms: 11.54x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.41x slower                                                               |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.285x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.35x
- 95% likely to have a slowdown of 1.33x
- 99% likely to have a slowdown of 1.26x

# Memory
- memory change: unknown