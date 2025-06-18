# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.214x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.14x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 289 ms: 1.33x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.12 sec: 1.27x slower                                                     |
| Geometric mean | (ref)                                                       | 1.30x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 554 ms: 1.39x faster                                                       |
| async_tree_io              | 731 ms                                                      | 536 ms: 1.37x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 288 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 229 ms: 1.24x faster                                                       |
| async_tree_none            | 291 ms                                                      | 236 ms: 1.24x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 289 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 428 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 432 ms: 1.13x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.25x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.7 ms: 1.34x faster                                                      |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                       |
| float          | 56.8 ms                                                     | 78.5 ms: 1.38x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.73 ms: 1.07x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.6 ms: 1.17x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 122 ms: 1.39x slower                                                       |
| Geometric mean | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_list        | 2.75 us                                                     | 3.12 us: 1.13x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 106 ms: 1.14x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| unpickle_pure_python | 133 us                                                      | 157 us: 1.18x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 22.7 us: 1.24x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 72.7 ms: 1.30x slower                                                      |
| pickle               | 7.43 us                                                     | 9.70 us: 1.31x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 87.2 ms: 1.34x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.94 us: 1.40x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 53.2 ms: 1.41x slower                                                      |
| unpickle             | 8.18 us                                                     | 11.7 us: 1.43x slower                                                      |
| json_loads           | 13.9 us                                                     | 20.8 us: 1.50x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 8.67 ms: 1.52x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 328 us: 1.68x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.33x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.9 ms: 1.22x slower                                                      |
| python_startup         | 19.5 ms                                                     | 27.3 ms: 1.40x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 38.7 ms: 1.69x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.30x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 34.4 ms: 2.34x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 554 ms: 1.39x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.51 sec: 1.39x faster                                                     |
| async_tree_io              | 731 ms                                                      | 536 ms: 1.37x faster                                                       |
| nbody                      | 71.9 ms                                                     | 53.7 ms: 1.34x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 288 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 229 ms: 1.24x faster                                                       |
| async_tree_none            | 291 ms                                                      | 236 ms: 1.24x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 289 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 428 ms: 1.17x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.21 sec: 1.14x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 432 ms: 1.13x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.74 us: 1.01x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.70 ms: 1.06x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.73 ms: 1.07x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 83.0 ms: 1.11x slower                                                      |
| comprehensions             | 14.1 us                                                     | 15.9 us: 1.12x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 552 ms: 1.13x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 3.12 us: 1.13x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 106 ms: 1.14x slower                                                       |
| fannkuch                   | 247 ms                                                      | 282 ms: 1.14x slower                                                       |
| deepcopy                   | 238 us                                                      | 273 us: 1.15x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| bench_thread_pool          | 857 us                                                      | 995 us: 1.16x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.6 ms: 1.17x slower                                                      |
| dulwich_log                | 44.3 ms                                                     | 52.1 ms: 1.18x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 157 us: 1.18x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.9 ms: 1.22x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 22.7 us: 1.24x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 116 ms: 1.27x slower                                                       |
| docutils                   | 1.66 sec                                                    | 2.12 sec: 1.27x slower                                                     |
| telco                      | 4.13 ms                                                     | 5.27 ms: 1.28x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 62.7 ms: 1.29x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 667 ms: 1.30x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 72.7 ms: 1.30x slower                                                      |
| pickle                     | 7.43 us                                                     | 9.70 us: 1.31x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.37 sec: 1.31x slower                                                     |
| sympy_integrate            | 13.0 ms                                                     | 17.0 ms: 1.31x slower                                                      |
| pyflate                    | 295 ms                                                      | 390 ms: 1.32x slower                                                       |
| 2to3                       | 218 ms                                                      | 289 ms: 1.33x slower                                                       |
| json                       | 3.05 ms                                                     | 4.07 ms: 1.33x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 87.2 ms: 1.34x slower                                                      |
| sympy_str                  | 175 ms                                                      | 238 ms: 1.36x slower                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.84 us: 1.36x slower                                                      |
| pycparser                  | 699 ms                                                      | 964 ms: 1.38x slower                                                       |
| float                      | 56.8 ms                                                     | 78.5 ms: 1.38x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 122 ms: 1.39x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.94 us: 1.40x slower                                                      |
| python_startup             | 19.5 ms                                                     | 27.3 ms: 1.40x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 53.2 ms: 1.41x slower                                                      |
| unpickle                   | 8.18 us                                                     | 11.7 us: 1.43x slower                                                      |
| sympy_expand               | 284 ms                                                      | 409 ms: 1.44x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 91.2 ms: 1.45x slower                                                      |
| async_generators           | 239 ms                                                      | 355 ms: 1.48x slower                                                       |
| json_loads                 | 13.9 us                                                     | 20.8 us: 1.50x slower                                                      |
| go                         | 91.6 ms                                                     | 137 ms: 1.50x slower                                                       |
| deepcopy_memo              | 23.7 us                                                     | 35.6 us: 1.50x slower                                                      |
| logging_format             | 6.72 us                                                     | 10.1 us: 1.51x slower                                                      |
| chaos                      | 43.3 ms                                                     | 65.7 ms: 1.52x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 8.67 ms: 1.52x slower                                                      |
| logging_simple             | 6.28 us                                                     | 9.56 us: 1.52x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 145 us: 1.52x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 105 ms: 1.52x slower                                                       |
| coverage                   | 40.8 ms                                                     | 62.9 ms: 1.54x slower                                                      |
| raytrace                   | 192 ms                                                      | 307 ms: 1.60x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 328 us: 1.68x slower                                                       |
| django_template            | 22.9 ms                                                     | 38.7 ms: 1.69x slower                                                      |
| generators                 | 22.5 ms                                                     | 38.3 ms: 1.70x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 74.6 ms: 1.71x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 115 ms: 1.72x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 137 ms: 1.74x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 26.8 ms: 1.88x slower                                                      |
| richards_super             | 32.1 ms                                                     | 60.9 ms: 1.90x slower                                                      |
| richards                   | 28.4 ms                                                     | 54.1 ms: 1.91x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.47 ms: 1.96x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 8.03 ms: 1.96x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 3.02 ms: 1.98x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 77.8 ns: 2.08x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 4.52 ms: 2.09x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 126 ms: 2.15x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 509 ns: 8.41x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.30x slower                                                               |

Benchmark hidden because not significant (2): scimark_fft, mako
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.214x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.20x
- 95% likely to have a slowdown of 1.17x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: unknown