# Results vs. 3.12.0

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.038x faster
- HPT reliability: 81.22%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 2.81 sec: 1.69x slower                                                     |
| Geometric mean | (ref)                                                       | 1.30x slower                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 318 ms: 2.42x faster                                                       |
| async_tree_io              | 731 ms                                                      | 342 ms: 2.14x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 185 ms: 1.99x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 144 ms: 1.99x faster                                                       |
| async_tree_none            | 291 ms                                                      | 165 ms: 1.76x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 305 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 327 ms: 1.50x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.87x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.3 ms: 1.28x faster                                                      |
| pidigits       | 152 ms                                                      | 136 ms: 1.12x faster                                                       |
| nbody          | 71.9 ms                                                     | 78.1 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 112 ms: 1.13x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 88.7 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 58.5 ms: 1.11x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 90.5 ms: 1.03x faster                                                      |
| pickle               | 7.43 us                                                     | 7.85 us: 1.06x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.07 ms: 1.07x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.3 us: 1.10x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 61.6 ms: 1.10x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.13 us: 1.11x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.14x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 3.13 us: 1.14x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 223 us: 1.14x slower                                                       |
| json_loads           | 13.9 us                                                     | 16.0 us: 1.15x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 43.4 ms: 1.15x slower                                                      |
| unpickle             | 8.18 us                                                     | 10.4 us: 1.28x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.31 sec: 1.69x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                      |
| mako            | 7.09 ms                                                     | 9.68 ms: 1.37x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.24x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.2 ms: 2.75x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 318 ms: 2.42x faster                                                       |
| async_tree_io              | 731 ms                                                      | 342 ms: 2.14x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 185 ms: 1.99x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 144 ms: 1.99x faster                                                       |
| async_tree_none            | 291 ms                                                      | 165 ms: 1.76x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 202 ms: 1.68x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 305 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 327 ms: 1.50x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.00 sec: 1.37x faster                                                     |
| gc_traversal               | 1.52 ms                                                     | 1.16 ms: 1.32x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.1 us: 1.31x faster                                                      |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.36 us: 1.29x faster                                                      |
| float                      | 56.8 ms                                                     | 44.3 ms: 1.28x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.5 us: 1.22x faster                                                      |
| regex_dna                  | 126 ms                                                      | 112 ms: 1.13x faster                                                       |
| pidigits                   | 152 ms                                                      | 136 ms: 1.12x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 58.5 ms: 1.11x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.8 ms: 1.09x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 457 ms: 1.07x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.1 ms: 1.07x faster                                                      |
| go                         | 91.6 ms                                                     | 86.4 ms: 1.06x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.54 ms: 1.05x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.02 us: 1.04x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 58.6 ns: 1.03x faster                                                      |
| scimark_fft                | 184 ms                                                      | 179 ms: 1.03x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.5 ms: 1.03x faster                                                      |
| pycparser                  | 699 ms                                                      | 685 ms: 1.02x faster                                                       |
| json                       | 3.05 ms                                                     | 3.07 ms: 1.01x slower                                                      |
| pyflate                    | 295 ms                                                      | 298 ms: 1.01x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 88.7 ms: 1.01x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 93.0 ms: 1.02x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 80.2 ms: 1.02x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.42 us: 1.02x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 526 ms: 1.03x slower                                                       |
| async_generators           | 239 ms                                                      | 246 ms: 1.03x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 38.5 ns: 1.03x slower                                                      |
| sympy_str                  | 175 ms                                                      | 180 ms: 1.03x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 60.8 ms: 1.03x slower                                                      |
| chaos                      | 43.3 ms                                                     | 45.0 ms: 1.04x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.99 us: 1.04x slower                                                      |
| raytrace                   | 192 ms                                                      | 202 ms: 1.05x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.85 us: 1.06x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.34 ms: 1.06x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.07 ms: 1.07x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.31 ms: 1.07x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 71.7 ms: 1.07x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 74.4 ms: 1.08x slower                                                      |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.09x slower                                                       |
| nbody                      | 71.9 ms                                                     | 78.1 ms: 1.09x slower                                                      |
| richards                   | 28.4 ms                                                     | 31.1 ms: 1.10x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 20.3 us: 1.10x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 61.6 ms: 1.10x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.13 us: 1.11x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.84 ms: 1.11x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.0 ms: 1.12x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 54.5 ms: 1.12x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 70.9 ms: 1.13x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.4 ms: 1.13x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.14x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 3.13 us: 1.14x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 223 us: 1.14x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 85.2 ms: 1.14x slower                                                      |
| json_loads                 | 13.9 us                                                     | 16.0 us: 1.15x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 43.4 ms: 1.15x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                      |
| fannkuch                   | 247 ms                                                      | 293 ms: 1.19x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 1.02 ms: 1.19x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.97 ms: 1.20x slower                                                      |
| unpickle                   | 8.18 us                                                     | 10.4 us: 1.28x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 125 us: 1.32x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                      |
| mako                       | 7.09 ms                                                     | 9.68 ms: 1.37x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.09 ms: 1.45x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.57 sec: 1.50x slower                                                     |
| coverage                   | 40.8 ms                                                     | 66.3 ms: 1.62x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 2.31 sec: 1.69x slower                                                     |
| docutils                   | 1.66 sec                                                    | 2.81 sec: 1.69x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (3): coroutines, 2to3, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251004-3.15.0a0-880c952-NOGIL/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 81.22% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown