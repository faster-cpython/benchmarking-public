# Results vs. 3.12.0

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: windows-amd64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.071x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                       |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.71x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.6 ms: 1.27x faster                                                      |
| nbody          | 71.9 ms                                                     | 62.7 ms: 1.15x faster                                                      |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.5 ms: 1.10x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                      |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 54.1 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 134 us: 1.00x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 37.9 ms: 1.01x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                     |
| unpickle_list        | 2.75 us                                                     | 2.81 us: 1.02x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.53 us: 1.04x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.6 us: 1.06x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.07x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 211 us: 1.08x slower                                                       |
| pickle               | 7.43 us                                                     | 8.02 us: 1.08x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.32 ms: 1.11x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.40 us: 1.20x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| python_startup         | 19.5 ms                                                     | 24.4 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.46 ms: 1.10x faster                                                      |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.8 ms: 2.70x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                       |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.71x faster                                                       |
| mdp                        | 1.37 sec                                                    | 811 ms: 1.69x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.29 sec: 1.62x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                       |
| deepcopy                   | 238 us                                                      | 173 us: 1.37x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.9 us: 1.32x faster                                                      |
| float                      | 56.8 ms                                                     | 44.6 ms: 1.27x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 404 ms: 1.21x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 57.3 ms: 1.17x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.82 us: 1.15x faster                                                      |
| nbody                      | 71.9 ms                                                     | 62.7 ms: 1.15x faster                                                      |
| go                         | 91.6 ms                                                     | 80.2 ms: 1.14x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 79.5 ms: 1.10x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.3 ms: 1.10x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.46 ms: 1.10x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.2 ms: 1.09x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.9 ms: 1.09x faster                                                      |
| scimark_fft                | 184 ms                                                      | 171 ms: 1.08x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 87.0 ms: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 88.4 ms: 1.05x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.44 ms: 1.05x faster                                                      |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 75.4 ms: 1.04x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.3 ms: 1.04x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                                      |
| pyflate                    | 295 ms                                                      | 283 ms: 1.04x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.3 ms: 1.04x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 56.7 ms: 1.04x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.7 ms: 1.04x faster                                                      |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.04x faster                                                      |
| richards_super             | 32.1 ms                                                     | 31.0 ms: 1.03x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 54.1 ms: 1.03x faster                                                      |
| json                       | 3.05 ms                                                     | 2.96 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.9 ms: 1.02x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| unpickle_pure_python       | 133 us                                                      | 134 us: 1.00x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 37.9 ms: 1.01x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 37.8 ns: 1.01x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                     |
| raytrace                   | 192 ms                                                      | 195 ms: 1.01x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.38 us: 1.02x slower                                                      |
| fannkuch                   | 247 ms                                                      | 251 ms: 1.02x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.81 us: 1.02x slower                                                      |
| sympy_expand               | 284 ms                                                      | 290 ms: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.93 us: 1.03x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.53 us: 1.04x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.10 sec: 1.05x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 543 ms: 1.06x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.6 us: 1.06x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.07x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 211 us: 1.08x slower                                                       |
| pickle                     | 7.43 us                                                     | 8.02 us: 1.08x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.56 ms: 1.10x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.32 ms: 1.11x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.11x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.40 us: 1.20x slower                                                      |
| python_startup             | 19.5 ms                                                     | 24.4 ms: 1.25x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 91.2 ms: 1.32x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.09 ms: 1.38x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.28 ms: 1.71x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 317 ns: 5.25x slower                                                       |
| coverage                   | 40.8 ms                                                     | 296 ms: 7.25x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (6): bench_thread_pool, deltablue, hexiom, 2to3, pycparser, regex_v8
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.071x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown