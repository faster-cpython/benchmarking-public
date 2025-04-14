# Results vs. 3.12.0

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: windows-amd64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.066x faster
- HPT reliability: 98.30%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 404 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 417 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.58x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 218 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 346 ms: 1.42x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.63x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 47.1 ms: 1.20x faster                                                       |
| nbody          | 71.9 ms                                                     | 60.0 ms: 1.20x faster                                                       |
| pidigits       | 152 ms                                                      | 152 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 83.7 ms: 1.05x faster                                                       |
| regex_dna      | 126 ms                                                      | 125 ms: 1.01x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 15.2 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 114 us: 1.17x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 51.6 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.0 ms: 1.05x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.8 ms: 1.02x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.2 ms: 1.02x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.66 us: 1.06x slower                                                       |
| pickle               | 7.43 us                                                     | 7.90 us: 1.06x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.93 us: 1.07x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 219 us: 1.12x slower                                                        |
| pickle_dict          | 18.4 us                                                     | 21.1 us: 1.15x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.25 us: 1.15x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.93 ms: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.34 ms: 1.33x faster                                                       |
| django_template | 22.9 ms                                                     | 25.8 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.9 ms: 2.52x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 404 ms: 1.91x faster                                                        |
| async_tree_io              | 731 ms                                                      | 417 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.66x faster                                                        |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.58x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 218 ms: 1.56x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.39 sec: 1.51x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 346 ms: 1.42x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.34 ms: 1.33x faster                                                       |
| deepcopy                   | 238 us                                                      | 184 us: 1.29x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.1 us: 1.27x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.09 ms: 1.22x faster                                                       |
| scimark_fft                | 184 ms                                                      | 152 ms: 1.21x faster                                                        |
| float                      | 56.8 ms                                                     | 47.1 ms: 1.20x faster                                                       |
| nbody                      | 71.9 ms                                                     | 60.0 ms: 1.20x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.1 us: 1.18x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 114 us: 1.17x faster                                                        |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.53 us: 1.15x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 51.6 ms: 1.08x faster                                                       |
| pyflate                    | 295 ms                                                      | 274 ms: 1.07x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 62.6 ms: 1.07x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.0 ms: 1.05x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 59.8 ms: 1.05x faster                                                       |
| go                         | 91.6 ms                                                     | 87.4 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 999 ms: 1.05x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 83.7 ms: 1.05x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.7 ms: 1.04x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.0 ms: 1.03x faster                                                       |
| json                       | 3.05 ms                                                     | 2.95 ms: 1.03x faster                                                       |
| chaos                      | 43.3 ms                                                     | 42.1 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.0 ms: 1.03x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.8 ms: 1.02x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 91.2 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 504 ms: 1.02x faster                                                        |
| regex_dna                  | 126 ms                                                      | 125 ms: 1.01x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 74.0 ms: 1.01x faster                                                       |
| pidigits                   | 152 ms                                                      | 152 ms: 1.00x faster                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                      |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.01 us: 1.04x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.07 ms: 1.04x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.32 ms: 1.05x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 841 us: 1.05x slower                                                        |
| pycparser                  | 699 ms                                                      | 730 ms: 1.05x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 45.7 ms: 1.05x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.57 us: 1.05x slower                                                       |
| async_generators           | 239 ms                                                      | 251 ms: 1.05x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 63.7 ns: 1.05x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.9 ms: 1.05x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 197 ms: 1.06x slower                                                        |
| unpickle                   | 8.18 us                                                     | 8.66 us: 1.06x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 36.6 ms: 1.06x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.90 us: 1.06x slower                                                       |
| richards_super             | 32.1 ms                                                     | 34.1 ms: 1.06x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.93 us: 1.07x slower                                                       |
| sympy_expand               | 284 ms                                                      | 303 ms: 1.07x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 15.2 ms: 1.07x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.39 ms: 1.07x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 84.5 ms: 1.07x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 64.8 ms: 1.10x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 41.4 ns: 1.11x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 219 us: 1.12x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.8 ms: 1.13x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 108 us: 1.14x slower                                                        |
| pickle_dict                | 18.4 us                                                     | 21.1 us: 1.15x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.25 us: 1.15x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.3 ms: 1.18x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.93 ms: 1.22x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 86.3 ms: 1.25x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.97 ms: 1.30x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.62x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (5): bench_thread_pool, fannkuch, asyncio_tcp, sympy_str, raytrace
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250301-3.14.0a5+-c9932a9-JIT/bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 98.30% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown