# Results vs. 3.12.0

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.403x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.54x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 337 ms: 1.55x slower                                                       |
| docutils       | 1.66 sec                                                    | 4.15 sec: 2.50x slower                                                     |
| Geometric mean | (ref)                                                       | 1.97x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 551 ms: 1.40x faster                                                       |
| async_tree_io              | 731 ms                                                      | 580 ms: 1.26x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 310 ms: 1.19x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 243 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 457 ms: 1.10x faster                                                       |
| async_tree_none            | 291 ms                                                      | 273 ms: 1.07x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 332 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 480 ms: 1.02x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 140 ms: 1.09x faster                                                       |
| float          | 56.8 ms                                                     | 98.6 ms: 1.74x slower                                                      |
| nbody          | 71.9 ms                                                     | 176 ms: 2.45x slower                                                       |
| Geometric mean | (ref)                                                       | 1.58x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.82 ms: 1.13x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 17.0 ms: 1.19x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 160 ms: 1.83x slower                                                       |
| Geometric mean | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 22.0 us: 1.20x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 112 ms: 1.20x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 3.44 us: 1.25x slower                                                      |
| pickle               | 7.43 us                                                     | 9.80 us: 1.32x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.75 us: 1.33x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 93.0 ms: 1.43x slower                                                      |
| unpickle             | 8.18 us                                                     | 12.2 us: 1.49x slower                                                      |
| json_loads           | 13.9 us                                                     | 22.5 us: 1.62x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 9.45 ms: 1.66x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 107 ms: 1.91x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 78.8 ms: 2.09x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 455 us: 2.33x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 357 us: 2.68x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 5.02 sec: 3.67x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.70x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                      |
| python_startup         | 19.5 ms                                                     | 27.5 ms: 1.41x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.33x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 45.3 ms: 1.97x slower                                                      |
| mako            | 7.09 ms                                                     | 16.4 ms: 2.31x slower                                                      |
| Geometric mean  | (ref)                                                       | 2.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 35.8 ms: 2.25x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 551 ms: 1.40x faster                                                       |
| async_tree_io              | 731 ms                                                      | 580 ms: 1.26x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 310 ms: 1.19x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 243 ms: 1.17x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 457 ms: 1.10x faster                                                       |
| pidigits                   | 152 ms                                                      | 140 ms: 1.09x faster                                                       |
| async_tree_none            | 291 ms                                                      | 273 ms: 1.07x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.68 us: 1.05x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 332 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 480 ms: 1.02x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 519 ms: 1.06x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.82 ms: 1.13x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.79 ms: 1.17x slower                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.46 sec: 1.17x slower                                                     |
| regex_v8                   | 14.2 ms                                                     | 17.0 ms: 1.19x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 22.0 us: 1.20x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 112 ms: 1.20x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.44 us: 1.25x slower                                                      |
| dulwich_log                | 44.3 ms                                                     | 56.2 ms: 1.27x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 89.5 ms: 1.29x slower                                                      |
| pickle                     | 7.43 us                                                     | 9.80 us: 1.32x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.75 us: 1.33x slower                                                      |
| json                       | 3.05 ms                                                     | 4.18 ms: 1.37x slower                                                      |
| deepcopy                   | 238 us                                                      | 332 us: 1.40x slower                                                       |
| python_startup             | 19.5 ms                                                     | 27.5 ms: 1.41x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 93.0 ms: 1.43x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.25 ms: 1.46x slower                                                      |
| unpickle                   | 8.18 us                                                     | 12.2 us: 1.49x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.13 ms: 1.50x slower                                                      |
| 2to3                       | 218 ms                                                      | 337 ms: 1.55x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 142 ms: 1.55x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 119 ms: 1.60x slower                                                       |
| json_loads                 | 13.9 us                                                     | 22.5 us: 1.62x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 21.0 ms: 1.62x slower                                                      |
| mdp                        | 1.37 sec                                                    | 2.23 sec: 1.63x slower                                                     |
| deepcopy_reduce            | 2.09 us                                                     | 3.41 us: 1.63x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 9.45 ms: 1.66x slower                                                      |
| sympy_str                  | 175 ms                                                      | 291 ms: 1.66x slower                                                       |
| async_generators           | 239 ms                                                      | 407 ms: 1.70x slower                                                       |
| logging_format             | 6.72 us                                                     | 11.5 us: 1.72x slower                                                      |
| float                      | 56.8 ms                                                     | 98.6 ms: 1.74x slower                                                      |
| sympy_expand               | 284 ms                                                      | 494 ms: 1.74x slower                                                       |
| logging_simple             | 6.28 us                                                     | 11.0 us: 1.76x slower                                                      |
| comprehensions             | 14.1 us                                                     | 25.4 us: 1.80x slower                                                      |
| deepcopy_memo              | 23.7 us                                                     | 43.2 us: 1.82x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 160 ms: 1.83x slower                                                       |
| generators                 | 22.5 ms                                                     | 41.8 ms: 1.86x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 107 ms: 1.91x slower                                                       |
| telco                      | 4.13 ms                                                     | 7.95 ms: 1.92x slower                                                      |
| django_template            | 22.9 ms                                                     | 45.3 ms: 1.97x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 126 ms: 2.01x slower                                                       |
| coverage                   | 40.8 ms                                                     | 83.7 ms: 2.05x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 198 us: 2.09x slower                                                       |
| go                         | 91.6 ms                                                     | 191 ms: 2.09x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 78.8 ms: 2.09x slower                                                      |
| pyflate                    | 295 ms                                                      | 617 ms: 2.09x slower                                                       |
| raytrace                   | 192 ms                                                      | 409 ms: 2.13x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 80.2 ns: 2.14x slower                                                      |
| chaos                      | 43.3 ms                                                     | 95.4 ms: 2.20x slower                                                      |
| scimark_fft                | 184 ms                                                      | 412 ms: 2.24x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 32.8 ms: 2.30x slower                                                      |
| mako                       | 7.09 ms                                                     | 16.4 ms: 2.31x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 455 us: 2.33x slower                                                       |
| fannkuch                   | 247 ms                                                      | 581 ms: 2.36x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 187 ms: 2.37x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 118 ms: 2.42x slower                                                       |
| pycparser                  | 699 ms                                                      | 1.70 sec: 2.44x slower                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 107 ms: 2.44x slower                                                       |
| nbody                      | 71.9 ms                                                     | 176 ms: 2.45x slower                                                       |
| richards                   | 28.4 ms                                                     | 69.7 ms: 2.46x slower                                                      |
| richards_super             | 32.1 ms                                                     | 79.2 ms: 2.47x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 166 ms: 2.48x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 6.39 ms: 2.50x slower                                                      |
| docutils                   | 1.66 sec                                                    | 4.15 sec: 2.50x slower                                                     |
| hexiom                     | 4.10 ms                                                     | 10.6 ms: 2.58x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 357 us: 2.68x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 5.89 ms: 2.73x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 1.40 sec: 2.74x slower                                                     |
| scimark_lu                 | 58.9 ms                                                     | 163 ms: 2.78x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 5.02 sec: 3.67x slower                                                     |
| pprint_pformat             | 1.05 sec                                                    | 4.05 sec: 3.87x slower                                                     |
| logging_silent             | 60.5 ns                                                     | 583 ns: 9.63x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.68x slower                                                               |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250614-3.15.0a0-2e15a50-NOGIL/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.403x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.66x
- 95% likely to have a slowdown of 1.62x
- 99% likely to have a slowdown of 1.54x

# Memory
- memory change: unknown