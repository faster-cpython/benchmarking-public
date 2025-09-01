# Results vs. 3.12.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.007x slower
- HPT reliability: 99.13%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.87 sec: 1.73x slower                                                     |
| Geometric mean | (ref)                                                       | 1.34x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 329 ms: 2.35x faster                                                       |
| async_tree_io              | 731 ms                                                      | 350 ms: 2.09x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 190 ms: 1.94x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 149 ms: 1.92x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.72x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 310 ms: 1.62x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.82x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 47.0 ms: 1.21x faster                                                      |
| pidigits       | 152 ms                                                      | 136 ms: 1.12x faster                                                       |
| nbody          | 71.9 ms                                                     | 82.6 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.09x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 94.6 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 59.8 ms: 1.09x faster                                                      |
| pickle_list          | 2.83 us                                                     | 2.93 us: 1.04x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.99 ms: 1.05x slower                                                      |
| pickle               | 7.43 us                                                     | 8.04 us: 1.08x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 63.5 ms: 1.14x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.13 us: 1.14x slower                                                      |
| json_loads           | 13.9 us                                                     | 16.0 us: 1.15x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 21.6 us: 1.17x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 44.7 ms: 1.19x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 237 us: 1.21x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 161 us: 1.21x slower                                                       |
| unpickle             | 8.18 us                                                     | 10.3 us: 1.26x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.41 sec: 1.77x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.15x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 27.4 ms: 1.19x slower                                                      |
| mako            | 7.09 ms                                                     | 9.98 ms: 1.41x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.30x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.2 ms: 2.66x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 329 ms: 2.35x faster                                                       |
| async_tree_io              | 731 ms                                                      | 350 ms: 2.09x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 190 ms: 1.94x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 149 ms: 1.92x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.72x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 310 ms: 1.62x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.35 us: 1.30x faster                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.20 ms: 1.27x faster                                                      |
| float                      | 56.8 ms                                                     | 47.0 ms: 1.21x faster                                                      |
| mdp                        | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| deepcopy                   | 238 us                                                      | 202 us: 1.18x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.3 us: 1.15x faster                                                      |
| pidigits                   | 152 ms                                                      | 136 ms: 1.12x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.2 us: 1.12x faster                                                      |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.8 ms: 1.09x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.0 ms: 1.05x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                      |
| go                         | 91.6 ms                                                     | 92.7 ms: 1.01x slower                                                      |
| pycparser                  | 699 ms                                                      | 715 ms: 1.02x slower                                                       |
| generators                 | 22.5 ms                                                     | 23.1 ms: 1.02x slower                                                      |
| json                       | 3.05 ms                                                     | 3.13 ms: 1.03x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.15 us: 1.03x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.93 us: 1.04x slower                                                      |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 63.1 ns: 1.04x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.99 ms: 1.05x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.64 us: 1.06x slower                                                      |
| pyflate                    | 295 ms                                                      | 312 ms: 1.06x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.12 us: 1.06x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 39.7 ns: 1.06x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 97.3 ms: 1.06x slower                                                      |
| async_generators           | 239 ms                                                      | 256 ms: 1.07x slower                                                       |
| chaos                      | 43.3 ms                                                     | 46.4 ms: 1.07x slower                                                      |
| sympy_str                  | 175 ms                                                      | 188 ms: 1.08x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 94.6 ms: 1.08x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 72.4 ms: 1.08x slower                                                      |
| pickle                     | 7.43 us                                                     | 8.04 us: 1.08x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 15.5 ms: 1.08x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.2 ms: 1.09x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 564 ms: 1.10x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.39 ms: 1.11x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 65.9 ms: 1.12x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 88.4 ms: 1.12x slower                                                      |
| raytrace                   | 192 ms                                                      | 217 ms: 1.13x slower                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.36 sec: 1.13x slower                                                     |
| sympy_expand               | 284 ms                                                      | 321 ms: 1.13x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 553 ms: 1.13x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 63.5 ms: 1.14x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.13 us: 1.14x slower                                                      |
| scimark_fft                | 184 ms                                                      | 210 ms: 1.14x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 79.4 ms: 1.15x slower                                                      |
| nbody                      | 71.9 ms                                                     | 82.6 ms: 1.15x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.71 ms: 1.15x slower                                                      |
| json_loads                 | 13.9 us                                                     | 16.0 us: 1.15x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 51.0 ms: 1.17x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 21.6 us: 1.17x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 57.0 ms: 1.18x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.87 ms: 1.18x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 88.2 ms: 1.18x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 44.7 ms: 1.19x slower                                                      |
| richards                   | 28.4 ms                                                     | 33.8 ms: 1.19x slower                                                      |
| django_template            | 22.9 ms                                                     | 27.4 ms: 1.19x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.08 ms: 1.21x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 75.8 ms: 1.21x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 237 us: 1.21x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 161 us: 1.21x slower                                                       |
| fannkuch                   | 247 ms                                                      | 301 ms: 1.22x slower                                                       |
| richards_super             | 32.1 ms                                                     | 39.6 ms: 1.23x slower                                                      |
| unpickle                   | 8.18 us                                                     | 10.3 us: 1.26x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.10 ms: 1.29x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 979 us: 1.30x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.9 ms: 1.33x slower                                                      |
| mako                       | 7.09 ms                                                     | 9.98 ms: 1.41x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 134 us: 1.41x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.71 sec: 1.63x slower                                                     |
| coverage                   | 40.8 ms                                                     | 66.8 ms: 1.64x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.87 sec: 1.73x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.41 sec: 1.77x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250830-3.15.0a0-d3d94e0-NOGIL/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 99.13% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown