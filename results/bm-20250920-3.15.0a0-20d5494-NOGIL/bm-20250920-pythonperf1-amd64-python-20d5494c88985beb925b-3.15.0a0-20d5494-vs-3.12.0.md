# Results vs. 3.12.0

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.008x faster
- HPT reliability: 97.16%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.74 sec: 1.65x slower                                                     |
| Geometric mean | (ref)                                                       | 1.30x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 326 ms: 2.36x faster                                                       |
| async_tree_io              | 731 ms                                                      | 347 ms: 2.11x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 188 ms: 1.95x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 147 ms: 1.93x faster                                                       |
| async_tree_none            | 291 ms                                                      | 167 ms: 1.74x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 303 ms: 1.66x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 325 ms: 1.50x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.84x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.2 ms: 1.23x faster                                                      |
| pidigits       | 152 ms                                                      | 136 ms: 1.12x faster                                                       |
| nbody          | 71.9 ms                                                     | 85.1 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 112 ms: 1.13x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.1 ms: 1.08x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 92.1 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 58.8 ms: 1.11x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 88.1 ms: 1.06x faster                                                      |
| pickle_list          | 2.83 us                                                     | 3.00 us: 1.06x slower                                                      |
| pickle               | 7.43 us                                                     | 8.17 us: 1.10x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.03 us: 1.10x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 62.3 ms: 1.12x slower                                                      |
| json_loads           | 13.9 us                                                     | 16.0 us: 1.15x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 44.0 ms: 1.17x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 156 us: 1.17x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 21.6 us: 1.18x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 233 us: 1.19x slower                                                       |
| unpickle             | 8.18 us                                                     | 10.1 us: 1.24x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.31 sec: 1.69x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.8 ms: 1.15x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.2 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 27.3 ms: 1.19x slower                                                      |
| mako            | 7.09 ms                                                     | 9.82 ms: 1.39x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.29x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.6 ms: 2.72x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 326 ms: 2.36x faster                                                       |
| async_tree_io              | 731 ms                                                      | 347 ms: 2.11x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 188 ms: 1.95x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 147 ms: 1.93x faster                                                       |
| async_tree_none            | 291 ms                                                      | 167 ms: 1.74x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 303 ms: 1.66x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 325 ms: 1.50x faster                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.14 ms: 1.34x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.36 us: 1.30x faster                                                      |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.8 us: 1.26x faster                                                      |
| mdp                        | 1.37 sec                                                    | 1.10 sec: 1.25x faster                                                     |
| float                      | 56.8 ms                                                     | 46.2 ms: 1.23x faster                                                      |
| comprehensions             | 14.1 us                                                     | 12.2 us: 1.15x faster                                                      |
| regex_dna                  | 126 ms                                                      | 112 ms: 1.13x faster                                                       |
| pidigits                   | 152 ms                                                      | 136 ms: 1.12x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 58.8 ms: 1.11x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.1 ms: 1.08x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.0 ms: 1.08x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 88.1 ms: 1.06x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 37.0 ns: 1.01x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                      |
| json                       | 3.05 ms                                                     | 3.09 ms: 1.02x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 61.8 ns: 1.02x slower                                                      |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| pycparser                  | 699 ms                                                      | 722 ms: 1.03x slower                                                       |
| generators                 | 22.5 ms                                                     | 23.4 ms: 1.04x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.58 us: 1.05x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 92.1 ms: 1.05x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 96.3 ms: 1.05x slower                                                      |
| pyflate                    | 295 ms                                                      | 311 ms: 1.05x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 73.4 ms: 1.06x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.00 us: 1.06x slower                                                      |
| chaos                      | 43.3 ms                                                     | 46.4 ms: 1.07x slower                                                      |
| sympy_str                  | 175 ms                                                      | 188 ms: 1.08x slower                                                       |
| async_generators           | 239 ms                                                      | 258 ms: 1.08x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.24 us: 1.08x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.0 ms: 1.08x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 64.1 ms: 1.09x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 73.6 ms: 1.10x slower                                                      |
| pickle                     | 7.43 us                                                     | 8.17 us: 1.10x slower                                                      |
| raytrace                   | 192 ms                                                      | 212 ms: 1.10x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.27 ms: 1.10x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.03 us: 1.10x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 567 ms: 1.10x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 540 ms: 1.11x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 62.3 ms: 1.12x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.61 ms: 1.13x slower                                                      |
| sympy_expand               | 284 ms                                                      | 320 ms: 1.13x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 89.5 ms: 1.14x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.0 ms: 1.14x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.47 ms: 1.14x slower                                                      |
| scimark_fft                | 184 ms                                                      | 212 ms: 1.15x slower                                                       |
| json_loads                 | 13.9 us                                                     | 16.0 us: 1.15x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.8 ms: 1.15x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 44.0 ms: 1.17x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 87.2 ms: 1.17x slower                                                      |
| richards                   | 28.4 ms                                                     | 33.2 ms: 1.17x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 156 us: 1.17x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 73.6 ms: 1.17x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 56.9 ms: 1.17x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 21.6 us: 1.18x slower                                                      |
| nbody                      | 71.9 ms                                                     | 85.1 ms: 1.18x slower                                                      |
| django_template            | 22.9 ms                                                     | 27.3 ms: 1.19x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.05 ms: 1.19x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 233 us: 1.19x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.97 ms: 1.20x slower                                                      |
| fannkuch                   | 247 ms                                                      | 298 ms: 1.21x slower                                                       |
| richards_super             | 32.1 ms                                                     | 38.9 ms: 1.21x slower                                                      |
| unpickle                   | 8.18 us                                                     | 10.1 us: 1.24x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.08 ms: 1.27x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.2 ms: 1.29x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 130 us: 1.36x slower                                                       |
| mako                       | 7.09 ms                                                     | 9.82 ms: 1.39x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.05 ms: 1.39x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.66 sec: 1.59x slower                                                     |
| coverage                   | 40.8 ms                                                     | 66.4 ms: 1.63x slower                                                      |
| docutils                   | 1.66 sec                                                    | 2.74 sec: 1.65x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.31 sec: 1.69x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (4): coroutines, go, deepcopy_reduce, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250920-3.15.0a0-20d5494-NOGIL/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 97.16% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown