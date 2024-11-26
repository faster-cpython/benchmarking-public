# Results vs. 3.12.0

- fork: python
- ref: c8db0e817e7e0db50153
- machine: windows-amd64
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.027x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 228 ms: 1.04x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 92.7 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 251 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.40x faster                                                       |
| async_tree_none            | 291 ms                                                      | 210 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 565 ms: 1.36x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 260 ms: 1.31x faster                                                       |
| async_tree_io              | 731 ms                                                      | 576 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 400 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.33x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 87.6 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 15.0 ms: 1.05x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 93.0 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 18.4 us                                                     | 18.3 us: 1.00x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 94.4 ms: 1.01x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.88 us: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.6 ms: 1.02x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.83 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 59.5 ms: 1.07x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 42.1 ms: 1.12x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 218 us: 1.12x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.52 us: 1.16x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.16x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.62 sec: 1.19x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.6 ms: 1.15x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.7 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.23 ms: 1.02x slower                                                      |
| django_template | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 251 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.40x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.50 sec: 1.39x faster                                                     |
| async_tree_none            | 291 ms                                                      | 210 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 565 ms: 1.36x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 260 ms: 1.31x faster                                                       |
| async_tree_io              | 731 ms                                                      | 576 ms: 1.27x faster                                                       |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 400 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.3 us: 1.15x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 21.5 us: 1.10x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.91 us: 1.10x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.64 us: 1.07x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.4 ms: 1.05x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 824 us: 1.04x faster                                                       |
| go                         | 91.6 ms                                                     | 88.9 ms: 1.03x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 78.4 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 43.7 ms: 1.01x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 90.4 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.3 us: 1.00x faster                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.53 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 94.4 ms: 1.01x slower                                                      |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.84 us: 1.02x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.88 us: 1.02x slower                                                      |
| mako                       | 7.09 ms                                                     | 7.23 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.6 ms: 1.02x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| logging_simple             | 6.28 us                                                     | 6.47 us: 1.03x slower                                                      |
| raytrace                   | 192 ms                                                      | 198 ms: 1.03x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.83 us: 1.03x slower                                                      |
| chaos                      | 43.3 ms                                                     | 44.8 ms: 1.03x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 92.7 ms: 1.03x slower                                                      |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 65.5 ms: 1.04x slower                                                      |
| 2to3                       | 218 ms                                                      | 228 ms: 1.04x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 195 ms: 1.04x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.9 ms: 1.05x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 72.5 ms: 1.05x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 50.9 ms: 1.05x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.0 ms: 1.05x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 93.0 ms: 1.06x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 59.5 ms: 1.07x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 79.5 ms: 1.07x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.8 ms: 1.07x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.31 ms: 1.07x slower                                                      |
| pycparser                  | 699 ms                                                      | 754 ms: 1.08x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 554 ms: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.09x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 65.9 ns: 1.09x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.14 sec: 1.09x slower                                                     |
| asyncio_tcp                | 487 ms                                                      | 534 ms: 1.09x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.52 sec: 1.11x slower                                                     |
| sqlglot_transpile          | 1.02 ms                                                     | 1.13 ms: 1.11x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.84 ms: 1.11x slower                                                      |
| pyflate                    | 295 ms                                                      | 329 ms: 1.11x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 42.1 ms: 1.12x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 218 us: 1.12x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 74.9 ms: 1.12x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 908 us: 1.13x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.63 ms: 1.13x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 42.8 ns: 1.14x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.8 ms: 1.15x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.6 ms: 1.15x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.6 ms: 1.15x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 67.9 ms: 1.15x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.16x slower                                                       |
| scimark_fft                | 184 ms                                                      | 214 ms: 1.16x slower                                                       |
| unpickle                   | 8.18 us                                                     | 9.52 us: 1.16x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.16x slower                                                       |
| python_startup             | 19.5 ms                                                     | 22.7 ms: 1.17x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 51.3 ms: 1.17x slower                                                      |
| coverage                   | 40.8 ms                                                     | 47.9 ms: 1.17x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 884 us: 1.18x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.87 ms: 1.18x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.62 sec: 1.19x slower                                                     |
| nbody                      | 71.9 ms                                                     | 87.6 ms: 1.22x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 96.2 ms: 1.22x slower                                                      |
| fannkuch                   | 247 ms                                                      | 307 ms: 1.24x slower                                                       |
| json                       | 3.05 ms                                                     | 4.15 ms: 1.36x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (2): float, pickle
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.027x slower
# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown