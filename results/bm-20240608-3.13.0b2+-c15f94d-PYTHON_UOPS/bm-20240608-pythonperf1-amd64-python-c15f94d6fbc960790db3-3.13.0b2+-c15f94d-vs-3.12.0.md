# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-amd64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.02x slower
- HPT reliability: 97.94%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 232 ms: 1.06x slower                                                        |
| chameleon      | 4.98 ms                                                     | 5.12 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.84 sec: 1.11x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 87.8 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 275 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 218 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 388 ms: 1.29x faster                                                        |
| async_tree_none            | 291 ms                                                      | 233 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 622 ms: 1.24x faster                                                        |
| async_tree_io              | 731 ms                                                      | 593 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 400 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 282 ms: 1.20x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 52.6 ms: 1.08x faster                                                       |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| nbody          | 71.9 ms                                                     | 73.8 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.0 ms: 1.05x slower                                                       |
| regex_compile  | 87.5 ms                                                     | 106 ms: 1.21x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.17 us: 1.04x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                       |
| pickle_list          | 2.83 us                                                     | 2.86 us: 1.01x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 5.81 ms: 1.02x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.84 us: 1.03x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.51 us: 1.04x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 39.4 ms: 1.04x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.08x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 156 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.34 ms: 1.04x slower                                                       |
| django_template | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.39 sec: 1.51x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 275 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 218 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 388 ms: 1.29x faster                                                        |
| async_tree_none            | 291 ms                                                      | 233 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 622 ms: 1.24x faster                                                        |
| async_tree_io              | 731 ms                                                      | 593 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 400 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 282 ms: 1.20x faster                                                        |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.15x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 12.6 ms: 1.13x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.10x faster                                                       |
| float                      | 56.8 ms                                                     | 52.6 ms: 1.08x faster                                                       |
| comprehensions             | 14.1 us                                                     | 13.3 us: 1.07x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.8 ms: 1.06x faster                                                       |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                        |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| json                       | 3.05 ms                                                     | 2.92 ms: 1.04x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.17 us: 1.04x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 67.0 ms: 1.03x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 475 ms: 1.03x faster                                                        |
| logging_format             | 6.72 us                                                     | 6.56 us: 1.02x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 91.0 ms: 1.02x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 87.8 ms: 1.02x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.16 us: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| chaos                      | 43.3 ms                                                     | 43.1 ms: 1.01x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 44.1 ms: 1.00x faster                                                       |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                       |
| pickle_list                | 2.83 us                                                     | 2.86 us: 1.01x slower                                                       |
| async_generators           | 239 ms                                                      | 243 ms: 1.01x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 5.81 ms: 1.02x slower                                                       |
| scimark_fft                | 184 ms                                                      | 189 ms: 1.02x slower                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 49.6 ms: 1.02x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 76.4 ms: 1.02x slower                                                       |
| nbody                      | 71.9 ms                                                     | 73.8 ms: 1.03x slower                                                       |
| chameleon                  | 4.98 ms                                                     | 5.12 ms: 1.03x slower                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.16 us: 1.03x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.84 us: 1.03x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.3 ms: 1.03x slower                                                       |
| richards_super             | 32.1 ms                                                     | 33.2 ms: 1.03x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                       |
| mako                       | 7.09 ms                                                     | 7.34 ms: 1.04x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.04x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.51 us: 1.04x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.4 ms: 1.04x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 536 ms: 1.04x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| python_startup             | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.0 ms: 1.05x slower                                                       |
| aiohttp                    | 884 us                                                      | 933 us: 1.06x slower                                                        |
| nqueens                    | 62.8 ms                                                     | 66.6 ms: 1.06x slower                                                       |
| 2to3                       | 218 ms                                                      | 232 ms: 1.06x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                      |
| coverage                   | 40.8 ms                                                     | 43.7 ms: 1.07x slower                                                       |
| deepcopy                   | 238 us                                                      | 255 us: 1.07x slower                                                        |
| fannkuch                   | 247 ms                                                      | 265 ms: 1.07x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.0 ms: 1.07x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 98.4 ms: 1.07x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.08x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 85.7 ms: 1.09x slower                                                       |
| pyflate                    | 295 ms                                                      | 321 ms: 1.09x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.10x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 881 us: 1.10x slower                                                        |
| sympy_str                  | 175 ms                                                      | 194 ms: 1.11x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.84 sec: 1.11x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 74.1 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 38.3 ms: 1.11x slower                                                       |
| go                         | 91.6 ms                                                     | 102 ms: 1.11x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.6 ms: 1.12x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 68.3 ns: 1.13x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.70 ms: 1.14x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.94 ms: 1.15x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 156 us: 1.17x slower                                                        |
| sympy_expand               | 284 ms                                                      | 335 ms: 1.18x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.55 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.19x slower                                                        |
| deepcopy_memo              | 23.7 us                                                     | 28.5 us: 1.20x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 106 ms: 1.21x slower                                                        |
| create_gc_cycles           | 752 us                                                      | 917 us: 1.22x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 73.6 ms: 1.25x slower                                                       |
| pycparser                  | 699 ms                                                      | 876 ms: 1.25x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 5.18 ms: 1.26x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (5): mypy2, bench_thread_pool, xml_etree_iterparse, pickle_dict, python_startup_no_site
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.94% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown