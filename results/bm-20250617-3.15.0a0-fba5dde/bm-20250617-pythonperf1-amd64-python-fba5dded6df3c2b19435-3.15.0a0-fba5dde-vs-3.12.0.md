# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.256x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 295 ms: 1.35x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.08 sec: 1.25x slower                                                     |
| Geometric mean | (ref)                                                       | 1.30x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 561 ms: 1.37x faster                                                       |
| async_tree_io              | 731 ms                                                      | 546 ms: 1.34x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 292 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 235 ms: 1.21x faster                                                       |
| async_tree_none            | 291 ms                                                      | 242 ms: 1.20x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 295 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 438 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 440 ms: 1.11x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| float          | 56.8 ms                                                     | 76.0 ms: 1.34x slower                                                      |
| nbody          | 71.9 ms                                                     | 99.6 ms: 1.39x slower                                                      |
| Geometric mean | (ref)                                                       | 1.21x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.73 ms: 1.07x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 17.0 ms: 1.19x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 122 ms: 1.39x slower                                                       |
| Geometric mean | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_list        | 2.75 us                                                     | 3.07 us: 1.12x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 108 ms: 1.16x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 22.7 us: 1.23x slower                                                      |
| pickle               | 7.43 us                                                     | 9.61 us: 1.29x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.79 us: 1.34x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 89.5 ms: 1.37x slower                                                      |
| unpickle             | 8.18 us                                                     | 11.5 us: 1.41x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.02 sec: 1.48x slower                                                     |
| json_loads           | 13.9 us                                                     | 21.1 us: 1.52x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 8.83 ms: 1.55x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 89.3 ms: 1.60x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 64.0 ms: 1.70x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 358 us: 1.83x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 275 us: 2.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.46x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.0 ms: 1.23x slower                                                      |
| python_startup         | 19.5 ms                                                     | 27.2 ms: 1.40x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 36.3 ms: 1.58x slower                                                      |
| mako            | 7.09 ms                                                     | 12.4 ms: 1.74x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.66x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 34.3 ms: 2.35x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.49 sec: 1.40x faster                                                     |
| async_tree_io_tg           | 771 ms                                                      | 561 ms: 1.37x faster                                                       |
| async_tree_io              | 731 ms                                                      | 546 ms: 1.34x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 292 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 235 ms: 1.21x faster                                                       |
| async_tree_none            | 291 ms                                                      | 242 ms: 1.20x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 295 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 438 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 440 ms: 1.11x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.86 us: 1.05x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.73 ms: 1.07x slower                                                      |
| deepcopy                   | 238 us                                                      | 262 us: 1.10x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 3.07 us: 1.12x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 554 ms: 1.14x slower                                                       |
| dulwich_log                | 44.3 ms                                                     | 50.8 ms: 1.15x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 987 us: 1.15x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 108 ms: 1.16x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 17.0 ms: 1.19x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 22.7 us: 1.23x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 20.0 ms: 1.23x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 92.3 ms: 1.24x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 115 ms: 1.25x slower                                                       |
| docutils                   | 1.66 sec                                                    | 2.08 sec: 1.25x slower                                                     |
| sympy_integrate            | 13.0 ms                                                     | 16.4 ms: 1.27x slower                                                      |
| pickle                     | 7.43 us                                                     | 9.61 us: 1.29x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.71 us: 1.29x slower                                                      |
| sympy_str                  | 175 ms                                                      | 231 ms: 1.32x slower                                                       |
| float                      | 56.8 ms                                                     | 76.0 ms: 1.34x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.79 us: 1.34x slower                                                      |
| 2to3                       | 218 ms                                                      | 295 ms: 1.35x slower                                                       |
| comprehensions             | 14.1 us                                                     | 19.3 us: 1.37x slower                                                      |
| json                       | 3.05 ms                                                     | 4.17 ms: 1.37x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 89.5 ms: 1.37x slower                                                      |
| async_generators           | 239 ms                                                      | 332 ms: 1.39x slower                                                       |
| nbody                      | 71.9 ms                                                     | 99.6 ms: 1.39x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 122 ms: 1.39x slower                                                       |
| deepcopy_memo              | 23.7 us                                                     | 33.0 us: 1.39x slower                                                      |
| pycparser                  | 699 ms                                                      | 974 ms: 1.39x slower                                                       |
| python_startup             | 19.5 ms                                                     | 27.2 ms: 1.40x slower                                                      |
| sympy_expand               | 284 ms                                                      | 396 ms: 1.40x slower                                                       |
| unpickle                   | 8.18 us                                                     | 11.5 us: 1.41x slower                                                      |
| go                         | 91.6 ms                                                     | 131 ms: 1.43x slower                                                       |
| scimark_fft                | 184 ms                                                      | 265 ms: 1.44x slower                                                       |
| logging_format             | 6.72 us                                                     | 9.74 us: 1.45x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 91.5 ms: 1.46x slower                                                      |
| logging_simple             | 6.28 us                                                     | 9.25 us: 1.47x slower                                                      |
| chaos                      | 43.3 ms                                                     | 64.0 ms: 1.48x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 2.02 sec: 1.48x slower                                                     |
| telco                      | 4.13 ms                                                     | 6.25 ms: 1.51x slower                                                      |
| json_loads                 | 13.9 us                                                     | 21.1 us: 1.52x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 105 ms: 1.52x slower                                                       |
| coverage                   | 40.8 ms                                                     | 62.3 ms: 1.53x slower                                                      |
| pyflate                    | 295 ms                                                      | 453 ms: 1.54x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 8.83 ms: 1.55x slower                                                      |
| raytrace                   | 192 ms                                                      | 300 ms: 1.56x slower                                                       |
| django_template            | 22.9 ms                                                     | 36.3 ms: 1.58x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 89.3 ms: 1.60x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 153 us: 1.60x slower                                                       |
| generators                 | 22.5 ms                                                     | 36.6 ms: 1.62x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 4.16 ms: 1.63x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 79.7 ms: 1.64x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 130 ms: 1.64x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 71.9 ms: 1.65x slower                                                      |
| fannkuch                   | 247 ms                                                      | 406 ms: 1.65x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 111 ms: 1.66x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 854 ms: 1.66x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.74 sec: 1.67x slower                                                     |
| xml_etree_process          | 37.7 ms                                                     | 64.0 ms: 1.70x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 24.7 ms: 1.73x slower                                                      |
| mako                       | 7.09 ms                                                     | 12.4 ms: 1.74x slower                                                      |
| richards_super             | 32.1 ms                                                     | 57.0 ms: 1.78x slower                                                      |
| richards                   | 28.4 ms                                                     | 50.5 ms: 1.78x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 7.36 ms: 1.80x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 358 us: 1.83x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.48 ms: 1.96x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 4.29 ms: 1.98x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 3.05 ms: 2.00x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 119 ms: 2.02x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 275 us: 2.06x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 77.9 ns: 2.08x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 494 ns: 8.16x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.36x slower                                                               |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.256x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.25x

# Memory
- memory change: unknown