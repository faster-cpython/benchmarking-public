# Results vs. 3.12.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: windows-amd64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.01x faster
- HPT reliability: 86.75%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 246 ms: 1.13x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.91 sec: 1.15x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 96.2 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 259 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 209 ms: 1.37x faster                                                        |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                        |
| async_tree_io              | 731 ms                                                      | 559 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 400 ms: 1.25x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 274 ms: 1.24x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 635 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 52.8 ms: 1.36x faster                                                       |
| float          | 56.8 ms                                                     | 47.5 ms: 1.19x faster                                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 123 ms: 1.03x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 91.1 ms: 1.04x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.26 sec: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.6 ms: 1.06x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.1 ms: 1.04x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 199 us: 1.02x slower                                                        |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 143 us: 1.07x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.30 ms: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.8 ms: 1.15x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 4.99 ms: 1.42x faster                                                       |
| django_template | 22.9 ms                                                     | 27.6 ms: 1.20x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 16.6 us: 1.43x faster                                                       |
| mako                       | 7.09 ms                                                     | 4.99 ms: 1.42x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 259 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 209 ms: 1.37x faster                                                        |
| nbody                      | 71.9 ms                                                     | 52.8 ms: 1.36x faster                                                       |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                        |
| async_tree_io              | 731 ms                                                      | 559 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                        |
| deepcopy                   | 238 us                                                      | 190 us: 1.25x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 400 ms: 1.25x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 54.0 ms: 1.24x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 274 ms: 1.24x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 64.3 ms: 1.23x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.6 us: 1.22x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 635 ms: 1.21x faster                                                        |
| float                      | 56.8 ms                                                     | 47.5 ms: 1.19x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 40.6 ms: 1.19x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.8 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.19 ms: 1.17x faster                                                       |
| scimark_fft                | 184 ms                                                      | 159 ms: 1.16x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 450 ms: 1.14x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 53.3 ms: 1.10x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 953 ms: 1.10x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.26 sec: 1.08x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.0 ms: 1.08x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 56.3 ns: 1.07x faster                                                       |
| fannkuch                   | 247 ms                                                      | 232 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.6 ms: 1.06x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.2 ms: 1.05x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.1 ms: 1.04x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.49 us: 1.03x faster                                                       |
| pyflate                    | 295 ms                                                      | 285 ms: 1.03x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                       |
| regex_dna                  | 126 ms                                                      | 123 ms: 1.03x faster                                                        |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 835 us: 1.03x faster                                                        |
| logging_simple             | 6.28 us                                                     | 6.15 us: 1.02x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 61.9 ms: 1.01x faster                                                       |
| go                         | 91.6 ms                                                     | 90.4 ms: 1.01x faster                                                       |
| generators                 | 22.5 ms                                                     | 22.7 ms: 1.01x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 75.4 ms: 1.01x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 199 us: 1.02x slower                                                        |
| pycparser                  | 699 ms                                                      | 725 ms: 1.04x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 91.1 ms: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.31 ms: 1.07x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 143 us: 1.07x slower                                                        |
| tornado_http               | 89.5 ms                                                     | 96.2 ms: 1.07x slower                                                       |
| async_generators           | 239 ms                                                      | 258 ms: 1.08x slower                                                        |
| sympy_str                  | 175 ms                                                      | 192 ms: 1.10x slower                                                        |
| raytrace                   | 192 ms                                                      | 212 ms: 1.10x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 206 ms: 1.10x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.56 ms: 1.10x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.30 ms: 1.11x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 893 us: 1.11x slower                                                        |
| sympy_sum                  | 91.5 ms                                                     | 102 ms: 1.12x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.54 sec: 1.12x slower                                                      |
| 2to3                       | 218 ms                                                      | 246 ms: 1.13x slower                                                        |
| sympy_expand               | 284 ms                                                      | 323 ms: 1.14x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.17 ms: 1.15x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.91 sec: 1.15x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.8 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.16x slower                                                        |
| richards_super             | 32.1 ms                                                     | 38.3 ms: 1.19x slower                                                       |
| richards                   | 28.4 ms                                                     | 34.0 ms: 1.20x slower                                                       |
| django_template            | 22.9 ms                                                     | 27.6 ms: 1.20x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 15.7 ms: 1.21x slower                                                       |
| coverage                   | 40.8 ms                                                     | 50.3 ms: 1.23x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 42.6 ms: 1.23x slower                                                       |
| python_startup             | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.13 ms: 1.25x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.96 ms: 1.29x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.2 ms: 1.29x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.40 ms: 1.86x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (3): pathlib, xml_etree_parse, json
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 86.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown