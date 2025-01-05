# Results vs. 3.12.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-amd64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.072x faster
- HPT reliability: 97.59%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 385 ms: 2.00x faster                                                        |
| async_tree_io              | 731 ms                                                      | 392 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 165 ms: 1.73x faster                                                        |
| async_tree_none            | 291 ms                                                      | 176 ms: 1.65x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 217 ms: 1.57x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 339 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 346 ms: 1.41x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.67x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 40.3 ms: 1.41x faster                                                       |
| nbody          | 71.9 ms                                                     | 52.4 ms: 1.37x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.7 ms: 1.10x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                       |
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 22.0 ms: 1.54x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 108 us: 1.23x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 49.6 ms: 1.13x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 59.3 ms: 1.10x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 86.1 ms: 1.08x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 35.7 ms: 1.06x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 205 us: 1.05x slower                                                        |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.23 ms: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.5 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.06 ms: 1.40x faster                                                       |
| django_template | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 385 ms: 2.00x faster                                                        |
| async_tree_io              | 731 ms                                                      | 392 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 165 ms: 1.73x faster                                                        |
| async_tree_none            | 291 ms                                                      | 176 ms: 1.65x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 217 ms: 1.57x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 339 ms: 1.48x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 16.2 us: 1.46x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 346 ms: 1.41x faster                                                        |
| float                      | 56.8 ms                                                     | 40.3 ms: 1.41x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.06 ms: 1.40x faster                                                       |
| nbody                      | 71.9 ms                                                     | 52.4 ms: 1.37x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 50.6 ms: 1.32x faster                                                       |
| scimark_fft                | 184 ms                                                      | 145 ms: 1.27x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 62.8 ms: 1.25x faster                                                       |
| deepcopy                   | 238 us                                                      | 190 us: 1.25x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 108 us: 1.23x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.09 ms: 1.22x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.7 ms: 1.19x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 41.3 ms: 1.17x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.13x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 49.6 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 39.8 ms: 1.11x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 53.5 ms: 1.10x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.3 ms: 1.10x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 79.7 ms: 1.10x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 86.1 ms: 1.08x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 972 ms: 1.08x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 56.5 ns: 1.07x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.07x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 483 ms: 1.06x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 35.7 ms: 1.06x faster                                                       |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                        |
| chaos                      | 43.3 ms                                                     | 41.1 ms: 1.05x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 76.3 ms: 1.05x faster                                                       |
| json                       | 3.05 ms                                                     | 2.90 ms: 1.05x faster                                                       |
| pyflate                    | 295 ms                                                      | 283 ms: 1.04x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 828 us: 1.03x faster                                                        |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| go                         | 91.6 ms                                                     | 89.9 ms: 1.02x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.65 us: 1.01x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 74.4 ms: 1.00x faster                                                       |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                        |
| nqueens                    | 62.8 ms                                                     | 63.4 ms: 1.01x slower                                                       |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                        |
| fannkuch                   | 247 ms                                                      | 252 ms: 1.02x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.24 ms: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 720 ms: 1.03x slower                                                        |
| generators                 | 22.5 ms                                                     | 23.2 ms: 1.03x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 838 us: 1.04x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.05x slower                                                       |
| raytrace                   | 192 ms                                                      | 202 ms: 1.05x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 205 us: 1.05x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.27 ms: 1.05x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.08 ms: 1.06x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                       |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.07x slower                                                        |
| async_generators           | 239 ms                                                      | 258 ms: 1.08x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 37.5 ms: 1.09x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.23 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 205 ms: 1.10x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.53 sec: 1.11x slower                                                      |
| coverage                   | 40.8 ms                                                     | 47.1 ms: 1.15x slower                                                       |
| richards_super             | 32.1 ms                                                     | 37.7 ms: 1.18x slower                                                       |
| richards                   | 28.4 ms                                                     | 33.4 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 82.7 ms: 1.19x slower                                                       |
| django_template            | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.5 ms: 1.21x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.00 ms: 1.22x slower                                                       |
| mypy2                      | 509 ms                                                      | 646 ms: 1.27x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.97 ms: 1.29x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 22.0 ms: 1.54x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (2): logging_simple, sympy_sum
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.072x faster

# HPT report

- Reliability score: 97.59% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown