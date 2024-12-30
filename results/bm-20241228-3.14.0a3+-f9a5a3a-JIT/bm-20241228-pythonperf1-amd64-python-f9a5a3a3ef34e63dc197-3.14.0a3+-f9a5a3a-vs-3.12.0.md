# Results vs. 3.12.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: windows-amd64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.067x faster
- HPT reliability: 97.93%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 406 ms: 1.80x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 214 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                        |
| async_tree_none            | 291 ms                                                      | 183 ms: 1.59x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 353 ms: 1.39x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 54.3 ms: 1.32x faster                                                       |
| float          | 56.8 ms                                                     | 47.3 ms: 1.20x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                       |
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 80.0 ms: 1.09x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 18.4 ms: 1.29x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 110 us: 1.21x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.18 sec: 1.15x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 58.8 ms: 1.11x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 87.3 ms: 1.07x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 205 us: 1.05x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.29 ms: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.11 ms: 1.39x faster                                                       |
| django_template | 22.9 ms                                                     | 26.8 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 406 ms: 1.80x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 214 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                        |
| async_tree_none            | 291 ms                                                      | 183 ms: 1.59x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 16.9 us: 1.40x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.11 ms: 1.39x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 353 ms: 1.39x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 48.6 ms: 1.38x faster                                                       |
| nbody                      | 71.9 ms                                                     | 54.3 ms: 1.32x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 61.5 ms: 1.28x faster                                                       |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.25x faster                                                        |
| deepcopy                   | 238 us                                                      | 190 us: 1.25x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 110 us: 1.21x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.12 ms: 1.20x faster                                                       |
| float                      | 56.8 ms                                                     | 47.3 ms: 1.20x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.7 ms: 1.19x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 41.1 ms: 1.18x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.18 sec: 1.15x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 58.8 ms: 1.11x faster                                                       |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 40.5 ms: 1.09x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 80.0 ms: 1.09x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 54.5 ms: 1.08x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 87.3 ms: 1.07x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 985 ms: 1.06x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 76.0 ms: 1.06x faster                                                       |
| pyflate                    | 295 ms                                                      | 279 ms: 1.06x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.05x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 57.5 ns: 1.05x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 816 us: 1.05x faster                                                        |
| chaos                      | 43.3 ms                                                     | 41.4 ms: 1.05x faster                                                       |
| json                       | 3.05 ms                                                     | 2.91 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 495 ms: 1.04x faster                                                        |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                        |
| go                         | 91.6 ms                                                     | 88.8 ms: 1.03x faster                                                       |
| fannkuch                   | 247 ms                                                      | 243 ms: 1.02x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 74.3 ms: 1.00x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 63.3 ms: 1.01x slower                                                       |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                        |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.30 ms: 1.04x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                       |
| async_generators           | 239 ms                                                      | 251 ms: 1.05x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 844 us: 1.05x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 205 us: 1.05x slower                                                        |
| pycparser                  | 699 ms                                                      | 735 ms: 1.05x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.09 ms: 1.07x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                       |
| generators                 | 22.5 ms                                                     | 24.2 ms: 1.07x slower                                                       |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.08x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 37.8 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 205 ms: 1.10x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.29 ms: 1.11x slower                                                       |
| raytrace                   | 192 ms                                                      | 213 ms: 1.11x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.52 sec: 1.11x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.6 ms: 1.14x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.8 ms: 1.17x slower                                                       |
| richards_super             | 32.1 ms                                                     | 37.7 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| richards                   | 28.4 ms                                                     | 33.6 ms: 1.18x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 82.6 ms: 1.19x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.01 ms: 1.22x slower                                                       |
| mypy2                      | 509 ms                                                      | 635 ms: 1.25x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 18.4 ms: 1.29x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.98 ms: 1.30x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (3): logging_simple, logging_format, sympy_sum
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.067x faster

# HPT report

- Reliability score: 97.93% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown