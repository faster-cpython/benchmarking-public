# Results vs. 3.12.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.144x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 380 ms: 2.03x faster                                                       |
| async_tree_io              | 731 ms                                                      | 386 ms: 1.90x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.71x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 200 ms: 1.70x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 332 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.72x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 52.3 ms: 1.37x faster                                                      |
| float          | 56.8 ms                                                     | 42.8 ms: 1.33x faster                                                      |
| pidigits       | 152 ms                                                      | 144 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.3 ms: 1.12x faster                                                      |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.52 ms: 1.06x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 105 us: 1.27x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.25x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 49.6 ms: 1.12x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.1 ms: 1.07x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 87.8 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.0 ms: 1.05x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.48 ms: 1.04x faster                                                      |
| unpickle_list        | 2.75 us                                                     | 2.70 us: 1.02x faster                                                      |
| pickle               | 7.43 us                                                     | 7.53 us: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.38 us: 1.02x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 203 us: 1.04x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.3 us: 1.05x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.19 us: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.25 ms: 1.35x faster                                                      |
| django_template | 22.9 ms                                                     | 23.8 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.7 ms: 2.71x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 380 ms: 2.03x faster                                                       |
| async_tree_io              | 731 ms                                                      | 386 ms: 1.90x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 209 ms: 1.76x faster                                                       |
| mdp                        | 1.37 sec                                                    | 783 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.71x faster                                                       |
| async_tree_none            | 291 ms                                                      | 171 ms: 1.71x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 200 ms: 1.70x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.32 sec: 1.58x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 332 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                       |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                       |
| nbody                      | 71.9 ms                                                     | 52.3 ms: 1.37x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.37x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.25 ms: 1.35x faster                                                      |
| float                      | 56.8 ms                                                     | 42.8 ms: 1.33x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 105 us: 1.27x faster                                                       |
| scimark_fft                | 184 ms                                                      | 146 ms: 1.26x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.25x faster                                                     |
| deepcopy_memo              | 23.7 us                                                     | 19.1 us: 1.24x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 849 ms: 1.23x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 424 ms: 1.21x faster                                                       |
| go                         | 91.6 ms                                                     | 77.4 ms: 1.18x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.2 ms: 1.17x faster                                                      |
| fannkuch                   | 247 ms                                                      | 211 ms: 1.17x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.53 us: 1.15x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.23 ms: 1.15x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 38.7 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.14x faster                                                      |
| pyflate                    | 295 ms                                                      | 260 ms: 1.13x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 49.6 ms: 1.12x faster                                                      |
| raytrace                   | 192 ms                                                      | 172 ms: 1.12x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 54.1 ns: 1.12x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.3 ms: 1.12x faster                                                      |
| telco                      | 4.13 ms                                                     | 3.75 ms: 1.10x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 34.2 ns: 1.09x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.2 ms: 1.09x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 84.4 ms: 1.08x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 44.9 ms: 1.08x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 62.1 ms: 1.08x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.2 ms: 1.08x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.1 ms: 1.07x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 455 ms: 1.07x faster                                                       |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.52 ms: 1.06x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.1 ms: 1.06x faster                                                      |
| pidigits                   | 152 ms                                                      | 144 ms: 1.06x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 87.8 ms: 1.06x faster                                                      |
| json                       | 3.05 ms                                                     | 2.88 ms: 1.06x faster                                                      |
| sympy_str                  | 175 ms                                                      | 166 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.0 ms: 1.05x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.1 ms: 1.05x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.1 ms: 1.05x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.01 us: 1.05x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.46 us: 1.04x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.9 ms: 1.04x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.48 ms: 1.04x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| unpickle_list              | 2.75 us                                                     | 2.70 us: 1.02x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 58.2 ms: 1.01x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 78.2 ms: 1.01x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.13 ms: 1.01x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.53 us: 1.01x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.21 ms: 1.02x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.38 us: 1.02x slower                                                      |
| sympy_expand               | 284 ms                                                      | 291 ms: 1.03x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 203 us: 1.04x slower                                                       |
| django_template            | 22.9 ms                                                     | 23.8 ms: 1.04x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.3 us: 1.05x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.09x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.19 us: 1.13x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.3 ms: 1.21x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.32x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 93.3 ms: 1.35x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.11 ms: 1.39x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.28 ms: 1.70x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                               |

Benchmark hidden because not significant (5): bench_thread_pool, coroutines, pycparser, 2to3, async_generators
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.144x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown