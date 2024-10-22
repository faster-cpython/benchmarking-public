# Results vs. 3.12.0

- fork: python
- ref: d66b06107b0104af513f
- machine: windows-amd64
- commit hash: d66b061
- commit date: 2024-07-19
- overall geometric mean: 1.03x faster
- HPT reliability: 56.78%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 91.2 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 189 ms: 1.51x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 244 ms: 1.50x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 532 ms: 1.45x faster                                                       |
| async_tree_none            | 291 ms                                                      | 210 ms: 1.39x faster                                                       |
| async_tree_io              | 731 ms                                                      | 552 ms: 1.32x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 256 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.38x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 55.4 ms: 1.02x faster                                                      |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 78.2 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 85.8 ms: 1.02x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 199 us: 1.02x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.2 ms: 1.03x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.90 ms: 1.04x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 139 us: 1.04x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 39.5 ms: 1.05x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.5 ms: 1.08x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.4 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 23.2 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 189 ms: 1.51x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 244 ms: 1.50x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 532 ms: 1.45x faster                                                       |
| async_tree_none            | 291 ms                                                      | 210 ms: 1.39x faster                                                       |
| deepcopy                   | 238 us                                                      | 174 us: 1.37x faster                                                       |
| async_tree_io              | 731 ms                                                      | 552 ms: 1.32x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 256 ms: 1.32x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.59 sec: 1.32x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.1 us: 1.27x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 19.6 us: 1.21x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                      |
| raytrace                   | 192 ms                                                      | 172 ms: 1.12x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.7 ms: 1.09x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 800 us: 1.07x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.07x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.04 ms: 1.06x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.98 us: 1.05x faster                                                      |
| chaos                      | 43.3 ms                                                     | 41.5 ms: 1.05x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.46 us: 1.04x faster                                                      |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 58.4 ns: 1.03x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.7 ms: 1.03x faster                                                      |
| sqlglot_normalize          | 187 ms                                                      | 181 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 88.7 ms: 1.03x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 67.1 ms: 1.03x faster                                                      |
| float                      | 56.8 ms                                                     | 55.4 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 85.8 ms: 1.02x faster                                                      |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.01x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 73.8 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| go                         | 91.6 ms                                                     | 91.0 ms: 1.01x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 58.6 ms: 1.01x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 48.6 ms: 1.00x slower                                                      |
| async_generators           | 239 ms                                                      | 241 ms: 1.01x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                     |
| richards                   | 28.4 ms                                                     | 28.6 ms: 1.01x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.14 ms: 1.01x slower                                                      |
| django_template            | 22.9 ms                                                     | 23.2 ms: 1.01x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 199 us: 1.02x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 91.2 ms: 1.02x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 523 ms: 1.02x slower                                                       |
| richards_super             | 32.1 ms                                                     | 32.7 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.02x slower                                                     |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.2 ms: 1.03x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                      |
| pyflate                    | 295 ms                                                      | 302 ms: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 68.9 ms: 1.03x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.06 ms: 1.03x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.90 ms: 1.04x slower                                                      |
| sympy_expand               | 284 ms                                                      | 294 ms: 1.04x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 139 us: 1.04x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.5 ms: 1.05x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 46.4 ms: 1.06x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 854 us: 1.06x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.73 ms: 1.07x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 84.4 ms: 1.07x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.5 ms: 1.08x slower                                                      |
| scimark_fft                | 184 ms                                                      | 199 ms: 1.08x slower                                                       |
| nbody                      | 71.9 ms                                                     | 78.2 ms: 1.09x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                                     |
| asyncio_tcp                | 487 ms                                                      | 534 ms: 1.10x slower                                                       |
| python_startup             | 19.5 ms                                                     | 21.4 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.11x slower                                                       |
| fannkuch                   | 247 ms                                                      | 280 ms: 1.14x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.3 ms: 1.16x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.82 ms: 1.17x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 903 us: 1.20x slower                                                       |
| pycparser                  | 699 ms                                                      | 848 ms: 1.21x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (4): pathlib, mako, xml_etree_parse, sqlglot_optimize
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240719-3.14.0a0-d66b061/bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 56.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown