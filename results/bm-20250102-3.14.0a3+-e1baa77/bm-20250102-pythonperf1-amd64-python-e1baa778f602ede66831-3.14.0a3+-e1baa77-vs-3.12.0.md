# Results vs. 3.12.0

- fork: python
- ref: e1baa778f602ede66831
- machine: windows-amd64
- commit hash: e1baa77
- commit date: 2025-01-02
- overall geometric mean: 1.015x faster
- HPT reliability: 89.57%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 408 ms: 1.79x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 182 ms: 1.60x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 225 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 352 ms: 1.39x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.63x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 51.8 ms: 1.10x faster                                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| nbody          | 71.9 ms                                                     | 75.9 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                       |
| regex_dna      | 126 ms                                                      | 124 ms: 1.02x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 86.4 ms: 1.01x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 24.6 ms: 1.72x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 86.7 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 57.0 ms: 1.02x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.1 ms: 1.06x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.10x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 222 us: 1.14x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.70 ms: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.3 ms: 1.07x slower                                                       |
| python_startup         | 19.5 ms                                                     | 23.3 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.77 ms: 1.05x faster                                                       |
| django_template | 22.9 ms                                                     | 25.3 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                        |
| async_tree_io              | 731 ms                                                      | 408 ms: 1.79x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 182 ms: 1.60x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 225 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 346 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 352 ms: 1.39x faster                                                        |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                                        |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.17x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.5 us: 1.16x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.44 ms: 1.12x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                                       |
| float                      | 56.8 ms                                                     | 51.8 ms: 1.10x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 86.7 ms: 1.07x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.6 ms: 1.06x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.2 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 63.7 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| json                       | 3.05 ms                                                     | 2.91 ms: 1.05x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.77 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.4 ms: 1.05x faster                                                       |
| go                         | 91.6 ms                                                     | 88.2 ms: 1.04x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 825 us: 1.04x faster                                                        |
| async_generators           | 239 ms                                                      | 232 ms: 1.03x faster                                                        |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| regex_dna                  | 126 ms                                                      | 124 ms: 1.02x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 47.8 ms: 1.01x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 86.4 ms: 1.01x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.65 us: 1.01x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.7 ms: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.25 us: 1.00x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                      |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 57.0 ms: 1.02x slower                                                       |
| raytrace                   | 192 ms                                                      | 197 ms: 1.02x slower                                                        |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| logging_silent             | 60.5 ns                                                     | 62.4 ns: 1.03x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 35.7 ms: 1.03x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 193 ms: 1.03x slower                                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.08 sec: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.04x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 65.1 ms: 1.04x slower                                                       |
| scimark_fft                | 184 ms                                                      | 191 ms: 1.04x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 77.5 ms: 1.04x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                      |
| pycparser                  | 699 ms                                                      | 732 ms: 1.05x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 541 ms: 1.05x slower                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.70 ms: 1.05x slower                                                       |
| nbody                      | 71.9 ms                                                     | 75.9 ms: 1.06x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.1 ms: 1.06x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.3 ms: 1.07x slower                                                       |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.07x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 63.2 ms: 1.07x slower                                                       |
| richards                   | 28.4 ms                                                     | 30.7 ms: 1.08x slower                                                       |
| pyflate                    | 295 ms                                                      | 319 ms: 1.08x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.44 ms: 1.08x slower                                                       |
| richards_super             | 32.1 ms                                                     | 34.8 ms: 1.09x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.09x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.2 ms: 1.10x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.10x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.3 ms: 1.10x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 900 us: 1.12x slower                                                        |
| fannkuch                   | 247 ms                                                      | 277 ms: 1.12x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 222 us: 1.14x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.77 ms: 1.15x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.3 ms: 1.16x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 91.3 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.16x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.70 ms: 1.18x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 82.3 ms: 1.19x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.3 ms: 1.20x slower                                                       |
| mypy2                      | 509 ms                                                      | 639 ms: 1.25x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.97 ms: 1.30x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 24.6 ms: 1.72x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): chaos
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250102-3.14.0a3+-e1baa77/bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.015x faster

# HPT report

- Reliability score: 89.57% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown