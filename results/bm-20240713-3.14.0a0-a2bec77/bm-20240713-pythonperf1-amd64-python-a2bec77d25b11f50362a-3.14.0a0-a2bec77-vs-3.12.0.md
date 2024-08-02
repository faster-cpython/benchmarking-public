# Results vs. 3.12.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-amd64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 92.49%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 81.5 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 244 ms: 1.50x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 191 ms: 1.50x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 528 ms: 1.46x faster                                                       |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.38x faster                                                       |
| async_tree_io              | 731 ms                                                      | 536 ms: 1.36x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 255 ms: 1.33x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 387 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.39x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 78.5 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 89.0 ms: 1.02x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 66.5 ms: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 58.0 ms: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 204 us: 1.04x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 5.97 ms: 1.05x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.6 ms: 1.08x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.12x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.57 sec: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.1 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.37 ms: 1.04x slower                                                      |
| django_template | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 244 ms: 1.50x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 191 ms: 1.50x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 528 ms: 1.46x faster                                                       |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.38x faster                                                       |
| async_tree_io              | 731 ms                                                      | 536 ms: 1.36x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.56 sec: 1.34x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 255 ms: 1.33x faster                                                       |
| deepcopy                   | 238 us                                                      | 181 us: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 387 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.6 us: 1.22x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.8 us: 1.14x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.13x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 81.5 ms: 1.10x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 74.1 ms: 1.09x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 793 us: 1.08x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.07x faster                                                       |
| raytrace                   | 192 ms                                                      | 181 ms: 1.06x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 65.2 ms: 1.06x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| json                       | 3.05 ms                                                     | 2.95 ms: 1.03x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.6 ms: 1.03x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 474 ms: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.60 us: 1.02x faster                                                      |
| generators                 | 22.5 ms                                                     | 22.2 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| sympy_str                  | 175 ms                                                      | 173 ms: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.21 us: 1.01x faster                                                      |
| sqlglot_normalize          | 187 ms                                                      | 185 ms: 1.01x faster                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 34.7 ms: 1.00x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.54 ms: 1.01x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| meteor_contest             | 74.6 ms                                                     | 75.7 ms: 1.01x slower                                                      |
| async_generators           | 239 ms                                                      | 243 ms: 1.01x slower                                                       |
| chaos                      | 43.3 ms                                                     | 44.0 ms: 1.02x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 89.0 ms: 1.02x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.5 ms: 1.02x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.21 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| mako                       | 7.09 ms                                                     | 7.37 ms: 1.04x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 58.0 ms: 1.04x slower                                                      |
| sympy_expand               | 284 ms                                                      | 296 ms: 1.04x slower                                                       |
| django_template            | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 204 us: 1.04x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.97 ms: 1.05x slower                                                      |
| pyflate                    | 295 ms                                                      | 309 ms: 1.05x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 63.5 ns: 1.05x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.10 sec: 1.06x slower                                                     |
| sqlglot_transpile          | 1.02 ms                                                     | 1.08 ms: 1.06x slower                                                      |
| go                         | 91.6 ms                                                     | 97.0 ms: 1.06x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 546 ms: 1.06x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 52.0 ms: 1.07x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.07x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 40.6 ms: 1.08x slower                                                      |
| richards_super             | 32.1 ms                                                     | 34.6 ms: 1.08x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 72.4 ms: 1.08x slower                                                      |
| richards                   | 28.4 ms                                                     | 30.7 ms: 1.08x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.1 ms: 1.08x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 878 us: 1.09x slower                                                       |
| nbody                      | 71.9 ms                                                     | 78.5 ms: 1.09x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.51 ms: 1.10x slower                                                      |
| pycparser                  | 699 ms                                                      | 773 ms: 1.11x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.53 sec: 1.11x slower                                                     |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.12x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.12x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 66.2 ms: 1.12x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.2 ms: 1.13x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.93 ms: 1.15x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.57 sec: 1.15x slower                                                     |
| scimark_sor                | 78.8 ms                                                     | 90.7 ms: 1.15x slower                                                      |
| scimark_fft                | 184 ms                                                      | 216 ms: 1.17x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.86 ms: 1.18x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 52.0 ms: 1.19x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 896 us: 1.19x slower                                                       |
| fannkuch                   | 247 ms                                                      | 304 ms: 1.23x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (4): float, xml_etree_parse, nqueens, sympy_integrate
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 92.49% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown