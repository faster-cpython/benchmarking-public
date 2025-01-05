# Results vs. 3.12.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-amd64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.025x faster
- HPT reliability: 68.46%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 396 ms: 1.95x faster                                                        |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                        |
| async_tree_none            | 291 ms                                                      | 179 ms: 1.62x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 345 ms: 1.42x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.65x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 52.1 ms: 1.09x faster                                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| nbody          | 71.9 ms                                                     | 75.3 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.46 ms: 1.11x faster                                                       |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 86.5 ms: 1.01x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 21.8 ms: 1.53x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.8 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.5 ms: 1.04x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.4 ms: 1.01x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.6 ms: 1.05x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 145 us: 1.09x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 220 us: 1.12x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.57 ms: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.3 ms: 1.07x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.6 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.69 ms: 1.06x faster                                                       |
| django_template | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 396 ms: 1.95x faster                                                        |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                        |
| async_tree_none            | 291 ms                                                      | 179 ms: 1.62x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 345 ms: 1.42x faster                                                        |
| deepcopy                   | 238 us                                                      | 185 us: 1.29x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 19.8 us: 1.20x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.20x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.88 us: 1.12x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.46 ms: 1.11x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.10x faster                                                       |
| float                      | 56.8 ms                                                     | 52.1 ms: 1.09x faster                                                       |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 62.2 ms: 1.08x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.2 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.06x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.8 ms: 1.06x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.69 ms: 1.06x faster                                                       |
| go                         | 91.6 ms                                                     | 87.1 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.1 ms: 1.05x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.8 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.5 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| json                       | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.9 ms: 1.02x faster                                                       |
| raytrace                   | 192 ms                                                      | 190 ms: 1.02x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 86.5 ms: 1.01x faster                                                       |
| async_generators           | 239 ms                                                      | 237 ms: 1.01x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 48.1 ms: 1.01x faster                                                       |
| chaos                      | 43.3 ms                                                     | 43.0 ms: 1.01x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.4 ms: 1.01x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.59 ms: 1.01x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.36 us: 1.01x slower                                                       |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.01x slower                                                        |
| nqueens                    | 62.8 ms                                                     | 63.7 ms: 1.01x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 61.6 ns: 1.02x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.02x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.86 us: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 60.5 ms: 1.03x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 76.9 ms: 1.03x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 531 ms: 1.03x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 35.9 ms: 1.04x slower                                                       |
| pycparser                  | 699 ms                                                      | 727 ms: 1.04x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 195 ms: 1.04x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                                       |
| scimark_fft                | 184 ms                                                      | 193 ms: 1.04x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 45.8 ms: 1.05x slower                                                       |
| nbody                      | 71.9 ms                                                     | 75.3 ms: 1.05x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.6 ms: 1.05x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.34 ms: 1.06x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.3 ms: 1.07x slower                                                       |
| richards                   | 28.4 ms                                                     | 30.4 ms: 1.07x slower                                                       |
| richards_super             | 32.1 ms                                                     | 34.5 ms: 1.07x slower                                                       |
| sympy_expand               | 284 ms                                                      | 306 ms: 1.08x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 145 us: 1.09x slower                                                        |
| pyflate                    | 295 ms                                                      | 321 ms: 1.09x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.09x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 86.1 ms: 1.09x slower                                                       |
| fannkuch                   | 247 ms                                                      | 270 ms: 1.09x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 895 us: 1.11x slower                                                        |
| coverage                   | 40.8 ms                                                     | 45.8 ms: 1.12x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 220 us: 1.12x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.76 ms: 1.15x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.57 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.19x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 82.3 ms: 1.19x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.6 ms: 1.21x slower                                                       |
| mypy2                      | 509 ms                                                      | 637 ms: 1.25x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.98 ms: 1.30x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 21.8 ms: 1.53x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.20 ms: 1.60x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (3): bench_thread_pool, docutils, json_loads
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 68.46% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown