# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache
- machine: windows-amd64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.04x faster
- HPT reliability: 97.36%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 240 ms: 1.10x slower                                                 |
| docutils       | 1.66 sec                                                    | 1.84 sec: 1.11x slower                                               |
| tornado_http   | 89.5 ms                                                     | 98.0 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                       | 1.10x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 260 ms: 1.41x faster                                                 |
| async_tree_none_tg         | 285 ms                                                      | 209 ms: 1.36x faster                                                 |
| async_tree_none            | 291 ms                                                      | 218 ms: 1.34x faster                                                 |
| async_tree_io              | 731 ms                                                      | 566 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 399 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                                 |
| async_tree_memoization     | 339 ms                                                      | 277 ms: 1.22x faster                                                 |
| async_tree_io_tg           | 771 ms                                                      | 631 ms: 1.22x faster                                                 |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.1 ms: 1.35x faster                                                |
| float          | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                       | 1.18x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 122 ms: 1.03x faster                                                 |
| regex_compile  | 87.5 ms                                                     | 86.7 ms: 1.01x faster                                                |
| regex_effbot   | 1.62 ms                                                     | 1.66 ms: 1.03x slower                                                |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                       | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                |
| tomli_loads          | 1.37 sec                                                    | 1.24 sec: 1.10x faster                                               |
| xml_etree_process    | 37.7 ms                                                     | 36.0 ms: 1.05x faster                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                |
| pickle_pure_python   | 195 us                                                      | 199 us: 1.02x slower                                                 |
| xml_etree_parse      | 93.0 ms                                                     | 95.5 ms: 1.03x slower                                                |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.05x slower                                                |
| unpickle_pure_python | 133 us                                                      | 142 us: 1.07x slower                                                 |
| json_dumps           | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.5 ms: 1.14x slower                                                |
| python_startup         | 19.5 ms                                                     | 24.2 ms: 1.25x slower                                                |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.08 ms: 1.39x faster                                                |
| django_template | 22.9 ms                                                     | 25.3 ms: 1.10x slower                                                |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.8 us: 1.50x faster                                                |
| async_tree_memoization_tg  | 367 ms                                                      | 260 ms: 1.41x faster                                                 |
| mako                       | 7.09 ms                                                     | 5.08 ms: 1.39x faster                                                |
| async_tree_none_tg         | 285 ms                                                      | 209 ms: 1.36x faster                                                 |
| nbody                      | 71.9 ms                                                     | 53.1 ms: 1.35x faster                                                |
| async_tree_none            | 291 ms                                                      | 218 ms: 1.34x faster                                                 |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                                 |
| comprehensions             | 14.1 us                                                     | 10.9 us: 1.30x faster                                                |
| async_tree_io              | 731 ms                                                      | 566 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 399 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                                 |
| scimark_sor                | 78.8 ms                                                     | 63.7 ms: 1.24x faster                                                |
| async_tree_memoization     | 339 ms                                                      | 277 ms: 1.22x faster                                                 |
| async_tree_io_tg           | 771 ms                                                      | 631 ms: 1.22x faster                                                 |
| crypto_pyaes               | 48.5 ms                                                     | 39.9 ms: 1.22x faster                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.1 ms: 1.21x faster                                                |
| spectral_norm              | 66.9 ms                                                     | 55.7 ms: 1.20x faster                                                |
| float                      | 56.8 ms                                                     | 47.4 ms: 1.20x faster                                                |
| pprint_safe_repr           | 513 ms                                                      | 433 ms: 1.18x faster                                                 |
| scimark_fft                | 184 ms                                                      | 157 ms: 1.18x faster                                                 |
| fannkuch                   | 247 ms                                                      | 212 ms: 1.16x faster                                                 |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.21 ms: 1.16x faster                                                |
| pprint_pformat             | 1.05 sec                                                    | 906 ms: 1.15x faster                                                 |
| go                         | 91.6 ms                                                     | 82.2 ms: 1.11x faster                                                |
| xml_etree_generate         | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                |
| dulwich_log                | 44.3 ms                                                     | 39.9 ms: 1.11x faster                                                |
| logging_silent             | 60.5 ns                                                     | 54.6 ns: 1.11x faster                                                |
| tomli_loads                | 1.37 sec                                                    | 1.24 sec: 1.10x faster                                               |
| chaos                      | 43.3 ms                                                     | 39.5 ms: 1.10x faster                                                |
| scimark_lu                 | 58.9 ms                                                     | 54.1 ms: 1.09x faster                                                |
| pyflate                    | 295 ms                                                      | 274 ms: 1.08x faster                                                 |
| xml_etree_process          | 37.7 ms                                                     | 36.0 ms: 1.05x faster                                                |
| logging_format             | 6.72 us                                                     | 6.44 us: 1.04x faster                                                |
| generators                 | 22.5 ms                                                     | 21.6 ms: 1.04x faster                                                |
| meteor_contest             | 74.6 ms                                                     | 71.9 ms: 1.04x faster                                                |
| logging_simple             | 6.28 us                                                     | 6.05 us: 1.04x faster                                                |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.03x faster                                                 |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.03x faster                                                |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                |
| regex_compile              | 87.5 ms                                                     | 86.7 ms: 1.01x faster                                                |
| pickle_pure_python         | 195 us                                                      | 199 us: 1.02x slower                                                 |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                 |
| xml_etree_parse            | 93.0 ms                                                     | 95.5 ms: 1.03x slower                                                |
| regex_effbot               | 1.62 ms                                                     | 1.66 ms: 1.03x slower                                                |
| deltablue                  | 2.16 ms                                                     | 2.23 ms: 1.03x slower                                                |
| sqlglot_normalize          | 187 ms                                                      | 194 ms: 1.04x slower                                                 |
| raytrace                   | 192 ms                                                      | 200 ms: 1.04x slower                                                 |
| hexiom                     | 4.10 ms                                                     | 4.28 ms: 1.04x slower                                                |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.05x slower                                                |
| sympy_expand               | 284 ms                                                      | 300 ms: 1.06x slower                                                 |
| sqlglot_parse              | 804 us                                                      | 850 us: 1.06x slower                                                 |
| unpickle_pure_python       | 133 us                                                      | 142 us: 1.07x slower                                                 |
| sympy_sum                  | 91.5 ms                                                     | 98.0 ms: 1.07x slower                                                |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.09x slower                                                |
| richards                   | 28.4 ms                                                     | 30.8 ms: 1.09x slower                                                |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                |
| richards_super             | 32.1 ms                                                     | 35.0 ms: 1.09x slower                                                |
| tornado_http               | 89.5 ms                                                     | 98.0 ms: 1.09x slower                                                |
| json_dumps                 | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                |
| 2to3                       | 218 ms                                                      | 240 ms: 1.10x slower                                                 |
| async_generators           | 239 ms                                                      | 264 ms: 1.10x slower                                                 |
| django_template            | 22.9 ms                                                     | 25.3 ms: 1.10x slower                                                |
| telco                      | 4.13 ms                                                     | 4.57 ms: 1.11x slower                                                |
| docutils                   | 1.66 sec                                                    | 1.84 sec: 1.11x slower                                               |
| mdp                        | 1.37 sec                                                    | 1.53 sec: 1.11x slower                                               |
| python_startup_no_site     | 16.2 ms                                                     | 18.5 ms: 1.14x slower                                                |
| sqlglot_optimize           | 34.5 ms                                                     | 39.4 ms: 1.14x slower                                                |
| sympy_integrate            | 13.0 ms                                                     | 15.0 ms: 1.16x slower                                                |
| coverage                   | 40.8 ms                                                     | 47.8 ms: 1.17x slower                                                |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                 |
| python_startup             | 19.5 ms                                                     | 24.2 ms: 1.25x slower                                                |
| gc_traversal               | 1.52 ms                                                     | 1.94 ms: 1.27x slower                                                |
| bench_mp_pool              | 69.2 ms                                                     | 89.1 ms: 1.29x slower                                                |
| create_gc_cycles           | 752 us                                                      | 1.39 ms: 1.85x slower                                                |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                         |

Benchmark hidden because not significant (4): bench_thread_pool, pycparser, pathlib, nqueens
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 97.36% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown