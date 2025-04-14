# Results vs. 3.12.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: windows-amd64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.052x faster
- HPT reliability: 86.12%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 228 ms: 1.05x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.75 sec: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 421 ms: 1.83x faster                                                        |
| async_tree_io              | 731 ms                                                      | 425 ms: 1.72x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 219 ms: 1.67x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.60x faster                                                        |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.54x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 227 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 348 ms: 1.41x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.58x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.9 ms: 1.21x faster                                                       |
| nbody          | 71.9 ms                                                     | 63.4 ms: 1.13x faster                                                       |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                                       |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 13.5 ms: 1.05x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 86.2 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.24 sec: 1.11x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 125 us: 1.07x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 52.6 ms: 1.06x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 88.6 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 38.3 ms: 1.02x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.55 us: 1.04x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.91 us: 1.06x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.8 us: 1.08x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.3 us: 1.10x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 217 us: 1.11x slower                                                        |
| pickle               | 7.43 us                                                     | 8.31 us: 1.12x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.37 us: 1.19x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 7.13 ms: 1.25x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.6 ms: 1.27x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.76 ms: 1.23x faster                                                       |
| django_template | 22.9 ms                                                     | 26.7 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.7 ms: 2.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 421 ms: 1.83x faster                                                        |
| async_tree_io              | 731 ms                                                      | 425 ms: 1.72x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 219 ms: 1.67x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.60x faster                                                        |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.54x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 227 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.45 sec: 1.45x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 348 ms: 1.41x faster                                                        |
| deepcopy                   | 238 us                                                      | 188 us: 1.26x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.76 ms: 1.23x faster                                                       |
| float                      | 56.8 ms                                                     | 46.9 ms: 1.21x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.8 us: 1.20x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                       |
| scimark_fft                | 184 ms                                                      | 159 ms: 1.16x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.53 us: 1.15x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 58.3 ms: 1.15x faster                                                       |
| nbody                      | 71.9 ms                                                     | 63.4 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.28 ms: 1.12x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.24 sec: 1.11x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.5 ms: 1.10x faster                                                       |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 125 us: 1.07x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 52.6 ms: 1.06x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.5 ms: 1.05x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 88.6 ms: 1.05x faster                                                       |
| pyflate                    | 295 ms                                                      | 281 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.0 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 86.2 ms: 1.02x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 59.6 ns: 1.01x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.07 us: 1.01x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 75.1 ms: 1.01x slower                                                       |
| raytrace                   | 192 ms                                                      | 194 ms: 1.01x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 38.3 ms: 1.02x slower                                                       |
| json                       | 3.05 ms                                                     | 3.10 ms: 1.02x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 59.9 ms: 1.02x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.0 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 523 ms: 1.02x slower                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 49.4 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.6 ms: 1.02x slower                                                       |
| fannkuch                   | 247 ms                                                      | 252 ms: 1.02x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 80.6 ms: 1.02x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 38.7 ns: 1.03x slower                                                       |
| richards_super             | 32.1 ms                                                     | 33.2 ms: 1.03x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.4 ms: 1.03x slower                                                       |
| sympy_str                  | 175 ms                                                      | 182 ms: 1.04x slower                                                        |
| async_generators           | 239 ms                                                      | 250 ms: 1.04x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.55 us: 1.04x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.55 us: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                                       |
| 2to3                       | 218 ms                                                      | 228 ms: 1.05x slower                                                        |
| logging_format             | 6.72 us                                                     | 7.06 us: 1.05x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.75 sec: 1.06x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.91 us: 1.06x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 516 ms: 1.06x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.45 ms: 1.08x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.8 us: 1.08x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.42 ms: 1.08x slower                                                       |
| pycparser                  | 699 ms                                                      | 759 ms: 1.09x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.38 ms: 1.10x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.3 us: 1.10x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 217 us: 1.11x slower                                                        |
| pickle                     | 7.43 us                                                     | 8.31 us: 1.12x slower                                                       |
| sympy_expand               | 284 ms                                                      | 319 ms: 1.12x slower                                                        |
| django_template            | 22.9 ms                                                     | 26.7 ms: 1.16x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.37 us: 1.19x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.64 sec: 1.20x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.20x slower                                                        |
| coverage                   | 40.8 ms                                                     | 49.4 ms: 1.21x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.13 ms: 1.25x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.6 ms: 1.27x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.7 ms: 1.28x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.05 ms: 1.35x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.24 ms: 1.65x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (5): go, chaos, sympy_sum, pprint_pformat, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 86.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown