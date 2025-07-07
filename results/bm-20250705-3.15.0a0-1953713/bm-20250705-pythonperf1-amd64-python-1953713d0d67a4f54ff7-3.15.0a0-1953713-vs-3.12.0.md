# Results vs. 3.12.0

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.089x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 387 ms: 1.99x faster                                                       |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                       |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                      |
| nbody          | 71.9 ms                                                     | 64.3 ms: 1.12x faster                                                      |
| pidigits       | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 80.2 ms: 1.09x faster                                                      |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.1 ms: 1.04x faster                                                      |
| unpickle_list        | 2.75 us                                                     | 2.76 us: 1.01x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 134 us: 1.01x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| xml_etree_process    | 37.7 ms                                                     | 38.9 ms: 1.03x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.47 us: 1.04x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.5 us: 1.06x slower                                                      |
| pickle               | 7.43 us                                                     | 7.99 us: 1.08x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 213 us: 1.09x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.41 ms: 1.13x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.33 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.85 ms: 1.04x faster                                                      |
| django_template | 22.9 ms                                                     | 23.7 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.6 ms: 2.55x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 387 ms: 1.99x faster                                                       |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 208 ms: 1.76x faster                                                       |
| async_tree_none            | 291 ms                                                      | 169 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                       |
| mdp                        | 1.37 sec                                                    | 817 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 206 ms: 1.65x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.33 sec: 1.57x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                       |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.9 us: 1.30x faster                                                      |
| float                      | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.5 us: 1.28x faster                                                      |
| go                         | 91.6 ms                                                     | 77.7 ms: 1.18x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.14x faster                                                      |
| nbody                      | 71.9 ms                                                     | 64.3 ms: 1.12x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.6 ms: 1.09x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 80.2 ms: 1.09x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.5 ns: 1.09x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 449 ms: 1.09x faster                                                       |
| raytrace                   | 192 ms                                                      | 178 ms: 1.08x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.8 ms: 1.07x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.7 ms: 1.06x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                                      |
| pidigits                   | 152 ms                                                      | 145 ms: 1.05x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 87.2 ms: 1.05x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 63.9 ms: 1.05x faster                                                      |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.1 ms: 1.04x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.8 ms: 1.04x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 493 ms: 1.04x faster                                                       |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                      |
| sympy_str                  | 175 ms                                                      | 168 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.04x faster                                                     |
| mako                       | 7.09 ms                                                     | 6.85 ms: 1.04x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.49 ms: 1.03x faster                                                      |
| async_generators           | 239 ms                                                      | 233 ms: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 36.5 ns: 1.03x faster                                                      |
| scimark_fft                | 184 ms                                                      | 180 ms: 1.03x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 61.5 ms: 1.02x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 73.2 ms: 1.02x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 77.4 ms: 1.02x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 57.8 ms: 1.02x faster                                                      |
| pyflate                    | 295 ms                                                      | 292 ms: 1.01x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 48.2 ms: 1.01x faster                                                      |
| unpickle_list              | 2.75 us                                                     | 2.76 us: 1.01x slower                                                      |
| sympy_expand               | 284 ms                                                      | 286 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 134 us: 1.01x slower                                                       |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.16 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| pycparser                  | 699 ms                                                      | 714 ms: 1.02x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| xml_etree_process          | 37.7 ms                                                     | 38.9 ms: 1.03x slower                                                      |
| django_template            | 22.9 ms                                                     | 23.7 ms: 1.04x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.47 us: 1.04x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.5 us: 1.06x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.99 us: 1.08x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 213 us: 1.09x slower                                                       |
| fannkuch                   | 247 ms                                                      | 270 ms: 1.10x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.54 ms: 1.10x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.41 ms: 1.13x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.33 us: 1.18x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| coverage                   | 40.8 ms                                                     | 50.7 ms: 1.24x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 95.2 ms: 1.38x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.40x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.75x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (6): bench_thread_pool, xml_etree_iterparse, logging_simple, logging_format, coroutines, regex_v8
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.089x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown