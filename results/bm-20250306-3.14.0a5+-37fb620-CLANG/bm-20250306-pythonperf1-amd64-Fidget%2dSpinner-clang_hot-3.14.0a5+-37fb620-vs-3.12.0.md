# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: clang_hot
- machine: windows-amd64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.014x faster
- HPT reliability: 80.39%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 229 ms: 1.05x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.77 sec: 1.06x slower                                                     |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 396 ms: 1.95x faster                                                       |
| async_tree_io              | 731 ms                                                      | 409 ms: 1.79x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.61x faster                                                       |
| async_tree_none            | 291 ms                                                      | 181 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 369 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 362 ms: 1.35x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.4 ms: 1.22x faster                                                      |
| nbody          | 71.9 ms                                                     | 69.2 ms: 1.04x faster                                                      |
| pidigits       | 152 ms                                                      | 156 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 86.3 ms: 1.01x faster                                                      |
| regex_dna      | 126 ms                                                      | 131 ms: 1.03x slower                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.87 ms: 1.16x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.7 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                     |
| xml_etree_iterparse  | 65.2 ms                                                     | 70.3 ms: 1.08x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 102 ms: 1.09x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 219 us: 1.12x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 66.5 ms: 1.19x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 46.1 ms: 1.22x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 7.86 ms: 1.38x slower                                                      |
| json_loads           | 13.9 us                                                     | 20.3 us: 1.46x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.17x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                                      |
| python_startup         | 19.5 ms                                                     | 27.3 ms: 1.40x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.33x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 25.6 ms: 1.12x slower                                                      |
| mako            | 7.09 ms                                                     | 8.19 ms: 1.16x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.9 ms: 2.52x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 396 ms: 1.95x faster                                                       |
| async_tree_io              | 731 ms                                                      | 409 ms: 1.79x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 210 ms: 1.61x faster                                                       |
| async_tree_none            | 291 ms                                                      | 181 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 369 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 362 ms: 1.35x faster                                                       |
| deepcopy                   | 238 us                                                      | 181 us: 1.31x faster                                                       |
| generators                 | 22.5 ms                                                     | 17.6 ms: 1.28x faster                                                      |
| float                      | 56.8 ms                                                     | 46.4 ms: 1.22x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.6 us: 1.22x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 19.8 us: 1.20x faster                                                      |
| go                         | 91.6 ms                                                     | 76.6 ms: 1.20x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 1.89 ms: 1.14x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 59.3 ms: 1.13x faster                                                      |
| raytrace                   | 192 ms                                                      | 175 ms: 1.10x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.94 us: 1.08x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 73.2 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.9 ms: 1.07x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.06x faster                                                      |
| async_generators           | 239 ms                                                      | 227 ms: 1.06x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.1 ms: 1.06x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.4 ms: 1.04x faster                                                      |
| nbody                      | 71.9 ms                                                     | 69.2 ms: 1.04x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                     |
| regex_compile              | 87.5 ms                                                     | 86.3 ms: 1.01x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 74.1 ms: 1.01x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.13 ms: 1.01x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.34 us: 1.01x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 92.5 ms: 1.01x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.81 us: 1.01x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 61.6 ns: 1.02x slower                                                      |
| pidigits                   | 152 ms                                                      | 156 ms: 1.03x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.03x slower                                                     |
| bench_thread_pool          | 857 us                                                      | 881 us: 1.03x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.7 ms: 1.03x slower                                                      |
| pyflate                    | 295 ms                                                      | 304 ms: 1.03x slower                                                       |
| scimark_fft                | 184 ms                                                      | 190 ms: 1.03x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.3 ms: 1.03x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.05 ms: 1.03x slower                                                      |
| sympy_str                  | 175 ms                                                      | 181 ms: 1.03x slower                                                       |
| regex_dna                  | 126 ms                                                      | 131 ms: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 724 ms: 1.04x slower                                                       |
| richards_super             | 32.1 ms                                                     | 33.4 ms: 1.04x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 534 ms: 1.04x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 195 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.67 ms: 1.04x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.1 ms: 1.05x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 843 us: 1.05x slower                                                       |
| 2to3                       | 218 ms                                                      | 229 ms: 1.05x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.77 sec: 1.06x slower                                                     |
| crypto_pyaes               | 48.5 ms                                                     | 51.7 ms: 1.07x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 70.3 ms: 1.08x slower                                                      |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.09x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 102 ms: 1.09x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.12x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.12x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 65.9 ms: 1.12x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 219 us: 1.12x slower                                                       |
| mako                       | 7.09 ms                                                     | 8.19 ms: 1.16x slower                                                      |
| fannkuch                   | 247 ms                                                      | 286 ms: 1.16x slower                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.87 ms: 1.16x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.7 ms: 1.17x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.63 sec: 1.19x slower                                                     |
| xml_etree_generate         | 55.8 ms                                                     | 66.5 ms: 1.19x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 46.1 ms: 1.22x slower                                                      |
| json                       | 3.05 ms                                                     | 3.82 ms: 1.25x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.18 ms: 1.26x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                                      |
| coverage                   | 40.8 ms                                                     | 53.2 ms: 1.30x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 92.2 ms: 1.33x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 7.86 ms: 1.38x slower                                                      |
| python_startup             | 19.5 ms                                                     | 27.3 ms: 1.40x slower                                                      |
| json_loads                 | 13.9 us                                                     | 20.3 us: 1.46x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.77 ms: 1.82x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.82x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250306-3.14.0a5+-37fb620-CLANG/bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 80.39% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown