# Results vs. 3.12.0

- fork: python
- ref: 6b10467fbc0b67bf217e
- machine: windows-amd64
- commit hash: 6b10467
- commit date: 2024-06-03
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 207 ms: 1.05x faster                                                        |
| chameleon      | 4.98 ms                                                     | 4.70 ms: 1.06x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                      |
| tornado_http   | 89.5 ms                                                     | 82.1 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 263 ms: 1.39x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                        |
| async_tree_none            | 291 ms                                                      | 216 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 263 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 607 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 388 ms: 1.26x faster                                                        |
| async_tree_io              | 731 ms                                                      | 580 ms: 1.26x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 50.6 ms: 1.12x faster                                                       |
| nbody          | 71.9 ms                                                     | 67.2 ms: 1.07x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.0 ms: 1.14x faster                                                       |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 175 us: 1.11x faster                                                        |
| unpickle_pure_python | 133 us                                                      | 123 us: 1.09x faster                                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.8 ms: 1.06x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 53.3 ms: 1.05x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                       |
| pickle               | 7.43 us                                                     | 7.19 us: 1.03x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.55 ms: 1.03x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.68 us: 1.02x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.3 ms: 1.02x faster                                                       |
| json_loads           | 13.9 us                                                     | 13.7 us: 1.01x faster                                                       |
| unpickle             | 8.18 us                                                     | 8.44 us: 1.03x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.03 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (2): tomli_loads, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 16.5 ms: 1.02x slower                                                       |
| python_startup         | 19.5 ms                                                     | 20.4 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.36 ms: 1.11x faster                                                       |
| django_template | 22.9 ms                                                     | 21.6 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.44 sec: 1.46x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 263 ms: 1.39x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                        |
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.36x faster                                                       |
| async_tree_none            | 291 ms                                                      | 216 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 263 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 607 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 388 ms: 1.26x faster                                                        |
| async_tree_io              | 731 ms                                                      | 580 ms: 1.26x faster                                                        |
| mypy2                      | 509 ms                                                      | 419 ms: 1.22x faster                                                        |
| raytrace                   | 192 ms                                                      | 159 ms: 1.21x faster                                                        |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 52.4 ns: 1.16x faster                                                       |
| chaos                      | 43.3 ms                                                     | 37.6 ms: 1.15x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 38.5 ms: 1.15x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.89 ms: 1.14x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 77.0 ms: 1.14x faster                                                       |
| float                      | 56.8 ms                                                     | 50.6 ms: 1.12x faster                                                       |
| go                         | 91.6 ms                                                     | 82.0 ms: 1.12x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.36 ms: 1.11x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 175 us: 1.11x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 12.8 ms: 1.11x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.4 ms: 1.11x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.70 ms: 1.11x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 56.7 ms: 1.11x faster                                                       |
| scimark_fft                | 184 ms                                                      | 167 ms: 1.10x faster                                                        |
| richards                   | 28.4 ms                                                     | 25.7 ms: 1.10x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.71 us: 1.10x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.13 us: 1.10x faster                                                       |
| richards_super             | 32.1 ms                                                     | 29.3 ms: 1.10x faster                                                       |
| deepcopy                   | 238 us                                                      | 218 us: 1.09x faster                                                        |
| tornado_http               | 89.5 ms                                                     | 82.1 ms: 1.09x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 54.1 ms: 1.09x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 44.6 ms: 1.09x faster                                                       |
| sympy_str                  | 175 ms                                                      | 161 ms: 1.09x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 123 us: 1.09x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 84.6 ms: 1.08x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 794 us: 1.08x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 74.8 ms: 1.08x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 174 ms: 1.07x faster                                                        |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 62.4 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.39 ms: 1.07x faster                                                       |
| async_generators           | 239 ms                                                      | 223 ms: 1.07x faster                                                        |
| nbody                      | 71.9 ms                                                     | 67.2 ms: 1.07x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 22.3 us: 1.07x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 65.1 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 483 ms: 1.06x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 74.1 ms: 1.06x faster                                                       |
| chameleon                  | 4.98 ms                                                     | 4.70 ms: 1.06x faster                                                       |
| django_template            | 22.9 ms                                                     | 21.6 ms: 1.06x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.98 us: 1.06x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 987 ms: 1.06x faster                                                        |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.8 ms: 1.06x faster                                                       |
| pyflate                    | 295 ms                                                      | 279 ms: 1.05x faster                                                        |
| 2to3                       | 218 ms                                                      | 207 ms: 1.05x faster                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 971 us: 1.05x faster                                                        |
| sqlglot_parse              | 804 us                                                      | 768 us: 1.05x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 53.3 ms: 1.05x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 33.0 ms: 1.05x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.0 ms: 1.04x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.19 us: 1.03x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 472 ms: 1.03x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                      |
| sympy_expand               | 284 ms                                                      | 276 ms: 1.03x faster                                                        |
| json_dumps                 | 5.70 ms                                                     | 5.55 ms: 1.03x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.68 us: 1.02x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 91.3 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| json_loads                 | 13.9 us                                                     | 13.7 us: 1.01x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                       |
| fannkuch                   | 247 ms                                                      | 250 ms: 1.01x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 16.5 ms: 1.02x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.44 us: 1.03x slower                                                       |
| python_startup             | 19.5 ms                                                     | 20.4 ms: 1.05x slower                                                       |
| coverage                   | 40.8 ms                                                     | 43.2 ms: 1.06x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.07x slower                                                        |
| pickle_list                | 2.83 us                                                     | 3.03 us: 1.07x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.60 ms: 1.11x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 906 us: 1.20x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (5): json, tomli_loads, pickle_dict, aiohttp, pycparser
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240603-3.13.0b1+-6b10467/bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown