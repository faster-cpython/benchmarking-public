# Results vs. 3.12.0

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.131x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 386 ms: 2.00x faster                                                       |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 40.2 ms: 1.41x faster                                                      |
| nbody          | 71.9 ms                                                     | 54.6 ms: 1.32x faster                                                      |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.7 ms: 1.11x faster                                                      |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.25x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 106 us: 1.25x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 50.0 ms: 1.12x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.4 ms: 1.07x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 87.5 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.7 ms: 1.06x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.44 ms: 1.05x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| pickle               | 7.43 us                                                     | 7.73 us: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 205 us: 1.05x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.71 us: 1.06x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.8 us: 1.08x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.25 us: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.5 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.36 ms: 1.32x faster                                                      |
| django_template | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.4 ms: 2.73x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 386 ms: 2.00x faster                                                       |
| async_tree_io              | 731 ms                                                      | 393 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                       |
| mdp                        | 1.37 sec                                                    | 807 ms: 1.70x faster                                                       |
| async_tree_none            | 291 ms                                                      | 174 ms: 1.68x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 338 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 332 ms: 1.48x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.43 sec: 1.46x faster                                                     |
| deepcopy                   | 238 us                                                      | 165 us: 1.45x faster                                                       |
| float                      | 56.8 ms                                                     | 40.2 ms: 1.41x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 16.8 us: 1.41x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.36 ms: 1.32x faster                                                      |
| nbody                      | 71.9 ms                                                     | 54.6 ms: 1.32x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.25x faster                                                     |
| unpickle_pure_python       | 133 us                                                      | 106 us: 1.25x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 864 ms: 1.21x faster                                                       |
| scimark_fft                | 184 ms                                                      | 154 ms: 1.20x faster                                                       |
| go                         | 91.6 ms                                                     | 76.5 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.78 us: 1.18x faster                                                      |
| pyflate                    | 295 ms                                                      | 251 ms: 1.18x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 439 ms: 1.17x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                      |
| fannkuch                   | 247 ms                                                      | 216 ms: 1.14x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.13x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.27 ms: 1.13x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 50.0 ms: 1.12x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.7 ms: 1.11x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 54.5 ns: 1.11x faster                                                      |
| raytrace                   | 192 ms                                                      | 176 ms: 1.10x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.1 ms: 1.09x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.7 ms: 1.09x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 34.5 ns: 1.09x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 62.4 ms: 1.07x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 45.3 ms: 1.07x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.5 ms: 1.07x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.4 ms: 1.07x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 87.5 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.7 ms: 1.06x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.44 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.1 ms: 1.04x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.06 us: 1.04x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.54 us: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| json                       | 3.05 ms                                                     | 2.97 ms: 1.02x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.3 ms: 1.02x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.8 ms: 1.02x faster                                                      |
| richards_super             | 32.1 ms                                                     | 31.4 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.02x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 58.1 ms: 1.01x faster                                                      |
| telco                      | 4.13 ms                                                     | 4.08 ms: 1.01x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 78.2 ms: 1.01x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.08 ms: 1.01x faster                                                      |
| async_generators           | 239 ms                                                      | 241 ms: 1.01x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.67 sec: 1.01x slower                                                     |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.18 ms: 1.01x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| pycparser                  | 699 ms                                                      | 712 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| sympy_expand               | 284 ms                                                      | 293 ms: 1.03x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 506 ms: 1.04x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.73 us: 1.04x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 205 us: 1.05x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.71 us: 1.06x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.8 us: 1.08x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.09x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.25 us: 1.15x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.3 ms: 1.21x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.5 ms: 1.31x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 91.4 ms: 1.32x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.13 ms: 1.40x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.28 ms: 1.70x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (3): meteor_contest, unpickle_list, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.131x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown