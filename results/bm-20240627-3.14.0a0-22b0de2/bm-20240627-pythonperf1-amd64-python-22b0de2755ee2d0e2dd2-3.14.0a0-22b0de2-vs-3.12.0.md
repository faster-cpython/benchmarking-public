# Results vs. 3.12.0

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: windows-amd64
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.01x slower
- HPT reliability: 98.97%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 82.7 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 247 ms: 1.48x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 198 ms: 1.44x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 539 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 218 ms: 1.34x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                       |
| async_tree_io              | 731 ms                                                      | 570 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 392 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 387 ms: 1.26x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| float          | 56.8 ms                                                     | 58.3 ms: 1.03x slower                                                      |
| nbody          | 71.9 ms                                                     | 83.8 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 88.1 ms: 1.01x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.5 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 67.7 ms: 1.04x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.00 ms: 1.05x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 59.5 ms: 1.07x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 214 us: 1.09x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 42.1 ms: 1.12x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.62 sec: 1.18x slower                                                     |
| unpickle_pure_python | 133 us                                                      | 161 us: 1.21x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.0 ms: 1.04x slower                                                      |
| python_startup         | 19.5 ms                                                     | 20.7 ms: 1.06x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.7 ms: 1.08x slower                                                      |
| mako            | 7.09 ms                                                     | 7.87 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 247 ms: 1.48x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 198 ms: 1.44x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 539 ms: 1.43x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.57 sec: 1.34x faster                                                     |
| async_tree_none            | 291 ms                                                      | 218 ms: 1.34x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                       |
| deepcopy                   | 238 us                                                      | 185 us: 1.29x faster                                                       |
| async_tree_io              | 731 ms                                                      | 570 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 392 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 387 ms: 1.26x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.5 us: 1.13x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 771 us: 1.11x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.8 us: 1.09x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 82.7 ms: 1.08x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 75.4 ms: 1.07x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 66.0 ms: 1.05x faster                                                      |
| raytrace                   | 192 ms                                                      | 186 ms: 1.03x faster                                                       |
| json                       | 3.05 ms                                                     | 2.96 ms: 1.03x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.8 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| sympy_str                  | 175 ms                                                      | 173 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 188 ms: 1.01x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 88.1 ms: 1.01x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| sqlglot_optimize           | 34.5 ms                                                     | 35.2 ms: 1.02x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| float                      | 56.8 ms                                                     | 58.3 ms: 1.03x slower                                                      |
| chaos                      | 43.3 ms                                                     | 44.6 ms: 1.03x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 64.8 ms: 1.03x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| generators                 | 22.5 ms                                                     | 23.3 ms: 1.04x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                     |
| xml_etree_iterparse        | 65.2 ms                                                     | 67.7 ms: 1.04x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 77.5 ms: 1.04x slower                                                      |
| sympy_expand               | 284 ms                                                      | 295 ms: 1.04x slower                                                       |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.0 ms: 1.04x slower                                                      |
| go                         | 91.6 ms                                                     | 95.8 ms: 1.05x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.27 ms: 1.05x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.00 ms: 1.05x slower                                                      |
| python_startup             | 19.5 ms                                                     | 20.7 ms: 1.06x slower                                                      |
| async_generators           | 239 ms                                                      | 255 ms: 1.07x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 59.5 ms: 1.07x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.7 ms: 1.08x slower                                                      |
| richards_super             | 32.1 ms                                                     | 34.7 ms: 1.08x slower                                                      |
| pycparser                  | 699 ms                                                      | 761 ms: 1.09x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 214 us: 1.09x slower                                                       |
| richards                   | 28.4 ms                                                     | 31.1 ms: 1.10x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 66.3 ns: 1.10x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.15 sec: 1.10x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 564 ms: 1.10x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 53.5 ms: 1.10x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.13 ms: 1.10x slower                                                      |
| mako                       | 7.09 ms                                                     | 7.87 ms: 1.11x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.56 ms: 1.11x slower                                                      |
| pyflate                    | 295 ms                                                      | 328 ms: 1.11x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 42.1 ms: 1.12x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 74.7 ms: 1.12x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 911 us: 1.13x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.4 ms: 1.14x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 67.5 ms: 1.15x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 16.5 ms: 1.16x slower                                                      |
| nbody                      | 71.9 ms                                                     | 83.8 ms: 1.17x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 92.0 ms: 1.17x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.62 sec: 1.18x slower                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 51.9 ms: 1.19x slower                                                      |
| scimark_fft                | 184 ms                                                      | 220 ms: 1.19x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 902 us: 1.20x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.09 ms: 1.21x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 161 us: 1.21x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.03 ms: 1.22x slower                                                      |
| fannkuch                   | 247 ms                                                      | 311 ms: 1.26x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (6): asyncio_tcp, regex_dna, logging_simple, xml_etree_parse, regex_effbot, logging_format
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240627-3.14.0a0-22b0de2/bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.97% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown