# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-amd64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.005x faster
- HPT reliability: 94.90%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.91 sec: 1.75x slower                                                     |
| Geometric mean | (ref)                                                       | 1.34x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 329 ms: 2.35x faster                                                       |
| async_tree_io              | 731 ms                                                      | 350 ms: 2.09x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 147 ms: 1.94x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 190 ms: 1.93x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 312 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.82x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.6 ms: 1.25x faster                                                      |
| pidigits       | 152 ms                                                      | 139 ms: 1.09x faster                                                       |
| nbody          | 71.9 ms                                                     | 76.9 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.10x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.4 ms: 1.06x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 91.4 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 59.0 ms: 1.10x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 91.7 ms: 1.01x faster                                                      |
| pickle               | 7.43 us                                                     | 8.17 us: 1.10x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 62.2 ms: 1.11x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 152 us: 1.14x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 21.2 us: 1.15x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.17 us: 1.15x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 228 us: 1.17x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 44.8 ms: 1.19x slower                                                      |
| json_loads           | 13.9 us                                                     | 16.7 us: 1.20x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.41 us: 1.21x slower                                                      |
| unpickle             | 8.18 us                                                     | 10.0 us: 1.23x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 7.28 ms: 1.28x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.58 sec: 1.89x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.18x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.1 ms: 1.23x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.6 ms: 1.36x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                      |
| mako            | 7.09 ms                                                     | 9.69 ms: 1.37x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.25x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.0 ms: 2.52x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 329 ms: 2.35x faster                                                       |
| async_tree_io              | 731 ms                                                      | 350 ms: 2.09x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 147 ms: 1.94x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 190 ms: 1.93x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 312 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.03 sec: 1.33x faster                                                     |
| sqlite_synth               | 1.76 us                                                     | 1.36 us: 1.30x faster                                                      |
| float                      | 56.8 ms                                                     | 45.6 ms: 1.25x faster                                                      |
| deepcopy                   | 238 us                                                      | 197 us: 1.21x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.8 us: 1.14x faster                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.36 ms: 1.12x faster                                                      |
| comprehensions             | 14.1 us                                                     | 12.8 us: 1.11x faster                                                      |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.10x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.0 ms: 1.10x faster                                                      |
| pidigits                   | 152 ms                                                      | 139 ms: 1.09x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.1 ms: 1.09x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.5 ms: 1.07x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.4 ms: 1.06x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 63.8 ms: 1.05x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 91.7 ms: 1.01x faster                                                      |
| go                         | 91.6 ms                                                     | 90.7 ms: 1.01x faster                                                      |
| pycparser                  | 699 ms                                                      | 706 ms: 1.01x slower                                                       |
| chaos                      | 43.3 ms                                                     | 43.8 ms: 1.01x slower                                                      |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 91.4 ms: 1.04x slower                                                      |
| json                       | 3.05 ms                                                     | 3.19 ms: 1.05x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 96.7 ms: 1.06x slower                                                      |
| pyflate                    | 295 ms                                                      | 313 ms: 1.06x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.30 ms: 1.06x slower                                                      |
| raytrace                   | 192 ms                                                      | 205 ms: 1.07x slower                                                       |
| nbody                      | 71.9 ms                                                     | 76.9 ms: 1.07x slower                                                      |
| sympy_str                  | 175 ms                                                      | 187 ms: 1.07x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 40.3 ns: 1.07x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 84.7 ms: 1.07x slower                                                      |
| scimark_fft                | 184 ms                                                      | 200 ms: 1.08x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 68.2 ms: 1.09x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.30 us: 1.09x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.1 ms: 1.09x slower                                                      |
| async_generators           | 239 ms                                                      | 260 ms: 1.09x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 561 ms: 1.09x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 64.4 ms: 1.09x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.88 us: 1.10x slower                                                      |
| pickle                     | 7.43 us                                                     | 8.17 us: 1.10x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.4 ms: 1.11x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.54 ms: 1.11x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 62.2 ms: 1.11x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.2 ms: 1.14x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 152 us: 1.14x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                      |
| sympy_expand               | 284 ms                                                      | 325 ms: 1.15x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 79.5 ms: 1.15x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 55.7 ms: 1.15x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 21.2 us: 1.15x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.94 ms: 1.15x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 562 ms: 1.15x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 3.17 us: 1.15x slower                                                      |
| richards_super             | 32.1 ms                                                     | 37.4 ms: 1.17x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 228 us: 1.17x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 88.1 ms: 1.18x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 44.8 ms: 1.19x slower                                                      |
| fannkuch                   | 247 ms                                                      | 293 ms: 1.19x slower                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.50 sec: 1.19x slower                                                     |
| json_loads                 | 13.9 us                                                     | 16.7 us: 1.20x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.41 us: 1.21x slower                                                      |
| unpickle                   | 8.18 us                                                     | 10.0 us: 1.23x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 20.1 ms: 1.23x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 7.28 ms: 1.28x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.30 ms: 1.28x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.10 ms: 1.29x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.6 ms: 1.36x slower                                                      |
| mako                       | 7.09 ms                                                     | 9.69 ms: 1.37x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 130 us: 1.37x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.08 ms: 1.43x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.74 sec: 1.66x slower                                                     |
| coverage                   | 40.8 ms                                                     | 68.2 ms: 1.67x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.91 sec: 1.75x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.58 sec: 1.89x slower                                                     |
| logging_silent             | 60.5 ns                                                     | 368 ns: 6.09x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (2): deepcopy_reduce, generators
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 94.90% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown