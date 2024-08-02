# Results vs. 3.12.0

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-amd64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 208 ms: 1.05x faster                                                        |
| chameleon      | 4.98 ms                                                     | 4.71 ms: 1.06x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                      |
| tornado_http   | 89.5 ms                                                     | 81.6 ms: 1.10x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 262 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 204 ms: 1.39x faster                                                        |
| async_tree_none            | 291 ms                                                      | 216 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 265 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 609 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 390 ms: 1.25x faster                                                        |
| async_tree_io              | 731 ms                                                      | 588 ms: 1.24x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 48.2 ms: 1.18x faster                                                       |
| nbody          | 71.9 ms                                                     | 66.2 ms: 1.09x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 76.9 ms: 1.14x faster                                                       |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 173 us: 1.13x faster                                                        |
| unpickle_pure_python | 133 us                                                      | 120 us: 1.11x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 52.9 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.62 us: 1.05x faster                                                       |
| pickle               | 7.43 us                                                     | 7.18 us: 1.04x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.57 ms: 1.02x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.3 ms: 1.02x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.01x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.45 us: 1.03x slower                                                       |
| pickle_list          | 2.83 us                                                     | 2.94 us: 1.04x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.4 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 19.5 ms                                                     | 20.2 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.28 ms: 1.13x faster                                                       |
| django_template | 22.9 ms                                                     | 21.1 ms: 1.09x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| comprehensions             | 14.1 us                                                     | 10.1 us: 1.40x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 262 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 204 ms: 1.39x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.55 sec: 1.35x faster                                                      |
| async_tree_none            | 291 ms                                                      | 216 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 265 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 609 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 390 ms: 1.25x faster                                                        |
| async_tree_io              | 731 ms                                                      | 588 ms: 1.24x faster                                                        |
| mypy2                      | 509 ms                                                      | 417 ms: 1.22x faster                                                        |
| raytrace                   | 192 ms                                                      | 161 ms: 1.20x faster                                                        |
| float                      | 56.8 ms                                                     | 48.2 ms: 1.18x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.3 ms: 1.16x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 52.8 ns: 1.15x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.90 ms: 1.14x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 76.9 ms: 1.14x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.2 ms: 1.13x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 39.1 ms: 1.13x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 55.5 ms: 1.13x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 173 us: 1.13x faster                                                        |
| mako                       | 7.09 ms                                                     | 6.28 ms: 1.13x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.64 ms: 1.13x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 12.7 ms: 1.12x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.1 ms: 1.12x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 60.1 ms: 1.11x faster                                                       |
| sympy_str                  | 175 ms                                                      | 158 ms: 1.11x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 120 us: 1.11x faster                                                        |
| richards                   | 28.4 ms                                                     | 25.8 ms: 1.10x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 170 ms: 1.10x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 467 ms: 1.10x faster                                                        |
| tornado_http               | 89.5 ms                                                     | 81.6 ms: 1.10x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.12 us: 1.10x faster                                                       |
| go                         | 91.6 ms                                                     | 83.5 ms: 1.10x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 53.7 ms: 1.10x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.73 us: 1.10x faster                                                       |
| richards_super             | 32.1 ms                                                     | 29.3 ms: 1.09x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.09x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 83.8 ms: 1.09x faster                                                       |
| deepcopy                   | 238 us                                                      | 218 us: 1.09x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 21.7 us: 1.09x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 959 ms: 1.09x faster                                                        |
| django_template            | 22.9 ms                                                     | 21.1 ms: 1.09x faster                                                       |
| nbody                      | 71.9 ms                                                     | 66.2 ms: 1.09x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 44.9 ms: 1.08x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 73.1 ms: 1.08x faster                                                       |
| sqlglot_parse              | 804 us                                                      | 749 us: 1.07x faster                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 954 us: 1.07x faster                                                        |
| scimark_fft                | 184 ms                                                      | 172 ms: 1.07x faster                                                        |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                        |
| sympy_integrate            | 13.0 ms                                                     | 12.1 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.39 ms: 1.07x faster                                                       |
| pyflate                    | 295 ms                                                      | 276 ms: 1.07x faster                                                        |
| sympy_expand               | 284 ms                                                      | 267 ms: 1.06x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 808 us: 1.06x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.97 us: 1.06x faster                                                       |
| chameleon                  | 4.98 ms                                                     | 4.71 ms: 1.06x faster                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 32.6 ms: 1.06x faster                                                       |
| async_generators           | 239 ms                                                      | 226 ms: 1.06x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 52.9 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 71.0 ms: 1.05x faster                                                       |
| 2to3                       | 218 ms                                                      | 208 ms: 1.05x faster                                                        |
| unpickle_list              | 2.75 us                                                     | 2.62 us: 1.05x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 66.2 ms: 1.05x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.18 us: 1.04x faster                                                       |
| fannkuch                   | 247 ms                                                      | 238 ms: 1.03x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                      |
| mdp                        | 1.37 sec                                                    | 1.33 sec: 1.03x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.57 ms: 1.02x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 91.3 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 79.3 ms: 1.02x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                      |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.01x slower                                                       |
| aiohttp                    | 884 us                                                      | 894 us: 1.01x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.45 us: 1.03x slower                                                       |
| python_startup             | 19.5 ms                                                     | 20.2 ms: 1.04x slower                                                       |
| pickle_list                | 2.83 us                                                     | 2.94 us: 1.04x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 100 us: 1.05x slower                                                        |
| pickle_dict                | 18.4 us                                                     | 19.4 us: 1.05x slower                                                       |
| coverage                   | 40.8 ms                                                     | 43.5 ms: 1.06x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.59 ms: 1.11x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 566 ms: 1.16x slower                                                        |
| create_gc_cycles           | 752 us                                                      | 903 us: 1.20x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (3): pycparser, python_startup_no_site, json
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown