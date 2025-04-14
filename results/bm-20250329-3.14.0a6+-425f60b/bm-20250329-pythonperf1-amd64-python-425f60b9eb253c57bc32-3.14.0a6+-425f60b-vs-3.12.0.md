# Results vs. 3.12.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-amd64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.076x faster
- HPT reliability: 99.10%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 407 ms: 1.89x faster                                                        |
| async_tree_io              | 731 ms                                                      | 416 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                        |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.57x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 216 ms: 1.57x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.63x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.7 ms: 1.27x faster                                                       |
| nbody          | 71.9 ms                                                     | 64.2 ms: 1.12x faster                                                       |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.39 ms: 1.16x faster                                                       |
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 82.3 ms: 1.06x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.4 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 87.6 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.1 ms: 1.02x faster                                                       |
| unpickle             | 8.18 us                                                     | 8.27 us: 1.01x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 57.2 ms: 1.02x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 140 us: 1.05x slower                                                        |
| xml_etree_process    | 37.7 ms                                                     | 40.9 ms: 1.08x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.1 us: 1.09x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 216 us: 1.10x slower                                                        |
| pickle               | 7.43 us                                                     | 8.52 us: 1.15x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 21.3 us: 1.16x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.78 ms: 1.19x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.58 us: 1.27x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.71 ms: 1.06x faster                                                       |
| django_template | 22.9 ms                                                     | 25.4 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.5 ms: 2.48x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 407 ms: 1.89x faster                                                        |
| async_tree_io              | 731 ms                                                      | 416 ms: 1.76x faster                                                        |
| mdp                        | 1.37 sec                                                    | 799 ms: 1.72x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                        |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.57x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 216 ms: 1.57x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.43 sec: 1.46x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 337 ms: 1.45x faster                                                        |
| deepcopy                   | 238 us                                                      | 180 us: 1.32x faster                                                        |
| float                      | 56.8 ms                                                     | 44.7 ms: 1.27x faster                                                       |
| generators                 | 22.5 ms                                                     | 17.9 ms: 1.26x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.1 us: 1.24x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.5 us: 1.23x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 55.1 ms: 1.22x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.39 ms: 1.16x faster                                                       |
| go                         | 91.6 ms                                                     | 80.8 ms: 1.13x faster                                                       |
| nbody                      | 71.9 ms                                                     | 64.2 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.88 us: 1.11x faster                                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                        |
| chaos                      | 43.3 ms                                                     | 40.2 ms: 1.08x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 56.3 ns: 1.07x faster                                                       |
| async_generators           | 239 ms                                                      | 223 ms: 1.07x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.06x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 82.3 ms: 1.06x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.4 ms: 1.06x faster                                                       |
| raytrace                   | 192 ms                                                      | 181 ms: 1.06x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 87.6 ms: 1.06x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.71 ms: 1.06x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.1 ms: 1.05x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 76.7 ms: 1.03x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.3 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.6 ms: 1.02x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.5 ms: 1.02x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.8 ms: 1.02x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.12 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.1 ms: 1.02x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 37.0 ns: 1.01x faster                                                       |
| pyflate                    | 295 ms                                                      | 291 ms: 1.01x faster                                                        |
| sympy_integrate            | 13.0 ms                                                     | 12.9 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 43.5 ms: 1.01x faster                                                       |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                        |
| unpickle                   | 8.18 us                                                     | 8.27 us: 1.01x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 63.5 ms: 1.01x slower                                                       |
| json                       | 3.05 ms                                                     | 3.09 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 521 ms: 1.02x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.39 us: 1.02x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.02x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 76.2 ms: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.88 us: 1.02x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 57.2 ms: 1.02x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| pycparser                  | 699 ms                                                      | 728 ms: 1.04x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 61.6 ms: 1.05x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 140 us: 1.05x slower                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.69 ms: 1.05x slower                                                       |
| fannkuch                   | 247 ms                                                      | 260 ms: 1.06x slower                                                        |
| sympy_expand               | 284 ms                                                      | 301 ms: 1.06x slower                                                        |
| asyncio_tcp                | 487 ms                                                      | 520 ms: 1.07x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 40.9 ms: 1.08x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.1 us: 1.09x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 216 us: 1.10x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.4 ms: 1.11x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 107 us: 1.13x slower                                                        |
| pickle                     | 7.43 us                                                     | 8.52 us: 1.15x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 21.3 us: 1.16x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.87 ms: 1.18x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.3 ms: 1.18x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.78 ms: 1.19x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.58 us: 1.27x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.9 ms: 1.28x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.08 ms: 1.37x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.66x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (6): docutils, scimark_fft, sympy_str, unpickle_list, hexiom, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.076x faster

# HPT report

- Reliability score: 99.10% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown