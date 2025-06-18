# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.407x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.54x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 337 ms: 1.55x slower                                                       |
| docutils       | 1.66 sec                                                    | 4.24 sec: 2.55x slower                                                     |
| Geometric mean | (ref)                                                       | 1.99x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 558 ms: 1.38x faster                                                       |
| async_tree_io              | 731 ms                                                      | 583 ms: 1.25x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 311 ms: 1.18x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 249 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 460 ms: 1.09x faster                                                       |
| async_tree_none            | 291 ms                                                      | 275 ms: 1.06x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 140 ms: 1.08x faster                                                       |
| float          | 56.8 ms                                                     | 97.6 ms: 1.72x slower                                                      |
| nbody          | 71.9 ms                                                     | 183 ms: 2.55x slower                                                       |
| Geometric mean | (ref)                                                       | 1.59x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.81 ms: 1.12x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.8 ms: 1.18x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 161 ms: 1.84x slower                                                       |
| Geometric mean | (ref)                                                       | 1.21x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 22.0 us: 1.20x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 113 ms: 1.21x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 3.53 us: 1.28x slower                                                      |
| pickle               | 7.43 us                                                     | 9.91 us: 1.33x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.82 us: 1.35x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 92.7 ms: 1.42x slower                                                      |
| unpickle             | 8.18 us                                                     | 11.9 us: 1.46x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 9.51 ms: 1.67x slower                                                      |
| json_loads           | 13.9 us                                                     | 23.2 us: 1.67x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 108 ms: 1.94x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 80.0 ms: 2.12x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 452 us: 2.31x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 358 us: 2.69x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 5.05 sec: 3.69x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.71x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.3 ms: 1.25x slower                                                      |
| python_startup         | 19.5 ms                                                     | 27.7 ms: 1.42x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.33x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 45.6 ms: 1.99x slower                                                      |
| mako            | 7.09 ms                                                     | 16.4 ms: 2.32x slower                                                      |
| Geometric mean  | (ref)                                                       | 2.15x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 35.4 ms: 2.27x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 558 ms: 1.38x faster                                                       |
| async_tree_io              | 731 ms                                                      | 583 ms: 1.25x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 311 ms: 1.18x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 249 ms: 1.15x faster                                                       |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 460 ms: 1.09x faster                                                       |
| pidigits                   | 152 ms                                                      | 140 ms: 1.08x faster                                                       |
| async_tree_none            | 291 ms                                                      | 275 ms: 1.06x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.70 us: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.81 ms: 1.12x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.72 ms: 1.13x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 16.8 ms: 1.18x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 22.0 us: 1.20x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 113 ms: 1.21x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.3 ms: 1.25x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 615 ms: 1.26x slower                                                       |
| dulwich_log                | 44.3 ms                                                     | 56.5 ms: 1.28x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.53 us: 1.28x slower                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.70 sec: 1.29x slower                                                     |
| bench_mp_pool              | 69.2 ms                                                     | 89.8 ms: 1.30x slower                                                      |
| pickle                     | 7.43 us                                                     | 9.91 us: 1.33x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.82 us: 1.35x slower                                                      |
| json                       | 3.05 ms                                                     | 4.23 ms: 1.39x slower                                                      |
| deepcopy                   | 238 us                                                      | 336 us: 1.41x slower                                                       |
| python_startup             | 19.5 ms                                                     | 27.7 ms: 1.42x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 92.7 ms: 1.42x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.24 ms: 1.45x slower                                                      |
| unpickle                   | 8.18 us                                                     | 11.9 us: 1.46x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.11 ms: 1.48x slower                                                      |
| 2to3                       | 218 ms                                                      | 337 ms: 1.55x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 143 ms: 1.56x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 118 ms: 1.58x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 21.0 ms: 1.62x slower                                                      |
| mdp                        | 1.37 sec                                                    | 2.22 sec: 1.62x slower                                                     |
| deepcopy_reduce            | 2.09 us                                                     | 3.47 us: 1.66x slower                                                      |
| sympy_str                  | 175 ms                                                      | 291 ms: 1.66x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 9.51 ms: 1.67x slower                                                      |
| json_loads                 | 13.9 us                                                     | 23.2 us: 1.67x slower                                                      |
| float                      | 56.8 ms                                                     | 97.6 ms: 1.72x slower                                                      |
| logging_format             | 6.72 us                                                     | 11.6 us: 1.73x slower                                                      |
| async_generators           | 239 ms                                                      | 415 ms: 1.73x slower                                                       |
| sympy_expand               | 284 ms                                                      | 499 ms: 1.76x slower                                                       |
| logging_simple             | 6.28 us                                                     | 11.1 us: 1.77x slower                                                      |
| comprehensions             | 14.1 us                                                     | 25.5 us: 1.80x slower                                                      |
| deepcopy_memo              | 23.7 us                                                     | 43.6 us: 1.84x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 161 ms: 1.84x slower                                                       |
| generators                 | 22.5 ms                                                     | 42.4 ms: 1.88x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 108 ms: 1.94x slower                                                       |
| telco                      | 4.13 ms                                                     | 8.06 ms: 1.95x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 124 ms: 1.98x slower                                                       |
| django_template            | 22.9 ms                                                     | 45.6 ms: 1.99x slower                                                      |
| coverage                   | 40.8 ms                                                     | 83.9 ms: 2.05x slower                                                      |
| pyflate                    | 295 ms                                                      | 614 ms: 2.08x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 199 us: 2.09x slower                                                       |
| go                         | 91.6 ms                                                     | 192 ms: 2.10x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 80.0 ms: 2.12x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 80.8 ns: 2.16x slower                                                      |
| raytrace                   | 192 ms                                                      | 419 ms: 2.18x slower                                                       |
| chaos                      | 43.3 ms                                                     | 96.8 ms: 2.23x slower                                                      |
| scimark_fft                | 184 ms                                                      | 424 ms: 2.30x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 452 us: 2.31x slower                                                       |
| mako                       | 7.09 ms                                                     | 16.4 ms: 2.32x slower                                                      |
| fannkuch                   | 247 ms                                                      | 573 ms: 2.32x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 33.9 ms: 2.38x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 189 ms: 2.40x slower                                                       |
| pycparser                  | 699 ms                                                      | 1.70 sec: 2.43x slower                                                     |
| crypto_pyaes               | 48.5 ms                                                     | 118 ms: 2.43x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 164 ms: 2.45x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 107 ms: 2.45x slower                                                       |
| richards_super             | 32.1 ms                                                     | 79.1 ms: 2.47x slower                                                      |
| richards                   | 28.4 ms                                                     | 70.3 ms: 2.48x slower                                                      |
| docutils                   | 1.66 sec                                                    | 4.24 sec: 2.55x slower                                                     |
| nbody                      | 71.9 ms                                                     | 183 ms: 2.55x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 6.58 ms: 2.57x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 10.6 ms: 2.57x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 358 us: 2.69x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 5.93 ms: 2.74x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 164 ms: 2.79x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 1.47 sec: 2.87x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 5.05 sec: 3.69x slower                                                     |
| pprint_pformat             | 1.05 sec                                                    | 4.23 sec: 4.05x slower                                                     |
| logging_silent             | 60.5 ns                                                     | 586 ns: 9.69x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.70x slower                                                               |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.407x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.66x
- 95% likely to have a slowdown of 1.62x
- 99% likely to have a slowdown of 1.54x

# Memory
- memory change: unknown