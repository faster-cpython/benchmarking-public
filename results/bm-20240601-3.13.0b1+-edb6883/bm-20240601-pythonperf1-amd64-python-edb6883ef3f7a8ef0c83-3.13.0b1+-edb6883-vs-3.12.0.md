# Results vs. 3.12.0

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: windows-amd64
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 208 ms: 1.05x faster                                                        |
| chameleon      | 4.98 ms                                                     | 4.86 ms: 1.02x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                      |
| tornado_http   | 89.5 ms                                                     | 82.0 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 207 ms: 1.38x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 267 ms: 1.37x faster                                                        |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 382 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 610 ms: 1.26x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 268 ms: 1.26x faster                                                        |
| async_tree_io              | 731 ms                                                      | 594 ms: 1.23x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 49.7 ms: 1.14x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| nbody          | 71.9 ms                                                     | 70.9 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.9 ms: 1.12x faster                                                       |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 16.4 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 179 us: 1.09x faster                                                        |
| unpickle_pure_python | 133 us                                                      | 125 us: 1.06x faster                                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.9 ms: 1.05x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 53.1 ms: 1.05x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.3 ms: 1.04x faster                                                       |
| pickle               | 7.43 us                                                     | 7.20 us: 1.03x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 90.2 ms: 1.03x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.69 us: 1.02x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.62 ms: 1.01x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.5 us: 1.00x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.40 us: 1.03x slower                                                       |
| pickle_list          | 2.83 us                                                     | 2.92 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 16.1 ms: 1.01x faster                                                       |
| python_startup         | 19.5 ms                                                     | 20.1 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.51 ms: 1.09x faster                                                       |
| django_template | 22.9 ms                                                     | 21.8 ms: 1.05x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.48 sec: 1.42x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 207 ms: 1.38x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 267 ms: 1.37x faster                                                        |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.36x faster                                                       |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 382 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 610 ms: 1.26x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 268 ms: 1.26x faster                                                        |
| async_tree_io              | 731 ms                                                      | 594 ms: 1.23x faster                                                        |
| mypy2                      | 509 ms                                                      | 418 ms: 1.22x faster                                                        |
| raytrace                   | 192 ms                                                      | 160 ms: 1.21x faster                                                        |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 38.7 ms: 1.15x faster                                                       |
| float                      | 56.8 ms                                                     | 49.7 ms: 1.14x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.3 ms: 1.13x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 12.7 ms: 1.12x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 77.9 ms: 1.12x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 54.1 ns: 1.12x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.94 ms: 1.11x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 56.6 ms: 1.11x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 83.5 ms: 1.10x faster                                                       |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| pickle_pure_python         | 195 us                                                      | 179 us: 1.09x faster                                                        |
| tornado_http               | 89.5 ms                                                     | 82.0 ms: 1.09x faster                                                       |
| deepcopy                   | 238 us                                                      | 218 us: 1.09x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 787 us: 1.09x faster                                                        |
| mako                       | 7.09 ms                                                     | 6.51 ms: 1.09x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.77 ms: 1.09x faster                                                       |
| sympy_str                  | 175 ms                                                      | 161 ms: 1.09x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 54.2 ms: 1.09x faster                                                       |
| go                         | 91.6 ms                                                     | 84.5 ms: 1.08x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.20 us: 1.08x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.83 us: 1.08x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 74.8 ms: 1.08x faster                                                       |
| async_generators           | 239 ms                                                      | 224 ms: 1.07x faster                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 64.8 ms: 1.07x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 125 us: 1.06x faster                                                        |
| sqlglot_normalize          | 187 ms                                                      | 176 ms: 1.06x faster                                                        |
| sqlglot_parse              | 804 us                                                      | 759 us: 1.06x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 45.8 ms: 1.06x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.98 us: 1.06x faster                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 969 us: 1.05x faster                                                        |
| richards_super             | 32.1 ms                                                     | 30.4 ms: 1.05x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.5 ms: 1.05x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 22.5 us: 1.05x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.9 ms: 1.05x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 53.1 ms: 1.05x faster                                                       |
| django_template            | 22.9 ms                                                     | 21.8 ms: 1.05x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 63.9 ms: 1.05x faster                                                       |
| 2to3                       | 218 ms                                                      | 208 ms: 1.05x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                       |
| pyflate                    | 295 ms                                                      | 283 ms: 1.04x faster                                                        |
| sympy_expand               | 284 ms                                                      | 273 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 494 ms: 1.04x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 36.3 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.04x faster                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 33.3 ms: 1.04x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.1 ms: 1.04x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.20 us: 1.03x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 472 ms: 1.03x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 90.2 ms: 1.03x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 76.8 ms: 1.03x faster                                                       |
| chameleon                  | 4.98 ms                                                     | 4.86 ms: 1.02x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.69 us: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| json_dumps                 | 5.70 ms                                                     | 5.62 ms: 1.01x faster                                                       |
| nbody                      | 71.9 ms                                                     | 70.9 ms: 1.01x faster                                                       |
| scimark_fft                | 184 ms                                                      | 182 ms: 1.01x faster                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 16.1 ms: 1.01x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.5 us: 1.00x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                      |
| fannkuch                   | 247 ms                                                      | 249 ms: 1.01x slower                                                        |
| unpickle                   | 8.18 us                                                     | 8.40 us: 1.03x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                       |
| pickle_list                | 2.83 us                                                     | 2.92 us: 1.03x slower                                                       |
| python_startup             | 19.5 ms                                                     | 20.1 ms: 1.03x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| coverage                   | 40.8 ms                                                     | 43.4 ms: 1.06x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.62 ms: 1.12x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.4 ms: 1.15x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 907 us: 1.21x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (5): json, json_loads, scimark_sparse_mat_mult, aiohttp, pycparser
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240601-3.13.0b1+-edb6883/bm-20240601-pythonperf1-amd64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown