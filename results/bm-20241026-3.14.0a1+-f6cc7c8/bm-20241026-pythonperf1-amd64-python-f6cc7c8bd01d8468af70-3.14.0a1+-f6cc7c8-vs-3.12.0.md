# Results vs. 3.12.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: windows-amd64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.027x slower
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 230 ms: 1.05x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.72 sec: 1.04x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 93.0 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 260 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                        |
| async_tree_none            | 291 ms                                                      | 218 ms: 1.34x faster                                                        |
| async_tree_io              | 731 ms                                                      | 564 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 410 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 644 ms: 1.20x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 54.9 ms: 1.04x faster                                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| nbody          | 71.9 ms                                                     | 78.1 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 91.6 ms: 1.05x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 15.8 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 66.7 ms: 1.02x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 57.8 ms: 1.03x slower                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 96.9 ms: 1.04x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 40.3 ms: 1.07x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.5 us: 1.12x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.13x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 223 us: 1.14x slower                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.60 sec: 1.17x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.84 ms: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.1 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.82 ms: 1.04x faster                                                       |
| django_template | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 260 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                        |
| async_tree_none            | 291 ms                                                      | 218 ms: 1.34x faster                                                        |
| async_tree_io              | 731 ms                                                      | 564 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                        |
| deepcopy                   | 238 us                                                      | 193 us: 1.24x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 410 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 644 ms: 1.20x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 20.1 us: 1.18x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.5 us: 1.13x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.94 us: 1.08x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| go                         | 91.6 ms                                                     | 88.0 ms: 1.04x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.82 ms: 1.04x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.7 ms: 1.04x faster                                                       |
| float                      | 56.8 ms                                                     | 54.9 ms: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 89.7 ms: 1.02x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.7 ms: 1.01x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 63.2 ms: 1.01x slower                                                       |
| async_generators           | 239 ms                                                      | 242 ms: 1.01x slower                                                        |
| chaos                      | 43.3 ms                                                     | 43.8 ms: 1.01x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.1 ms: 1.01x slower                                                       |
| raytrace                   | 192 ms                                                      | 196 ms: 1.02x slower                                                        |
| spectral_norm              | 66.9 ms                                                     | 68.3 ms: 1.02x slower                                                       |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.7 ms: 1.02x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 62.2 ns: 1.03x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 76.8 ms: 1.03x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.95 us: 1.03x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 57.8 ms: 1.03x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.72 sec: 1.04x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.51 us: 1.04x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 93.0 ms: 1.04x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 61.2 ms: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 96.9 ms: 1.04x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 91.6 ms: 1.05x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.27 ms: 1.05x slower                                                       |
| json                       | 3.05 ms                                                     | 3.20 ms: 1.05x slower                                                       |
| pycparser                  | 699 ms                                                      | 734 ms: 1.05x slower                                                        |
| 2to3                       | 218 ms                                                      | 230 ms: 1.05x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 199 ms: 1.06x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 36.9 ms: 1.07x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.73 ms: 1.07x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.3 ms: 1.07x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.40 ms: 1.07x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.1 ms: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 306 ms: 1.08x slower                                                        |
| nbody                      | 71.9 ms                                                     | 78.1 ms: 1.09x slower                                                       |
| pyflate                    | 295 ms                                                      | 323 ms: 1.10x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 562 ms: 1.10x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 15.8 ms: 1.11x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                       |
| richards_super             | 32.1 ms                                                     | 35.8 ms: 1.11x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.5 us: 1.12x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.14 ms: 1.12x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.13x slower                                                        |
| scimark_fft                | 184 ms                                                      | 209 ms: 1.13x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.56 sec: 1.13x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.2 ms: 1.14x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 223 us: 1.14x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 922 us: 1.15x slower                                                        |
| fannkuch                   | 247 ms                                                      | 283 ms: 1.15x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 90.6 ms: 1.15x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.60 sec: 1.17x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.87 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.84 ms: 1.20x slower                                                       |
| coverage                   | 40.8 ms                                                     | 49.3 ms: 1.21x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 84.6 ms: 1.22x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.1 ms: 1.24x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.93 ms: 1.27x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.40 ms: 1.86x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (2): bench_thread_pool, pathlib
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.027x slower
# HPT report

- Reliability score: 99.85% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown