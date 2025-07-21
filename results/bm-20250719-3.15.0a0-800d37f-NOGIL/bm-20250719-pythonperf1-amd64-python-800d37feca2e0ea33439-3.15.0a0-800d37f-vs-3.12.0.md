# Results vs. 3.12.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.012x slower
- HPT reliability: 98.94%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 231 ms: 1.06x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.87 sec: 1.73x slower                                                     |
| Geometric mean | (ref)                                                       | 1.35x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 328 ms: 2.35x faster                                                       |
| async_tree_io              | 731 ms                                                      | 352 ms: 2.08x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 189 ms: 1.94x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 148 ms: 1.93x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 311 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.82x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.6 ms: 1.22x faster                                                      |
| pidigits       | 152 ms                                                      | 138 ms: 1.10x faster                                                       |
| nbody          | 71.9 ms                                                     | 81.0 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.5 ms: 1.05x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.68 ms: 1.04x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 94.6 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 59.1 ms: 1.10x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                                      |
| pickle_list          | 2.83 us                                                     | 3.09 us: 1.09x slower                                                      |
| pickle               | 7.43 us                                                     | 8.18 us: 1.10x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.2 us: 1.10x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 63.0 ms: 1.13x slower                                                      |
| json_loads           | 13.9 us                                                     | 15.8 us: 1.13x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.12 us: 1.13x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 156 us: 1.17x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.69 ms: 1.17x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 45.2 ms: 1.20x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 239 us: 1.22x slower                                                       |
| unpickle             | 8.18 us                                                     | 10.5 us: 1.29x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.66 sec: 1.95x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 27.3 ms: 1.19x slower                                                      |
| mako            | 7.09 ms                                                     | 9.63 ms: 1.36x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.27x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.5 ms: 2.64x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 328 ms: 2.35x faster                                                       |
| async_tree_io              | 731 ms                                                      | 352 ms: 2.08x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 189 ms: 1.94x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 148 ms: 1.93x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 311 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.15 ms: 1.32x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.33 us: 1.32x faster                                                      |
| float                      | 56.8 ms                                                     | 46.6 ms: 1.22x faster                                                      |
| mdp                        | 1.37 sec                                                    | 1.15 sec: 1.20x faster                                                     |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.18x faster                                                      |
| deepcopy                   | 238 us                                                      | 203 us: 1.17x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.4 us: 1.11x faster                                                      |
| pidigits                   | 152 ms                                                      | 138 ms: 1.10x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.1 ms: 1.10x faster                                                      |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.6 ms: 1.06x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 461 ms: 1.06x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.5 ms: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                                      |
| json                       | 3.05 ms                                                     | 3.08 ms: 1.01x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.13 us: 1.02x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 61.8 ns: 1.02x slower                                                      |
| go                         | 91.6 ms                                                     | 94.5 ms: 1.03x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.68 ms: 1.04x slower                                                      |
| pycparser                  | 699 ms                                                      | 731 ms: 1.05x slower                                                       |
| 2to3                       | 218 ms                                                      | 231 ms: 1.06x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 97.1 ms: 1.06x slower                                                      |
| pyflate                    | 295 ms                                                      | 315 ms: 1.07x slower                                                       |
| chaos                      | 43.3 ms                                                     | 46.4 ms: 1.07x slower                                                      |
| sympy_str                  | 175 ms                                                      | 188 ms: 1.07x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 94.6 ms: 1.08x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.80 us: 1.08x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.0 ms: 1.08x slower                                                      |
| raytrace                   | 192 ms                                                      | 209 ms: 1.09x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.33 us: 1.09x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.09 us: 1.09x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 73.6 ms: 1.10x slower                                                      |
| pickle                     | 7.43 us                                                     | 8.18 us: 1.10x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 20.2 us: 1.10x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 41.6 ns: 1.11x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 571 ms: 1.11x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.61 ms: 1.12x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 66.2 ms: 1.12x slower                                                      |
| nbody                      | 71.9 ms                                                     | 81.0 ms: 1.13x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.44 ms: 1.13x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 63.0 ms: 1.13x slower                                                      |
| sympy_expand               | 284 ms                                                      | 320 ms: 1.13x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.8 us: 1.13x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.12 us: 1.13x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 90.0 ms: 1.14x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 79.1 ms: 1.14x slower                                                      |
| async_generators           | 239 ms                                                      | 275 ms: 1.15x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.8 ms: 1.16x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 73.1 ms: 1.16x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 156 us: 1.17x slower                                                       |
| scimark_fft                | 184 ms                                                      | 216 ms: 1.17x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.69 ms: 1.17x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 88.2 ms: 1.18x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 57.4 ms: 1.18x slower                                                      |
| richards                   | 28.4 ms                                                     | 33.6 ms: 1.18x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| django_template            | 22.9 ms                                                     | 27.3 ms: 1.19x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 45.2 ms: 1.20x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.11 ms: 1.22x slower                                                      |
| richards_super             | 32.1 ms                                                     | 39.1 ms: 1.22x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 239 us: 1.22x slower                                                       |
| fannkuch                   | 247 ms                                                      | 307 ms: 1.24x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 1.09 ms: 1.27x slower                                                      |
| unpickle                   | 8.18 us                                                     | 10.5 us: 1.29x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.39 ms: 1.30x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                      |
| mako                       | 7.09 ms                                                     | 9.63 ms: 1.36x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 130 us: 1.37x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.04 ms: 1.38x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.72 sec: 1.65x slower                                                     |
| coverage                   | 40.8 ms                                                     | 68.3 ms: 1.67x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.87 sec: 1.73x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.66 sec: 1.95x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (2): generators, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.012x slower

# HPT report

- Reliability score: 98.94% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown