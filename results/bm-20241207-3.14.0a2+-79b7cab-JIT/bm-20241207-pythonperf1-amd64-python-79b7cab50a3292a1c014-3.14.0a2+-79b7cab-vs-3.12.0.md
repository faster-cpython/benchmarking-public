# Results vs. 3.12.0

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: windows-amd64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.069x faster
- HPT reliability: 99.82%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 397 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 396 ms: 1.84x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 221 ms: 1.66x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 182 ms: 1.60x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 221 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 364 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 359 ms: 1.36x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.61x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.5 ms: 1.34x faster                                                       |
| float          | 56.8 ms                                                     | 48.8 ms: 1.16x faster                                                       |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.43 ms: 1.14x faster                                                       |
| regex_dna      | 126 ms                                                      | 114 ms: 1.10x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 81.3 ms: 1.08x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 18.4 ms: 1.29x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 111 us: 1.20x faster                                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 57.5 ms: 1.13x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 50.4 ms: 1.11x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 84.4 ms: 1.10x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 35.3 ms: 1.07x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.30 sec: 1.05x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 203 us: 1.04x slower                                                        |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.05x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.50 ms: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.5 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.17 ms: 1.37x faster                                                       |
| django_template | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 397 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 396 ms: 1.84x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 221 ms: 1.66x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 182 ms: 1.60x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 221 ms: 1.54x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 16.7 us: 1.42x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 364 ms: 1.38x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.17 ms: 1.37x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 359 ms: 1.36x faster                                                        |
| nbody                      | 71.9 ms                                                     | 53.5 ms: 1.34x faster                                                       |
| deepcopy                   | 238 us                                                      | 191 us: 1.25x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 64.1 ms: 1.23x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 54.7 ms: 1.22x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.7 us: 1.21x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.2 ms: 1.21x faster                                                       |
| scimark_fft                | 184 ms                                                      | 153 ms: 1.21x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 111 us: 1.20x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 41.1 ms: 1.18x faster                                                       |
| float                      | 56.8 ms                                                     | 48.8 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.21 ms: 1.16x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.43 ms: 1.14x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 57.5 ms: 1.13x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 933 ms: 1.12x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.88 us: 1.12x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 462 ms: 1.11x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 50.4 ms: 1.11x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.10x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 84.4 ms: 1.10x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 54.1 ms: 1.09x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.7 ms: 1.09x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 74.3 ms: 1.08x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 81.3 ms: 1.08x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 56.4 ns: 1.07x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 35.3 ms: 1.07x faster                                                       |
| chaos                      | 43.3 ms                                                     | 40.8 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.06x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.30 sec: 1.05x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 815 us: 1.05x faster                                                        |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 72.6 ms: 1.03x faster                                                       |
| pyflate                    | 295 ms                                                      | 287 ms: 1.03x faster                                                        |
| fannkuch                   | 247 ms                                                      | 240 ms: 1.03x faster                                                        |
| go                         | 91.6 ms                                                     | 89.7 ms: 1.02x faster                                                       |
| pycparser                  | 699 ms                                                      | 690 ms: 1.01x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 90.7 ms: 1.01x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.66 us: 1.01x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 62.6 ms: 1.00x faster                                                       |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 203 us: 1.04x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.05x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.34 ms: 1.05x slower                                                       |
| generators                 | 22.5 ms                                                     | 23.7 ms: 1.05x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                                       |
| raytrace                   | 192 ms                                                      | 204 ms: 1.06x slower                                                        |
| sympy_expand               | 284 ms                                                      | 303 ms: 1.07x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 864 us: 1.07x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                                       |
| async_generators           | 239 ms                                                      | 262 ms: 1.09x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 206 ms: 1.10x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 38.3 ms: 1.11x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.50 ms: 1.14x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.8 ms: 1.15x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 81.8 ms: 1.18x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.95 ms: 1.21x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.5 ms: 1.21x slower                                                       |
| richards_super             | 32.1 ms                                                     | 39.4 ms: 1.23x slower                                                       |
| richards                   | 28.4 ms                                                     | 35.2 ms: 1.24x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.90 ms: 1.25x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 18.4 ms: 1.29x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.09 ms: 1.45x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (3): 2to3, logging_simple, json
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241207-3.14.0a2+-79b7cab-JIT/bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 99.82% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown