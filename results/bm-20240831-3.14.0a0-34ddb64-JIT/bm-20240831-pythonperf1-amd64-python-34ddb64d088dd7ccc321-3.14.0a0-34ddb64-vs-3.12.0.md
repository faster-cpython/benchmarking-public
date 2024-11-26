# Results vs. 3.12.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-amd64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.042x faster
- HPT reliability: 89.92%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 243 ms: 1.11x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.94 sec: 1.17x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 99.1 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 198 ms: 1.44x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 257 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.42x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 559 ms: 1.38x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 251 ms: 1.35x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                       |
| async_tree_io              | 731 ms                                                      | 586 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 395 ms: 1.24x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 50.0 ms: 1.44x faster                                                      |
| float          | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 124 ms: 1.02x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.0 ms: 1.05x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 95.6 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 50.5 ms: 1.11x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.27 sec: 1.08x faster                                                     |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.7 ms: 1.06x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.8 ms: 1.05x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 195 us: 1.00x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 94.0 ms: 1.01x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.78 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 145 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.6 ms: 1.14x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.3 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.26 ms: 1.35x faster                                                      |
| django_template | 22.9 ms                                                     | 26.8 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.0 us: 1.58x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 44.1 ms: 1.52x faster                                                      |
| nbody                      | 71.9 ms                                                     | 50.0 ms: 1.44x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 198 ms: 1.44x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 257 ms: 1.43x faster                                                       |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.42x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 559 ms: 1.38x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.53 sec: 1.37x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 251 ms: 1.35x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.26 ms: 1.35x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.8 us: 1.31x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                       |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 60.5 ms: 1.30x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 38.2 ms: 1.27x faster                                                      |
| float                      | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                      |
| async_tree_io              | 731 ms                                                      | 586 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 395 ms: 1.24x faster                                                       |
| scimark_fft                | 184 ms                                                      | 149 ms: 1.24x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.82 ms: 1.19x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.18 ms: 1.17x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                      |
| pyflate                    | 295 ms                                                      | 262 ms: 1.12x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.5 ms: 1.11x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 54.0 ms: 1.09x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.27 sec: 1.08x faster                                                     |
| chaos                      | 43.3 ms                                                     | 40.7 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.7 ms: 1.06x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 57.3 ns: 1.06x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.8 ms: 1.05x faster                                                      |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.05 us: 1.04x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 827 us: 1.04x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.7 ms: 1.04x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| fannkuch                   | 247 ms                                                      | 239 ms: 1.03x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.56 us: 1.02x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.4 ms: 1.02x faster                                                      |
| regex_dna                  | 126 ms                                                      | 124 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 79.1 ms: 1.02x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 507 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 43.5 ms: 1.01x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 44.0 ms: 1.01x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 195 us: 1.00x faster                                                       |
| go                         | 91.6 ms                                                     | 92.0 ms: 1.00x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 94.0 ms: 1.01x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.78 ms: 1.01x slower                                                      |
| raytrace                   | 192 ms                                                      | 198 ms: 1.03x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.58 ms: 1.04x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.0 ms: 1.05x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                     |
| pycparser                  | 699 ms                                                      | 750 ms: 1.07x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 74.4 ms: 1.08x slower                                                      |
| sympy_str                  | 175 ms                                                      | 190 ms: 1.08x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 99.3 ms: 1.09x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 203 ms: 1.09x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 530 ms: 1.09x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 145 us: 1.09x slower                                                       |
| async_generators           | 239 ms                                                      | 261 ms: 1.09x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 95.6 ms: 1.09x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 99.1 ms: 1.11x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.58 ms: 1.11x slower                                                      |
| 2to3                       | 218 ms                                                      | 243 ms: 1.11x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 901 us: 1.12x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.6 ms: 1.14x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.17 ms: 1.14x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.3 ms: 1.15x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 15.0 ms: 1.16x slower                                                      |
| sympy_expand               | 284 ms                                                      | 329 ms: 1.16x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 40.0 ms: 1.16x slower                                                      |
| coverage                   | 40.8 ms                                                     | 47.6 ms: 1.17x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.94 sec: 1.17x slower                                                     |
| django_template            | 22.9 ms                                                     | 26.8 ms: 1.17x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.87 ms: 1.19x slower                                                      |
| richards_super             | 32.1 ms                                                     | 39.3 ms: 1.22x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 933 us: 1.24x slower                                                       |
| richards                   | 28.4 ms                                                     | 36.0 ms: 1.27x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (3): regex_effbot, meteor_contest, pprint_pformat
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.042x faster
# HPT report

- Reliability score: 89.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown