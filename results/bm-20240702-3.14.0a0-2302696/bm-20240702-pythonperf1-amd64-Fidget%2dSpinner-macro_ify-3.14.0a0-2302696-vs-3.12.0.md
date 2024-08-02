# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: macro_ify
- machine: windows-amd64
- commit hash: 2302696
- commit date: 2024-07-02
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 216 ms: 1.01x faster                                                      |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                    |
| tornado_http   | 89.5 ms                                                     | 80.2 ms: 1.12x faster                                                     |
| Geometric mean | (ref)                                                       | 1.05x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 183 ms: 1.56x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 238 ms: 1.54x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 514 ms: 1.50x faster                                                      |
| async_tree_none            | 291 ms                                                      | 201 ms: 1.45x faster                                                      |
| async_tree_io              | 731 ms                                                      | 517 ms: 1.41x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 245 ms: 1.38x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 375 ms: 1.34x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 376 ms: 1.30x faster                                                      |
| Geometric mean             | (ref)                                                       | 1.43x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 52.5 ms: 1.08x faster                                                     |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                      |
| nbody          | 71.9 ms                                                     | 73.2 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                       | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.4 ms: 1.10x faster                                                     |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                     |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                       | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 185 us: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.6 ms: 1.04x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 131 us: 1.01x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                     |
| xml_etree_process    | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                     |
| json_dumps           | 5.70 ms                                                     | 5.75 ms: 1.01x slower                                                     |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                     |
| tomli_loads          | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.1 ms: 1.05x slower                                                     |
| python_startup         | 19.5 ms                                                     | 20.6 ms: 1.06x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.78 ms: 1.04x faster                                                     |
| django_template | 22.9 ms                                                     | 22.5 ms: 1.02x faster                                                     |
| Geometric mean  | (ref)                                                       | 1.03x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 183 ms: 1.56x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 238 ms: 1.54x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 514 ms: 1.50x faster                                                      |
| async_tree_none            | 291 ms                                                      | 201 ms: 1.45x faster                                                      |
| async_tree_io              | 731 ms                                                      | 517 ms: 1.41x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 245 ms: 1.38x faster                                                      |
| deepcopy                   | 238 us                                                      | 173 us: 1.38x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.34x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 375 ms: 1.34x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.57 sec: 1.33x faster                                                    |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 376 ms: 1.30x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.4 us: 1.29x faster                                                     |
| deepcopy_reduce            | 2.09 us                                                     | 1.76 us: 1.19x faster                                                     |
| bench_thread_pool          | 857 us                                                      | 748 us: 1.14x faster                                                      |
| raytrace                   | 192 ms                                                      | 168 ms: 1.14x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 80.2 ms: 1.12x faster                                                     |
| regex_compile              | 87.5 ms                                                     | 79.4 ms: 1.10x faster                                                     |
| chaos                      | 43.3 ms                                                     | 39.6 ms: 1.09x faster                                                     |
| float                      | 56.8 ms                                                     | 52.5 ms: 1.08x faster                                                     |
| sympy_str                  | 175 ms                                                      | 163 ms: 1.07x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 58.7 ms: 1.07x faster                                                     |
| generators                 | 22.5 ms                                                     | 21.0 ms: 1.07x faster                                                     |
| sympy_sum                  | 91.5 ms                                                     | 85.6 ms: 1.07x faster                                                     |
| deltablue                  | 2.16 ms                                                     | 2.02 ms: 1.07x faster                                                     |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.07x faster                                                     |
| pathlib                    | 80.5 ms                                                     | 75.4 ms: 1.07x faster                                                     |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                      |
| go                         | 91.6 ms                                                     | 86.0 ms: 1.06x faster                                                     |
| spectral_norm              | 66.9 ms                                                     | 63.2 ms: 1.06x faster                                                     |
| pickle_pure_python         | 195 us                                                      | 185 us: 1.06x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 65.4 ms: 1.06x faster                                                     |
| sqlglot_normalize          | 187 ms                                                      | 178 ms: 1.05x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.96 us: 1.05x faster                                                     |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                     |
| richards                   | 28.4 ms                                                     | 27.2 ms: 1.05x faster                                                     |
| logging_format             | 6.72 us                                                     | 6.43 us: 1.05x faster                                                     |
| mako                       | 7.09 ms                                                     | 6.78 ms: 1.04x faster                                                     |
| logging_silent             | 60.5 ns                                                     | 57.9 ns: 1.04x faster                                                     |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.6 ms: 1.04x faster                                                     |
| async_generators           | 239 ms                                                      | 231 ms: 1.04x faster                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 33.4 ms: 1.04x faster                                                     |
| crypto_pyaes               | 48.5 ms                                                     | 46.9 ms: 1.03x faster                                                     |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.03x faster                                                     |
| scimark_lu                 | 58.9 ms                                                     | 57.0 ms: 1.03x faster                                                     |
| hexiom                     | 4.10 ms                                                     | 3.97 ms: 1.03x faster                                                     |
| pprint_pformat             | 1.05 sec                                                    | 1.02 sec: 1.03x faster                                                    |
| pprint_safe_repr           | 513 ms                                                      | 499 ms: 1.03x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                    |
| django_template            | 22.9 ms                                                     | 22.5 ms: 1.02x faster                                                     |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                      |
| sympy_expand               | 284 ms                                                      | 279 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                     |
| unpickle_pure_python       | 133 us                                                      | 131 us: 1.01x faster                                                      |
| 2to3                       | 218 ms                                                      | 216 ms: 1.01x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 43.3 ms: 1.01x faster                                                     |
| xml_etree_generate         | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                                     |
| meteor_contest             | 74.6 ms                                                     | 74.0 ms: 1.01x faster                                                     |
| xml_etree_process          | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                     |
| json_dumps                 | 5.70 ms                                                     | 5.75 ms: 1.01x slower                                                     |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                     |
| nbody                      | 71.9 ms                                                     | 73.2 ms: 1.02x slower                                                     |
| scimark_sor                | 78.8 ms                                                     | 80.4 ms: 1.02x slower                                                     |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                     |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                     |
| mdp                        | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                    |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.69 ms: 1.05x slower                                                     |
| scimark_fft                | 184 ms                                                      | 194 ms: 1.05x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.1 ms: 1.05x slower                                                     |
| python_startup             | 19.5 ms                                                     | 20.6 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 95.1 us                                                     | 101 us: 1.07x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                    |
| coverage                   | 40.8 ms                                                     | 45.2 ms: 1.11x slower                                                     |
| fannkuch                   | 247 ms                                                      | 277 ms: 1.12x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.64 ms: 1.12x slower                                                     |
| pycparser                  | 699 ms                                                      | 819 ms: 1.17x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 883 us: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                              |

Benchmark hidden because not significant (6): asyncio_tcp, sqlglot_transpile, xml_etree_parse, pyflate, sqlglot_parse, json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240702-3.14.0a0-2302696/bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown