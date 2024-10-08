# Results vs. 3.12.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-amd64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.00x slower
- HPT reliability: 97.19%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.04x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 93.8 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 250 ms: 1.47x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 204 ms: 1.40x faster                                                       |
| async_tree_none            | 291 ms                                                      | 210 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 564 ms: 1.37x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 260 ms: 1.31x faster                                                       |
| async_tree_io              | 731 ms                                                      | 573 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 399 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 390 ms: 1.25x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 56.2 ms: 1.01x faster                                                      |
| nbody          | 71.9 ms                                                     | 83.6 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 91.5 ms: 1.05x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 95.6 ms: 1.03x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.7 ms: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.07x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 40.9 ms: 1.08x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.87 ms: 1.03x faster                                                      |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 250 ms: 1.47x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 204 ms: 1.40x faster                                                       |
| async_tree_none            | 291 ms                                                      | 210 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 564 ms: 1.37x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 260 ms: 1.31x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.61 sec: 1.30x faster                                                     |
| deepcopy                   | 238 us                                                      | 186 us: 1.28x faster                                                       |
| async_tree_io              | 731 ms                                                      | 573 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 399 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 390 ms: 1.25x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.5 us: 1.22x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.19x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.90 us: 1.10x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.6 ms: 1.10x faster                                                      |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| go                         | 91.6 ms                                                     | 84.7 ms: 1.08x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.87 ms: 1.03x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 831 us: 1.03x faster                                                       |
| raytrace                   | 192 ms                                                      | 188 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.1 ms: 1.02x faster                                                      |
| chaos                      | 43.3 ms                                                     | 42.7 ms: 1.02x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.8 ms: 1.01x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 79.4 ms: 1.01x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.63 us: 1.01x faster                                                      |
| float                      | 56.8 ms                                                     | 56.2 ms: 1.01x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 68.7 ms: 1.01x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.25 us: 1.00x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 67.4 ms: 1.01x slower                                                      |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.1 ms: 1.01x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                     |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 191 ms: 1.02x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 95.6 ms: 1.03x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 62.5 ns: 1.03x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.7 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| 2to3                       | 218 ms                                                      | 226 ms: 1.04x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 65.2 ms: 1.04x slower                                                      |
| async_generators           | 239 ms                                                      | 249 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.66 ms: 1.04x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 91.5 ms: 1.05x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                     |
| tornado_http               | 89.5 ms                                                     | 93.8 ms: 1.05x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 78.3 ms: 1.05x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 512 ms: 1.05x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 36.3 ms: 1.05x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.05x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.32 ms: 1.05x slower                                                      |
| scimark_fft                | 184 ms                                                      | 195 ms: 1.06x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 62.3 ms: 1.06x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                     |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.07x slower                                                       |
| sympy_expand               | 284 ms                                                      | 307 ms: 1.08x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.08x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 555 ms: 1.08x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.9 ms: 1.08x slower                                                      |
| pycparser                  | 699 ms                                                      | 759 ms: 1.09x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                      |
| pyflate                    | 295 ms                                                      | 322 ms: 1.09x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 891 us: 1.11x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.12x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.1 ms: 1.12x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 88.7 ms: 1.13x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.2 ms: 1.13x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.4 ms: 1.14x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                     |
| nbody                      | 71.9 ms                                                     | 83.6 ms: 1.16x slower                                                      |
| fannkuch                   | 247 ms                                                      | 291 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                       |
| coverage                   | 40.8 ms                                                     | 49.3 ms: 1.21x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 917 us: 1.22x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.09 ms: 1.23x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (4): pidigits, xml_etree_iterparse, dulwich_log, json
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.19% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown