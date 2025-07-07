# Results vs. 3.12.0

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.025x slower
- HPT reliability: 98.87%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.04x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.89 sec: 1.74x slower                                                     |
| Geometric mean | (ref)                                                       | 1.34x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 370 ms: 2.08x faster                                                       |
| async_tree_io              | 731 ms                                                      | 406 ms: 1.80x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 222 ms: 1.66x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                       |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 374 ms: 1.31x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.56x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.4 ms: 1.22x faster                                                      |
| pidigits       | 152 ms                                                      | 136 ms: 1.12x faster                                                       |
| nbody          | 71.9 ms                                                     | 83.9 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 93.3 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 58.3 ms: 1.12x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 89.7 ms: 1.04x faster                                                      |
| pickle               | 7.43 us                                                     | 7.64 us: 1.03x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.04 us: 1.07x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.2 us: 1.10x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.03 us: 1.10x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 63.5 ms: 1.14x slower                                                      |
| json_loads           | 13.9 us                                                     | 16.0 us: 1.15x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 154 us: 1.15x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.65 ms: 1.17x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 44.5 ms: 1.18x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 232 us: 1.19x slower                                                       |
| unpickle             | 8.18 us                                                     | 10.4 us: 1.27x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.66 sec: 1.95x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.20x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                      |
| mako            | 7.09 ms                                                     | 9.81 ms: 1.38x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.29x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.2 ms: 2.50x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 370 ms: 2.08x faster                                                       |
| async_tree_io              | 731 ms                                                      | 406 ms: 1.80x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 222 ms: 1.66x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                       |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.33 us: 1.33x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 374 ms: 1.31x faster                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.22 ms: 1.25x faster                                                      |
| float                      | 56.8 ms                                                     | 46.4 ms: 1.22x faster                                                      |
| mdp                        | 1.37 sec                                                    | 1.13 sec: 1.21x faster                                                     |
| deepcopy                   | 238 us                                                      | 201 us: 1.18x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.18x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.8 us: 1.14x faster                                                      |
| pidigits                   | 152 ms                                                      | 136 ms: 1.12x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 58.3 ms: 1.12x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.1 ms: 1.05x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 89.7 ms: 1.04x faster                                                      |
| generators                 | 22.5 ms                                                     | 22.7 ms: 1.01x slower                                                      |
| go                         | 91.6 ms                                                     | 92.4 ms: 1.01x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.64 us: 1.03x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 62.3 ns: 1.03x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 38.6 ns: 1.03x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.16 us: 1.03x slower                                                      |
| 2to3                       | 218 ms                                                      | 226 ms: 1.04x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| pycparser                  | 699 ms                                                      | 729 ms: 1.04x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 97.4 ms: 1.06x slower                                                      |
| pyflate                    | 295 ms                                                      | 314 ms: 1.07x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 93.3 ms: 1.07x slower                                                      |
| chaos                      | 43.3 ms                                                     | 46.3 ms: 1.07x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.04 us: 1.07x slower                                                      |
| async_generators           | 239 ms                                                      | 257 ms: 1.08x slower                                                       |
| sympy_str                  | 175 ms                                                      | 190 ms: 1.09x slower                                                       |
| raytrace                   | 192 ms                                                      | 210 ms: 1.09x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.1 ms: 1.09x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 86.2 ms: 1.09x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.35 us: 1.10x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 20.2 us: 1.10x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.89 us: 1.10x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 564 ms: 1.10x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 3.03 us: 1.10x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 73.8 ms: 1.10x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.56 ms: 1.11x slower                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.33 sec: 1.11x slower                                                     |
| scimark_lu                 | 58.9 ms                                                     | 65.7 ms: 1.12x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.42 ms: 1.12x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 63.5 ms: 1.14x slower                                                      |
| sympy_expand               | 284 ms                                                      | 323 ms: 1.14x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.9 ms: 1.14x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 71.9 ms: 1.15x slower                                                      |
| scimark_fft                | 184 ms                                                      | 211 ms: 1.15x slower                                                       |
| json_loads                 | 13.9 us                                                     | 16.0 us: 1.15x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 79.5 ms: 1.15x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 85.8 ms: 1.15x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 55.8 ms: 1.15x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 154 us: 1.15x slower                                                       |
| nbody                      | 71.9 ms                                                     | 83.9 ms: 1.17x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.65 ms: 1.17x slower                                                      |
| richards                   | 28.4 ms                                                     | 33.2 ms: 1.17x slower                                                      |
| fannkuch                   | 247 ms                                                      | 291 ms: 1.18x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 44.5 ms: 1.18x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 232 us: 1.19x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.20x slower                                                      |
| django_template            | 22.9 ms                                                     | 27.5 ms: 1.20x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.10 ms: 1.21x slower                                                      |
| richards_super             | 32.1 ms                                                     | 40.0 ms: 1.25x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.08 ms: 1.26x slower                                                      |
| unpickle                   | 8.18 us                                                     | 10.4 us: 1.27x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.54 ms: 1.34x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 128 us: 1.34x slower                                                       |
| mako                       | 7.09 ms                                                     | 9.81 ms: 1.38x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.05 ms: 1.40x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.71 sec: 1.64x slower                                                     |
| coverage                   | 40.8 ms                                                     | 67.1 ms: 1.64x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.89 sec: 1.74x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.66 sec: 1.95x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (3): regex_effbot, json, asyncio_tcp
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250705-3.15.0a0-1953713-NOGIL/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.025x slower

# HPT report

- Reliability score: 98.87% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown