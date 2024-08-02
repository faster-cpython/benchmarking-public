# Results vs. 3.12.0

- fork: zooba
- ref: cfg
- machine: windows-amd64
- commit hash: 7466cb2
- commit date: 2024-05-20
- overall geometric mean: 1.00x slower
- HPT reliability: 58.34%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 215 ms: 1.01x faster                                     |
| chameleon      | 4.98 ms                                                     | 5.03 ms: 1.01x slower                                    |
| docutils       | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                   |
| tornado_http   | 89.5 ms                                                     | 86.1 ms: 1.04x faster                                    |
| Geometric mean | (ref)                                                       | 1.00x slower                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 279 ms: 1.31x faster                                     |
| async_tree_none_tg         | 285 ms                                                      | 220 ms: 1.30x faster                                     |
| async_tree_none            | 291 ms                                                      | 234 ms: 1.24x faster                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 405 ms: 1.24x faster                                     |
| async_tree_io_tg           | 771 ms                                                      | 640 ms: 1.21x faster                                     |
| async_tree_memoization     | 339 ms                                                      | 282 ms: 1.20x faster                                     |
| async_tree_io              | 731 ms                                                      | 618 ms: 1.18x faster                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 420 ms: 1.16x faster                                     |
| Geometric mean             | (ref)                                                       | 1.23x faster                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| float          | 56.8 ms                                                     | 55.6 ms: 1.02x faster                                    |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                     |
| nbody          | 71.9 ms                                                     | 72.4 ms: 1.01x slower                                    |
| Geometric mean | (ref)                                                       | 1.01x faster                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                     |
| regex_compile  | 87.5 ms                                                     | 85.5 ms: 1.02x faster                                    |
| regex_effbot   | 1.62 ms                                                     | 1.66 ms: 1.02x slower                                    |
| regex_v8       | 14.2 ms                                                     | 15.0 ms: 1.05x slower                                    |
| Geometric mean | (ref)                                                       | 1.00x faster                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.23 us: 1.03x faster                                    |
| pickle_pure_python   | 195 us                                                      | 192 us: 1.02x faster                                     |
| pickle_dict          | 18.4 us                                                     | 18.7 us: 1.01x slower                                    |
| unpickle_pure_python | 133 us                                                      | 137 us: 1.03x slower                                     |
| xml_etree_generate   | 55.8 ms                                                     | 58.2 ms: 1.04x slower                                    |
| xml_etree_process    | 37.7 ms                                                     | 39.7 ms: 1.05x slower                                    |
| unpickle_list        | 2.75 us                                                     | 2.90 us: 1.05x slower                                    |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.06x slower                                    |
| json_dumps           | 5.70 ms                                                     | 6.08 ms: 1.07x slower                                    |
| tomli_loads          | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                   |
| xml_etree_iterparse  | 65.2 ms                                                     | 70.9 ms: 1.09x slower                                    |
| unpickle             | 8.18 us                                                     | 9.08 us: 1.11x slower                                    |
| pickle_list          | 2.83 us                                                     | 3.14 us: 1.11x slower                                    |
| xml_etree_parse      | 93.0 ms                                                     | 104 ms: 1.12x slower                                     |
| Geometric mean       | (ref)                                                       | 1.05x slower                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                    |
| python_startup         | 19.5 ms                                                     | 21.7 ms: 1.12x slower                                    |
| Geometric mean         | (ref)                                                       | 1.11x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| mako           | 7.09 ms                                                     | 6.96 ms: 1.02x faster                                    |
| Geometric mean | (ref)                                                       | 1.01x faster                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.51 sec: 1.39x faster                                   |
| async_tree_memoization_tg  | 367 ms                                                      | 279 ms: 1.31x faster                                     |
| async_tree_none_tg         | 285 ms                                                      | 220 ms: 1.30x faster                                     |
| comprehensions             | 14.1 us                                                     | 11.1 us: 1.28x faster                                    |
| async_tree_none            | 291 ms                                                      | 234 ms: 1.24x faster                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 405 ms: 1.24x faster                                     |
| async_tree_io_tg           | 771 ms                                                      | 640 ms: 1.21x faster                                     |
| async_tree_memoization     | 339 ms                                                      | 282 ms: 1.20x faster                                     |
| async_tree_io              | 731 ms                                                      | 618 ms: 1.18x faster                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 420 ms: 1.16x faster                                     |
| raytrace                   | 192 ms                                                      | 166 ms: 1.16x faster                                     |
| generators                 | 22.5 ms                                                     | 20.1 ms: 1.12x faster                                    |
| chaos                      | 43.3 ms                                                     | 39.5 ms: 1.10x faster                                    |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                    |
| go                         | 91.6 ms                                                     | 85.9 ms: 1.07x faster                                    |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                     |
| nqueens                    | 62.8 ms                                                     | 59.4 ms: 1.06x faster                                    |
| deltablue                  | 2.16 ms                                                     | 2.07 ms: 1.04x faster                                    |
| logging_format             | 6.72 us                                                     | 6.44 us: 1.04x faster                                    |
| logging_simple             | 6.28 us                                                     | 6.01 us: 1.04x faster                                    |
| logging_silent             | 60.5 ns                                                     | 58.1 ns: 1.04x faster                                    |
| tornado_http               | 89.5 ms                                                     | 86.1 ms: 1.04x faster                                    |
| sqlite_synth               | 1.76 us                                                     | 1.69 us: 1.04x faster                                    |
| pickle                     | 7.43 us                                                     | 7.23 us: 1.03x faster                                    |
| regex_compile              | 87.5 ms                                                     | 85.5 ms: 1.02x faster                                    |
| float                      | 56.8 ms                                                     | 55.6 ms: 1.02x faster                                    |
| mako                       | 7.09 ms                                                     | 6.96 ms: 1.02x faster                                    |
| richards_super             | 32.1 ms                                                     | 31.5 ms: 1.02x faster                                    |
| pickle_pure_python         | 195 us                                                      | 192 us: 1.02x faster                                     |
| pycparser                  | 699 ms                                                      | 687 ms: 1.02x faster                                     |
| sqlglot_parse              | 804 us                                                      | 792 us: 1.02x faster                                     |
| hexiom                     | 4.10 ms                                                     | 4.04 ms: 1.02x faster                                    |
| deepcopy                   | 238 us                                                      | 235 us: 1.01x faster                                     |
| sqlglot_normalize          | 187 ms                                                      | 184 ms: 1.01x faster                                     |
| 2to3                       | 218 ms                                                      | 215 ms: 1.01x faster                                     |
| richards                   | 28.4 ms                                                     | 28.1 ms: 1.01x faster                                    |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                     |
| sqlglot_transpile          | 1.02 ms                                                     | 1.01 ms: 1.01x faster                                    |
| pathlib                    | 80.5 ms                                                     | 79.8 ms: 1.01x faster                                    |
| meteor_contest             | 74.6 ms                                                     | 74.3 ms: 1.00x faster                                    |
| nbody                      | 71.9 ms                                                     | 72.4 ms: 1.01x slower                                    |
| sympy_sum                  | 91.5 ms                                                     | 92.3 ms: 1.01x slower                                    |
| pprint_pformat             | 1.05 sec                                                    | 1.05 sec: 1.01x slower                                   |
| pprint_safe_repr           | 513 ms                                                      | 518 ms: 1.01x slower                                     |
| chameleon                  | 4.98 ms                                                     | 5.03 ms: 1.01x slower                                    |
| pickle_dict                | 18.4 us                                                     | 18.7 us: 1.01x slower                                    |
| sqlglot_optimize           | 34.5 ms                                                     | 35.0 ms: 1.02x slower                                    |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                    |
| bench_mp_pool              | 69.2 ms                                                     | 70.6 ms: 1.02x slower                                    |
| pyflate                    | 295 ms                                                      | 302 ms: 1.02x slower                                     |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                     |
| regex_effbot               | 1.62 ms                                                     | 1.66 ms: 1.02x slower                                    |
| unpickle_pure_python       | 133 us                                                      | 137 us: 1.03x slower                                     |
| crypto_pyaes               | 48.5 ms                                                     | 50.1 ms: 1.03x slower                                    |
| xml_etree_generate         | 55.8 ms                                                     | 58.2 ms: 1.04x slower                                    |
| spectral_norm              | 66.9 ms                                                     | 70.0 ms: 1.05x slower                                    |
| docutils                   | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                   |
| deepcopy_memo              | 23.7 us                                                     | 24.9 us: 1.05x slower                                    |
| regex_v8                   | 14.2 ms                                                     | 15.0 ms: 1.05x slower                                    |
| xml_etree_process          | 37.7 ms                                                     | 39.7 ms: 1.05x slower                                    |
| json                       | 3.05 ms                                                     | 3.21 ms: 1.05x slower                                    |
| unpickle_list              | 2.75 us                                                     | 2.90 us: 1.05x slower                                    |
| async_generators           | 239 ms                                                      | 253 ms: 1.06x slower                                     |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.06x slower                                    |
| scimark_sor                | 78.8 ms                                                     | 83.8 ms: 1.06x slower                                    |
| json_dumps                 | 5.70 ms                                                     | 6.08 ms: 1.07x slower                                    |
| tomli_loads                | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                   |
| fannkuch                   | 247 ms                                                      | 265 ms: 1.07x slower                                     |
| sympy_expand               | 284 ms                                                      | 307 ms: 1.08x slower                                     |
| scimark_lu                 | 58.9 ms                                                     | 63.9 ms: 1.09x slower                                    |
| xml_etree_iterparse        | 65.2 ms                                                     | 70.9 ms: 1.09x slower                                    |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                    |
| unpickle                   | 8.18 us                                                     | 9.08 us: 1.11x slower                                    |
| pickle_list                | 2.83 us                                                     | 3.14 us: 1.11x slower                                    |
| python_startup             | 19.5 ms                                                     | 21.7 ms: 1.12x slower                                    |
| xml_etree_parse            | 93.0 ms                                                     | 104 ms: 1.12x slower                                     |
| typing_runtime_protocols   | 95.1 us                                                     | 109 us: 1.15x slower                                     |
| coverage                   | 40.8 ms                                                     | 46.9 ms: 1.15x slower                                    |
| scimark_fft                | 184 ms                                                      | 212 ms: 1.15x slower                                     |
| mdp                        | 1.37 sec                                                    | 1.61 sec: 1.17x slower                                   |
| telco                      | 4.13 ms                                                     | 5.05 ms: 1.22x slower                                    |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.14 ms: 1.23x slower                                    |
| create_gc_cycles           | 752 us                                                      | 1.08 ms: 1.43x slower                                    |
| gc_traversal               | 1.52 ms                                                     | 2.80 ms: 1.84x slower                                    |
| Geometric mean             | (ref)                                                       | 1.00x slower                                             |

Benchmark hidden because not significant (5): asyncio_tcp, bench_thread_pool, scimark_monte_carlo, django_template, deepcopy_reduce
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240520-3.14.0a0-7466cb2/bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 58.34% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown