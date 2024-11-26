# Results vs. 3.12.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: windows-amd64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.009x faster
- HPT reliability: 75.11%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 250 ms: 1.15x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.89 sec: 1.14x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 99.5 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 263 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 210 ms: 1.36x faster                                                        |
| async_tree_none            | 291 ms                                                      | 218 ms: 1.33x faster                                                        |
| async_tree_io              | 731 ms                                                      | 564 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 400 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 634 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 281 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 54.3 ms: 1.32x faster                                                       |
| float          | 56.8 ms                                                     | 48.0 ms: 1.18x faster                                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 91.9 ms: 1.05x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 15.2 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.29 sec: 1.06x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.3 ms: 1.03x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 94.6 ms: 1.02x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 199 us: 1.02x slower                                                        |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.1 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 4.97 ms: 1.43x faster                                                       |
| django_template | 22.9 ms                                                     | 26.4 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako                       | 7.09 ms                                                     | 4.97 ms: 1.43x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 263 ms: 1.40x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 17.1 us: 1.39x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 210 ms: 1.36x faster                                                        |
| async_tree_none            | 291 ms                                                      | 218 ms: 1.33x faster                                                        |
| nbody                      | 71.9 ms                                                     | 54.3 ms: 1.32x faster                                                       |
| async_tree_io              | 731 ms                                                      | 564 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                        |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 400 ms: 1.25x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 64.2 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.10 ms: 1.22x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 634 ms: 1.22x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 39.9 ms: 1.21x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.6 us: 1.21x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 281 ms: 1.21x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 55.6 ms: 1.20x faster                                                       |
| scimark_fft                | 184 ms                                                      | 154 ms: 1.20x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.8 ms: 1.19x faster                                                       |
| float                      | 56.8 ms                                                     | 48.0 ms: 1.18x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 450 ms: 1.14x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.12x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 949 ms: 1.10x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.0 ms: 1.08x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 55.0 ms: 1.07x faster                                                       |
| fannkuch                   | 247 ms                                                      | 232 ms: 1.06x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.29 sec: 1.06x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 57.3 ns: 1.06x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.5 ms: 1.04x faster                                                       |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                       |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.3 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| pyflate                    | 295 ms                                                      | 288 ms: 1.02x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.63 us: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.20 us: 1.01x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 94.6 ms: 1.02x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 76.1 ms: 1.02x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 199 us: 1.02x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| pycparser                  | 699 ms                                                      | 730 ms: 1.05x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 91.9 ms: 1.05x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 15.0 ms: 1.05x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.2 ms: 1.07x slower                                                       |
| generators                 | 22.5 ms                                                     | 24.2 ms: 1.07x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.32 ms: 1.07x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                       |
| sympy_str                  | 175 ms                                                      | 192 ms: 1.10x slower                                                        |
| raytrace                   | 192 ms                                                      | 212 ms: 1.10x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.11x slower                                                        |
| tornado_http               | 89.5 ms                                                     | 99.5 ms: 1.11x slower                                                       |
| async_generators           | 239 ms                                                      | 268 ms: 1.12x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 902 us: 1.12x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 210 ms: 1.12x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.64 ms: 1.12x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 103 ms: 1.13x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.89 sec: 1.14x slower                                                      |
| 2to3                       | 218 ms                                                      | 250 ms: 1.15x slower                                                        |
| sympy_expand               | 284 ms                                                      | 326 ms: 1.15x slower                                                        |
| django_template            | 22.9 ms                                                     | 26.4 ms: 1.15x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.19 ms: 1.17x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.61 sec: 1.17x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                       |
| richards_super             | 32.1 ms                                                     | 38.6 ms: 1.20x slower                                                       |
| richards                   | 28.4 ms                                                     | 34.2 ms: 1.21x slower                                                       |
| coverage                   | 40.8 ms                                                     | 49.3 ms: 1.21x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 15.8 ms: 1.22x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 117 us: 1.23x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 42.7 ms: 1.24x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.17 ms: 1.26x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.94 ms: 1.28x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.1 ms: 1.29x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 91.1 ms: 1.32x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.41 ms: 1.87x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (4): bench_thread_pool, nqueens, go, pathlib
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.009x faster
# HPT report

- Reliability score: 75.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown