# Results vs. 3.12.0

- fork: python
- ref: v3.13.1
- machine: windows-amd64
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.048x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 216 ms: 1.01x faster                                        |
| chameleon      | 4.98 ms                                                     | 4.87 ms: 1.02x faster                                       |
| docutils       | 1.66 sec                                                    | 1.55 sec: 1.07x faster                                      |
| tornado_http   | 89.5 ms                                                     | 82.1 ms: 1.09x faster                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 534 ms: 1.44x faster                                        |
| async_tree_none_tg         | 285 ms                                                      | 200 ms: 1.42x faster                                        |
| async_tree_io              | 731 ms                                                      | 516 ms: 1.42x faster                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 275 ms: 1.34x faster                                        |
| async_tree_none            | 291 ms                                                      | 221 ms: 1.32x faster                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                        |
| async_tree_memoization     | 339 ms                                                      | 269 ms: 1.26x faster                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 410 ms: 1.22x faster                                        |
| Geometric mean             | (ref)                                                       | 1.33x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 56.8 ms                                                     | 49.1 ms: 1.16x faster                                       |
| nbody          | 71.9 ms                                                     | 67.0 ms: 1.07x faster                                       |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                       |
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                        |
| regex_compile  | 87.5 ms                                                     | 81.7 ms: 1.07x faster                                       |
| regex_v8       | 14.2 ms                                                     | 25.8 ms: 1.81x slower                                       |
| Geometric mean | (ref)                                                       | 1.08x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|---------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_iterparse | 65.2 ms                                                     | 62.5 ms: 1.04x faster                                       |
| xml_etree_generate  | 55.8 ms                                                     | 53.9 ms: 1.04x faster                                       |
| pickle_pure_python  | 195 us                                                      | 190 us: 1.03x faster                                        |
| xml_etree_process   | 37.7 ms                                                     | 36.9 ms: 1.02x faster                                       |
| json_dumps          | 5.70 ms                                                     | 6.20 ms: 1.09x slower                                       |
| json_loads          | 13.9 us                                                     | 15.8 us: 1.13x slower                                       |
| Geometric mean      | (ref)                                                       | 1.01x slower                                                |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.1 ms: 1.05x slower                                       |
| python_startup         | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                       |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 20.5 ms: 1.12x faster                                       |
| mako            | 7.09 ms                                                     | 6.65 ms: 1.07x faster                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 534 ms: 1.44x faster                                        |
| async_tree_none_tg         | 285 ms                                                      | 200 ms: 1.42x faster                                        |
| async_tree_io              | 731 ms                                                      | 516 ms: 1.42x faster                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 275 ms: 1.34x faster                                        |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                       |
| async_tree_none            | 291 ms                                                      | 221 ms: 1.32x faster                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                        |
| async_tree_memoization     | 339 ms                                                      | 269 ms: 1.26x faster                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 410 ms: 1.22x faster                                        |
| raytrace                   | 192 ms                                                      | 158 ms: 1.22x faster                                        |
| float                      | 56.8 ms                                                     | 49.1 ms: 1.16x faster                                       |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.16x faster                                       |
| chaos                      | 43.3 ms                                                     | 37.9 ms: 1.14x faster                                       |
| logging_silent             | 60.5 ns                                                     | 53.7 ns: 1.13x faster                                       |
| django_template            | 22.9 ms                                                     | 20.5 ms: 1.12x faster                                       |
| deltablue                  | 2.16 ms                                                     | 1.93 ms: 1.12x faster                                       |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.12x faster                                       |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                       |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                        |
| sqlalchemy_declarative     | 86.4 ms                                                     | 78.8 ms: 1.10x faster                                       |
| nqueens                    | 62.8 ms                                                     | 57.3 ms: 1.10x faster                                       |
| dulwich_log                | 44.3 ms                                                     | 40.4 ms: 1.09x faster                                       |
| tornado_http               | 89.5 ms                                                     | 82.1 ms: 1.09x faster                                       |
| logging_format             | 6.72 us                                                     | 6.21 us: 1.08x faster                                       |
| docutils                   | 1.66 sec                                                    | 1.55 sec: 1.07x faster                                      |
| logging_simple             | 6.28 us                                                     | 5.84 us: 1.07x faster                                       |
| crypto_pyaes               | 48.5 ms                                                     | 45.2 ms: 1.07x faster                                       |
| nbody                      | 71.9 ms                                                     | 67.0 ms: 1.07x faster                                       |
| regex_compile              | 87.5 ms                                                     | 81.7 ms: 1.07x faster                                       |
| pathlib                    | 80.5 ms                                                     | 75.2 ms: 1.07x faster                                       |
| sqlglot_normalize          | 187 ms                                                      | 175 ms: 1.07x faster                                        |
| mako                       | 7.09 ms                                                     | 6.65 ms: 1.07x faster                                       |
| sympy_sum                  | 91.5 ms                                                     | 86.0 ms: 1.06x faster                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 966 us: 1.06x faster                                        |
| scimark_fft                | 184 ms                                                      | 174 ms: 1.06x faster                                        |
| go                         | 91.6 ms                                                     | 86.6 ms: 1.06x faster                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.4 ms: 1.06x faster                                       |
| meteor_contest             | 74.6 ms                                                     | 70.8 ms: 1.05x faster                                       |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                        |
| hexiom                     | 4.10 ms                                                     | 3.91 ms: 1.05x faster                                       |
| richards                   | 28.4 ms                                                     | 27.1 ms: 1.05x faster                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.05x faster                                       |
| richards_super             | 32.1 ms                                                     | 30.7 ms: 1.05x faster                                       |
| sqlglot_parse              | 804 us                                                      | 769 us: 1.05x faster                                        |
| sympy_str                  | 175 ms                                                      | 168 ms: 1.05x faster                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 33.1 ms: 1.04x faster                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.5 ms: 1.04x faster                                       |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                        |
| pprint_safe_repr           | 513 ms                                                      | 494 ms: 1.04x faster                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.04x faster                                      |
| deepcopy                   | 238 us                                                      | 230 us: 1.04x faster                                        |
| xml_etree_generate         | 55.8 ms                                                     | 53.9 ms: 1.04x faster                                       |
| pyflate                    | 295 ms                                                      | 286 ms: 1.03x faster                                        |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                       |
| pickle_pure_python         | 195 us                                                      | 190 us: 1.03x faster                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.49 ms: 1.03x faster                                       |
| chameleon                  | 4.98 ms                                                     | 4.87 ms: 1.02x faster                                       |
| spectral_norm              | 66.9 ms                                                     | 65.5 ms: 1.02x faster                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.9 ms: 1.02x faster                                       |
| pycparser                  | 699 ms                                                      | 685 ms: 1.02x faster                                        |
| 2to3                       | 218 ms                                                      | 216 ms: 1.01x faster                                        |
| scimark_lu                 | 58.9 ms                                                     | 58.3 ms: 1.01x faster                                       |
| scimark_sor                | 78.8 ms                                                     | 78.3 ms: 1.01x faster                                       |
| deepcopy_memo              | 23.7 us                                                     | 23.6 us: 1.00x faster                                       |
| sqlalchemy_imperative      | 9.29 ms                                                     | 9.39 ms: 1.01x slower                                       |
| sympy_expand               | 284 ms                                                      | 287 ms: 1.01x slower                                        |
| fannkuch                   | 247 ms                                                      | 254 ms: 1.03x slower                                        |
| mdp                        | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                      |
| json                       | 3.05 ms                                                     | 3.18 ms: 1.04x slower                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.1 ms: 1.05x slower                                       |
| json_dumps                 | 5.70 ms                                                     | 6.20 ms: 1.09x slower                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.09x slower                                        |
| coverage                   | 40.8 ms                                                     | 45.1 ms: 1.10x slower                                       |
| json_loads                 | 13.9 us                                                     | 15.8 us: 1.13x slower                                       |
| telco                      | 4.13 ms                                                     | 4.94 ms: 1.20x slower                                       |
| bench_mp_pool              | 69.2 ms                                                     | 84.3 ms: 1.22x slower                                       |
| python_startup             | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                       |
| gc_traversal               | 1.52 ms                                                     | 1.92 ms: 1.26x slower                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                       |
| regex_v8                   | 14.2 ms                                                     | 25.8 ms: 1.81x slower                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                |

Benchmark hidden because not significant (5): bench_thread_pool, xml_etree_parse, deepcopy_reduce, unpickle_pure_python, tomli_loads
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20241203-3.13.1-0671451/bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451.json: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown