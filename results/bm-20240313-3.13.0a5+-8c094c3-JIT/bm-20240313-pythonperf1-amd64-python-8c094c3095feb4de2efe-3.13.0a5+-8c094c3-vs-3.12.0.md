# Results vs. 3.12.0

- fork: python
- ref: 8c094c3095feb4de2efe
- machine: windows-amd64
- commit hash: 8c094c3
- commit date: 2024-03-13
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                        |
| chameleon      | 4.98 ms                                                     | 4.76 ms: 1.05x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                      |
| tornado_http   | 89.5 ms                                                     | 85.0 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 260 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 446 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 462 ms: 1.09x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 341 ms: 1.07x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 267 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 743 ms: 1.04x faster                                                        |
| async_tree_io              | 731 ms                                                      | 716 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 58.7 ms: 1.22x faster                                                       |
| float          | 56.8 ms                                                     | 47.8 ms: 1.19x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 83.1 ms: 1.05x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 17.3 ms: 1.22x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 178 us: 1.10x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 53.2 ms: 1.05x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 127 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.3 ms: 1.05x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.49 ms: 1.04x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 17.9 us: 1.03x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.9 ms: 1.02x faster                                                       |
| pickle_list          | 2.83 us                                                     | 2.77 us: 1.02x faster                                                       |
| json_loads           | 13.9 us                                                     | 13.8 us: 1.01x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                                       |
| pickle               | 7.43 us                                                     | 7.55 us: 1.02x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.64 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 24.7 ms: 1.27x slower                                                       |
| python_startup_no_site | 16.2 ms                                                     | 22.5 ms: 1.38x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.54 ms: 1.28x faster                                                       |
| django_template | 22.9 ms                                                     | 21.5 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 95.1 us                                                     | 71.1 us: 1.34x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 51.0 ms: 1.31x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.54 ms: 1.28x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.65 sec: 1.27x faster                                                      |
| nbody                      | 71.9 ms                                                     | 58.7 ms: 1.22x faster                                                       |
| float                      | 56.8 ms                                                     | 47.8 ms: 1.19x faster                                                       |
| mypy2                      | 509 ms                                                      | 436 ms: 1.17x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                      |
| fannkuch                   | 247 ms                                                      | 217 ms: 1.13x faster                                                        |
| generators                 | 22.5 ms                                                     | 19.9 ms: 1.13x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 43.3 ms: 1.12x faster                                                       |
| async_tree_none            | 291 ms                                                      | 260 ms: 1.12x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 39.7 ms: 1.12x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 466 ms: 1.10x faster                                                        |
| chaos                      | 43.3 ms                                                     | 39.4 ms: 1.10x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 178 us: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 446 ms: 1.10x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 954 ms: 1.10x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 55.5 ns: 1.09x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 462 ms: 1.09x faster                                                        |
| deepcopy                   | 238 us                                                      | 219 us: 1.09x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.93 us: 1.09x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.24 us: 1.08x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.08x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 341 ms: 1.07x faster                                                        |
| scimark_fft                | 184 ms                                                      | 172 ms: 1.07x faster                                                        |
| sympy_str                  | 175 ms                                                      | 164 ms: 1.07x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 267 ms: 1.07x faster                                                        |
| logging_simple             | 6.28 us                                                     | 5.87 us: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.39 ms: 1.07x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 175 ms: 1.07x faster                                                        |
| django_template            | 22.9 ms                                                     | 21.5 ms: 1.06x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.03 ms: 1.06x faster                                                       |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 83.1 ms: 1.05x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 85.0 ms: 1.05x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 76.6 ms: 1.05x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 53.2 ms: 1.05x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 127 us: 1.05x faster                                                        |
| chameleon                  | 4.98 ms                                                     | 4.76 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.3 ms: 1.05x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.9 ms: 1.04x faster                                                       |
| pyflate                    | 295 ms                                                      | 282 ms: 1.04x faster                                                        |
| sqlglot_parse              | 804 us                                                      | 772 us: 1.04x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 22.8 us: 1.04x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.3 ms: 1.04x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.49 ms: 1.04x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 743 ms: 1.04x faster                                                        |
| asyncio_tcp                | 487 ms                                                      | 470 ms: 1.04x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.60 sec: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.5 ms: 1.03x faster                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 991 us: 1.03x faster                                                        |
| pickle_dict                | 18.4 us                                                     | 17.9 us: 1.03x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.9 ms: 1.02x faster                                                       |
| async_tree_io              | 731 ms                                                      | 716 ms: 1.02x faster                                                        |
| pickle_list                | 2.83 us                                                     | 2.77 us: 1.02x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.6 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.50 ms: 1.01x faster                                                       |
| json_loads                 | 13.9 us                                                     | 13.8 us: 1.01x faster                                                       |
| sympy_expand               | 284 ms                                                      | 281 ms: 1.01x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                                       |
| richards                   | 28.4 ms                                                     | 28.2 ms: 1.01x faster                                                       |
| async_generators           | 239 ms                                                      | 238 ms: 1.01x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.61 ms: 1.01x faster                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 34.3 ms: 1.01x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 75.0 ms: 1.00x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.1 ms: 1.01x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.55 us: 1.02x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 70.3 ms: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| go                         | 91.6 ms                                                     | 96.1 ms: 1.05x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.32 ms: 1.05x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.64 us: 1.06x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 84.4 ms: 1.07x slower                                                       |
| json                       | 3.05 ms                                                     | 3.36 ms: 1.10x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.57 ms: 1.11x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.1 ms: 1.15x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 70.7 ms: 1.20x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 17.3 ms: 1.22x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.7 ms: 1.27x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 48.6 ns: 1.30x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 22.5 ms: 1.38x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (7): bench_thread_pool, create_gc_cycles, async_tree_memoization, regex_dna, unpickle_list, aiohttp, pycparser
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240313-3.13.0a5+-8c094c3-JIT/bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x


# Memory

- memory change: unknown