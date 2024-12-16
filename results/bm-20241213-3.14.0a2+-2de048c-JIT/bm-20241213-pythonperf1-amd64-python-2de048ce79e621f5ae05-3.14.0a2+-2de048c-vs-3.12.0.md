# Results vs. 3.12.0

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: windows-amd64
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.067x faster
- HPT reliability: 98.64%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                        |
| async_tree_io              | 731 ms                                                      | 395 ms: 1.85x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                        |
| async_tree_none            | 291 ms                                                      | 181 ms: 1.61x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 350 ms: 1.43x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 354 ms: 1.38x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.64x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 52.8 ms: 1.36x faster                                                       |
| float          | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.40 ms: 1.15x faster                                                       |
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 81.3 ms: 1.08x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 20.9 ms: 1.47x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 110 us: 1.21x faster                                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 58.3 ms: 1.12x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 50.8 ms: 1.10x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 85.0 ms: 1.09x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.07x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.22 ms: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.3 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.11 ms: 1.39x faster                                                       |
| django_template | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                        |
| async_tree_io              | 731 ms                                                      | 395 ms: 1.85x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                        |
| async_tree_none            | 291 ms                                                      | 181 ms: 1.61x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 350 ms: 1.43x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 16.6 us: 1.42x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.11 ms: 1.39x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 354 ms: 1.38x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 49.1 ms: 1.36x faster                                                       |
| nbody                      | 71.9 ms                                                     | 52.8 ms: 1.36x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 61.2 ms: 1.29x faster                                                       |
| scimark_fft                | 184 ms                                                      | 146 ms: 1.27x faster                                                        |
| deepcopy                   | 238 us                                                      | 188 us: 1.26x faster                                                        |
| float                      | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.11 ms: 1.21x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 110 us: 1.21x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.4 ms: 1.20x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 40.7 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.15x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.40 ms: 1.15x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.13x faster                                                       |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 58.3 ms: 1.12x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 50.8 ms: 1.10x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 85.0 ms: 1.09x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.9 ms: 1.08x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 81.3 ms: 1.08x faster                                                       |
| pyflate                    | 295 ms                                                      | 276 ms: 1.07x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 55.5 ms: 1.06x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 988 ms: 1.06x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 76.2 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 489 ms: 1.05x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 828 us: 1.03x faster                                                        |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| json                       | 3.05 ms                                                     | 2.97 ms: 1.03x faster                                                       |
| chaos                      | 43.3 ms                                                     | 42.4 ms: 1.02x faster                                                       |
| go                         | 91.6 ms                                                     | 90.0 ms: 1.02x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.20 us: 1.01x faster                                                       |
| fannkuch                   | 247 ms                                                      | 244 ms: 1.01x faster                                                        |
| logging_format             | 6.72 us                                                     | 6.66 us: 1.01x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.9 ms: 1.01x faster                                                       |
| sympy_str                  | 175 ms                                                      | 176 ms: 1.01x slower                                                        |
| pycparser                  | 699 ms                                                      | 707 ms: 1.01x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.22 ms: 1.02x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.5 ms: 1.03x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 838 us: 1.04x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                                       |
| generators                 | 22.5 ms                                                     | 23.8 ms: 1.06x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.09 ms: 1.06x slower                                                       |
| async_generators           | 239 ms                                                      | 255 ms: 1.07x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.07x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                       |
| sympy_expand               | 284 ms                                                      | 304 ms: 1.07x slower                                                        |
| raytrace                   | 192 ms                                                      | 208 ms: 1.08x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.49 sec: 1.08x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.22 ms: 1.09x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 38.0 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 207 ms: 1.11x slower                                                        |
| coverage                   | 40.8 ms                                                     | 47.1 ms: 1.15x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 82.3 ms: 1.19x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.3 ms: 1.20x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                        |
| django_template            | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.97 ms: 1.21x slower                                                       |
| richards_super             | 32.1 ms                                                     | 39.1 ms: 1.22x slower                                                       |
| richards                   | 28.4 ms                                                     | 34.7 ms: 1.22x slower                                                       |
| mypy2                      | 509 ms                                                      | 634 ms: 1.24x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.98 ms: 1.30x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 20.9 ms: 1.47x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (3): meteor_contest, 2to3, logging_silent
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.067x faster

# HPT report

- Reliability score: 98.64% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown