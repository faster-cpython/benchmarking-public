# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-amd64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.05x faster
- HPT reliability: 99.33%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 231 ms: 1.06x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 86.3 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 273 ms: 1.35x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 214 ms: 1.33x faster                                                        |
| async_tree_none            | 291 ms                                                      | 226 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 391 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 620 ms: 1.24x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                        |
| async_tree_io              | 731 ms                                                      | 595 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 400 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.27x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 50.4 ms: 1.43x faster                                                       |
| float          | 56.8 ms                                                     | 44.3 ms: 1.28x faster                                                       |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 88.0 ms: 1.01x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 16.9 ms: 1.19x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 171 us: 1.14x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 52.4 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.4 ms: 1.06x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 126 us: 1.06x faster                                                        |
| pickle_dict          | 18.4 us                                                     | 17.6 us: 1.05x faster                                                       |
| pickle               | 7.43 us                                                     | 7.18 us: 1.04x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 90.7 ms: 1.03x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 37.0 ms: 1.02x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.70 us: 1.02x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.77 ms: 1.01x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.02x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.50 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.09x slower                                                       |
| python_startup         | 19.5 ms                                                     | 21.9 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.07 ms: 1.40x faster                                                       |
| django_template | 22.9 ms                                                     | 25.6 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| spectral_norm              | 66.9 ms                                                     | 44.4 ms: 1.51x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.46 sec: 1.44x faster                                                      |
| nbody                      | 71.9 ms                                                     | 50.4 ms: 1.43x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.07 ms: 1.40x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.38x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 273 ms: 1.35x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 214 ms: 1.33x faster                                                        |
| async_tree_none            | 291 ms                                                      | 226 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 391 ms: 1.28x faster                                                        |
| float                      | 56.8 ms                                                     | 44.3 ms: 1.28x faster                                                       |
| scimark_fft                | 184 ms                                                      | 148 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 620 ms: 1.24x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                        |
| async_tree_io              | 731 ms                                                      | 595 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 400 ms: 1.22x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.14 ms: 1.19x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.1 us: 1.18x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 41.4 ms: 1.17x faster                                                       |
| fannkuch                   | 247 ms                                                      | 211 ms: 1.17x faster                                                        |
| pyflate                    | 295 ms                                                      | 257 ms: 1.14x faster                                                        |
| pickle_pure_python         | 195 us                                                      | 171 us: 1.14x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.4 ms: 1.11x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 462 ms: 1.11x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 947 ms: 1.10x faster                                                        |
| chaos                      | 43.3 ms                                                     | 39.3 ms: 1.10x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.5 ms: 1.09x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.78 us: 1.09x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.24 us: 1.08x faster                                                       |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 56.5 ns: 1.07x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 52.4 ms: 1.06x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.7 ms: 1.06x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 59.1 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.4 ms: 1.06x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 126 us: 1.06x faster                                                        |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                        |
| generators                 | 22.5 ms                                                     | 21.5 ms: 1.05x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 17.6 us: 1.05x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 824 us: 1.04x faster                                                        |
| tornado_http               | 89.5 ms                                                     | 86.3 ms: 1.04x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.18 us: 1.04x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 474 ms: 1.03x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 90.7 ms: 1.03x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.8 ms: 1.02x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 37.0 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| unpickle_list              | 2.75 us                                                     | 2.70 us: 1.02x faster                                                       |
| deepcopy                   | 238 us                                                      | 237 us: 1.01x faster                                                        |
| sqlglot_parse              | 804 us                                                      | 800 us: 1.01x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 88.0 ms: 1.01x slower                                                       |
| richards_super             | 32.1 ms                                                     | 32.3 ms: 1.01x slower                                                       |
| richards                   | 28.4 ms                                                     | 28.6 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.03 ms: 1.01x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.77 ms: 1.01x slower                                                       |
| go                         | 91.6 ms                                                     | 93.6 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.02x slower                                                       |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.03x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 93.9 ms: 1.03x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 81.1 ms: 1.03x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.50 us: 1.04x slower                                                       |
| async_generators           | 239 ms                                                      | 249 ms: 1.04x slower                                                        |
| aiohttp                    | 884 us                                                      | 929 us: 1.05x slower                                                        |
| 2to3                       | 218 ms                                                      | 231 ms: 1.06x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 36.7 ms: 1.06x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.49 ms: 1.09x slower                                                       |
| pycparser                  | 699 ms                                                      | 762 ms: 1.09x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 14.1 ms: 1.09x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.09x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.37 ms: 1.10x slower                                                       |
| sympy_expand               | 284 ms                                                      | 312 ms: 1.10x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.12x slower                                                       |
| python_startup             | 19.5 ms                                                     | 21.9 ms: 1.13x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.66 ms: 1.14x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.8 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 69.0 ms: 1.17x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.9 ms: 1.19x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 924 us: 1.23x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (6): mypy2, pickle_list, chameleon, json, deepcopy_reduce, bench_mp_pool
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.33% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown