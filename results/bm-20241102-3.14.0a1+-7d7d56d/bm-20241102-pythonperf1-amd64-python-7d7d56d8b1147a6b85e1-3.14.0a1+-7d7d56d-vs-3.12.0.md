# Results vs. 3.12.0

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: windows-amd64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.028x slower
- HPT reliability: 99.80%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 93.4 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                        |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.32x faster                                                        |
| async_tree_io              | 731 ms                                                      | 566 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 382 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 400 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 631 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| float          | 56.8 ms                                                     | 54.9 ms: 1.03x faster                                                       |
| nbody          | 71.9 ms                                                     | 79.4 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                       |
| regex_compile  | 87.5 ms                                                     | 92.2 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 95.5 ms: 1.03x slower                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 67.6 ms: 1.04x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 59.4 ms: 1.06x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 228 us: 1.17x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.73 ms: 1.18x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 159 us: 1.19x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.8 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.95 ms: 1.02x faster                                                       |
| django_template | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                        |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.32x faster                                                        |
| async_tree_io              | 731 ms                                                      | 566 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 382 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 400 ms: 1.26x faster                                                        |
| deepcopy                   | 238 us                                                      | 192 us: 1.24x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 631 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                                        |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.16x faster                                                       |
| regex_dna                  | 126 ms                                                      | 113 ms: 1.12x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 21.5 us: 1.10x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.07x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.05x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 826 us: 1.04x faster                                                        |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| float                      | 56.8 ms                                                     | 54.9 ms: 1.03x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.0 ms: 1.03x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 78.9 ms: 1.02x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.95 ms: 1.02x faster                                                       |
| go                         | 91.6 ms                                                     | 90.1 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.2 ms: 1.01x faster                                                       |
| async_generators           | 239 ms                                                      | 243 ms: 1.01x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                      |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                        |
| chaos                      | 43.3 ms                                                     | 44.3 ms: 1.02x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.3 ms: 1.02x slower                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 95.5 ms: 1.03x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| raytrace                   | 192 ms                                                      | 199 ms: 1.03x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.50 us: 1.04x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 67.6 ms: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.97 us: 1.04x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 77.5 ms: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 93.4 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.68 ms: 1.05x slower                                                       |
| pycparser                  | 699 ms                                                      | 734 ms: 1.05x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 92.2 ms: 1.05x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 198 ms: 1.06x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 59.4 ms: 1.06x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 71.6 ms: 1.07x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 551 ms: 1.07x slower                                                        |
| sympy_expand               | 284 ms                                                      | 306 ms: 1.08x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 37.3 ms: 1.08x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 65.6 ns: 1.08x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 64.5 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                       |
| pyflate                    | 295 ms                                                      | 324 ms: 1.10x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.51 sec: 1.10x slower                                                      |
| nbody                      | 71.9 ms                                                     | 79.4 ms: 1.10x slower                                                       |
| scimark_fft                | 184 ms                                                      | 206 ms: 1.12x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.60 ms: 1.12x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.16 ms: 1.13x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.9 ms: 1.14x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.7 ms: 1.14x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.16x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 938 us: 1.17x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 228 us: 1.17x slower                                                        |
| fannkuch                   | 247 ms                                                      | 289 ms: 1.17x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.84 ms: 1.17x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 93.0 ms: 1.18x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.73 ms: 1.18x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 159 us: 1.19x slower                                                        |
| richards                   | 28.4 ms                                                     | 34.0 ms: 1.20x slower                                                       |
| richards_super             | 32.1 ms                                                     | 38.5 ms: 1.20x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 83.1 ms: 1.20x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.8 ms: 1.22x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.91 ms: 1.25x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.36 ms: 1.81x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (3): json, generators, crypto_pyaes
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.028x slower
# HPT report

- Reliability score: 99.80% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown