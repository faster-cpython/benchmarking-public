# Results vs. 3.12.0

- fork: python
- ref: dcaf33a41d5d220523d7
- machine: windows-amd64
- commit hash: dcaf33a
- commit date: 2024-03-20
- overall geometric mean: 1.17x slower
- HPT reliability: 55.71%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 235 ms: 1.08x slower                                                        |
| chameleon      | 4.98 ms                                                     | 4.67 ms: 1.07x faster                                                       |
| docutils       | 1.66 sec                                                    | 2.43 sec: 1.46x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 86.9 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 489 ms                                                      | 2.25 sec: 4.61x slower                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 2.46 sec: 4.90x slower                                                      |
| async_tree_none            | 291 ms                                                      | 1.81 sec: 6.22x slower                                                      |
| async_tree_memoization     | 339 ms                                                      | 2.32 sec: 6.84x slower                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 2.53 sec: 6.89x slower                                                      |
| async_tree_none_tg         | 285 ms                                                      | 1.99 sec: 6.99x slower                                                      |
| async_tree_io              | 731 ms                                                      | 7.30 sec: 9.99x slower                                                      |
| async_tree_io_tg           | 771 ms                                                      | 7.85 sec: 10.18x slower                                                     |
| Geometric mean             | (ref)                                                       | 6.82x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 58.4 ms: 1.23x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| float          | 56.8 ms                                                     | 81.6 ms: 1.44x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 82.8 ms: 1.06x faster                                                       |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 177 us: 1.11x faster                                                        |
| unpickle_pure_python | 133 us                                                      | 128 us: 1.04x faster                                                        |
| json_loads           | 13.9 us                                                     | 13.6 us: 1.02x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.59 ms: 1.02x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 19.2 us: 1.04x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.59 us: 1.05x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.00 us: 1.06x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 59.7 ms: 1.07x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 40.6 ms: 1.08x slower                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 123 ms: 1.32x slower                                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 94.3 ms: 1.45x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 23.9 ms: 1.23x slower                                                       |
| python_startup_no_site | 16.2 ms                                                     | 21.6 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.58 ms: 1.27x faster                                                       |
| django_template | 22.9 ms                                                     | 21.9 ms: 1.05x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 95.1 us                                                     | 71.2 us: 1.33x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.31x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 51.3 ms: 1.31x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.58 ms: 1.27x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.66 sec: 1.26x faster                                                      |
| nbody                      | 71.9 ms                                                     | 58.4 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.23 ms: 1.15x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 43.3 ms: 1.12x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.2 ms: 1.12x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.2 us: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.37 ms: 1.11x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 177 us: 1.11x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 54.8 ns: 1.10x faster                                                       |
| scimark_fft                | 184 ms                                                      | 168 ms: 1.10x faster                                                        |
| chaos                      | 43.3 ms                                                     | 39.9 ms: 1.09x faster                                                       |
| fannkuch                   | 247 ms                                                      | 228 ms: 1.08x faster                                                        |
| deepcopy                   | 238 us                                                      | 221 us: 1.08x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.94 us: 1.08x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 479 ms: 1.07x faster                                                        |
| logging_simple             | 6.28 us                                                     | 5.88 us: 1.07x faster                                                       |
| chameleon                  | 4.98 ms                                                     | 4.67 ms: 1.07x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.5 ms: 1.07x faster                                                       |
| json                       | 3.05 ms                                                     | 2.86 ms: 1.07x faster                                                       |
| raytrace                   | 192 ms                                                      | 181 ms: 1.06x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 983 ms: 1.06x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.2 ms: 1.06x faster                                                       |
| sympy_str                  | 175 ms                                                      | 165 ms: 1.06x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 82.8 ms: 1.06x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 86.7 ms: 1.06x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.37 us: 1.05x faster                                                       |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                       |
| pyflate                    | 295 ms                                                      | 280 ms: 1.05x faster                                                        |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                        |
| django_template            | 22.9 ms                                                     | 21.9 ms: 1.05x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 77.1 ms: 1.04x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.2 ms: 1.04x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.3 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 128 us: 1.04x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 181 ms: 1.03x faster                                                        |
| tornado_http               | 89.5 ms                                                     | 86.9 ms: 1.03x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 835 us: 1.03x faster                                                        |
| json_loads                 | 13.9 us                                                     | 13.6 us: 1.02x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.59 ms: 1.02x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.14 ms: 1.01x faster                                                       |
| sympy_expand               | 284 ms                                                      | 285 ms: 1.00x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.0 ms: 1.00x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 81.4 ms: 1.03x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 71.5 ms: 1.03x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.06 ms: 1.04x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.2 us: 1.04x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 840 us: 1.04x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 36.2 ms: 1.05x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.59 us: 1.05x slower                                                       |
| go                         | 91.6 ms                                                     | 96.6 ms: 1.06x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.35 ms: 1.06x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.00 us: 1.06x slower                                                       |
| aiohttp                    | 884 us                                                      | 941 us: 1.06x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 59.7 ms: 1.07x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                      |
| 2to3                       | 218 ms                                                      | 235 ms: 1.08x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 40.6 ms: 1.08x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.74 ms: 1.15x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.2 ms: 1.16x slower                                                       |
| async_generators           | 239 ms                                                      | 281 ms: 1.18x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 69.5 ms: 1.18x slower                                                       |
| pycparser                  | 699 ms                                                      | 828 ms: 1.19x slower                                                        |
| python_startup             | 19.5 ms                                                     | 23.9 ms: 1.23x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 46.7 ns: 1.25x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 123 ms: 1.32x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 21.6 ms: 1.33x slower                                                       |
| float                      | 56.8 ms                                                     | 81.6 ms: 1.44x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 94.3 ms: 1.45x slower                                                       |
| docutils                   | 1.66 sec                                                    | 2.43 sec: 1.46x slower                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 2.25 sec: 4.61x slower                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 2.46 sec: 4.90x slower                                                      |
| async_tree_none            | 291 ms                                                      | 1.81 sec: 6.22x slower                                                      |
| async_tree_memoization     | 339 ms                                                      | 2.32 sec: 6.84x slower                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 2.53 sec: 6.89x slower                                                      |
| async_tree_none_tg         | 285 ms                                                      | 1.99 sec: 6.99x slower                                                      |
| async_tree_io              | 731 ms                                                      | 7.30 sec: 9.99x slower                                                      |
| async_tree_io_tg           | 771 ms                                                      | 7.85 sec: 10.18x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.17x slower                                                                |

Benchmark hidden because not significant (6): asyncio_tcp, mypy2, unpickle_list, pickle, meteor_contest, create_gc_cycles
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240320-3.13.0a5+-dcaf33a-JIT/bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 55.71% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: unknown